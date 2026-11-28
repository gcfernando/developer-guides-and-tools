# Data source and licence

Wine [Dataset]. Stefan Aeberhard and M. Forina (1992). UCI Machine Learning Repository. DOI: [10.24432/C5PC7J](https://doi.org/10.24432/C5PC7J).

Source page: [UCI Wine](https://archive.ics.uci.edu/dataset/109/wine).

Licence: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Credit the creators when sharing a copy. These data are not invented course rows.

This copy was exported from the Wine dataset included with scikit-learn 1.6.1. It keeps its 178 observations and 13 measurements. The scikit-learn target codes are 0, 1 and 2; the original UCI class codes are 1, 2 and 3. This is a change of names, not an ordered quantity.

Course changes: added row IDs; renamed target to wine_type; used a fixed random split, keeping a similar share of each type; separated test answers into an instructor file. Random seed is 7 for the final test split and 11 for the validation split. No measured values were changed. The split does not test future dates or new producers.

This is a small historical classification benchmark. It is not evidence that a model can identify every wine or handle new measurement methods. Units are not documented for every input in the source table. Keep the supplied values and record that limit rather than guessing units.
