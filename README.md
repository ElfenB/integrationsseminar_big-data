# Integrationsseminar big data

This project is for university. It covers a 'big data' topic of my choice.

Data preparation is mainly done with Excel and Python. There are 4 main data sources, covering mainly the years 2016-2020:

- Fuel prices
- Mortality in Germany
- Traffic accidents in Germany
- Temperature from 20 different places in Germany

The focus is on the correlation and the r- and p-values, to prove hypotheses for correlation.

test.py shows the in Milestone requested import and a first plot.
h1.py, h2.py, h3.py and h4.py calculate the values needed for each hypotheses.

## File structure needed

To do the calculation, the refined data is needed. Therefore, the refined-data folder should be prepared as follows.

- fuel-and-temperature (folder)
  - Augsburg.csv
  - Braunschweig.csv
  - (...)
- deaths-and-accidents.csv
- 2020-12-06-prices.csv (only needed for test.py)

## Data preparation

The data in the files should be prepared as below.

### fuel-and-temperature

|date|temperature|e5|
|---|---|---|
|01.01.2016|1.6|1.297|
|02.01.2016|0.4|1.283|
|03.01.2016|0.4|1.296|
||(...)|

### deaths-and-accidents

|day|month|year|date|deaths|accidents|
|---|---|---|---|---|---|
|1|1|2016|01.01.2016|2558|370|
|2|1|2016|02.01.2016|2422|397|
|3|1|2016|03.01.2016|2522|349|
||||(...)|

### 2020-12-06-prices

|date|station_uuid|diesel|e5|e10|dieselchange|e5change|e10change|
|---|---|---|---|---|---|---|---|
|2020-12-06 00:00:09+01|cee140c2-e424-426e-afaa-cd6706163b56|1.099|1.279|1.229|1|1|1|
|2020-12-06 00:01:06+01|9bb515a4-c551-41b8-a8a1-e120f29474fd|1.049|1.199|0.000|1|1|0|
|2020-12-06 00:01:06+01|0d58c4ba-3267-404a-89d6-6ba15a8fc422|1.149|1.269|1.219|1|1|1|
|||||(...)|
