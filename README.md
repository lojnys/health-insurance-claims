# Health Insurance Claims Modeling
Frequency-Severity Modeling with GLMs

## Description
This project develops an actuarial pricing framework for health insurance using frequency-severity modeling. Non-linear GLMs such as Possion and Negative Binomial, are expected to be employed to model claim frequency. On the other hand, Gamma GLM are expected to be used to model claim severity. However, through a thorough analysis, we will provide an opportunity to look into more sophisticated models. The project will expand to estimate pure premium. Results highlight the predictive importance of factors such as age, bmi, and other prior conditions in determining expected claims costs. The final model will provide an interpretable pricing structure suitable for health insurance underwriting rate setting.

## Dataset Description
* Source: https://www.kaggle.com/datasets/thedevastator/insurance-claim-analysis-demographic-and-health
* Dimensions: 11x1340

|Variable|Type|Description|
|---|---|---|
|PatientID|Count|ID of patient|
|age|Continuous|Patient's age|
|gender|Categorical|Patient's gender|
|bmi|Continuous|Patient's Body Mass Indicator|
|bloodpressure|Continuous|Patient's blood pressure|
|diabetic|Categorical|Patient's diabetic status|
|children|Count|Number of children|
|smoker|Categorical|Whether the patient smoke or not|
|region|Categorical|Patient's region of living|
|claim|Continuous(Target)|Claim amount|

## Project Structure
```
health_claims_analysis/
│
├── data/
│   └── raw_data/
│
├── notebooks/
│
├── src/
│
├── reports/
│   └── figures/
│
└── README.md

```

## Exploratory Data Analysis

## Methodology

### Frequency Modeling

### Severity Modeling


## Model Evaluation & Refinement

## Results & Interpretation

## References
* PennState Note STAT 462 Applied Regression Analysis - 10.8 *Detecting Multicollinearity Using Variance Inflation Factors* -  https://online.stat.psu.edu/stat462/node/209/
* PennState Note STAT 462 Applied Regression Analysis - 12.3 *Poisson Regression* - https://online.stat.psu.edu/stat462/node/180/
* CAS Monogrph Series Number 5 Second Edition (2025 revision) - *Generalized Linear Models For Insurance Rating*