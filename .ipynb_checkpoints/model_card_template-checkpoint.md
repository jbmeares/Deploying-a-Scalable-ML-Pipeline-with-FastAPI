# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

Name: Predictve Census Pipeline
Type: AdaBoostClassifier
Version: 1
Developed by: James Meares
Date: 4/16/2024

## Intended Use

Development of a classification model on publicly available Census Bureau data. 

## Training Data
Dataset: [Census](https://archive.ics.uci.edu/dataset/20/census+income)

1994 United States Census
80% data from dataset was used for training
Includes: 
    Age
    workclass
    education
    marital_status
    occupation
    relationship
    race
    sex
    capital_gain
    capital_loss
    hours_per_week
    native-country
    income

## Evaluation Data
20% of data from dataset was used for testing.

## Metrics

Precision: 0.7637 
Recall: 0.6276 
F1: 0.6890

## Ethical Considerations
Not all data is conclusive to a persons actual income and should be considered when using this data and model for any official capacity

## Caveats and Recommendations
Extremely old data (1994)

Ethical considerations as mentioned above

