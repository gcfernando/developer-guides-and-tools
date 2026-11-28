"""Rebuild teaching figures and their accessible equivalents from course sources.

Run from the course folder: python course_tools/build_visuals.py
Lesson scripts run in disposable copies. This does not update their expected output.
The resulting JSON records source hashes and computed values, not learner-test claims.
"""

from contextlib import redirect_stdout
import hashlib
import io
import json
import os
from pathlib import Path
import re
import runpy
import shutil
import sys
import tempfile
import textwrap

os.environ.setdefault('MPLBACKEND', 'Agg')
os.environ.setdefault('OMP_NUM_THREADS', '1')
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_curve

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'workbook-figures'
BLUE, TEAL, ORANGE = '#225da8', '#087f77', '#b35c20'
INK, MUTED = '#182f46', '#465c72'
COLORS = [BLUE, TEAL, ORANGE]
MARKERS = ['o', 's', 'D']
CATALOG = {}
CACHE = {}
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13,
                     'axes.labelsize': 14, 'axes.titlesize': 16,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.edgecolor': '#879db2', 'text.color': INK,
                     'axes.labelcolor': INK, 'xtick.color': MUTED,
                     'ytick.color': MUTED, 'savefig.facecolor': 'white'})


def lesson(number):
    return next(p for p in (ROOT/'lessons').iterdir() if p.name.startswith(f'{number:03d}-'))


def execute(number, script='lesson.py'):
    """Keep source data, model predictions and plotted calculations in agreement."""
    key=(number,script)
    if key in CACHE:
        return CACHE[key]
    source = lesson(number)
    with tempfile.TemporaryDirectory(prefix='ml-visual-build-') as temporary:
        copy = Path(temporary)/source.name
        shutil.copytree(source, copy)
        previous = Path.cwd()
        output = io.StringIO()
        old_show, old_close = plt.show, plt.close
        plt.show = lambda *a, **k: None
        plt.close = lambda *a, **k: None
        sys.path.insert(0, str(copy))
        try:
            os.chdir(copy)
            with redirect_stdout(output):
                values = runpy.run_path(str(copy/script), run_name='__main__')
                if script=='penalty_lab.py': values['_coefficient_table']=pd.read_csv(copy/'coefficient-check.csv')
        finally:
            os.chdir(previous)
            sys.path.pop(0)
            plt.show, plt.close = old_show, old_close
            plt.close('all')
            for module in ('fit_delivery_model', 'service', 'send_requests', 'monitor'):
                sys.modules.pop(module, None)
    values['_stdout'] = output.getvalue()
    CACHE[key] = values
    return values


def clean(value):
    if isinstance(value, (np.integer,)): return int(value)
    if isinstance(value, (float, np.floating)):
        return round(float(value), 6) if np.isfinite(value) else 'Missing'
    if isinstance(value, (bool, np.bool_)): return bool(value)
    if pd.isna(value): return 'Missing'
    return str(value)


def table(frame, index=False):
    if isinstance(frame, pd.Series): frame=frame.to_frame()
    if index: frame=frame.reset_index()
    return {'columns': [str(c) for c in frame.columns],
            'rows': [[clean(v) for v in row] for row in frame.itertuples(index=False, name=None)]}


def register(name, number, question, instructions, observation, limit, data, *, steps=None, kind='chart'):
    source = lesson(number) if isinstance(number, int) else ROOT/'lessons/train-and-test'
    source_files = sorted(source.glob('*.py'))+sorted(source.glob('*.csv'))
    if kind=='flow':source_files.append(ROOT/'course_tools/visual-flow-sources.json')
    entry = {'teaching_question': question, 'kind': kind,
             'read_instructions': instructions, 'observation': observation,
             'limit': limit, 'table_data': table(data) if isinstance(data, (pd.DataFrame,pd.Series)) else data,
             'source_description': source.relative_to(ROOT).as_posix()+('. The cards explain the authored practice process; they are not measured real-service results.' if kind=='flow' else '. Values below are calculated from the supplied example; they are not evidence from a real service.'),
             'sources': [{'path':p.relative_to(ROOT).as_posix(), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in source_files if p.is_file()],
             'generation_source': 'course_tools/build_visuals.py',
             'review_status': {'source_calculations':'generated from course sources', 'three_role_review':'pending', 'beginner_study':'not performed', 'browser_review':'pending'}}
    if steps: entry['steps']=steps
    if kind=='chart': entry['mobile_asset']=name+'-mobile.png'
    CATALOG[name+'.png']=entry
    return entry


def chart(name, number, question, instructions, observation, limit, data, draw):
    entry=register(name,number,question,instructions,observation,limit,data)
    for mobile in (False,True):
        fig, ax=plt.subplots(figsize=(5.2,6.4) if mobile else (10,5.8),layout='constrained')
        ax.set_title(textwrap.fill(question,35 if mobile else 76),pad=16)
        ax.grid(axis='y',alpha=.18);ax.set_axisbelow(True)
        draw(ax,mobile)
        if mobile:
            for panel in fig.axes:
                panel.tick_params(labelsize=16)
                panel.xaxis.label.set_size(17);panel.yaxis.label.set_size(17)
                for annotation in panel.texts:
                    if annotation.get_fontsize()<12:annotation.set_fontsize(12)
                legend=panel.get_legend()
                if legend:
                    for label in legend.get_texts():label.set_fontsize(12)
            if len(fig.axes) in (2,3,4):fig.set_size_inches(5.8,3.5*len(fig.axes))
        fig.savefig(OUT/(name+('-mobile' if mobile else '')+'.png'),dpi=160)
        plt.close(fig)
    # Every generated mobile asset has the same numerical/text equivalent.
    CATALOG[entry['mobile_asset']]={**entry,'mobile_asset':None,'variant_of':name+'.png'}


FLOW_LESSONS={'api-request-steps':215,'audio-feature-steps':118,'boolean-input-steps':90,
 'choose-model-setting':187,'convert-to-lowercase-remove-punctuation':79,'data-collection-steps':10,
 'datetime-feature-steps':93,'duplicate-check-steps':49,'encoding-choices-steps':74,
 'features-from-raw-data':160,'image-feature-steps':113,'large-number-steps':102,
 'missing-values-steps':31,'monitoring-steps':234,'outlier-source-decision':69,
 'pick-model-metric':195,'problem-definition-steps':4,'reinforcement-steps':410,
 'request-journey':1,'semi-supervised-steps':402,'standardize-formats-steps':55,
 'supervised-model-steps':357,'text-cleaning-steps':78,'train-save-test-steps':None,
 'training-validation-test-steps':179,'unsupervised-model-steps':382,'video-feature-steps':122,
 'workbook-pipeline':3}


def make_flows():
    """Editable flow wording is stored separately from its PNG presentation."""
    path=ROOT/'course_tools/visual-flow-sources.json'
    if path.exists():
        flows=json.loads(path.read_text(encoding='utf-8'))
    else:
        workbook=(ROOT/'Data-Science-and-Machine-Learning.md').read_text(encoding='utf-8')
        alternatives={Path(url).stem:alt for alt,url in re.findall(r'!\[([^\]]*)\]\(([^)]+\.png)\)',workbook)}
        flows={}
        for name,number in FLOW_LESSONS.items():
            alt=alternatives[name+'-mobile']
            parts=alt.split(' → ')
            if len(parts)==1: parts=re.split(r'(?<=\.) (?=[A-Z])',alt,maxsplit=2)
            steps=[]
            for part in parts:
                label,separator,body=part.partition('. ')
                steps.append({'label':label.rstrip('.'),'text':body if separator else part})
            flows[name]={'title':name.replace('-',' ').capitalize(), 'steps':steps}
        # Source review explicitly decides among three actions; it does not presume correction.
        flows['outlier-source-decision']={'title':'What does the source tell us to do?', 'steps':[
            {'label':'Confirmed 5 kg: CORRECT','text':'Use the source-confirmed weight in the reviewed training copy. Keep the original record for tracing the change.'},
            {'label':'Confirmed 90 kg: KEEP','text':'The unusual value is real. Keep it and check whether the intended model should handle heavy parcels.'},
            {'label':'No usable slip: FLAG','text':'Ask for a source check. For this practice run, set the uncertain row aside; do not invent its true weight.'}]}
        path.write_text(json.dumps(flows,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    for name,spec in flows.items():
        data={'columns':['Step or option','Meaning'],'rows':[[s['label'],s['text']] for s in spec['steps']]}
        number=FLOW_LESSONS[name]
        entry=register(name,number,spec['title'],'Read the numbered cards in order. For a decision diagram, compare the named options instead of doing all of them.',
                       spec.get('observation','Use the accompanying lesson to try these inputs and explain the result.'),
                       'These cards explain a process. They do not measure model accuracy or prove the process is suitable for every project.',data,steps=spec['steps'],kind='flow')
        entry['sequence_type']='options' if name in {'outlier-source-decision','boolean-input-steps','encoding-choices-steps','pick-model-metric'} else 'steps'
        for mobile in (False,True):
            fig,ax=plt.subplots(figsize=(6,10) if mobile else (13,5.2));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
            ax.text(.04,.97,textwrap.fill(spec['title'],28 if mobile else 70),va='top',fontsize=18,weight='bold',color=INK)
            n=len(spec['steps'])
            for i,step in enumerate(spec['steps']):
                x=.06 if mobile else .025+i*.325;y=.59-i*.25 if mobile else .09
                width=.88 if mobile else .30;height=.22 if mobile else .60
                ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle='round,pad=.012',facecolor=['#edf3fb','#e9f5f2','#fcf1e8'][i%3],edgecolor='#96a9bc'))
                marker='Option ' if entry['sequence_type']=='options' else ''
                label=textwrap.fill(f'{marker}{i+1}. '+step['label'],31 if mobile else 24)
                ax.text(x+.025,y+height-.025,label,va='top',fontsize=13,weight='bold',color=INK)
                ax.text(x+.025,y+height-.12 if mobile else y+height-.24,textwrap.fill(step['text'],44 if mobile else 32),va='top',fontsize=11.5,color=INK,linespacing=1.4)
            fig.savefig(OUT/(name+('-mobile' if mobile else '')+'.png'),dpi=160,bbox_inches='tight');plt.close(fig)
        CATALOG[name+'-mobile.png']={**entry,'variant_of':name+'.png'}


def line(ax,x,y,label,color=BLUE,marker='o',style='-'):
    ax.plot(x,y,label=label,color=color,marker=marker,linestyle=style,linewidth=2,markersize=6)


def bars(ax,labels,values,xlabel):
    y=np.arange(len(labels));ax.barh(y,values,color=[COLORS[i%3] for i in y],edgecolor=INK)
    ax.set(yticks=y,yticklabels=labels,xlabel=xlabel);ax.invert_yaxis()
    for i,v in enumerate(values):ax.annotate(f'{v:.2f}',(v,i),xytext=(5,0),textcoords='offset points',va='center',fontsize=12)
    ax.set_xlim(0,max(values)*1.2 if max(values)>0 else 1)


def make_basic_charts():
    v=execute(2);d=v['deliveries'];prediction=v['model'].predict(d[['distance_km']]);t=d.copy();t['predicted_minutes']=prediction;t['role']=['Training']*3+['Check']*(len(d)-3)
    def first(ax,m):
        line(ax,d.distance_km,prediction,'Fitted rule')
        ax.scatter(d.distance_km[:3],d.minutes[:3],s=75,marker='o',label='Training records',color=BLUE)
        ax.scatter(d.distance_km[3:],d.minutes[3:],s=85,marker='s',label='Known check records',color=TEAL)
        ax.scatter([4],[18],s=100,marker='D',label='New request: 4 km',color=ORANGE)
        ax.set(xlabel='Distance (km)',ylabel='Delivery time (minutes)');ax.legend(fontsize=10)
    chart('your-first-prediction',2,'What time does the rule predict for 4 km?','Read distance across the bottom and delivery minutes up the side. Circles teach the model; squares are separate checks; the diamond is a request.',
          'The supplied three training rows follow 10 + 2 × distance. At 4 km the estimate is 18 minutes.','These invented rows are exact. Real trips vary, and two checks do not establish real-service accuracy.',t,first)
    v=execute(32);d=v['data'];counts=d.isna().sum();frame=pd.DataFrame({'Column':counts.index,'Missing cells':counts.values})
    chart('identify-missing-values',32,'Which fields need a missing-value check?','Each bar counts blank cells in one column. Zero means no missing cells in that column.',
          'There are two missing zones and one missing weight. A question mark is treated as missing.','Count gaps before deciding how to handle them. A blank is not the same as zero.',frame,
          lambda ax,m:bars(ax,frame.Column,frame['Missing cells'],'Number of missing cells'))
    v=execute(48);t=v['results']
    chart('when-missing-values-change-the-answer',48,'What happens when slow trips are missing?','Compare the average computed from all six true times with the average from the recorded times only.',
          'The all-times average is 23 minutes. The recorded-only average is 18 minutes because two slow trips are missing.','The true times are supplied only to illustrate this invented example. In real work, investigate why records are absent.',t,
          lambda ax,m:bars(ax,t.iloc[:,0],t.iloc[:,1],'Average delivery time (minutes)'))
    v=execute(37);t=v['table'];first=t[t['New row']==1]
    def fills(ax,m):
        fig=ax.figure;ax.remove();axes=fig.subplots(2,1)
        bars(axes[0],first.Method,first['Filled kg'],'Filled parcel weight (kg)')
        bars(axes[1],first.Method,first['Prediction in minutes'],'Predicted delivery time (minutes)')
        axes[1].axvline(first['Actual minutes'].iloc[0],linestyle='--',color=INK,label='Measured time: 33 min');axes[1].legend(fontsize=9)
    chart('numerical-data-mean-median-mode-knn-imputer',37,'How does filling one weight change the forecast?','Every bar is a prediction for the same first request. Compare it with the dashed measured-time line. The table also gives the filled weight.',
          'Each fill method learns from the same training deliveries. Its filled weight and model estimate can differ.','One known request is a worked comparison, not enough evidence to select the best fill method.',t,
          fills)
    v=execute(64);w=v['weight'];q1,q3=w.quantile([.25,.75]);upper=q3+1.5*(q3-q1)
    t=pd.DataFrame({'Weight (kg)':w,'Above upper IQR limit':w>upper})
    def iqr(ax,m):
        fig=ax.figure;ax.remove();axes=fig.subplots(2,1)
        for panel in axes:
            panel.boxplot(w,vert=False,showmeans=False);panel.axvline(upper,color=ORANGE,linestyle='--');panel.set(yticks=[],xlabel='Recorded parcel weight (kg)');panel.grid(axis='x',alpha=.18)
        axes[0].set_title('Full range: the 80 kg parcel needs review',fontsize=13)
        axes[1].set_xlim(0,upper*1.2);axes[1].set_title(f'Close view: upper review limit {upper:g} kg',fontsize=13)
    chart('interquartile-range-iqr',64,'Which parcel weight needs a source check?','The box shows the middle half of the recorded weights. The dashed line is an upper review limit, not a boundary between true and false values.',
          f'The supplied 80 kg reading is beyond the {upper:g} kg upper review limit.','A statistical flag does not prove a recording error. Check the source before changing or removing a parcel.',t,iqr)
    v=execute(69);d=v['deliveries'];limit=v['upper_limit']
    def outlier(ax,m):
        ax.scatter(d.parcel.iloc[:-1],d.weight_kg.iloc[:-1],marker='o',color=BLUE,label='Training parcels');ax.scatter(d.parcel.iloc[-1:],d.weight_kg.iloc[-1:],marker='s',color=TEAL,s=75,label='Kept-back parcel');ax.scatter([5],[90],marker='D',s=120,color=ORANGE,label='Parcel 5: inspect source')
        ax.axhline(limit,linestyle='--',color=TEAL,label=f'Upper training review limit: {limit:g} kg');ax.set(xlabel='Parcel ID (a name, not weight)',ylabel='Recorded weight (kg)');ax.legend(fontsize=9)
    chart('spot-check-and-handle-an-outlier-1',69,'Which recorded parcel should we investigate?','Each point is one parcel. Horizontal position is its ID; vertical position is recorded kg. The dashed review limit uses training parcels 1–7 only. Square parcel 8 is a separate check.',
          'Parcel 5 is recorded as 90 kg, far above the other supplied weights. The weighing slip determines the action.','The unusual height asks for investigation; it does not justify replacing 90 with a guessed value.',d,outlier)
    t=v['comparison']
    def comparison(ax,m):
        bars(ax,t.iloc[:,0],t.iloc[:,1],'Predicted delivery time (minutes)')
        for bar,color in zip(ax.patches,[ORANGE,TEAL]):bar.set_facecolor(color)
        ax.axvline(t.iloc[0,2],color=INK,linestyle='--',label='Measured time');ax.legend(fontsize=10)
    chart('spot-check-and-handle-an-outlier-2',69,'What changed after checking the weighing slip?','Both bars predict the same kept-back parcel. The dashed line is its measured delivery time.',
          'With the supplied slip confirming 5 kg, the reviewed fit predicts 26 minutes instead of about 17.7.','Only the source-confirmed correction justifies changing the training value. One check parcel does not prove a general improvement.',t,
          comparison)
    v=execute(75);t=v['encoding_table']
    def encoding(ax,m):
        a=t[['Red','Blue','Green']].to_numpy();ax.imshow(a,cmap='Blues',vmin=0,vmax=1,aspect='auto');ax.grid(False)
        ax.set(xticks=range(3),xticklabels=['Red','Blue','Green'],yticks=range(len(t)),yticklabels=t.iloc[:,0],xlabel='Fixed input columns: Red, Blue, Green',ylabel='Colour in the request')
        for i in range(a.shape[0]):
            for j in range(3):ax.text(j,i,str(a[i,j]),ha='center',va='center',color='white' if a[i,j] else INK,weight='bold',fontsize=16)
    chart('one-hot-encoding-for-unordered-categories',75,'How does a colour name become three input columns?','Read one request across its row. A 1 marks its known colour column; the other columns contain 0. Keep this column order for every request.',
          'Red is 1, 0, 0. The unfamiliar Purple becomes 0, 0, 0 because this encoder ignores unknown names.','All zeros do not mean the model learned about Purple. A real service needs a tested policy for unfamiliar names.',t,encoding)


def make_transform_charts():
    for name,number in [('normalization-min-max-scaling',71),('standardization-z-score-scaling',72)]:
        v=execute(number);train=v['training'];inputs=v['inputs'];scaled=v['scaler'].transform(train[inputs]);t=train[inputs].copy();t['Scaled distance']=scaled[:,0];t['Scaled weight']=scaled[:,1]
        def draw(ax,m,v=v,train=train,scaled=scaled):
            fig=ax.figure;ax.remove();axes=fig.subplots(2,1) if m else fig.subplots(1,2)
            for i,(panel,field,unit) in enumerate(zip(axes,['distance_km','weight_kg'],['km','kg'])):
                line(panel,train[field],scaled[:,i],field,COLORS[i],MARKERS[i]);panel.set(xlabel=f'Original {"distance" if i==0 else "weight"} ({unit})',ylabel='Scaled value (unitless)');panel.grid(alpha=.18)
            fig.suptitle('Apply a separate training scale to each field',fontsize=15)
        chart(name,number,'How does the training distance change scale?','Read an original distance on the horizontal axis and its converted value on the vertical axis. The table also includes the separately converted weight.',
              'Each field has its own fitted conversion. Reuse the training conversion when a new request arrives.','Scaling does not recover missing information or prove the prediction is reliable. Ordinary unpenalized linear fits may give the same predictions after scaling.',t,draw)
    # Read the saved-range data directly; do not create or load a model artifact here.
    f=lesson(71);training=pd.read_csv(f/'range_training.csv');requests=pd.read_csv(f/'range_requests.csv');low=training.distance_km.min();high=training.distance_km.max();t=requests.copy();t['Scaled distance']=(t.distance_km-low)/(high-low)
    def rangeplot(ax,m):
        line(ax,[low,high],[0,1],'Fitted training range')
        outside=t[t.distance_km>high]
        if not outside.empty:
            far=outside.iloc[-1];line(ax,[high,far.distance_km],[1,far['Scaled distance']],'Outside training range',ORANGE,'D','--')
            ax.annotate(f'{far.distance_km:g} km → {far["Scaled distance"]:.4f}',(far.distance_km,far['Scaled distance']),xytext=(-140,-30),textcoords='offset points',fontsize=11)
        ax.axhline(1,color=INK,linestyle=':');ax.set(xlabel='Request distance (km)',ylabel='Scaled distance (unitless)');ax.legend(fontsize=10)
    chart('min-max-outside-training-range',71,'Why can a scaled distance be greater than 1?','The fitted endpoints are 1 and 50 km. Read the new distance on the bottom and its scaled number up the side.',
          'The supplied 90 km request maps to (90 − 1) ÷ (50 − 1), about 1.8163.','Do not refit a scaler on each request. A possible distance outside the fitted range needs a stated service policy.',t,
          rangeplot)
    transforms=[('min-max-scaling-normalization',132),('z-score-standardization-standardization',135),('log-transformation-log-scaling',136),('robust-scaling-median-iqr-scaling',138),('power-transformations-box-cox-yeo-johnson',139),('quantile-transformation-rank-scaling',142),('binning-discretization',145),('polynomial-features-feature-expansion',146)]
    for name,number in transforms:
        v=execute(number);training=v['training'];x=training.signal.to_numpy();t=pd.DataFrame({'Original reading':x})
        pairs=v.get('methods',[(v.get('name',name),v.get('transform'))])
        for label,transform in pairs:
            values=np.asarray(transform.transform(training[['signal']]))
            for j in range(values.shape[1]):t[label+(f' column {j+1}' if values.shape[1]>1 else '')]=values[:,j]
        def draw(ax,m,t=t,number=number):
            if number==145:
                fig=ax.figure;fig.clear();panels=fig.subplots(len(t.columns)-1,1,sharex=True)
                for i,(panel,column) in enumerate(zip(panels,t.columns[1:])):
                    panel.scatter(t.iloc[:,0],t[column],color=COLORS[i%3],marker=MARKERS[i%3],s=55)
                    panel.set(yticks=[0,1],ylim=(-.15,1.15),ylabel=f'Bin {i+1}\n(0 or 1)')
                    panel.grid(axis='y',alpha=.18)
                panels[-1].set_xlabel('Original sensor reading\n(course units)')
                fig.suptitle('Each reading activates one bin column',fontsize=15)
                return
            for i,c in enumerate(t.columns[1:]):line(ax,t.iloc[:,0],t[c],str(c).replace('Polynomial Features column ','x power '),COLORS[i%3],MARKERS[i%3],'None' if number==145 else ['-','--',':'][i%3])
            if number==146:ax.set_yscale('log')
            ax.set(xlabel='Original sensor reading (course units)',ylabel='Prepared feature value'+(' (log axis)' if number==146 else ''));ax.legend(fontsize=9)
        note='The table records the actual prepared values from the fitted training rule.'
        if number==145:note='Each original reading has three bin columns. Exactly one is 1 and the others are 0. Match all three markers at the same horizontal position. Values between the markers are not fractional bin assignments.'
        if number==146:note='One reading creates x, x² and x³. For positive x above 1, the cubic grows fastest. Equal vertical steps on this log axis mean multiplication, not equal addition.'
        chart(name,number,'What numbers does this preparation give the model?','Match one original reading with all its prepared values. Read the legend before comparing curves or bin columns.',note,
              'Fit any learned rule on training rows only. Compare candidate preparation on validation; a change of representation does not guarantee better predictions.',t,draw)


def make_model_charts():
    v=execute(179);t=v['table']
    chart('stratified-sampling',179,'Do the three sets keep the urgent-order share?','Read the number of rows and urgent orders together. The sets have different jobs and different sizes.',
          'The supplied training, validation and test sets have 70, 20 and 10 rows, each with 20% urgent orders.','Stratification preserves class shares. It does not replace checks for repeated shipment IDs, time order or shared customers.',t,
          lambda ax,m:(ax.barh(t['Set'],t['Urgent'],label='Urgent',color=ORANGE,hatch='//'),ax.barh(t['Set'],t['Rows']-t['Urgent'],left=t['Urgent'],label='Regular',color='#e2eaf5',edgecolor=BLUE),ax.set(xlabel='Number of orders'),ax.legend(fontsize=10)))
    for name,number in [('lesson-205-confusion-matrix',205),('feature-importance-plot-1',207)]:
        v=execute(number)
        if number==205:counts=v['counts']
        else:counts=confusion_matrix(v['y_test'],v['predictions'],labels=[0,1])
        t=pd.DataFrame(counts,index=['Actual regular','Actual urgent'],columns=['Predicted regular','Predicted urgent']).reset_index(names='Actual answer')
        def draw(ax,m,counts=counts):
            ax.imshow(counts,cmap='Blues');ax.grid(False);ax.set(xticks=[0,1],yticks=[0,1],xticklabels=['Regular','Urgent'],yticklabels=['Regular','Urgent'],xlabel='Predicted category',ylabel='Actual category')
            for i in range(2):
                for j in range(2):ax.text(j,i,str(counts[i,j]),ha='center',va='center',fontsize=22,color='white' if counts[i,j]>=counts.max()/2 else INK)
        chart(name,number,'Where are the misses and false alarms?','Rows are actual answers; columns are model decisions. Actual urgent predicted regular is a miss. Actual regular predicted urgent is a false alarm.',
              f'The supplied check has {counts[1,0]} missed urgent orders and {counts[0,1]} false alarms.','The count table describes these supplied check rows and this decision rule. Choose an operating cutoff on validation rows.',t,draw)
    for name,number in [('lesson-206-roc-cutoffs',206),('feature-importance-plot-2',207)]:
        v=execute(number);y=v['test']['answer'] if number==206 else v['y_test'];risk=v['risk'] if number==206 else v['probability'];fpr,tpr,threshold=roc_curve(y,risk)
        t=pd.DataFrame({'False alarm share':fpr,'Urgent share caught':tpr,'Cutoff':threshold})
        def rocplot(ax,m,fpr=fpr,tpr=tpr,y=y,risk=risk,number=number):
            line(ax,fpr,tpr,'Classifier');ax.plot([0,1],[0,1],'--',color=MUTED,label='Chance reference')
            for i,cut in enumerate([.25,.75] if number==206 else [.5]):
                tn,fp,fn,tp=confusion_matrix(y,risk>=cut,labels=[0,1]).ravel();x=fp/(fp+tn);yy=tp/(tp+fn)
                ax.scatter(x,yy,color=COLORS[(i+1)%3],marker=MARKERS[(i+1)%3],s=90,label=f'Cutoff {cut:g}')
                ax.annotate(f'{cut:g}: {tp} caught, {fn} missed, {fp} false', (x,yy),xytext=(8,-28-i*30),textcoords='offset points',fontsize=8)
            ax.set(xlabel='False alarm share',ylabel='Urgent-order recall',xlim=(0,1),ylim=(0,1.03));ax.legend(fontsize=9,loc='lower right')
        chart(name,number,'How do catches and false alarms trade off?','Horizontal position is false alarms divided by truly regular orders. Vertical position is urgent orders caught divided by truly urgent orders.',
              'Changing the decision cutoff moves along the curve; it does not retrain the model.','This is a teaching curve on supplied check rows. Use validation and real review capacity to choose a cutoff.',t,
              rocplot)
    v=execute(207);importance=v['importance'];t=pd.DataFrame({'Input':v['X'].columns,'Mean F1 drop':importance.importances_mean,'SD across shuffles':importance.importances_std})
    chart('feature-importance-plot-3',207,'Which input did this fitted model rely on?','Each bar is the average change in F1 after shuffling one input on the check rows. A larger positive drop means more reliance in this check.',
          'Compare the measured drops for distance and weight in the table.','Permutation importance is not a causal effect. Correlated inputs and the check sample affect the result.',t,
          lambda ax,m:(bars(ax,t.Input,t['Mean F1 drop'],'Mean drop in F1 after shuffling'),ax.errorbar(t['Mean F1 drop'],np.arange(len(t)),xerr=t['SD across shuffles'],fmt='none',ecolor=INK,capsize=4)))
    v=execute(208);t=v['error_rows']
    chart('residual-plots',208,'Did the two predictions guess too little or too much?','The horizontal position is predicted minutes. The vertical value is actual minus predicted minutes. Above zero means the estimate was too short.',
          'The two supplied check deliveries each have a positive residual of 2 minutes.','Two points show the arithmetic. Use a larger independent batch to investigate error patterns.',t,
          lambda ax,m:(ax.scatter(t.iloc[:,1],t.iloc[:,2],s=80,color=BLUE,marker='o'),ax.axhline(0,color=INK,linestyle='--'),ax.set(xlabel='Predicted delivery time (minutes)',ylabel='Actual − predicted (minutes)')))


def make_exploration_charts():
    v=execute(148);d=v['data'];t=d.copy()
    def panels(ax,m):
        fig=ax.figure;ax.remove();axes=np.ravel(fig.subplots(4,1) if m else fig.subplots(2,2))
        axes[0].hist(d.weight,bins=6,color=BLUE,edgecolor='white');axes[0].set(xlabel='Parcel weight (kg)',ylabel='Count')
        axes[1].scatter(d.distance,d.minutes,color=TEAL);axes[1].set(xlabel='Distance (km)',ylabel='Time (min)')
        axes[2].boxplot(d.weight,vert=False);axes[2].set(xlabel='Parcel weight (kg)',yticks=[])
        correlation=d.corr();a=correlation.to_numpy();axes[3].imshow(a,vmin=-1,vmax=1,cmap='Blues');axes[3].set(xticks=range(4),yticks=range(4),xticklabels=correlation.columns,yticklabels=correlation.columns);axes[3].tick_params(axis='x',rotation=45,labelsize=8);axes[3].tick_params(axis='y',labelsize=8)
        for i in range(4):
            for j in range(4):axes[3].text(j,i,f'{a[i,j]:.2f}',ha='center',va='center',fontsize=8,color='white' if a[i,j]>.7 else INK)
    chart('pair-plots-1',148,'What do separate fields and paired fields reveal?','The panels show weight counts, distance versus minutes, a weight box plot and correlations. Read each panel’s own axes.',
          'The supplied high weight deserves review. Distance and route_distance repeat the same pattern.','A pattern is not proof of cause. Use training data when exploration informs model choices.',t,panels)
    corr=d.corr();ct=corr.reset_index(names='Field')
    def heat(ax,m):
        a=corr.to_numpy();ax.imshow(a,vmin=-1,vmax=1,cmap='coolwarm');ax.grid(False);labels=[str(c).replace('_','\n') for c in corr.columns];ax.set(xticks=range(len(labels)),yticks=range(len(labels)),xticklabels=labels,yticklabels=labels)
        ax.tick_params(axis='x',rotation=45)
        for i in range(len(a)):
            for j in range(len(a)):ax.text(j,i,f'{a[i,j]:.2f}',ha='center',va='center',color=INK,fontsize=11)
    def pairgrid(ax,m):
        fig=ax.figure;ax.remove();axes=fig.subplots(3,3);fields=['distance','weight','minutes']
        for i,y in enumerate(fields):
            for j,x in enumerate(fields):
                panel=axes[i,j]
                if i==j:panel.hist(d[x],bins=5,color=BLUE)
                else:panel.scatter(d[x],d[y],s=18,color=TEAL)
                panel.tick_params(labelsize=7)
                if i==2:panel.set_xlabel(x,fontsize=9)
                if j==0:panel.set_ylabel(y,fontsize=9)
    chart('pair-plots-2',148,'How do the same measurements look in pairs?','Read the column field across each panel and the row field up it. Diagonal panels show one field’s counts instead of a pair.',
          'The dots are the same supplied deliveries in every off-diagonal panel. Use the table or full-size view for small labels.','Several views do not create more observations. Inspect original records before drawing conclusions.',t,pairgrid)
    v=execute(283);train=v['train'];t=train.copy()
    def flower(ax,m):
        for i,(name,g) in enumerate(train.groupby('species')):ax.scatter(g.sepal_length,g.petal_length,label=name,marker=MARKERS[i%3],color=COLORS[i%3],s=80)
        ax.set(xlabel='Sepal length (supplied units)',ylabel='Petal length (supplied units)');ax.legend(fontsize=11)
    chart('source-4',283,'How do the invented flower measurements compare?','Each marker is one training flower. Shape and text identify its given species. Only two of the four input fields appear on these axes.',
          'The supplied star, fan and bell examples occupy different parts of this small plot.','These are invented flowers, not the published Iris data. A visible separation is not a reliable population accuracy estimate.',t,flower)
    for name,number in [('k-means',385),('hierarchical-clustering-2',386),('dbscan',387),('gaussian-mixture-models-gmm',388)]:
        v=execute(number);d=v['data'];groups=v['group'];t=d.copy();t.insert(0,'Shopper row',np.arange(1,len(d)+1));t['Assigned group']=groups
        def draw(ax,m,d=d,groups=groups):
            for i,g in enumerate(sorted(set(groups))):
                mask=groups==g;ax.scatter(d.loc[mask,'income'],d.loc[mask,'spending'],label='Noise' if g==-1 else f'Group {g}',marker=MARKERS[i%3] if g!=-1 else 'x',color=COLORS[i%3],s=80)
            for j,row in enumerate(d.itertuples(),1):ax.annotate(str(j),(row.income,row.spending),xytext=(4,-12),textcoords='offset points',fontsize=10)
            ax.set(xlabel='Income (supplied course units)',ylabel='Spending score (course units)');ax.legend(fontsize=10)
        chart(name,number,'Which shoppers were assigned to the same group?','A marker is one shopper row. Match its number to the table. Shapes and text distinguish groups; the fit also used age, absent from these axes.',
              'Inspect the table profiles before describing the groups. Group IDs are names, not rankings.','These small invented groups do not establish useful customer segments. Different methods or settings can produce different groupings.',t,draw)
    v=execute(386);values=v['values'];from scipy.cluster.hierarchy import dendrogram,linkage
    links=linkage(values,method='ward');t=pd.DataFrame(links,columns=['Joined item A','Joined item B','Ward merge distance','Rows joined'])
    def tree(ax,m):
        cut=(links[-2,2]+links[-3,2])/2
        dendrogram(links,labels=[str(i+1) for i in range(len(values))],ax=ax,color_threshold=cut)
        ax.axhline(cut,linestyle='--',color=ORANGE,label='Three-group cut');ax.set(xlabel='Shopper row ID',ylabel='Ward merge distance (scaled inputs)');ax.legend(fontsize=10)
    chart('hierarchical-clustering-1',386,'Which shopper branches join first?','Read upward from numbered shopper leaves. Each horizontal join combines branches; a lower join means more similar under this fitted Ward-distance rule.',
          'The tree shows how the same supplied shoppers combine into larger groups.','Merge distance is based on scaled inputs, not currency. The number of groups depends on the chosen cut.',t,
          tree)
    v=execute(391);a=v['projected'];t=v['data'][['long','wide','score']].copy();t['t-SNE 1']=a[:,0];t['t-SNE 2']=a[:,1]
    def tsne(ax,m):
        ax.scatter(a[:,0],a[:,1],color=BLUE,s=80)
        for i,(x,y) in enumerate(a,1):ax.annotate(str(i),(x,y),xytext=(5,5),textcoords='offset points')
        ax.set(xlabel='t-SNE coordinate 1 (no physical unit)',ylabel='t-SNE coordinate 2 (no physical unit)')
    chart('t-distributed-stochastic-neighbor-embedding-t-sne',391,'Which rows are near one another in this fitted map?','Each numbered marker refers to one source row. Inspect nearby rows, then compare their original measurements in the table.',
          'The fitted coordinates help inspect local neighbours in this supplied data.','Axis values, far-apart spacing and apparent clusters can be misleading. Re-running a changed dataset can move every point.',t,tsne)
    v=execute(114);t=v['results'];t=t.rename(columns={t.columns[0]:'Vertical pixel spread',t.columns[1]:'Horizontal pixel spread'})
    def drawings(ax,m):
        fig=ax.figure;ax.remove();axes=fig.subplots(3,1) if m else fig.subplots(1,3)
        images=[v['images'][0],v['images'][2],v['new_image']];labels=['Sideways training','Upright training','New drawing']
        for panel,pixels,label in zip(axes,images,labels):
            vector=v['embedding'](pixels);panel.imshow(pixels,cmap='Blues',vmin=0,vmax=1);panel.set(xticks=[],yticks=[]);panel.set_title(label,fontsize=12);panel.set_xlabel(f'Vertical {vector[0]:.2f}\nHorizontal {vector[1]:.2f}',fontsize=11)
    chart('image-embeddings',114,'How do two measurements describe a line drawing?','Vertical spread measures how far lit pixels extend across rows. Horizontal spread does the same across columns. A drawing becomes a pair of numbers.',
          'An upright line has vertical spread and zero horizontal spread. A sideways line has the opposite pattern.','These hand-built features work for this drawing task. They are not a pretrained image model or proof of broad image recognition.',t,
          drawings)


def make_applied_charts():
    v=execute(234);b=v['batches'];t=b.copy();history=v['historical'];recent=v['recent']
    def drift(ax,m):
        fig=ax.figure;ax.remove();axes=fig.subplots(2,1) if m else fig.subplots(1,2);ax=axes[0]
        for label,d,style,color in [('Historical',history,'-',BLUE),('Recent',recent,'--',TEAL)]:
            x=np.sort(d.km.to_numpy());y=np.arange(1,len(x)+1)/len(x);ax.step(x,y,where='post',label=label,linestyle=style,color=color)
        ax.set(xlabel='Delivery distance (km)',ylabel='Share at or below distance');ax.legend(fontsize=10)
        bars(axes[1],['Historical reference','Recent'],[v['baseline'],v['recent_score']],'Accuracy after labels arrive')
    chart('real-time-model-accuracy-tracking-dashboards',234,'Did the incoming delivery distances change?','At each distance, read the share of that batch at or below it. Compare the solid historical line with the dashed recent line.',
          'The supplied recent trips cover longer distances. The lesson separately calculates accuracy after true labels arrive.','An input shift is a reason to investigate. It does not prove that retraining is required or that a candidate is better.',t,drift)
    v=execute(420);q=v['q'];t=pd.DataFrame({'Cell':range(4),'Left action value':q[:4,0],'Right action value':q[:4,1]})
    def qplot(ax,m):
        x=np.arange(4);ax.bar(x-.18,q[:4,0],width=.36,label='Left (0)',color=BLUE,hatch='//');ax.bar(x+.18,q[:4,1],width=.36,label='Right (1)',color=TEAL)
        ax.set(xticks=x,xlabel='Current track cell',ylabel='Learned discounted return');ax.legend(fontsize=10)
    chart('q-learning',420,'Which move has the higher learned action value?','Compare left and right at the same cell. Action value estimates discounted reward along future moves, not the immediate reward alone.',
          'The supplied learned policy prefers right in cells 0 through 3.','This deterministic toy track has very few states. A real policy needs suitable independent trials and checks.',t,qplot)
    v=execute(442);t=v['table']
    chart('lesson-442-split-checks',442,'What does each split keep separate?','Compare shared shipment IDs, shared customers and date order in the table before reading model error.',
          'The customer split shares no customers. Only the time split places every test date after training.','Different splits ask different questions. Do not choose a split simply because its error is smallest.',t,
          lambda ax,m:bars(ax,t['Plan'],t['Shared customers'],'Customers shared across training and test'))
    v=execute(443);t=v['curve']
    def curve(ax,m):
        line(ax,t.Depth,t['Training MAE'],'Training',BLUE,'o','-');line(ax,t.Depth,t['Validation MAE'],'Validation',ORANGE,'s','--');ax.set(xlabel='Maximum tree depth (decision levels)',ylabel='Mean absolute error (minutes)');ax.legend(fontsize=11)
        best=t.sort_values(['Validation MAE','Depth']).iloc[0];ax.scatter(best.Depth,best['Validation MAE'],marker='D',s=110,color=ORANGE,zorder=5)
    chart('lesson-443-validation-curve',443,'Can lower training error hide worse new results?','Read each depth across both lines. Training shows fit to learned rows; validation helps choose the setting.',
          'Deep trees fit training closely while the supplied validation error rises. The script selects depth using validation only.','Freeze the choice before the final test. Repeatedly changing settings after test results turns the test into selection data.',t,curve)
    v=execute(444);t=v['choices'];chosen=v['chosen'];prevalence=v['prevalence']
    def pr(ax,m):
        line(ax,v['recall'],v['precision'],'Validation curve',marker=None);ax.axhline(prevalence,color=MUTED,linestyle='--',label='Urgent share');ax.scatter(chosen.Recall,chosen.Precision,color=ORANGE,marker='D',s=90,label='Chosen on validation');ax.set(xlabel='Recall: share of urgent orders caught',ylabel='Precision: share of alerts truly urgent',xlim=(0,1),ylim=(0,1.03));ax.legend(fontsize=9)
    chart('lesson-444-precision-recall',444,'What trade-off does an alert cutoff make?','Read recall across and precision up. The diamond is the cutoff selected on validation; the test-count table is a separate final check.',
          'Catching more urgent orders can also create more false alarms. The script maximizes validation precision among cutoffs meeting its recall target.','This rule does not include a real team-capacity limit or monetary cost. Agree those constraints before a real operational choice.',t,pr)
    # Calibration uses the actual adjusted/raw models from the lesson, including its frozen estimator.
    v=execute(445);from sklearn.calibration import calibration_curve
    records=[];curves=[]
    for label,model in [('Raw forest',v['base']),('Adjusted forest',v['adjusted'])]:
        risk=model.predict_proba(v['test'][v['inputs']])[:,1];actual,mean=calibration_curve(v['test']['urgent'],risk,n_bins=v['bins'],strategy='quantile');curves.append((label,mean,actual))
        records.extend([[label,float(x),float(y)] for x,y in zip(mean,actual)])
    t=pd.DataFrame(records,columns=['Model','Mean predicted probability','Observed urgent fraction'])
    def calibration(ax,m):
        ax.plot([0,1],[0,1],':',color=MUTED,label='Predicted = observed')
        for i,(label,x,y) in enumerate(curves):line(ax,x,y,label,COLORS[i],MARKERS[i],['-','--'][i])
        ax.set(xlabel='Mean predicted urgency probability',ylabel='Observed urgent fraction',xlim=(0,1),ylim=(0,1));ax.legend(fontsize=9)
    chart('lesson-445-calibration',445,'Do similar predicted chances match observed rates?','Each point summarizes a group of test orders with similar predicted chances. Compare it with the predicted-equals-observed diagonal.',
          'Read the numeric pairs in the table. Adjustment need not improve every independent check.','Small groups are uncertain. Changing bins changes the picture, not the saved model probabilities or Brier score.',t,calibration)
    v=execute(446);test=v['test'];t=test.groupby('weight',dropna=False).agg(orders=('shipment_id','count'),model_mae=('model_error','mean'),baseline_mae=('baseline_error','mean')).reset_index()
    chart('lesson-446-errors-by-weight',446,'Which weight group needs a closer look?','Read each group’s order count beside its average error. MAE is the average size of an error in minutes.',
          'The supplied missing-weight group has the largest model error and the smallest count.','A small group needs more evidence. Inspect source records before blaming missingness or claiming a cause.',t,
          lambda ax,m:bars(ax,[f'{r.weight}: {r.orders} orders' for r in t.itertuples()],t.model_mae,'Mean absolute error (minutes)'))
    v=execute(447);output=v['_stdout'];zone_lines=re.findall(r'^(North|South|West)\s+(\d+)\s+([\d.]+)\s*$',output,re.M)
    if len(zone_lines)!=3:raise RuntimeError('Cannot identify capstone zone results; update the visual recipe for the changed output.')
    t=pd.DataFrame(zone_lines,columns=['Zone','Orders','Later MAE (minutes)']);t['Orders']=t.Orders.astype(int);t['Later MAE (minutes)']=t['Later MAE (minutes)'].astype(float)
    final=float(re.search(r'Final test MAE: ([\d.]+)',output).group(1));later=float(re.search(r'Later batch: \d+ orders, MAE ([\d.]+)',output).group(1))
    def capstone(ax,m):
        fig=ax.figure;ax.remove();axes=fig.subplots(2,1)
        bars(axes[0],['Final test: 150 orders','Later: 180 orders'],[final,later],'Overall MAE (minutes)')
        bars(axes[1],[f'{r.Zone}: {r.Orders} orders' for r in t.itertuples()],t['Later MAE (minutes)'],'Later MAE by zone (minutes)')
    table_rows=pd.concat([pd.DataFrame([['Final test',150,final],['All later',180,later]],columns=t.columns),t],ignore_index=True)
    chart('lesson-447-later-batch-monitoring',447,'Where did the saved model make larger later errors?','Read later error by zone and keep each order count beside the error. The top panel compares overall later and final-test error.',
          f'West has the largest supplied later error: {float(t.loc[t.Zone=="West","Later MAE (minutes)"].iloc[0]):.2f} minutes. Read its order count in the table.','An alert asks for investigation, not automatic replacement. Verify measurements and changes before comparing a candidate on separate later rows.',table_rows,capstone)


def make_penalty_chart():
    v=execute(363,'penalty_lab.py');t=v['_coefficient_table']
    def penalty(ax,m):
        fig=ax.figure;ax.remove();axes=fig.subplots(2,1)
        for i,method in enumerate(['Ridge','Lasso']):
            values=t[t.method==method]
            for j,column in enumerate(['km_coefficient','kg_coefficient']):
                line(axes[0],values.alpha,values[column],f'{method}: {"distance" if j==0 else "weight"}',COLORS[i],MARKERS[j],'-' if j==0 else '--')
            line(axes[1],values.alpha,values.validation_mae_minutes,method,COLORS[i],MARKERS[i],'-' if i==0 else '--')
        axes[0].set(xscale='log',ylabel='Coefficient: minutes per\n1 training SD increase');axes[0].axhline(0,color=INK,linestyle=':');axes[0].legend(fontsize=8)
        axes[1].set(xscale='log',xlabel='Alpha: penalty setting (log axis)',ylabel='Validation MAE (minutes)');axes[1].legend(fontsize=10)
    chart('lasso-coefficients',363,'Does shrinking a coefficient improve validation error?','Compare settings within each method. Solid lines show distance coefficients and dashed lines show weight coefficients. The lower panel checks validation error. Alpha uses a log axis: equal steps multiply the value.',
          'Lasso can set coefficients to zero in this example, but the largest penalty also makes much worse validation predictions. The table includes the no-penalty comparison.','A coefficient is measured in minutes per one training-standard-deviation increase of that input, holding the other prepared input fixed. Individual coefficient paths need not always decrease monotonically. A zero does not prove a field never matters.',t,penalty)
    target=lesson(363)/'lasso-coefficients.png';shutil.copyfile(OUT/target.name,target)
    shutil.copyfile(OUT/'lasso-coefficients-mobile.png',target.with_name('lasso-coefficients-mobile.png'))


def sync_lesson_images():
    for source in (ROOT/'lessons').rglob('*.png'):
        if source.name in CATALOG:
            shutil.copyfile(OUT/source.name,source)
            mobile=CATALOG[source.name].get('mobile_asset')
            if mobile:shutil.copyfile(OUT/mobile,source.with_name(mobile))
        elif source.name=='hierarchical-clustering.png':
            shutil.copyfile(OUT/'hierarchical-clustering-1.png',source)
    if 'hierarchical-clustering-1.png' in CATALOG:
        CATALOG['hierarchical-clustering.png']={**CATALOG['hierarchical-clustering-1.png'],'mobile_asset':None,'alias_of':'hierarchical-clustering-1.png'}


def main():
    OUT.mkdir(exist_ok=True)
    make_flows();make_basic_charts();make_transform_charts();make_model_charts();make_exploration_charts();make_applied_charts();make_penalty_chart()
    sync_lesson_images()
    existing={p.name for p in OUT.glob('*.png')}
    missing=existing-set(CATALOG)
    if missing:raise RuntimeError('Images without teaching metadata: '+', '.join(sorted(missing)))
    report={'schema_version':1,'generation_command':'python course_tools/build_visuals.py','visuals':CATALOG,
            'limits':['Generated source values and expert inspection do not establish beginner understanding.','Browser and three-role review status must be recorded separately after the relevant checks.']}
    (ROOT/'course_tools/visuals.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
    print(f'Generated {len(CATALOG)} figure records, including mobile variants and lesson aliases.')


if __name__=='__main__':main()
