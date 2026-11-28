# Extra topics, one small step at a time

[Learning path](LEARNING-PATH.md) · [Word list](GLOSSARY.md)

These topics are optional. Finish the main path first. A technical name is useful for looking things up. You do not need to remember every name now.

Before starting an extra topic, explain its small first example on paper. If that is hard, use the named earlier skill first.

| Topic | Know this first | Start with this small task | What the name means |
| --- | --- | --- | --- |
| KNN fill, lesson 041 | Missing values, scaling, averages | Draw three deliveries. Fill a blank from two nearby examples. | KNN means nearest neighbours. “Near” depends on the input scale. |
| Target encoding, 077 | Categories, training and leakage | Count delayed orders for one supplier. Leave a row's own answer out when preparing that training row. | Replace a name with a number learned from training answers. Small groups need care. |
| Power and rank changes, 139–144 | Graphs, training and validation | Write five numbers before and after one change. Explain what happened to their gaps. | Box–Cox and Yeo–Johnson change a number's shape. Quantiles use ranks. |
| Powers of inputs, 146/364 | Multiplication, overfitting | For x = 2, calculate x, x squared and x cubed: 2, 4 and 8. | Polynomial features add powers or products so a model can fit a curve. |
| Feature tests, 169–173 | Inputs, labels, validation | Compare a useful field, a random field and an ID. | ANOVA compares group variation. Chi-square checks count or indicator features. Each has assumptions. |
| Cross-validation, 194 | Training, validation and average error | Make three piles of cards. Take turns holding one pile back. | Use several training/check divisions to inspect performance. Learn preparation again within each training pile. |
| Grid and random search, 191–192 | A setting and cross-validation | Compare just two settings by hand. | Grid tries listed settings. Random search samples choices. |
| Bayesian search, 193 | Validation, search, uncertainty | Draw a list of tried settings and scores. Ask which untried setting is worth trying next. | Use earlier trials to guide a later trial. The helper model and search rule need extra study. |
| ROC and precision-recall curves, 206/444 | Error counts and fractions | Change a cutoff on ten scored orders. Count misses and false alarms each time. | Curves show trade-offs as the cutoff moves. They do not choose the business policy for you. |
| Calibration, 445 | Probability and many check rows | Group cases with similar predicted chances. Compare the average chance with the share that happened. | Check whether stated chances match observed rates. A small group is uncertain. |
| PCA, 390 | Columns, graphs and spread | Draw two overlapping measurements and a new direction that keeps much of their spread. | Combine columns into fewer directions. High retained spread does not prove a useful prediction. |
| LDA, 392 | Known labels and projections | Draw a direction that helps separate two known groups. | This method uses labels, so it is supervised. |
| ICA, 393 | Mixed measurements | Imagine two microphones both hearing two speakers. | Try to separate mixed signals into more independent parts. Parts can change order or sign. |
| t-SNE, 391 | Similarity and scaling | Mark each row on a two-dimensional picture. Check its nearby neighbours. | Show local neighbours. Far-apart groups and axis values have limited meaning. |
| K-Means, DBSCAN and GMM, 385–388 | Distance, scaling and groups | Group paper points. Add a point between groups and one far away. | K-Means uses centres. DBSCAN uses dense areas. GMM gives chances across groups. |
| TF-IDF, 086 | Word counts | Count one word in three messages. Compare a common word with one found in only one message. | Give words different weights based on how common they are across training messages. |
| Word2Vec and BERT, 088–089 | Words as numbers, vectors, neural networks | Compare a word-count row with a short list of numbers representing a message. | These are ways to make word or message representations. The workbook's random BERT example has no learned language knowledge. |
| Images and CNNs, 113–117 | Arrays and basic networks | Draw a 3 by 3 pixel grid. Flatten it. Then move a small filter over it by hand. | A CNN learns filters over nearby pixels. The pixel/KNN lesson is only preparation. |
| Image features, 114 | Pixels, rows and columns | Compare the vertical and horizontal spread of a small line drawing. | An embedding is a list of numbers representing an item. It can be hand-built or learned. |
| Audio and MFCC, 118–121 | Time, waves and sampling | Compare two tones, their wave pictures and their frequency peaks. | MFCC is a compact summary made through several frequency-processing steps. Study these separately. |
| Video and LSTM, 122–124 | Images, arrays and networks | Read the same frames forwards and backwards. Explain why motion changes. | An LSTM processes a sequence. A tensor is an array with named or understood dimensions. |
| Semi-supervised methods, 402–409 | Supervised learning and a fair holdout | Mark confirmed labels and guessed labels in different colours. Show one wrong guess spreading. | Learn from some known answers and some unanswered rows. Guesses are not confirmed facts. |
| Q-learning, 420 | Actions, rewards and averages | Move along the five-cell track. Work out one action's reward and a discounted later reward. | Learn a table of action values from feedback. Exploration means trying a move to learn about it. |
| DQN, 421 | Q-learning, networks and loss | Replace one small Q-table row with two network outputs. | Use a neural network for action values. Replay reuses past moves; a target copy helps the updates. |
| Actor–critic, 423 | Probability, rewards and policy | Choose between two buttons. Compare the reward with an expected reward. | The actor chooses. The critic estimates value. This toy task is not a full robot system. |
| MCTS, 424 | Trees, rewards and planning | Draw two possible move paths. Try each and record its return. | Search possible futures before choosing a move. The planner needs a way to simulate what happens next. |

## A few useful safeguards for learning

Do not apply every preparation method to the same table. First name the problem. Compare one sensible candidate with doing nothing, using validation rows.

Scaling can leave an ordinary straight-line model's predictions unchanged. That is a useful result. To see why scale can matter, compare the nearest-neighbour model with and without scaling. Use the same validation rows. Do not decide from training scores.

For groups, try two choices of K, where K is the number of centres. Then try data without clear groups. Compare profiles and whether small changes produce very different groups. A silhouette score describes separation under a distance rule. It does not prove the groups help a business.

For dates, hours repeat. 23:00 and 00:00 are only an hour apart. Do not assume their written hour numbers give a useful distance. Time zones also matter: record whether a timestamp is local time or UTC. Keep the meaning and prediction time with the data.

For text, try “not late”, “late!”, a product code and a name where case matters. Removing punctuation or common words can remove useful meaning. The right choice depends on the task and language.

For neural networks, learn one step at a time: inputs, weights, output, loss, update, and a separate check. A **loss** measures mistakes during learning. An **optimizer** changes weights to reduce that loss. An **epoch** is one pass through training data. Do not start by memorizing a long training loop.
