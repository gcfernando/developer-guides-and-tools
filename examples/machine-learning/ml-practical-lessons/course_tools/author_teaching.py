"""Author the reviewed concept notes in lesson READMEs and the workbook.

Curated profiles describe the shared idea; every entry also keeps its own goal
and example files. The tool updates the primary lesson explanations and marked
workbook notes, and keeps disclosure markup and browser-guide links consistent.
Run after changing a profile, then build_course.py and check_course.py.
"""
from pathlib import Path
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]
PROFILES = {}
LESSON_PROFILES = {}
COURSE_URL = 'https://gcfernando.github.io/developer-guides-and-tools/examples/machine-learning/ml-practical-lessons/'
TEACHING_ALIASES = json.loads((ROOT/'course_tools/reader-compatibility.json').read_text(encoding='utf-8'))['teaching_note_aliases']
BROWSER_GUIDES = ('LEARNING-PATH', 'PYTHON-BASICS', 'PRACTICE', 'PROJECT-CHOICES',
                  'ELECTIVES', 'TEACHING', 'INDEPENDENT-PROJECT')


def prepare_reader_markdown(text):
    """Render disclosures in Jekyll and link readers without removing raw sources."""
    text = re.sub(r'(?m)^<details>$', '<details markdown="1">', text)
    pattern = r'\]\(('+'|'.join(BROWSER_GUIDES)+r')\.md(#[^)]*)?\)'
    return re.sub(pattern, lambda match: ']('+COURSE_URL+match.group(1)+'.html'+(match.group(2) or '')+')', text)


def concept(key, ids, ready, meaning, use, example, caution, task, answer):
    PROFILES[key] = dict(ready=ready, meaning=meaning, use=use, example=example,
                         caution=caution, task=task, answer=answer)
    for number in ids:
        if number in LESSON_PROFILES:
            raise ValueError(f'Duplicate lesson mapping: {number}')
        LESSON_PROFILES[number] = key


concept('first_prediction', range(1, 3),
 'Read one row and multiply a small number by two.',
 'A prediction is an estimate made from inputs. Training learns the rule from completed examples.',
 'Use a prediction when the answer is not yet known. A fixed rule is enough when the rule is already agreed.',
 'A trip of 4 km has no measured time yet. The tiny training table follows 10 + 2 × distance, so the estimate is 18 minutes. Compare a completed trip with its recorded time before trusting a rule.',
 'These exact made-up numbers show the calculation. They do not show how traffic or a new town will affect a real trip.',
 'Without running Python, predict 8 km. Which field must stay unknown until that trip finishes?',
 'The estimate is 26 minutes. The actual time remains unknown. Editing a request does not create a measured answer.')
concept('project_brief', range(3, 10),
 'Name a person who needs to make a decision.',
 'A project brief states the decision, wanted answer, available inputs, useful score and practical limits.',
 'Write the brief before choosing an algorithm. It can reveal that a report or ordinary rule is enough.',
 'A shop wants a delivery estimate before dispatch. Distance is available then; the finished delivery time is not. Minutes of error answer this question more directly than a percentage of correct category names.',
 'A convenient score is not automatically a useful business goal. State units, when fields arrive, and who acts on the result.',
 'For a rule giving free delivery above 50 currency units, write the decision and decide whether training is needed. Then change the question to estimated arrival time.',
 'Free delivery follows an agreed threshold, so no learned model is needed. Arrival time may need examples; compare it with a simple existing estimate and choose an acceptable error in minutes.')
concept('collection', [10,11,12,13,14,15,22],
 'Read a CSV header and count rows.',
 'Collection brings recorded facts into a table. A database query, API request and web-page parser are different ways to obtain rows.',
 'Use a source whose fields, permissions and update times fit the question. Keep the original source identifiable.',
 'The three order IDs in sample.csv are copied into an in-memory SQLite table and returned by a local API. The HTML example extracts the same zones from supplied tags. Count IDs at each step: a successful request alone does not prove every row arrived.',
 'The script uses local fixtures, not a live public API or web scraper. Real APIs may paginate, fail or change their schema. An HTML page can change its tags.',
 'Add one invented order with a unique ID. Before running, predict the CSV, database and local API row counts. Which source would you inspect if they disagree?',
 'Every complete copy should contain the extra order once. Trace its ID from the original CSV through each result. Investigate filtering, paging or parsing rather than silently accepting fewer rows.')
concept('files_metadata', list(range(16,22))+list(range(23,30)),
 'Tell a file name, folder and CSV field apart.',
 'A file list records where items are. Metadata records how they were obtained and what they mean.',
 'Use these notes whenever someone else must find, reproduce or safely share the data. Keep only fields needed for the agreed purpose.',
 'The exercise writes deliveries.csv without the fictional contact field. A manifest lists text, picture and video files. File size is measured in bytes; it does not tell you whether the facts are correct.',
 'A local folder is not a cloud upload. Removing one contact field does not establish legal compliance, consent, access control or a retention policy. The named legal topics illustrate only this small data-sharing step.',
 'Imagine the image file has a name but cannot be opened. Which checks should supplement its entry in the manifest? What should accompany a shared table?',
 'Check that the file exists, can be decoded and has the expected content and dimensions. Share the needed table fields plus source, collection method, meanings, access permission and retention notes. Use the optional service walkthrough for actual cloud practice.')
concept('missing_detection', range(30,34),
 'Explain why a blank weight differs from a weight of zero.',
 'A missing value means a fact was not recorded. NaN is one marker Python uses for a missing number.',
 'Count missing cells and inspect their rows before deciding whether to recover, fill or remove them.',
 'In sample.csv one weight is blank and two zones are missing after treating ? as a missing marker. A row can have a measured time even when one input is missing.',
 'Zero is a known quantity. Replacing every blank with zero can invent measurements. A question mark becomes missing only because the reader was told to interpret it that way.',
 'Turn the blank weight into a source-confirmed 2 kg. Predict the weight missing-count change. Would writing a guess of 2 recover the fact?',
 'The count falls by one. A confirmed measurement recovers the fact; an invented fill does not. Keep that distinction in the project notes.')
concept('remove_missing', [34,35],
 'Identify inputs and the measured answer.',
 'Removing a row or column means deliberately leaving information out of a fit.',
 'Remove an unavailable training answer from supervised training. Drop a spare note only when its meaning and purpose justify doing so.',
 'The lesson drops the spare note column and rows without distance or minutes. The retained rows train a distance-to-time model; the held-back completed trip checks it.',
 'Removing all incomplete rows can remove a particular kind of delivery. Missing inputs can sometimes be filled; missing target values are not recovered by ordinary input imputation.',
 'A row has a known distance but no time because the trip starts tomorrow. Can it teach supervised regression? Can the trained model receive it?',
 'It cannot teach that model without a confirmed answer. It can be a new prediction request. Keep it separate from completed training/check rows.')
concept('numeric_fill', [36,37,38,39,40,41],
 'Sort 1, 2 and 4; calculate their average and identify their middle.',
 'Imputation supplies an estimate for a missing input. Mean, median and mode use training summaries; KNN uses similar training rows.',
 'Use a fill when an input is unavailable but a justified prediction is still possible. Learn the rule on training data and reuse it.',
 'The observed training weights are 1, 2 and 4 kg. Their mean is about 2.33; median is 2. All occur once, so the most-frequent imputer breaks this tie by taking the smallest value, 1. KNN uses distance and scaled input differences to find two neighbours.',
 'A fill is not a recovered measurement. Nearest neighbours depend on scaling. Comparing methods on one case does not establish the best method for future deliveries.',
 'Training weights are 1, 2, 4, 5 and 8 kg. Fill a new blank by median. Does a new 90 kg request change that saved median?',
 'The median is 4 kg. Apply 4 to the blank and keep the saved rule unchanged for the 90 kg request. Only an explicit new training procedure learns a new median.')
concept('category_fill', [42,43,44],
 'Distinguish a missing zone from a new, named zone.',
 'A categorical fill replaces a missing name with the most common training name or an explicit Unknown name.',
 'Use the mode if a common-category assumption is defensible. Preserve Unknown when missingness deserves its own visible category.',
 'The lesson fits the fill and encoder on the first four rows. It then handles the same blank zone under both choices. An explicit Unknown is a chosen placeholder, not a measurement that the parcel came from a zone called Unknown.',
 'An Unknown category with no training examples does not gain a learned effect merely because the name is written down. A new east zone and an absent zone are different situations.',
 'A request says east and another leaves zone blank. Which one can a missing-value fill change? What must the service decide separately?',
 'The fill changes the blank. It does not turn the named east zone into the training mode. Unknown-name handling belongs to the encoder and service policy; test it explicitly.')
concept('time_fill', [45,46,47],
 'Put days in order and say when a reading becomes available.',
 'Forward fill copies the last available reading. Backward fill copies a later reading into an earlier gap.',
 'Forward fill may suit a value that stays current until replaced. Backward fill is for retrospective repair when the later reading is already known.',
 'With counts 10, blank, 16 on days 1, 2, 3, forward fill gives day 2 a value of 10 and backward fill gives 16. These are estimates with different timing assumptions.',
 'A live day-2 decision cannot use a day-3 reading. Long gaps, resets and rapidly changing measurements may make either fill unsuitable.',
 'Day 3 changes to 18. Which day-2 fill changes? Which fill is available during day 2?',
 'Backward fill changes to 18; forward fill stays 10. Only the past value is available during day 2. Whether carrying it forward is useful still needs validation.')
concept('missing_bias', [48],
 'Calculate an average from a list.',
 'A missing-data pattern can change which cases a summary represents.',
 'Investigate missingness when some routes, people or times are less likely to be recorded.',
 'All six invented times average 23 minutes. The recorded subset averages 18 because two slow trips are absent. The lower number describes recorded trips, not necessarily all deliveries.',
 'Filling gaps does not establish fairness or recover unknown outcomes. In real data the missing true times may be unavailable.',
 'If a broken recorder misses long routes, does a complete-looking filled table prove its average is representative?',
 'No. Compare missing counts by route and time, inspect the recorder/source, and report what is unknown. A fill alone cannot establish the absent outcomes.')
concept('exact_duplicates', [49,50],
 'Explain what one order ID represents.',
 'An exact duplicate repeats the same recorded row; it can give one event extra influence.',
 'Check identity and source before removing copies or dividing records into training and test groups.',
 'If order A appears twice with identical distance and minutes, keeping one confirmed copy stops A being counted twice. Orders B and C may legitimately share the same measurements.',
 'Equal measurements alone do not prove duplicate events. Conflicting records with one ID need investigation rather than keeping the first arbitrarily.',
 'Two distinct shipment IDs both have 5 km and 20 minutes. Remove one? What if they have the same ID but different times?',
 'Keep distinct confirmed shipments. For one ID with conflicting times, review the source and correction history. Do not silently choose a time.')
concept('near_duplicates', [51,52,53],
 'Compare names and order identities separately.',
 'Text cleanup makes comparison easier; fuzzy matching scores similarity without proving identity.',
 'Use similarity to find records for review when spelling or spacing differs.',
 'Maya Jensen and maya   jensen have the same normalized comparison key. Maya Jenson is similar, but the lesson keeps a different order ID separate.',
 'A high name-match score is not permission to merge people or orders. Different people may share a name, and one person may place several orders.',
 'Two similar names have different order IDs and valid source records. Should a fuzzy score above 0.9 merge them?',
 'No. The score suggests a review candidate. Confirm what one row represents and use reliable identity evidence before merging.')
concept('standard_formats', [54,55,56,57,58],
 'Read a date format and distinguish pounds from kilograms.',
 'Standardizing formats gives the same meaning one consistent representation.',
 'Do this before combining systems whose dates, units or category spellings differ.',
 'The lesson knows that 01/02/2025 uses month/day/year, so it becomes 2025-01-02. A 10 lb measurement becomes about 4.54 kg. Trimming NORTH gives north; its meaning stays the same.',
 'Do not guess an ambiguous date format. A unit conversion is a fixed known rule, unlike a training median learned from data. Check unsupported names rather than silently treating them as a known zone.',
 'A new source says 02/03/2025 but gives no date convention. May you assume the same format? What is 22 lb in kg?',
 'Ask the source about its date convention. The fixed conversion gives about 9.98 kg. Apply the same confirmed conversion rules to training and later requests.')
concept('spellings', [59],
 'Explain the difference between text spelling and field meaning.',
 'A spelling map explicitly lists variants known to mean the same category.',
 'Use a reviewed map when a source confirms the aliases. Keep an audit of the original value.',
 'The exercise maps M and male to Male only because its small vocabulary defines that meaning. It then encodes the standardized category.',
 'Do not infer sensitive identity or a category from an unfamiliar abbreviation. An unrecognized spelling should raise a review question.',
 'The file contains an unfamiliar value X. Should you add X → Male to make the script pass?',
 'No. Ask what X means or leave it unresolved. A successful script is not evidence that a guessed mapping is correct.')
concept('outlier_detection', [60,61,62,63,64,152,157],
 'Sort weights and read graph axes in kg.',
 'An outlier is unusual under a stated comparison rule. A flag asks for investigation.',
 'Use plots and numerical rules to find records that deserve attention before fitting or reporting.',
 'The 80 kg value lies far from most weights. A z-score compares it with the average and standard deviation. IQR compares it with the middle half. On a box plot, read kg on the value axis; a whisker limit is a review rule, not a physical weight limit.',
 'Do not delete every flagged value. Large valid deliveries may be exactly the cases a service must support. Small samples and skew affect the rules.',
 'A weighing slip confirms an unusual 80 kg shipment. What should you do before choosing a model that cannot handle it?',
 'Keep the confirmed fact, check whether such shipments are in scope, gather suitable training/check examples, or state a service limit. Do not edit a real value merely to improve a score.')
concept('outlier_handling', [65,66,67,68],
 'Separate a physically invalid value from a valid unusual value.',
 'Removing, clipping and transforming are different actions with different meanings.',
 'Remove confirmed recording errors; consider a fitted clipping or log rule only for a stated modeling reason.',
 'A negative parcel weight is invalid in this exercise. A real 40 kg shipment is not. Clipping changes the model input to a limit learned from training; a log compresses gaps while preserving order for its valid domain.',
 'Keep the original measurement. Fit data-based limits inside training folds. Neither clipping nor logging proves an outlier was wrong.',
 'A new weight exceeds the saved clipping limit. Recalculate that limit using the request?',
 'No. Apply the training limit and record that clipping happened. Relearning a limit is part of explicit retraining, followed by a new fair check.')
concept('outlier_review', [69],
 'Find a parcel ID on the horizontal axis and kg on the vertical axis.',
 'Source review decides whether a flagged measurement is wrong, valid or unresolved.',
 'Use the source record before changing an unusual training value.',
 'Parcel 5 has recorded weight 90 kg and crosses the 12.5 kg review line. A slip confirming 5 kg justifies correction; 90 kg justifies keeping it; an absent usable slip leaves it flagged. The later chart compares predictions for the same held-back parcel 8, whose actual time is 26 minutes.',
 'The flag does not establish an error, and improvement on one held-back trip does not establish general improvement. Do not use the test answer to invent a correction.',
 'The slip confirms 90 kg, but correcting to 5 would improve this one score. Which value belongs in the reviewed data?',
 'Keep 90 kg. Evidence about the measurement decides correction. Model suitability is a separate question requiring more suitable check examples.')

concept('scaling', [70,71,72,125,131,132,133,134,135,138,175],
 'Read a minimum, maximum, average and spread.',
 'Scaling changes the numbers passed to a model, using a rule fitted on training values.',
 'Use it when input units affect distances or penalties. Compare with unchanged inputs; trees often do not need ordinary linear scaling.',
 'Min-max uses (value − training minimum) ÷ training range. With limits 1 and 50 km, 90 km becomes 89 ÷ 49, about 1.8163. Standard scaling subtracts the training mean and divides by its standard deviation. Robust scaling uses the training median and IQR.',
 'New values can fall outside a fitted 0–1 range. Do not refit on each request. Scaling is not a guarantee of better predictions or a way to make a distribution normal.',
 'The fitted range is 1–50 km. What does 25 km become? Does an out-of-range number automatically mean an invalid measurement?',
 '25 becomes 24 ÷ 49, about 0.4898. An out-of-range number may be physically possible but outside the evidence for a service. Keep the fitted rule and apply a stated acceptance/fallback policy.')
concept('choose_transform', [73,147],
 'Calculate an error and distinguish training from validation.',
 'A transformation is a candidate preparation choice, not a compulsory checklist.',
 'Compare a sensible change with unchanged inputs on identical validation folds.',
 'The script fits each transformation inside a pipeline for each training fold, then reports error on that fold’s held-back rows. This prevents a fold’s check values from choosing its scale or bin edges.',
 'The best score on this tiny table may be unstable. Do not apply every transform or use repeated final test scores to choose among them.',
 'Transform A has lower training error but higher validation error than raw inputs. Which setup has better evidence for the next check?',
 'Raw inputs have better validation evidence in this comparison. State the counts and variation, freeze the choice, and assess it on a separate final check.')
concept('one_hot', [74,75,126,174],
 'Tell a category name from a measured amount.',
 'One-hot encoding gives each known category a separate 0-or-1 column. It avoids inventing an order between names.',
 'Use it for a modest set of unordered names when the chosen model requires numeric inputs.',
 'This script explicitly declares the column order Red, Blue, Green. Green becomes 0, 0, 1. Fit the encoder using training inputs, then transform check rows and new requests with that same encoder. The order and number of columns stay fixed.',
 'Purple becomes 0, 0, 0 here because handle_unknown is ignore. That is an allowed representation, not evidence about Purple-specific demand. Do not fit a separate encoder on new requests. Thousands of categories may need a different, validated approach.',
 'Encode Blue on paper. A new request says Yellow. Add a Yellow column only to that request, or keep the saved three-column schema? Explain what the service must decide.',
 'Blue is 0, 1, 0. Keep the saved schema; changing only the request columns breaks the model contract. This demonstration maps Yellow to all zeros. A real service must explicitly reject, review or use a tested fallback for unfamiliar names.')
concept('ordinal', [76],
 'Explain why low, medium and high have an order.',
 'Ordinal encoding records an explicit order between input categories. Label encoding gives identifiers to answer classes.',
 'Use an order only when the field meaning supports it. The model may also impose a spacing assumption on those numbers.',
 'Low, Medium, High become 0, 1, 2 in this exercise. LabelEncoder separately turns the wait/review answers into class IDs and reverses predictions to readable names.',
 'Codes 0, 1, 2 do not prove that the gap between low and medium equals the gap between medium and high. Unordered colours need a different representation.',
 'Could North, South and West be ordered 0, 1, 2 because a terminal prints them that way?',
 'No. Alphabetical or display order is not a real scale. Use separate columns or another justified categorical representation.')
concept('target_encoding', [77],
 'Count delayed orders and explain training-only preparation.',
 'Target encoding replaces a category with a summary learned from training answers.',
 'Consider it for many categories when one-hot columns become unwieldy. Validate the whole preparation/model pipeline.',
 'If two of five supplier orders were delayed, the simple observed rate is 0.40. The lesson uses smoothing for small groups and cross-fitting so a training row does not provide its own encoded answer. An unseen supplier uses broader training information.',
 'A supplier with one delayed order does not establish a true delay chance of 100%. Predicting wholly new suppliers needs a supplier-grouped evaluation.',
 'A supplier has one order and its answer is delayed. Is writing 1.0 into that same training row a safe target encoding?',
 'No. It can reveal the row’s own answer. Use a training procedure with cross-fitting and appropriate smoothing, and keep evaluation answers out of all preparation.')
concept('text_clean', [78,79,127],
 'Read a message and distinguish its words from its category.',
 'Text cleaning gives messages a consistent representation before words are counted.',
 'Lowercase or remove punctuation only when doing so preserves information useful to the task.',
 'WHERE IS MY PARCEL!!! becomes where is my parcel in this exercise. The fitted vocabulary gives a word-count column to known words; the trained classifier turns those numbers into a delivery or billing guess.',
 'NOT LATE differs from LATE. Case and punctuation may matter for names, product codes or sentiment. Unknown words do not receive new columns at prediction time.',
 'Try not late and late. If your cleanup makes them identical, what information was lost? Should every language use the same cleanup?',
 'Negation was lost. Retain it or change the representation and validate it. Languages and tasks need their own tested tokenization and cleanup rules.')
concept('stop_words', [80],
 'Count a word in a short sentence.',
 'A stop-word list removes selected common words before the model sees counts.',
 'Try it only if those words add little useful information for the task.',
 'The explicit list removes the, and, is. The example keeps not, so the phrase not here retains a clue that the parcel is absent.',
 'A general stop list may remove negation or words useful for your language and task. Shorter text is not automatically a better representation.',
 'Would a stop list that removes not be safe for distinguishing late from not late?',
 'Not without evidence. Those phrases could become identical. Compare token lists and validation mistakes before deciding.')
concept('token_lemma', [81,82,83],
 'Identify individual words and their spelling variants.',
 'Tokenization splits text into pieces. Lemmatization maps word forms to a base form using language rules or a stated lookup.',
 'Use tokens to form features; consider base forms when variants should share evidence.',
 'This small lookup turns charged and charges into charge, then counts the resulting tokens. It is an explicit exercise dictionary rather than a full language system.',
 'The lookup covers only listed forms. Context, language and ambiguous words can change the correct base form.',
 'An unfamiliar word arrives. Should the lesson’s dictionary invent its base form? What should remain consistent between old and new messages?',
 'Keep an unlisted token unchanged or apply a tested language tool. Reuse exactly the same tokenizer and vocabulary preparation for training and prediction.')
concept('word_counts', [84,85,86],
 'Count parcel in three short messages.',
 'Word counts record occurrences. TF-IDF changes weights using how common a word is across training messages.',
 'Use counts as a simple text baseline; compare TF-IDF when common words should contribute differently.',
 'A known word has one fixed column. Its raw count may be 1 in a message; its TF-IDF value also depends on the training corpus and normalization. The script prints both values for parcel before predicting held-back categories.',
 'A TF-IDF weight is not a probability or a semantic meaning. Fit vocabulary and IDF on training only; a new message must not relearn them.',
 'A new message contains only words absent from training. Does a predicted category establish that the text was understood?',
 'No. Its representation can contain no known-word evidence. Inspect it, record the limitation and use an appropriate fallback or better training coverage.')
concept('word_vectors', [87,88,89],
 'Read a list of numbers as a vector; complete the network bridge in Extra topics.',
 'An embedding is a list of numbers representing an item. Its usefulness depends on how that representation was constructed or learned.',
 'Use embeddings when a validated representation captures information useful for your task. Compare with a word-count baseline.',
 'Word2Vec learns tiny vectors from the supplied training messages and averages known-word vectors. The BERT exercise starts a random small encoder to show token vectors and pooling; it is not a pretrained language model.',
 'A returned array does not prove language understanding. The tiny corpus and random BERT weights do not justify claims about real message meaning.',
 'Which evidence would you need before replacing a word-count model with these vectors?',
 'Use the same untouched validation examples, report suitable errors and inspect new words/languages and failures. Check representation provenance. Do not choose from a single convenient prediction.')
concept('booleans', [90,91,92,128],
 'Tell known yes, known no and unknown apart.',
 'Boolean preparation converts agreed yes/no spellings into two known values while preserving unknowns.',
 'Use it when a source really records a two-state field. Fill an absent value only through a stated training rule.',
 'Yes, true and 1 map to 1; no, false and 0 map to 0. Unknown remains missing. The imputation variant learns the most frequent training flag rather than claiming the missing person answered no.',
 'Do not treat every nonempty string as true or every unknown as false. Verify source spellings; some fields have more than two real states.',
 'A signup field contains false, 1 and undecided. Which values are known under this lesson’s mapping?',
 'false is known 0 and 1 is known 1. undecided is unmapped/missing under this mapping. Review its meaning rather than inventing a confirmed answer.')
concept('dates', [93,94,95,96,97,98,99,100,130],
 'Read a calendar date and a clock time.',
 'Parsing turns a written time into a date value; feature extraction selects parts such as year, weekday or hour.',
 'Use a part only if it is known when predicting and relevant to the job. Record the date convention and timezone.',
 '2025-02-03 08:00 has year 2025, month 2, day 3, weekday 0 (Monday in pandas) and hour 8. The lesson fits the named date parts and reuses the same parser on later inputs.',
 'Written hour numbers are not distances around a clock: 23:00 and 00:00 are one hour apart. A Unix timestamp needs a stated unit and time convention. Do not guess ambiguous formats.',
 'Two systems write 02/03/2025. What must be known before combining them? Can using a later correction time leak information?',
 'Confirm month/day versus day/month and the timezone. A later correction time may be unavailable at prediction time; use only fields actually known then.')
concept('interpolation', [101],
 'Sort dates and check one reading per date.',
 'Interpolation estimates a gap between known readings on a stated calendar.',
 'Use it for a retrospective series when the neighboring readings and a smooth-change assumption make sense.',
 'February 1 has 10 orders and February 3 has 16. A straight time interpolation gives February 2 a value of 13. Changing February 3 to 18 makes the midpoint 14.',
 'This estimates the missing measurement, not the missing date. It uses the later reading; a live February 2 prediction could not use February 3.',
 'May a real-time February 2 forecast report the interpolated 13 as though it used only available information?',
 'No. That would use a future observation. For live forecasting restrict information to what had arrived; keep retrospective repair clearly labelled.')
concept('log', [102,103,136,137,167],
 'Compare 10, 100 and 1000 and explain a zero.',
 'A logarithm compresses large positive gaps; log1p applies natural log to 1 + value.',
 'Try a log for a skewed measurement or a multiplicative relationship, then compare validation results with unchanged input.',
 'Base-10 log maps 1, 10, 100, 1000 to 0, 1, 2, 3. log1p keeps zero valid and uses a different base. The lesson trains on the transformed signal and predicts cost in its original unit.',
 'Scientific notation is only a display choice. A log actually changes the numeric feature. Check the domain; logging negative values can fail, and a target log needs its inverse before interpreting predictions.',
 'Does writing 1000 as 1e3 make it a log feature? What happens to zero under log10 and log1p?',
 '1e3 is still 1000. log10(0) is not finite, while log1p(0) is 0. Choose a justified valid transformation and reuse it consistently.')
concept('scientific_notation', [104,129],
 'Distinguish an identifier from a measured count.',
 'Scientific notation writes the same value compactly. An ID remains a name even when all its characters are digits.',
 'Use compact notation to display large measurements, and exact strings to preserve long IDs.',
 '1000 and 1e3 mean the same number. The script preserves event_id as text and separately passes log-transformed visits to the cost model.',
 'Rounding an ID or treating its magnitude as a useful measurement can destroy identity or invent a relationship.',
 'A table has an account ID 000123 and a count of 1000000. Which may be formatted as 1e6 and which should preserve characters?',
 'The count may be displayed as 1e6. Preserve 000123 exactly as text; its leading zeros can be part of its identity.')
concept('nested', [105,109,110,111,112],
 'Find a field name and value in a row.',
 'A nested record holds values inside named groups. Flattening selects those values into columns.',
 'Use it when JSON, XML or dictionaries must supply a fixed model input table.',
 'A parcel object with kg inside it becomes parcel.kg after flattening. A missing kg key must remain missing rather than being assumed zero. XML field extraction similarly reads an explicitly named field.',
 'A flattened table can still contain absent fields, repeated records or mixed units. Do not pass IDs, nested text or unavailable answers to a model by accident.',
 'One parcel has no kg key and another has kg equal to zero. Should flattening make those records identical?',
 'No. One weight is unknown and the other is a recorded zero requiring a domain check. Preserve missingness and validate the expected schema and units.')
concept('geography', [106,107,108],
 'Read latitude and longitude as two different coordinates.',
 'Geocoding finds coordinates for a named place. A local lookup only knows its listed places.',
 'Use coordinates when location is relevant and the match is verified. Live geocoding is a separate service step.',
 'North Depot maps to the supplied coordinate pair. Unknown Depot remains unlocated; the script does not invent a point or make a live request.',
 'Ambiguous place names can resolve incorrectly. Latitude/longitude degrees do not directly give travel distance. Do not send personal addresses to an unapproved service.',
 'An unknown address gets coordinates 0,0 from a guessed fallback. Is that a safe representation of missing location?',
 'No. 0,0 is an actual location. Keep the match unresolved and request a source lookup or use a separately tested missing-location policy.')
concept('pixels', [113,115,116,117],
 'Draw a small grid and label row and column positions.',
 'A digital picture stores pixel values. Resize changes its grid size; grayscale changes colour representation; flatten arranges values in a row.',
 'Prepare all images with the same rules for a pixel-based model. Keep spatial dimensions for models that use neighborhoods.',
 'This exercise makes a 6-by-6 RGB image, converts brightness to a 4-by-4 grid and flattens it into 16 values divided by 255. A nearest-neighbour classifier compares those numeric rows; it is not a CNN.',
 'Grayscale can discard useful colour information. Resizing and flattening are different operations. A uniform-colour toy image is far simpler than an everyday photograph.',
 'A 4-by-4 grayscale grid becomes how many values after flattening? Could a new 5-by-5 row be sent to the same 16-input model?',
 'It becomes 16 values. Apply the saved resizing/preparation rule first; the model expects the same input count and ordering.')
concept('image_embedding', [114],
 'Find lit cells in rows and columns of a grid.',
 'A feature vector can summarize a picture without passing every pixel.',
 'Use hand-built measurements when they preserve the information the task needs, and compare their failures with alternatives.',
 'A sideways bar has horizontal spread and little vertical spread. An upright bar reverses that pattern. The lesson gives those two spread values to a nearest-neighbour model.',
 'These hand-built features do not prove that a neural image encoder was trained. Two different images can share the same summary and become indistinguishable.',
 'Would these two spread values alone reliably distinguish a handwritten 6 from an 8? What test would reveal a weakness?',
 'Not necessarily. Find distinct drawings with similar spreads and compare their feature vectors and held-back predictions. A summary must be assessed for the actual task.')
concept('audio', [118,119,120,121],
 'Read a time axis, a frequency in hertz, and a simple wave.',
 'Audio samples record a changing signal. A spectrogram shows frequency content over time; MFCCs summarize a transformed frequency representation.',
 'Use a fixed sample rate and the same feature calculation when comparing recordings.',
 'The script creates low and high tones, saves WAV, extracts frequency features and classifies pitch. A decoded MP3 is checked through the same feature function rather than treated as identical bytes.',
 'A tone classifier does not recognize speech. Compression and sample rate can change values. Extra FFmpeg/media dependencies must be available before running the audio tasks.',
 'Two recordings have different sample rates. May you compare their feature columns without checking how those columns were constructed?',
 'No. Decode and prepare a consistent sample rate, channels and frame procedure, then check feature shape and validation behavior. The same column position must retain the same meaning.')
concept('video', [122,123,124],
 'Complete pixel and small-network bridges; read an array shape.',
 'A video is an ordered sequence of frames. Frame features describe pictures; a sequence model can use their order.',
 'Use a temporal model when motion or order matters rather than a single still image.',
 'The moving dot appears at the same four columns in opposite time orders. A small CNN reads frames, and an LSTM reads the resulting sequence. The script also decodes an MP4 before prediction.',
 'Keep frames from one source clip in the same evaluation group. Toy dot motion is not evidence for reliable recognition in real videos.',
 'If you reverse all frames of a right-moving dot, what changes? Could random frame splitting exaggerate performance?',
 'The direction reverses although the set of frames is unchanged. Splitting related frames can leak clip information; split by independent source clip or recording session as needed.')
concept('power', [139,140,141],
 'Read a graph and distinguish zero from a positive value.',
 'Power transformations reshape numerical gaps using parameters learned from training data.',
 'Try them when a skewed feature or model assumptions suggest a reason, and compare validation evidence.',
 'Box–Cox requires strictly positive values. Yeo–Johnson accepts zero and negative values. The fitted transformation is reused for new signal readings before the cost model.',
 'A more symmetric-looking histogram is not proof of better predictions. Fit parameters within training, and do not shift inputs arbitrarily merely to make a command run.',
 'A feature contains −4, 0 and 14. Which of these two methods can accept it directly?',
 'Yeo–Johnson. Box–Cox cannot directly accept its nonpositive entries. Suitability and validation still decide whether transforming is useful.')
concept('quantile', [142,143,144],
 'Sort numbers and explain rank.',
 'A quantile transformation maps training ranks to a chosen output distribution.',
 'Use it when a model benefits from the changed spacing and the distortion is acceptable.',
 'Training readings can be mapped across a uniform scale or a normal-shaped scale. The distances between original readings change; new rows use the saved training mapping.',
 'The method does not recover a true normal-generating process. Ties and values beyond the training range need inspection; an inverse can only reflect the fitted mapping.',
 'If two different readings are close in rank but far apart in original units, will rank scaling preserve that large physical gap?',
 'Not necessarily. It changes spacing based on ranks. Keep original units available for interpretation and validate whether losing gap information helps the task.')
concept('bins', [145],
 'Place a value between two stated limits.',
 'Binning puts a continuous measurement into one of several intervals.',
 'Use bins when a coarse representation is useful and the information lost inside an interval is acceptable.',
 'The lesson learns training edges and makes indicator columns for bins. Two readings inside the same interval receive the same bin representation.',
 'An edge convention determines which interval owns a boundary value. Relearning edges on each request changes what a column means.',
 'Read the printed edges. If readings 20 and 30 fall in the same bin, can a model receiving only that bin distinguish them?',
 'No. It sees the same representation. Compare this loss with using the original signal, and keep training edges fixed for later rows.')
concept('polynomial', [146,166,168,364],
 'Calculate 2 × 2 and 2 × 2 × 2; keep validation separate.',
 'Polynomial features add powers and products so a linear model can represent curved relationships.',
 'Try a small degree when a curve is plausible, then check whether the added flexibility helps on validation rows.',
 'For one input x = 2, the degree-three row is x, x², x³ = 2, 4, 8. These are three features from one measured input. For x greater than 1, the cubic grows faster than the square. A graph with a logarithmic output axis uses multiplicative spacing, so start with the small table before reading that optional graph.',
 'High powers can grow rapidly outside training and overfit. More columns are not automatically more evidence. Scaling and regularization may matter.',
 'Write the three features for x = 3. Does the cubic term make predictions safe far outside the observed range?',
 'They are 3, 9 and 27. No: large powers can make extrapolation unstable. Choose degree within validation and state the supported range.')

concept('exploration', [148,149,150,151,153,154,155,156,158,159,178],
 'Read horizontal and vertical axes and identify one record.',
 'Exploration asks questions of recorded data using summaries and charts.',
 'Use a chart that answers a particular question before making a modeling decision.',
 'A histogram counts records in weight ranges; a scatterplot puts one delivery at distance and time; a heatmap summarizes correlations; a pair plot shows several pairs. The duplicate route_distance column moves exactly with distance in the tiny sample.',
 'Correlation does not establish cause. Axis scales, missing rows and small counts can change a story. Use training data when exploration guides model choices.',
 'Which chart would show whether longer trips tend to take longer? Which chart would show how often a weight range occurs?',
 'Use a distance-versus-time scatterplot for the relationship and a weight histogram for frequency. Name units and counts; do not infer causation from a sloping cloud.')
concept('importance', [160,161,176,177,195,196,197,198,204,207,214],
 'Explain a held-back score and why a target is not an input.',
 'Model evaluation measures mistakes; permutation importance asks how a fitted model’s score changes when one input is shuffled.',
 'Use importance to investigate model reliance on a particular check set, alongside errors and data knowledge.',
 'The lesson compares classifiers using training folds, checks the chosen rule on kept-back orders, and shuffles distance or weight on separate check rows. A larger score drop suggests more reliance in that check.',
 'Importance is not a cause or a universal property of a field. Correlated inputs can share or hide reliance. A final test is not a repeated feature-selection tool.',
 'Shuffling distance reduces F1. Does this prove making a delivery shorter would cause it to become less urgent?',
 'No. It shows reliance by this fitted model under this check. Causal effects require a suitable design and assumptions, not a shuffled prediction score.')
concept('feature_creation', [162,163,164,165],
 'Read dates and messages; know when the prediction happens.',
 'Feature engineering derives a useful input from recorded information.',
 'Create a feature when its meaning is justified and its source is available at prediction time.',
 'Age is computed at the stated reference date with a birthday check. A separate flag marks the complete word urgent in a message. The same function prepares old and new rows.',
 'A keyword can miss negation or other languages. Age depends on the reference date; using a future reference or later field can introduce unavailable information.',
 'On a date before someone’s birthday, should subtracting birth year alone give their age? Does not urgent mean the same thing as urgent?',
 'Subtract one when the birthday is still ahead. The keyword flag alone does not distinguish not urgent, so inspect and validate that failure rather than treating the flag as meaning.')
concept('feature_selection', [169,170,171,172,173],
 'Distinguish a measurement, an ID and a known answer.',
 'Feature selection chooses a subset of inputs using a stated rule.',
 'Use it to remove unusable/redundant fields or compare a smaller representation, while learning selection inside training.',
 'The script excludes id and duplicate_minutes. ANOVA compares class-related variation in candidate inputs. The chi-square example uses the nonnegative keyword indicator; mere positivity does not make every measurement suitable for that test.',
 'A high score is not causality. Selecting from the full dataset before cross-validation leaks check information. Respect assumptions and check whether selection improves actual validation behavior.',
 'An ID column changes when records are sorted. Should its statistical association automatically make it a good input?',
 'No. Investigate how it was assigned and whether its apparent relationship will exist at prediction time. An accidental identifier association can fail on later records.')
concept('split', range(179,187),
 'Name inputs and answers; count urgent and regular orders.',
 'Training learns, validation chooses, and test checks the frozen choice. A split defines which new-case question is being tested.',
 'Set aside suitable check rows before any data-based preparation or model selection.',
 'The 70/20/10 recipe uses 70 orders for fitting, 20 for choosing tree depth and 10 for testing. Balanced accuracy averages recall within each class: if 8/10 urgent and 18/20 regular are correct, it is (0.8 + 0.9) ÷ 2 = 0.85. This is a reading aid, not the script’s measured result.',
 'A percentage ratio does not establish independence. Keep repeated shipment identity together. Stratification preserves class shares; it does not fix time or customer leakage.',
 'A tree catches 4 of 5 urgent orders and correctly leaves 9 of 10 regular orders unflagged. Calculate balanced accuracy. May you choose its depth from final test answers?',
 'The average of 0.8 and 0.9 is 0.85. Choose depth on validation or inside training cross-validation, then use the final test once for the chosen procedure.')
concept('model_comparison', [187,188,189],
 'Calculate a baseline score and explain validation.',
 'Model comparison tests candidate learning rules on the same task, rows and metric.',
 'Use the simplest justified baseline first, then add candidates whose assumptions suit the input and decision.',
 'The lesson places scaling inside a pipeline and takes the same validation folds for each classifier. A DummyClassifier provides a comparison that learns no useful input relationship.',
 'A larger model is not automatically better. A validation winner is not a final test estimate. Also compare practical requirements and failure types.',
 'One candidate has slightly better validation F1 but cannot meet the agreed response time. Must it be chosen?',
 'No. Check uncertainty and the project constraints. Choose a usable procedure with documented trade-offs, then evaluate the frozen choice separately.')
concept('search', [190,191,192,193],
 'Explain a model setting, validation folds and an error.',
 'A search compares settings. Grid tries a list; random search samples it; Bayesian search uses earlier results to suggest a later trial.',
 'Use a small justified search after a working baseline. Keep each setting’s preparation inside its training folds.',
 'The script varies Ridge alpha and uses the same folds for error comparisons. Its small Bayesian example fits a helper model to tried settings and estimates which untried setting may improve the score.',
 'More search can overfit the validation process. A winning validation score is optimistic as a final claim. Record the search budget and use separate final evaluation.',
 'You try 100 settings and report the best validation result as guaranteed future error. What is missing?',
 'A separate final assessment of the selected procedure, plus counts and limits. The many comparisons used validation information to make a choice.')
concept('cross_validation', [194],
 'Calculate an average error and distinguish training from check rows.',
 'Cross-validation takes turns holding groups back so a procedure is checked on several divisions.',
 'Use it inside model development when the fold design matches the intended new cases.',
 'For three folds, each part is held back once while the other parts train a fresh fit. The lesson prints training size, check size and each fold’s average error in minutes.',
 'Refit imputers/scalers inside each training fold. Random folds are unsuitable for some future-time or repeated-customer tasks. Fold variation is not automatically a confidence interval.',
 'May you scale every row first and then cross-validate a classifier using the scaled table?',
 'Fit a preparation/model pipeline separately inside each training fold. Otherwise its check distribution can influence preparation before the check.')
concept('accuracy', [199], 'Count correct and incorrect category guesses.',
 'Accuracy is correct predictions divided by all predictions.',
 'Use it when correct classifications have a useful common meaning; inspect class counts and error costs too.',
 'If 27 of 30 orders are classified correctly, accuracy is 27 ÷ 30 = 90%. It does not say which three orders were wrong.',
 'Rare urgent orders can be missed while overall accuracy remains high.',
 'There are 99 regular orders and one urgent order. A model always says regular. Is its 99% accuracy enough?',
 'No. It misses the only urgent order. Report the confusion counts, recall and the decision costs.')
concept('precision', [200], 'Count alerts and truly urgent alerts.',
 'Precision is truly urgent alerts divided by all alerts.',
 'Use it to assess how often a review team’s alerts are useful, together with missed cases and capacity.',
 'If 17 of 19 alerts are urgent, precision is 17 ÷ 19, about 89.5%. Two alerts are false alarms.',
 'High precision alone can hide many missed urgent cases. It changes with prevalence and the cutoff.',
 'Eight alerts include six urgent orders. What is precision, and what additional count is needed for recall?',
 'Precision is 6 ÷ 8 = 75%. Recall also needs the total number of truly urgent orders, including missed ones.')
concept('recall', [201], 'Count all truly urgent orders and those detected.',
 'Recall is detected urgent orders divided by all truly urgent orders.',
 'Use it when missed cases matter, while also checking false alarms and team capacity.',
 'If 17 of 18 urgent orders are caught, recall is 17 ÷ 18, about 94.4%. One was missed.',
 'Flagging every order can achieve full recall but overwhelm a team with false alarms.',
 'Six of ten urgent orders are caught. What is recall? Is catching ten by flagging every order necessarily useful?',
 'Recall is 60%. Full recall is only part of the decision; count false alarms and whether reviewers can act on them.')
concept('f1', [202], 'Explain precision and recall.',
 'F1 combines precision and recall with their harmonic mean.',
 'Use it when that balance suits the class of interest, but still report the underlying counts.',
 'When precision and recall are both 0.5, F1 is 0.5. When one is low, F1 is pulled down rather than taking a simple arithmetic average.',
 'F1 ignores true negatives and does not encode every business cost. Zero-denominator handling needs a stated rule.',
 'A business considers misses ten times more costly than false alarms. Does maximizing F1 automatically express that policy?',
 'No. Define the costs and capacity explicitly and choose a cutoff using validation. Report precision and recall beside F1.')
concept('roc', [203,206], 'Explain a false alarm, urgent recall and a score cutoff.',
 'ROC plots the share of urgent cases caught against the share of regular cases falsely alerted across cutoffs. AUC summarizes ranking.',
 'Use it for ranking comparisons; inspect precision-recall and counts when the positive event is rare.',
 'Lowering a cutoff may catch more urgent orders and create more false alarms. The lesson’s two cutoff points are reading practice on fixed check rows, not an invitation to optimize an app on its final test.',
 'AUC is not probability calibration or a chosen operating cutoff. A good ranking can still yield an unusable number of alerts.',
 'Can changing a cutoff improve ranking AUC without changing the model’s scores?',
 'No. It changes the decisions at one operating point; ranking scores stay the same. Choose that decision rule using validation and practical constraints.')
concept('confusion', [205], 'Distinguish actual classes from predicted classes.',
 'A confusion matrix counts each combination of actual and predicted class.',
 'Use it to make missed cases and false alarms concrete before calculating ratios.',
 'Read actual urgent along the row and predicted regular down the column: that cell counts misses. Actual regular with predicted urgent counts false alarms. Write the row and column meanings before reading a number.',
 'Libraries or charts may swap axis conventions. Never infer a cell’s meaning from position or colour alone.',
 'A matrix has actual rows and predicted columns. Where is an urgent order that received no alert?',
 'In actual urgent / predicted regular. Count that cell as a false negative. Explain which class is considered positive.')
concept('regression_errors', [208,209,210,211,212,213],
 'Subtract times and average mistake sizes.',
 'A residual is actual minus predicted. MAE averages its size; RMSE gives large errors more weight; R squared compares squared errors with a mean benchmark.',
 'Use errors in the target’s units to assess number predictions. Inspect counts and individual mistakes beside a summary.',
 'Actual times 30 and 40 with predictions 28 and 36 have errors 2 and 4 minutes. MAE is 3 minutes; RMSE is √10, about 3.16 minutes. A positive residual means the estimate was too short. These are worked arithmetic values, not a new measured experiment.',
 'Two rows teach arithmetic, not stable model performance. R squared’s mean benchmark uses the same check outcomes and is not the trained deployment baseline.',
 'Errors 0, 0, 0, 0, 10 and errors 2, 2, 2, 2, 2 both have MAE 2. Why could a customer prefer the second model?',
 'The first has one very large miss. Examine tail errors, limits and how errors affect decisions, not just a matching average.')
concept('service', [215,216,217,220,221,222,228,229,230],
 'Train a small model and identify its required input names and units.',
 'A prediction service accepts a request, validates inputs and returns an estimate or a clear error.',
 'Use a service when another program needs the saved model. Test locally before considering hosting.',
 'A request supplies distance_km and weight_kg; the response contains minutes. A negative distance should be rejected rather than quietly producing a normal estimate. HTTP status reports success or the kind of failure.',
 'Local test-client calls do not deploy a public server. Valid types do not establish in-scope ranges or reliable predictions. Load only model files you created or trust.',
 'A client sends metres in a field named distance_km. Will a numeric type check detect the mistake? What belongs in the input contract?',
 'Not necessarily. Record units, names, ranges, missing-value rules and unfamiliar-category policy, and test examples that violate them.')
concept('web_form', [218,223,231,232],
 'Explain an input field, a request and a response.',
 'A form collects inputs and displays the service response. It is another way to use the same model contract.',
 'Use it to let a person make a controlled local request after the prediction code works.',
 'Enter a distance, select Predict and read returned minutes. The endpoint must still validate a negative or missing value, even if the browser provides a numeric input control.',
 'A working server test is not a tested browser layout. The practice app is local; it does not establish deployment security or production reliability.',
 'If someone bypasses the form and sends a negative number directly, should the endpoint accept it because the form normally blocks it?',
 'No. Validate at the service boundary and return a clear problem. Show an understandable message in the form as well.')
concept('hosting', [219,224,225,226,227,233],
 'Run the local Flask or FastAPI request example first.',
 'Hosting runs an application on another service’s computers. Packaging and access rules are separate from the prediction calculation.',
 'Use an approved learning account only after local request checks and a cost/removal plan.',
 'These scripts inspect a local request contract. The companion service notes describe preparing files for a selected platform; they do not mean the platform was deployed or tested.',
 'Keep credentials out of code and avoid uploading private data. Platform instructions and costs change. Preserve the prediction route, dependencies and input contract when adapting the module.',
 'A script prints expected HTTP 200. Does that prove a hosted endpoint was called successfully?',
 'No. It is a local expected-contract result. Deployment evidence requires the actual approved service, a request to its endpoint and recorded response, with costs and cleanup checked.')
concept('monitoring', [234,235,236,237,238,239,244,245,246,247,249],
 'Read an error or category score and distinguish prediction from later outcome.',
 'Monitoring watches inputs and measured results over time. Drift means a change worth investigating.',
 'Use it after a model starts receiving new cases, with a named owner and action for each alert.',
 'Later trips may be longer than historical trips. Compare their input distributions, then calculate accuracy or error only after outcomes arrive. A candidate retrained on recent labeled rows needs a separate later comparison with the current model.',
 'Input change alone does not prove worse predictions. An alert does not automatically authorize retraining or replacement. Delayed labels limit what is currently measurable.',
 'West-zone error rises. Name three checks before replacing the model.',
 'Verify units/schema and labels, inspect affected cases and counts, and check changes in routes or population. Use the agreed fallback if needed; compare any candidate fairly before promotion.')
concept('dashboard', [240,241,242,243,248],
 'Divide correct predictions by checked predictions.',
 'A dashboard presents recorded monitoring results; refreshing a view does not retrain a model.',
 'Use a dashboard to help an owner notice a change and decide what to inspect.',
 'Sixteen correct out of twenty is 80%, below the example’s 85% alert line. Eighteen out of twenty is 90%. The local display reloads monitoring data; Tableau and Power BI require the documented import/refresh steps.',
 'Show counts, units, period and refresh time. A green display or a small batch is not proof of reliability; do not calculate new accuracy without outcomes.',
 'The display refreshes every five seconds but outcomes arrive tomorrow. Can today’s newest accuracy be measured every five seconds?',
 'No. Only the view refreshes. Clearly mark which batches have confirmed outcomes and the age of the latest measured result.')

# A shared dataset is not a shared learning goal. Each named operation below
# gets its own question, worked case and application answer for that dataset.
DATASETS = [
 (250,258,'salary','experience and department','salary','A missing salary is a missing training answer, not a blank input to fill.'),
 (259,267,'ferry boarding','age, fare, pass type and family details','priority','The cabin-recorded flag preserves whether a cabin entry was supplied.'),
 (268,276,'house listings','area, rooms and property categories','price','An explicit no-pool category differs from an unresolved field.'),
 (277,284,'flower measurements','sepal and petal measurements','species','The flower names star, fan and bell are invented classes with no ranking.'),
 (285,292,'income records','age, hours and work/education categories','income_group','A sensitive social outcome in invented rows does not validate real-world decisions about people.'),
 (293,301,'drink measurements','alcohol, citric acid and sulphates','quality','The exercise explores both a number and a separately defined higher/lower category.'),
 (302,309,'neighbourhood records','crime_per_1000, rooms, household_income and zone','price','These invented fields are not the historical Boston Housing dataset.'),
 (310,317,'digit drawings','pixel_rows','label','A # is a lit pixel, a dot is dark, and / starts a new row.'),
 (318,325,'shopper records','age, annual_income, score and region','cluster assignment','There are no supplied correct cluster labels. A numeric group ID is just a name.'),
 (326,333,'bank campaign records','age, balance, job, marital, education and prior','subscribed','Current-call duration is unavailable before calling and stays outside prediction inputs.'),
 (334,340,'health-related practice rows','age, cholesterol, blood_pressure, exercise_score and categories','example_label','The fabricated labels have no diagnostic or clinical use.'),
 (341,348,'clothing drawings','pixel_rows','label','The drawings are invented pixels, not the published Fashion-MNIST benchmark.'),
 (349,355,'app listings','price, rating and app categories','installs','Price and install strings need parsing; a huge made-up install count can dominate a tiny regression fit.'),
]


def dataset_profile(number, name):
    start,end,title,inputs,target,specific = next(d for d in DATASETS if d[0] <= number <= d[1])
    low = name.lower()
    prefix = f'The {title} exercise uses {inputs}. Its output is {target}. '
    if low in ('description','source'):
        meaning='A source note states where a table came from; a description explains what one row and each field mean.'
        use=f'Use it before treating the {title} as evidence about a real population.'
        ex=prefix+'These are original invented practice rows, even where the folder preserves an old benchmark name. '+specific
        caution='Do not claim that a historical benchmark was downloaded or that a made-up label was measured. The separate Wine project has its own real source and licence.'
        task=f'Write a source note for this {title} exercise: are the rows invented, what does one row represent, and what does the final answer mean?'
        answer='Say that the rows were created for this workbook, name the row entity and target, and state the limitation. A familiar folder name is not proof of provenance.'
    elif 'missing' in low:
        meaning='A missing-data audit separates missing inputs from missing answers and counts the affected records.'
        use=f'Use it before fitting this {title} exercise; decide which blanks can be recovered or filled.'
        ex=prefix+'Inspect the supplied blank cells before the pipeline learns its training fill values. '+specific
        caution='Do not fill training targets merely to enlarge the sample. Keep check answers out of fill statistics; a clean table can still omit important cases.'
        task=f'Choose a blank input in this {title} exercise. Write which training-only rule would handle it and whether the original fact is recovered.'
        answer='Identify the actual field and its type. A median or category placeholder supplies an estimate/representation, not a recovered measurement. A missing answer remains excluded from ordinary supervised fitting.'
    elif 'outlier' in low:
        meaning='An outlier check identifies an unusual recorded value or pattern without establishing that it is wrong.'
        use=f'Use it to choose source records for review in this {title} exercise.'
        ex=prefix+'Read the printed flags beside their field names, then return to the original row. '+specific
        caution='A rare but valid case should not be deleted just to improve a fit. Pixel outliers need inspection of drawings rather than a parcel-weight rule.'
        task=f'Pick one possibly unusual case in this {title} exercise. List evidence that would justify keeping it, correcting it, or leaving it flagged.'
        answer='Keep a source-confirmed valid case; correct only from a reliable source; preserve uncertainty when evidence is absent. State whether the case belongs within the model’s intended scope.'
    elif any(word in low for word in ('scaling','normalization')):
        meaning='Scaling changes numerical representation using one saved training rule.'
        use=f'Use it when units or pixel ranges affect the model in the {title} exercise.'
        ex=prefix+('Dividing pixel intensity by 255 maps the known 0–255 representation to 0–1; it does not estimate an image-specific maximum. ' if 'drawings' in title else 'Learn numeric scales from training rows and apply them unchanged to the kept-back rows. ')+specific
        caution='Do not fit a fresh scale to each request. An ordinary linear model may retain its predictions after rescaling; distance models or penalties can behave differently.'
        task=f'Explain one actual scaled input in this {title} exercise. Would changing only that input’s unit during prediction preserve the contract?'
        answer='Name the input, original unit/range and training rule. The same rule and units must prepare later rows. Changing only the request unit makes the saved model interpret a different quantity.'
    elif any(word in low for word in ('encoding','categor')):
        meaning='Encoding gives a name a consistent numeric representation while preserving whether it is an input category or an answer label.'
        use=f'Use it before the numeric estimator receives the {title} fields.'
        ex=prefix+'Read the script’s selected category fields or target encoder. A class ID names a class; it does not turn that class into a measured amount. '+specific
        caution='Do not invent a category ranking or fit a separate column list on new rows. One-hot target labels in a drawing demonstration are separate from input encoding.'
        task=f'Find one category or target label in this {title} exercise. Is it a model input or the answer? What happens if a new name arrives?'
        answer='Trace the named field into features or target. Inputs use the saved category schema; unknown names need a stated policy. Targets remain the known classes the classifier was trained to distinguish.'
    elif 'resizing' in low:
        meaning='Resizing changes an image’s row and column count.'
        use='Use it when a model expects one fixed image shape.'
        ex=prefix+'An 8-by-8 grayscale image has 64 pixels; a 10-by-10 version has 100. '+specific
        caution='More pixels do not create new measured detail. Choose an interpolation rule suited to the task and reuse it for all splits.'
        task='Resize a copy to 10 by 10. Predict the number of pixels and explain why that is not flattening.'
        answer='There are 100 pixels. Resizing changes the grid; flattening rearranges an existing grid into one row without changing its element count.'
    elif 'flattening' in low:
        meaning='Flattening arranges an existing grid into a one-dimensional sequence.'
        use='Use it for an estimator expecting one feature row per image.'
        ex=prefix+'A 5-by-5 grid becomes 25 values. C order reads rows first; F order reads columns first.'
        caution='Training and prediction must use the same traversal order. Flattening removes explicit spatial arrangement from the input shape.'
        task='Switch the traversal order, then reconstruct using that same order. Should the original grid be recovered?'
        answer='Yes. Matching flatten and reshape orders recover the grid. Mixing the orders can rearrange pixels and corrupt the representation.'
    elif number == 266:
        meaning='Feature extraction makes a new input from recorded fields, using the same rule for old and new rows.'
        use='Use family size when the source definitions make the combined count meaningful for this boarding task.'
        ex='The lesson uses family_size = 1 + siblings + parents. With siblings=1 and parents=2, the value is 4: the traveler plus three recorded accompanying relatives.'
        caution='Confirm the source meaning of each count. Do not count the traveler twice or use relatives learned only after the decision.'
        task='A new row has siblings=0 and parents=1. Calculate family_size. Must the rule be relearned from that request?'
        answer='The value is 2. This fixed definition is applied consistently, not fitted anew. Any learned preparation and model remain trained on the training rows.'
    elif number == 275:
        meaning='A target transformation changes the answer scale during fitting and reverses that change for reported predictions.'
        use='Try a log target when prices have a long upper tail and the resulting error trade-off fits the decision.'
        ex='The lesson wraps a cloned model in TransformedTargetRegressor with log1p and expm1. log1p(price) is used while fitting; expm1 maps the model output back to price units before the kept-back comparison.'
        caution='Do not report a log-price as a price. Reversing a log fit does not automatically estimate the conditional mean price; compare the original-unit errors and the decision need.'
        task='A fitted model returns a value on the log1p-price scale. Which operation returns the price scale, and which rows choose whether that fit is useful?'
        answer='Use expm1, the inverse of log1p, then compare errors in the original price unit on validation. Keep final test answers out of choosing the transformation.'
    elif any(word in low for word in ('feature extraction','visualization','skewed')):
        meaning='Inspect or derive a representation for a stated data question before using it in a fit.'
        use=f'Use this focused task to explain what the {title} representation keeps and changes.'
        ex=prefix+specific+' Keep the original fields beside the derived value or chart so its meaning can be checked.'
        caution='A clearer picture or a transformed target is not proof of improved validation. Reverse a target transform before interpreting predictions in original units.'
        task=f'Explain one original field and its derived value or plotted point in the {title}. What information could the change lose?'
        answer='Name the actual field, units and transformation or axis. Identify the retained meaning and any discarded detail; compare a justified alternative using validation rather than appearance alone.'
    else:
        meaning='A complete practice pipeline connects input preparation with a fit and a separate check.'
        use=f'Use this {title} exercise to trace one row through the supplied workflow.'
        ex=prefix+specific+' Find one kept-back row and compare its prediction with its recorded answer where a confirmed answer exists.'
        caution='The tiny invented table illustrates mechanics. Two correct predictions, a cluster assignment or a familiar benchmark name does not establish real-world performance.'
        task=f'Write a three-line handoff for the {title}: input contract, result meaning, and one reason the result may fail on new cases.'
        answer=f'Name {inputs}; explain {target} in the appropriate unit or category; state a specific missing population, recording problem or representation limit. Use more suitable independent data before making a general claim.'
    return ('Read the named fields and explain the preparation taught earlier.',meaning,use,ex,caution,task,answer)

concept('linear', [356,357,358,359,360,431,432,434,435,436],
 'Name predictors and a numeric target; calculate an error in minutes.',
 'Linear regression learns an intercept and input weights for a numerical prediction. Simple regression uses one input; multiple regression uses several.',
 'Use it as an interpretable baseline when a straight-line/additive relation is plausible over the supported range.',
 'A delivery rule might start with a fixed preparation time and add minutes for km and kg. The fitted coefficients describe that model’s associations, not guaranteed real-world effects. The lesson compares predictions with held-back measured times.',
 'Inputs may overlap, important factors may be absent, and a line can extrapolate implausibly. Good training fit is insufficient.',
 'Does a positive fitted weight for km prove that changing only route length will cause exactly that many extra minutes in the world?',
 'No. It describes the fitted association under this data and model. State the inputs, units, supported range and independent-check errors.')
concept('penalties', [361,362,363],
 'Read an intercept and input coefficients; explain validation and scaling.',
 'Regularization discourages some complex fits. Ridge penalizes squared weights; Lasso uses an absolute-weight penalty and can make some coefficients zero.',
 'Compare a penalty when noisy, overlapping or numerous inputs make an unpenalized fit unstable.',
 'Run the companion penalty_lab.py to compare coefficients and validation MAE at several alpha values on the same split. Its scaler is fitted on training only, so a displayed coefficient corresponds to a one-training-standard-deviation input increase. The final test is used after choosing the setting.',
 'Larger alpha can remove useful signal. Individual correlated-feature coefficients need not move monotonically. A zero coefficient does not prove a field never matters. Do not compare penalties across arbitrary input units without checking scaling.',
 'A setting has smaller coefficient magnitudes but worse validation MAE. Is smaller automatically better? Which rows choose alpha?',
 'No. The penalty is a trade-off, not the goal. Choose a useful validation result with its limits; preserve the final test for the frozen choice.')
concept('svr', [365], 'Explain scaled inputs, a validation error and a model setting.',
 'Support vector regression fits a rule with a margin of tolerated error and a penalty for larger deviations.',
 'Consider it for a numerical target when a suitable kernel and scaling can describe the relation.',
 'The script scales km and kg before SVR and estimates delivery minutes for new rows. Its C setting controls a fit/penalty trade-off; the model’s predictions are still measured against actual held-back times.',
 'Scaling and settings matter, and extrapolation may be poor. A default setting is not an established best choice.',
 'Should you choose C by rerunning the final test until its error is smallest?',
 'No. Compare justified settings within validation or training cross-validation. Freeze the procedure before the final check.')
concept('regression_tree', [366], 'Read a threshold decision and an average.',
 'A regression tree divides inputs by conditions and predicts a numerical value within a final region.',
 'Use it for nonlinear splits and interactions when interpretability and stability are checked.',
 'A split might ask whether distance is above a learned threshold. Cases reaching a leaf receive its learned value. The script limits depth to reduce how finely the training table is divided.',
 'Deep trees can memorize; small changes can alter splits. Ordinary trees do not extend a trend beyond their training target values.',
 'Two new deliveries fall into the same leaf. Must their predicted times differ because their distances differ?',
 'No. A standard leaf gives the same learned prediction to both. Check whether that coarse behavior suits the task.')
concept('forest', [367,376], 'Explain one tree and separate check rows.',
 'A random forest combines trees fitted with randomized training samples and input choices.',
 'Use it to compare an ensemble with a single tree on the same validation problem.',
 'For regression the trees’ time estimates are averaged. For classification their class probabilities are averaged before a decision. Many trees can reduce some variation without removing every bias.',
 'More trees do not fix leakage, unrepresentative data or an invalid target. Importance scores do not establish causes.',
 'Every tree learned from a leaked future field. Will averaging hundreds of trees remove that leakage?',
 'No. Fix the prediction-time inputs and fair split first, then compare valid procedures.')
concept('boosting', [368,369,370,378,379,380], 'Explain a fitted tree, an error and validation.',
 'Boosting adds models in sequence so later components address remaining fitting errors under a chosen loss.',
 'Consider it for structured-table tasks after a simple baseline, with controlled complexity and validation.',
 'The supplied boosting model receives distance and weight. Read prediction minutes for regression or late/on-time labels for classification, then inspect held-back errors. XGBoost and LightGBM are separate implementations with their own settings.',
 'Sequential fitting can overfit; model size, learning rate and tree complexity need care. Package availability and fast execution are not evidence of better learning.',
 'A boosted model beats a baseline on training but loses on validation. Should it replace the baseline?',
 'Not on that evidence. Keep the stronger validated procedure or investigate a justified simpler setting without using the final test for selection.')
concept('logistic', [371,372,437], 'Count two classes and explain a probability cutoff.',
 'Logistic regression estimates class probabilities from a weighted input score; it is a classifier despite its name.',
 'Use it as a classification baseline and inspect calibration and threshold trade-offs for the decision.',
 'The lesson uses km and kg to predict late=1 or on-time=0. A score becomes a class through a decision rule; the measured class checks the prediction.',
 'A predicted probability is not a promise. Accuracy alone can hide a rare class, and the standard cutoff may not match review costs.',
 'Would a 0.7 late probability guarantee this one delivery will be late?',
 'No. It expresses a model probability whose reliability needs checking across suitable confirmed cases.')
concept('knn', [373], 'Read distance between two scaled input rows.',
 'K-nearest neighbours classifies using the labels of nearby training cases.',
 'Use it when the chosen representation and distance make nearby cases meaningfully comparable.',
 'The script scales km and kg before looking at five neighbours. Their labels supply evidence for the new delivery’s class.',
 'Unscaled units can dominate distance. Too many irrelevant inputs, few neighbours or a new population can make similarity misleading.',
 'Changing kg to grams without changing the saved preparation changes which neighbours? Why can that matter?',
 'It can make weight dominate a raw distance. Keep consistent units and fit scaling within training, then validate the neighbour rule.')
concept('svm', [374], 'Explain a boundary, scaled inputs and two classes.',
 'A support vector classifier learns a separating boundary with a margin and penalties for violations.',
 'Consider it when a suitable scaled representation and kernel can separate the task’s classes.',
 'The pipeline scales delivery km and kg before fitting SVC. Later rows pass through that same scale and receive a class label.',
 'A class label alone is not a calibrated probability. Kernel/settings and sample size affect practicality and generalization.',
 'A point far outside the training range receives a class. Does the boundary establish reliable evidence there?',
 'No. Inspect scope and distance from training coverage, and use a stated fallback or new suitable evidence.')
concept('classification_tree', [375], 'Read a yes/no condition and count classes.',
 'A classification tree learns conditions that divide rows into regions with class evidence.',
 'Use it for threshold/interacting patterns while controlling depth and checking separate cases.',
 'A branch asks about one input, then another. A new delivery follows the same conditions to a leaf; its class comes from the training evidence there.',
 'Deep leaves can contain very few cases. A readable rule is not automatically a reliable or causal rule.',
 'A leaf contains one urgent training order and no others. Should its apparently perfect training purity establish certainty?',
 'No. One case is weak evidence. Check independent rows, constrain complexity and report the available counts.')
concept('naive_bayes', [377], 'Read class proportions and a simple probability.',
 'Naive Bayes combines class evidence under a conditional-independence assumption; GaussianNB models each numeric input with a class-specific bell-shaped distribution.',
 'Use it as a simple fast classifier when its assumptions are reasonable enough for the task.',
 'The lesson learns km and kg distributions within late and on-time classes and combines their evidence for a new delivery.',
 'Correlated inputs can violate its simplifying assumption. Useful classification does not establish well-calibrated probabilities.',
 'If two input columns duplicate the same measurement, does the model gain two independent pieces of evidence?',
 'No. The repeated information can be counted too strongly under the independence assumption. Inspect redundancy and validate the result.')
concept('cluster_classifier', [381], 'Distinguish a discovered cluster ID from a confirmed class.',
 'A cluster-to-class mapping adds a supervised decision rule to an unsupervised grouping.',
 'Use it as a specific constructed baseline, not as a claim that ordinary K-Means is supervised.',
 'The script forms two clusters from training inputs, then maps each to its most common known training label. New cluster IDs are translated using that saved mapping.',
 'Clusters need not correspond to classes. Do not use test labels to assign the cluster names or choose K.',
 'If cluster 0 mostly contains the class long, can you call every future cluster 0 long after refitting?',
 'Not automatically. Cluster IDs may change between fits. Learn and save the mapping with each training procedure.')
concept('kmeans', [382,383,384,385,438], 'Compare scaled measurements and group means.',
 'Clustering groups inputs without supplied group labels. K-Means chooses K centres and assigns cases by its distance rule.',
 'Explore whether profiles help a decision; compare sensible K values and data without clear groups.',
 'Scale age, income and spending, then read each of the three groups in original units. A new shopper uses the saved scale and centres.',
 'IDs are arbitrary names. K-Means favours certain shapes and can impose groups where none are useful.',
 'Old group 0 resembles new group 2 after refitting. Must the shoppers have changed?',
 'No. Compare profiles, membership and stability rather than numeric IDs.')
concept('hierarchy', [386], 'Read distance and trace a tree from its leaves.',
 'Hierarchical clustering joins groups; a dendrogram records join order and distances.',
 'Explore nested grouping and compare possible cuts.',
 'Leaves name shoppers. A horizontal cut crossing three branches gives three groups. The paired scatterplot shows only two of the three inputs.',
 'Height depends on scaling and linkage. This example refits the whole table; it has no saved new-row predict method.',
 'Move the cut upward so it crosses fewer branches. What changes?',
 'The number of groups decreases as branches merge. Explain the cut from the joins, not colours alone.')
concept('dbscan', [387], 'Explain nearby points and a dense region.',
 'DBSCAN links dense neighborhoods and can leave isolated cases as noise.',
 'Use it when density is meaningful and fixed K is undesirable; check scaling and density variation.',
 'eps controls neighborhood distance; min_samples controls the local count. Label −1 means the rule did not assign the case to a dense group.',
 'Noise is not proof of a bad record. One global density rule can struggle with unequal group densities.',
 'An isolated source-confirmed shopper gets −1. Delete the record?',
 'No. Review the density rule and intended analysis; preserve confirmed facts.')
concept('mixture', [388], 'Read a probability and a cluster profile.',
 'A Gaussian mixture uses overlapping components and gives membership probabilities under that fitted model.',
 'Use soft assignments when overlapping groups are a reasonable modeling idea.',
 'A shopper may have evidence spread across components. Read the printed probabilities as well as the chosen component.',
 'Components are model shapes, not established customer types. Membership probability is not probability of a business outcome.',
 'A case gets 0.51 and 0.49 for two components. What should the report say?',
 'The assignment is weak under this model. Report the ambiguity rather than a certain identity.')
concept('pca', [389,390,439], 'Explain numerical columns and spread.',
 'PCA combines inputs into directions retaining variance.',
 'Use it for compression or exploration of overlapping measurements, checking whether useful prediction information survives.',
 'Three scaled inputs become two mixed columns. Explained variance describes retained spread, not accuracy. Later rows use the same scale and projection.',
 'Large variance need not be useful signal. Scale matters; component signs can reverse without changing information.',
 'Does retaining 95% of input variance retain 95% of information needed for a rare-event prediction?',
 'Not necessarily. Check the complete prediction pipeline on suitable validation rows.')
concept('tsne', [391], 'Compare nearby rows and read a two-axis plot.',
 't-SNE draws a low-dimensional view emphasizing local neighbors.',
 'Inspect local structure in the displayed sample and compare settings.',
 'The lesson projects scaled long, wide and score into two display coordinates. The axes have no original physical unit.',
 'Distant gaps, group sizes and orientations can mislead. This example refits the sample rather than transforming separate new rows.',
 'Are far-apart islands a reliable distance in the original units?',
 'No. Inspect original measurements and neighbors before interpreting the gap.')
concept('lda', [392], 'Explain supplied labels and a projection.',
 'LDA uses known class labels to find separating directions under its assumptions.',
 'Use it as a supervised projection/classifier with suitable validation.',
 'The fit receives group labels. New inputs use the saved projection without their true answers. With C classes, the discriminant projection has at most C−1 directions.',
 'This is supervised. A separated training picture does not establish held-back performance.',
 'May final test labels help fit the projection before evaluating a classifier?',
 'No. Fit the supervised projection inside training; otherwise it leaks test answers.')
concept('ica', [393], 'Explain a mixed signal and vector.',
 'ICA seeks components that are statistically more independent under a mixing model.',
 'Use it when source-separation assumptions and interpretation are plausible.',
 'Two microphones hearing two speakers illustrate mixing. The lesson projects measured columns; it does not establish that physical sources were recovered.',
 'Component order, sign and scale can be ambiguous. Convergence and source meaning need checks.',
 'A component reverses sign between fits. Must its information have changed?',
 'Not necessarily. Compare patterns and reconstructions, accounting for sign/order ambiguity.')
concept('anomaly', [394,395,396,440], 'Read a training reference and unusual parcel.',
 'An anomaly detector flags inputs unlike its reference under a selected rule.',
 'Prioritize source review using a suitable reference and acceptable alert workload.',
 'Isolation Forest uses random partitions; One-Class SVM learns a reference boundary. Here −1 flags a new parcel unlike routine training measurements.',
 'A flag proves neither harm nor recording error. An incomplete or contaminated reference changes what looks unusual.',
 'A valid new parcel type repeatedly gets flagged. What comes before deleting it?',
 'Verify its source and scope, inspect counts and examples, then validate any reference or service-policy change.')
concept('zscore', [397], 'Explain a mean and standard deviation.',
 'A z-score measures distance from a reference mean in reference standard deviations.',
 'Use a simple review rule only when reference spread and distribution are meaningful.',
 'A z-score of 3 means three training standard deviations above the training mean, not a weight of 3 kg.',
 'Zero spread makes ordinary z-scoring undefined. Skew and extreme reference values affect the rule.',
 'Should a new request change the reference mean used for its own score?',
 'No. Keep the fitted reference; updating it is an explicit monitored training change.')
concept('association', [398,399,400,401,441], 'Count baskets and fractions.',
 'Support measures co-occurrence share; confidence conditions on a rule’s starting item.',
 'Explore item patterns, then check whether they support a useful action.',
 'Milk and bread in 3 of 5 baskets give 60% pair support. If 4 baskets contain milk, milk→bread confidence is 3/4 = 75%. Apriori and FP-Growth search frequent sets differently.',
 'Confidence is not cause and may be high for a common consequent. Five baskets cannot establish a stable retail policy.',
 'Must milk→bread and bread→milk have equal confidence?',
 'No. They have different conditional denominators. Their pair support is the same.')
concept('s3vm', [402,403,404], 'Separate confirmed labels from unlabeled inputs.',
 'Semi-supervised learning uses confirmed labels and unlabeled training inputs under extra assumptions.',
 'Consider it when labels are scarce and unlabeled structure plausibly helps.',
 'This tiny SVM enumerates balanced label assignments for four unlabeled points and compares weighted objectives. New-row guesses have no confirmed answers, so do not measure accuracy.',
 'Guesses are not facts. The search grows exponentially and its balance constraint is an assumption.',
 'May guessed labels count as confirmed evaluation successes?',
 'No. Compare with a labeled-only baseline on separate confirmed answers.')
concept('label_propagation', [405], 'Explain similarity and missing labels.',
 'Label propagation spreads evidence between nearby training points.',
 'Use it when neighborhoods reasonably correspond to the wanted classes.',
 'The lesson retains four confirmed labels per class, masks other training labels, then checks a separate labeled holdout.',
 'A wrong seed or unsuitable scale can spread mistakes. Holdout answers must not enter the fitting graph.',
 'Classes overlap under the chosen distance. Does more unlabeled data guarantee improvement?',
 'No. It may strengthen wrong links; compare with a labeled-only baseline and inspect confirmed mistakes.')
concept('self_training', [406,409], 'Explain confidence and a labeled check.',
 'Self-training adds confident model guesses as temporary training labels.',
 'Experiment only with a justified confidence rule and independent confirmed evaluation.',
 'Fit from known labels, add sufficiently confident guesses, and compare with the original baseline on the same untouched answers.',
 'Confidence may be wrong or poorly calibrated. Repeating guesses can reinforce early errors.',
 'Many pseudo-labels are added but held-back performance does not improve. Is adding them itself success?',
 'No. Added guesses are a mechanism. Prefer the better justified procedure and report actual evaluation.')
concept('co_training', [407], 'Distinguish two measurements of one case.',
 'Co-training exchanges confident guessed labels between models using different views.',
 'Consider it when views are complementary and label assumptions are defensible.',
 'One classifier uses x, another y. They exchange a limited number of guesses and combine evidence for held-back cases.',
 'Views can share a bias. Agreement is not independent confirmation of truth.',
 'Both models confidently make the same error on a new population. Does agreement prove correctness?',
 'No. Inspect confirmed answers and coverage assumptions; report agreement separately from accuracy.')
concept('semi_regression', [408], 'Calculate a numeric prediction error.',
 'A semi-supervised regression heuristic can add guessed numbers where regressors agree.',
 'Treat it as an experiment against a confirmed-label baseline.',
 'The lesson adds values where two regressors agree. Its supplied held-back error worsens after adding guesses, showing why comparison matters.',
 'Agreement does not establish a true answer. Never replace a test answer with the model’s own prediction.',
 'Guessed training values increase held-back MAE. What should you keep and report?',
 'Report the worse error and keep the stronger baseline. More rows do not automatically mean better evidence.')
concept('rl_return', [410,411,418], 'Read state, action and reward on a track.',
 'A policy chooses actions. Return adds rewards; a value function is an expected return under a policy.',
 'Use sequential reasoning when actions affect later situations.',
 'The five-cell track gives −0.02 for ordinary moves and +1 at the goal. Discounting weights later rewards less. This script follows one fixed route, not a stochastic expectation.',
 'One rewarded move does not establish a reliable policy. A designed reward may miss the real goal.',
 'Can changing move rewards change the preferred policy on an unchanged track?',
 'Yes. Review reward meaning and evaluate behavior across suitable trials.')
RL_WORDS = {
 412:('agent','the learner choosing a move','Who chooses an action?','The agent chooses; the environment decides the resulting transition.'),
 413:('environment','the world and transition rules','Who determines what happens at the track edge?','The environment transition rule determines the next state and reward.'),
 414:('action','an available choice, left or right here','Must both actions from one cell have the same result?','No. Read each state/action transition. Codes 0 and 1 mean left and right here.'),
 415:('state','the information available now for choosing','Can the same action differ from two starting cells?','Yes. The transition depends on the current state as well as the action.'),
 416:('reward','a number received after a move','Does a high immediate reward guarantee the best route?','No. Compare later consequences and total or discounted return.'),
 417:('policy','a rule for choosing actions','Does this fixed right-moving policy learn its rule?','No. This rule is supplied. The Q-learning lesson later learns action values.'),
}
for n,(term,meaning,task,answer) in RL_WORDS.items():
    concept('rl_'+term,[n],'Trace a move from a known cell.',
      f'{term.capitalize()} means {meaning}.','Use this term to explain its particular part of a sequential decision.',
      'Read state, action, next_state, reward and done in one CSV row; compare it with the requested move.',
      'Codes are conventions. Printing a transition does not establish a learned or reliably evaluated policy.',task,answer)
concept('q_learning', [419,420,425], 'Explain state, action and discounted return.',
 'Q-learning updates a table of action values from observed transitions and later estimated values.',
 'Use a small table when states/actions are manageable and interaction is appropriate.',
 'The agent explores sometimes, otherwise choosing its largest value. It updates the observed entry; a terminal goal adds no next-action value.',
 'Early greedy choices can prevent discovery. Learning depends on exploration and sufficient suitable experience.',
 'If all values start at zero and the agent never explores, what can remain untested?',
 'Moves not selected by initial tie-breaking can remain untested. Inspect experience coverage and evaluate the policy.')
concept('dqn', [421], 'Complete the network bridge and one Q update.',
 'DQN uses a neural network to approximate action values instead of a separate table entry for each state.',
 'Study its mechanics on the track before a larger control task.',
 'A one-hot state yields left/right values. Replay stores transitions; a target copy supplies later values. A terminal mask stops future value being added after the goal.',
 'This complete tiny replay batch does not establish robust control, safe exploration or image understanding.',
 'Why does a terminal goal target contain no next-state value?',
 'The episode ended, so no later action rewards follow within that return.')
concept('policy_gradient', [422,423,426], 'Read a probability and expected reward.',
 'Policy gradient changes action probabilities from rewards. Actor–critic also learns a baseline value.',
 'Study probabilistic action choice and evaluate the resulting policy separately.',
 'In the two-button task the actor changes logits. The critic estimates reward, and reward minus that estimate changes the actor update. This is a one-state bandit illustration.',
 'One lucky reward is not evidence of the better action. Randomness and reward design matter.',
 'Swap reward chances while keeping button order. What should be checked?',
 'Check adaptation toward the more rewarding button across suitable trials, reporting reward and variability rather than one fixed action.')
concept('mcts', [424], 'Trace a tree and route return.',
 'MCTS explores simulated futures to guide a current action.',
 'Use it with an appropriate simulator and acceptable planning cost.',
 'The track search expands branches, balances return and exploration, rolls out continuations and backs up returns. First-action visits summarize the search.',
 'A wrong simulator yields misleading plans. Search budget, horizon and reward affect the result.',
 'Does a rarely visited branch alone prove a bad move?',
 'No. It may need exploration; interpret visits with returns and the available simulation budget.')
concept('model_based', [427,428,429], 'Read transitions and distinguish observations from given rules.',
 'Model-based planning uses a supplied or learned representation of action consequences.',
 'Plan when transition predictions and their uncertainty are appropriate for the decision.',
 'The lesson compares a given deterministic rule with a lookup learned from one observation per state/action pair, then looks ahead through possible moves.',
 'One observation per pair suffices only for this deterministic toy. It does not establish probabilities for an uncertain task.',
 'A move sometimes slips left and sometimes right. Store its first result as a certain rule?',
 'No. Gather observations and represent transition uncertainty, then evaluate the planner under those outcomes.')
concept('categories', [430], 'Name numbers, categories, groups and rewards.',
 'Learning categories describe the available feedback and the learning task.',
 'Choose a workflow from the question rather than memorize every algorithm.',
 'Known answers suggest supervised learning; unlabeled grouping is unsupervised; mixed labels can motivate semi-supervised methods; actions and rewards motivate reinforcement learning.',
 'Numeric class IDs do not turn classification into regression. One product can combine tasks.',
 'A robot classifies pictures and learns routes from rewards. Must it have only one learning category?',
 'No. Its components have different feedback, outputs and evaluation.')
concept('multioutput', [433], 'Distinguish several predictors from several outcomes.',
 'Multiple regression uses several predictors; multivariate/multioutput regression predicts several numeric targets.',
 'Use several outputs when each has defined meaning and suitable training/check answers.',
 'The lesson predicts minutes and a separately constructed fuel value from distance and weight. Each output needs its own unit and error interpretation.',
 'Fuel is a created teaching rule, not measured consumption. Do not combine litres and minutes into an unexplained score.',
 'Does adding weight as a second input make a single-time-output task multioutput?',
 'No. Multioutput needs multiple target columns, each evaluated meaningfully.')
concept('split_choice', [442], 'Read a held-back row and error in minutes.',
 'A split defines the new-case question: comparable orders, unseen customers or later dates.',
 'Choose the question before inspecting which split produces the best score.',
 'MAE averages mistake sizes: actual 30 versus prediction 27 is an absolute error of 3 minutes. The script prints shared shipment IDs, shared customer IDs and date order before MAE.',
 'No shared shipment IDs is not sufficient for every job. Customer ID is deliberately included here to illustrate known versus unseen customers, not as a universal input recommendation.',
 'A model must handle new customers next month. What checks can a random split miss?',
 'Keep customers unseen for the new-customer question, and consider later-time evaluation for future use. Design combined evaluation for the actual job.')
concept('overfitting', [443], 'Read training and validation errors in the same units.',
 'Overfitting helps the training fit while harming performance on separate relevant cases.',
 'Use validation to select complexity before a final test.',
 'Depth varies while training and validation errors are printed together. A deep tree can nearly memorize training while losing to a shallower tree on validation.',
 'A gap concerns these samples, not every future case. Repeated choices using test results consume that test.',
 'Depth 25 wins training; depth 3 wins validation. Which proceeds to final assessment?',
 'Depth 3 on that evidence. Freeze the procedure, then report separate test errors, counts and limitations.')
concept('threshold', [444], 'Calculate precision and recall from counts.',
 'A cutoff converts fixed scores into actions, changing alerts without retraining the model.',
 'Choose it on validation using misses, false alarms, costs and capacity.',
 'The script picks highest precision among candidates meeting minimum validation recall. This illustrates one constraint; it does not automatically enforce staffing capacity.',
 'Lowering a cutoff can overwhelm reviewers. A validation recall target is not guaranteed on a new population.',
 'A rule creates 100 alerts daily but reviewers can handle 20. Is recall alone enough?',
 'No. Check validation workload and costs against agreed capacity and decide a practical policy or fallback.')
concept('calibration', [445], 'Read probabilities and group outcome fractions.',
 'Calibration asks whether similar predicted chances correspond to similar observed event rates.',
 'Check it when probability values inform decisions, alongside ranking and counts.',
 'Train the base forest, fit a sigmoid adjustment on separate validation rows, then compare test probabilities. Brier score averages squared probability errors; it reflects more than calibration alone.',
 'More chart bins change grouping, not the underlying Brier score. Small bins are uncertain and adjustment need not improve a particular test.',
 'Does a 0.7 average predicted chance guarantee seven successes in the next ten cases?',
 'No. Assess rates across suitable groups with counts and uncertainty, not promises for one small batch.')
concept('group_errors', [446], 'Calculate MAE and a training-median baseline.',
 'Group evaluation finds different error behavior hidden by an overall average.',
 'Inspect meaningful routes, missing inputs and zones with counts beside scores.',
 'The lesson checks later deliveries, compares model and baseline in minutes, then groups errors. Reporting-boundary changes affect membership, not already-computed predictions.',
 'Small-group scores are uncertain. Inspect actual cases before claiming a cause or repeatedly selecting from final-test subgroup results.',
 'A missing-weight group has high MAE and few orders. What belongs in the report?',
 'Its count, error, underlying cases, missingness pattern and limitations; investigate source/pipeline behavior and check further suitable examples.')
concept('capstone', [447], 'Complete preparation, fair checks, baseline, API and monitoring.',
 'A checked workflow connects an input contract to learning, choice, evaluation, saved preparation and later use.',
 'Explain the guided workflow before attempting the independent project.',
 'Split whole dates, compare Ridge with a training-median baseline, save the winner, validate requests, then compare a later labeled batch. Missing weights use the saved training preparation.',
 'Synthetic results do not prove real-service quality. Valid inputs, accuracy, operational readiness and permission to deploy are separate questions.',
 'A valid request is accepted but West-zone errors rise. Does input validation prove continued usefulness?',
 'No. Inspect measured outcomes, counts and source changes. Apply the agreed fallback and compare any replacement fairly before promotion.')

ROWS = list(csv.DictReader((ROOT / 'coverage.csv').open(encoding='utf-8-sig')))
for row in ROWS:
    number = int(row['ID'])
    if 250 <= number <= 355:
        concept('dataset_' + str(number), [number], *dataset_profile(number, row['Lesson name']))
if set(LESSON_PROFILES) != set(range(1,448)):
    raise ValueError('Unmapped lessons: ' + str(sorted(set(range(1,448))-set(LESSON_PROFILES))))

BEGIN = '<!-- teaching-note:start -->'
END = '<!-- teaching-note:end -->'


def teaching_note(row, folder, workbook=False):
    number = int(row['ID'])
    p = PROFILES[LESSON_PROFILES[number]]
    # Goals remain entry-specific even when a demonstration is shared.
    readme = (folder/'README.md').read_text(encoding='utf-8')
    goal = re.search(r'## Your goal\s+(.+?)(?=\n\n)',readme,re.S).group(1).strip()
    sample = folder/'sample.csv'
    if not sample.is_file(): sample = folder/'training_deliveries.csv'
    cells = list(csv.reader(sample.open(encoding='utf-8-sig',newline=''))) if sample.is_file() else []
    schema = ', '.join('`'+name+'`' for name in cells[0]) if cells else 'the input files named in the run instructions'
    first = ' | '.join(value if value else '(missing)' for value in cells[1]) if len(cells)>1 else '(see the supplied rows)'
    expected = folder/('penalty-expected-output.txt' if number in (361,362,363) else 'expected-output.txt')
    excerpt = expected.read_text(encoding='utf-8').splitlines()[:6] if expected.exists() else ['Run the named training and prediction scripts in order; compare the documented result above.']
    script = 'penalty_lab.py' if number in (361,362,363) else ('lesson.py' if (folder/'lesson.py').exists() else 'train_delivery_model.py')
    output = '\n'.join(excerpt)
    link = f'lessons/{folder.name}/{script}' if workbook else script
    package_link = f'lessons/{folder.name}/requirements.txt' if workbook else 'requirements.txt'
    result_link = f'lessons/{folder.name}/{expected.name}' if workbook else expected.name
    result_text = f'[full recorded output]({result_link})' if expected.exists() else 'the documented prediction result'
    # The table is an input record, not a claim about an invented new outcome.
    aliases = '\n'.join('<a id="'+anchor+'"></a>' for anchor in TEACHING_ALIASES[str(number)])
    text = f'''{aliases}

**Learn and apply: {row['Lesson name']}**

**Your decision.** {goal}

**Ready check.** {p['ready']} Use [the learning path](LEARNING-PATH.md) and [the word list](GLOSSARY.md) for the earlier skill. Trace the small example on paper before code.

**What it means.** {p['meaning']}

**Why and when.** {p['use']}

**A worked example to follow.** {p['example']}

**Input → steps → output.** Open the supplied table. Its fields are {schema}. One original row is shown below in that same field order; `(missing)` marks a blank rather than zero.

```text
{first}
```

1. Name the particular field or object involved in this lesson’s decision above. Keep its meaning and units with it.
2. Open the [complete runnable Python example]({link}). Its numbered comments connect reading, preparation and the resulting calculation. Install only the [declared requirements]({package_link}) using the same course Python, as shown in Setup.
3. Trace the worked example above through the script. {code_flow(number)}
4. Read the result by its headings. Compare with {result_text}; the excerpt below belongs to the original supplied files. Your edits can change it.

```text
{output}
```

**How to interpret it.** Trace the worked case into the result above. Tell a calculated estimate from a measured answer.

**Common mistakes and limits.** {p['caution']}

**Use it yourself.** {p['task']}

<details>
<summary>Check your choice and reason</summary>

{p['answer']}

</details>

**A second check later.** Close the notes and explain the same decision using a different row from the supplied table. State one condition that would make this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.
'''
    return prepare_reader_markdown(text)


def code_flow(number):
    key = LESSON_PROFILES[number]
    if key in {'project_brief','files_metadata','collection','hosting','categories','dashboard'} or (250 <= number <= 355 and ROWS[number-1]['Lesson name'].lower() in ('source','description')):
        return 'Trace the named source fields into the printed table, file or request result. Check names and counts before interpreting what the program reports.'
    if key.startswith('rl_') or key in {'q_learning','dqn','policy_gradient','mcts','model_based'}:
        return 'Find the state/action inputs, follow the transition and reward calculation, then inspect the policy, action values or planned move this particular script produces.'
    if key in {'kmeans','hierarchy','dbscan','mixture','pca','tsne','ica','anomaly','zscore','association'}:
        return 'Follow the chosen measurements through their preparation and fitted grouping, projection or review rule. Read the resulting representation or flag using the explanation above; do not invent confirmed group answers.'
    if key in {'missing_detection','missing_bias','exact_duplicates','near_duplicates','standard_formats','spellings','outlier_detection','outlier_review','outlier_handling','dates','interpolation','scientific_notation','nested','geography','exploration','bins'}:
        return 'Keep the original field beside the inspected or changed value. Trace the named preparation or review step, and check whether it uses a fixed rule or a value learned from training.'
    return 'Keep inputs apart from measured answers. Follow this script’s split and fit, then trace the saved preparation into the held-back result and any new request. A request must not supply its own training answer.'


def replace_section(text, title, body):
    pattern = r'(^## '+re.escape(title)+r'\n)(.*?)(?=^## |\Z)'
    def replace(match):
        # Preserve authored topic subheadings such as the special split note.
        extra = re.search(r'\n### .*', match.group(2), re.S)
        suffix = '\n'+extra.group(0).strip()+'\n' if extra else ''
        return match.group(1)+'\n'+body.strip()+'\n'+suffix+'\n'
    if not re.search(pattern,text,re.M|re.S):
        raise ValueError('Missing README section: '+title)
    return re.sub(pattern,replace,text,flags=re.M|re.S)


def revise_readme(row, folder, text):
    number=int(row['ID']); key=LESSON_PROFILES[number];p=PROFILES[key]
    text=re.sub(r'\n?<!-- teaching-note:start -->.*?<!-- teaching-note:end -->\n?', '\n', text, flags=re.S).rstrip()
    text=re.sub(r'\n?<!-- extra-lab:start -->.*?<!-- extra-lab:end -->\n?', '\n', text, flags=re.S).rstrip()
    sample=folder/'sample.csv'
    records=list(csv.reader(sample.open(encoding='utf-8-sig',newline='')))
    schema=', '.join('`'+name+'`' for name in records[0])
    first=' | '.join(value if value else '(missing)' for value in records[1])
    text=replace_section(text,'Before you start',p['ready']+'\n\nUse the [learning path](../../LEARNING-PATH.md) to find the earlier skill, the [word list](../../GLOSSARY.md) for a term, and [Setup](../../SETUP.md) for computer steps. Extra-topic prerequisites and bridges are in [Extra topics](../../ELECTIVES.md). In an extracted ZIP, open README.html for the browser links and keep this folder directly inside the complete course folder.')
    primary=f'''{p['meaning']}

**Why and when.** {p['use']}

**A worked example to follow.** {p['example']}

**Input and output.** The supplied sample fields are {schema}. In that field order, one original row is:

```text
{first}
```

`(missing)` means a blank, not zero. The result table below belongs to the original supplied files.

**Follow the Python.** Open the complete [lesson.py](lesson.py) beside these instructions. {code_flow(number)} The [requirements file](requirements.txt) lists its packages. The next section gives exact run commands; use the same course Python to install and run.
'''
    text=replace_section(text,'The idea in simple words',primary)
    text=replace_section(text,'Guess first',p['task']+' Write a reason before running or opening the answer.')
    answer=f'''**Common mistakes and limits.** {p['caution']}

<details>
<summary>Check your choice and reason</summary>

{p['answer']}

</details>

After the guided file change above, close the notes and explain the same decision for a different supplied row. State one condition that makes this method unsuitable. If you cannot explain the reason, repeat the small worked example before adding more code.
'''
    text=replace_section(text,'Explain the result',answer)
    return prepare_reader_markdown(text+extra_lab_notes(number,folder)+'\n\n'+BEGIN+'\n<!-- teaching-profile:'+key+' -->\n'+END+'\n')


def extra_lab_notes(number, folder):
    if number in (361,362,363):
        output=(folder/'penalty-expected-output.txt').read_text(encoding='utf-8').strip()
        figure='\n![Compare coefficients and validation error as the penalty changes. Smaller coefficients need not give smaller errors.](lasso-coefficients.png)\n' if (folder/'lasso-coefficients.png').is_file() else ''
        return '''

<!-- extra-lab:start -->
## See the coefficients change

The first script predicts using a fixed setting. This companion lab shows the learned weights and compares penalty settings fairly. A coefficient is the learned amount attached to one input. Here the inputs use training scales, so a coefficient means minutes per one training-standard-deviation increase, holding the other prepared input fixed.

Open the complete [penalty_lab.py](penalty_lab.py). It uses the supplied `sample.csv` and the same requirements. From this folder, run:

```bash
python penalty_lab.py
```

The lab reserves separate training, validation and final test groups. It fits the scaler on training only, compares settings on validation, and checks the chosen procedure on the final test. The no-penalty comparison uses ordinary linear regression. This special group split tests distance/weight combinations absent from training; equal measurements do not by themselves prove copied events.

**Recorded result.** These values were produced by the supplied lab:

```text
'''+output+'''
```

Read coefficients and errors together. A stronger penalty can make a coefficient zero while also making predictions worse. A zero does not prove that the field never matters in the world. The [coefficient table](coefficient-check.csv) contains the unrounded chart values.
'''+figure+'''
**Your task.** Which validation row wins? Why is the largest penalty not the best choice? Name the rows that must stay out of that choice.

<details>
<summary>Answer and reason</summary>

Ridge with alpha 1 has the lowest supplied validation MAE, about 0.896 minutes. Large penalties remove useful signal here. Final test answers do not select the setting; the frozen choice's final test MAE is about 1.527 minutes. These small invented data do not establish real-service performance.

</details>
<!-- extra-lab:end -->
'''
    if (folder/'network_bridge.py').is_file():
        return '''

<!-- extra-lab:start -->
## Trace one update before a network

Read the [network bridge](../../ELECTIVES.md#a-bridge-before-networks-trace-one-learning-step) before the larger training loop. The complete [network_bridge.py](network_bridge.py) needs only Python:

```bash
python network_bridge.py
```

Its [recorded output](network-expected-output.txt) follows one input, a weighted sum, a squared mistake, and a change to the weight and bias. It does not measure performance on separate examples. In that practice file change `learning_rate = 0.1` to `learning_rate = 1.0`, save, and run again. This row's loss rises from 1 to 81: a larger step can make learning worse. Restore 0.1 afterward. Complete the array-shape paper task in Extra topics before reading frame or token tensors.
<!-- extra-lab:end -->
'''
    return ''


def main():
    notes = {}
    for row in ROWS:
        number = int(row['ID'])
        folder = next(p for p in (ROOT/'lessons').iterdir() if p.name.startswith(row['ID']+'-'))
        path = folder/'README.md'
        text = path.read_text(encoding='utf-8')
        text=revise_readme(row,folder,text)
        path.write_text(text,encoding='utf-8',newline='\n')
        notes[number] = teaching_note(row,folder,True)
    workbook_path = ROOT/'Data-Science-and-Machine-Learning.md'
    text = workbook_path.read_text(encoding='utf-8')
    text = re.sub(r'\n\n## Focused tasks for shared exercises\n.*\Z', '', text, flags=re.S)
    text = re.sub(r'\n?<!-- workbook-teaching:\d+:start -->.*?<!-- workbook-teaching:\d+:end -->\n?', '\n', text, flags=re.S)
    # Numbered teaching sections use this exact three-column table, unlike the
    # Core summary and download catalogue. Insert once per numbered entry.
    pattern = r'(\| Lesson name \| What you’ll do \| Download \|\n\| --- \| --- \| --- \|\n\| (\d{3}) -[^\n]+\n)'
    used = set()
    def attach(match):
        number = int(match.group(2))
        if number in used: return match.group(0)
        used.add(number)
        return match.group(0)+f'\n<!-- workbook-teaching:{number}:start -->\n<details>\n<summary>Learn, trace and apply this idea</summary>\n\n'+notes[number]+f'\n</details>\n<!-- workbook-teaching:{number}:end -->\n'
    text = re.sub(pattern,attach,text)
    # Historical subentries with no standalone teaching table still need their
    # own focused explanation. Keep their existing stable IDs/download links;
    # group these additional notes near the shared lesson library.
    supplement = []
    for number in sorted(set(range(1,448))-used):
        supplement.append(f'<!-- workbook-teaching:{number}:start -->\n<details>\n<summary>{number:03}: '+next(r['Lesson name'] for r in ROWS if int(r['ID'])==number)+'</summary>\n\n'+notes[number]+f'\n</details>\n<!-- workbook-teaching:{number}:end -->')
    if supplement:
        text += '\n\n## Focused tasks for shared exercises\n\nThese entries share runnable files with related lessons. Each note asks a different teaching question where the goal differs. Open the named entry rather than rerunning every shared script.\n\n'+'\n\n'.join(supplement)+'\n'
    workbook_path.write_text(prepare_reader_markdown(text),encoding='utf-8',newline='\n')
    for guide in ROOT.glob('*.md'):
        if guide.name == 'AGENTS.md':
            continue
        original = guide.read_text(encoding='utf-8')
        prepared = prepare_reader_markdown(original)
        if prepared != original:
            guide.write_text(prepared,encoding='utf-8',newline='\n')
    print(f'Authored {len(ROWS)} self-contained lesson notes; {len(used)} section notes and {len(supplement)} shared-exercise notes. Profiles: {len(PROFILES)}.')


if __name__ == '__main__':
    main()

