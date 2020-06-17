Repo for data domain salary prediction 

1. Built a simple model that estimates data domain oriented salaries (MAE ~ $ 8K).
2. Scraped over 1000 job descriptions from glassdoor using python and selenium
3. Cleaned the date and did EDA to get a better understanding of the data.
4. Optimized Linear, Lasso, Random Forest Regressor and XGB Regressor using GridsearchCV to reach the best model.


Code and Resources Used

Python Version: 3.7
Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium
Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

Youtube tutorial : https://www.youtube.com/watch?v=agHKuUoMwvY 

Model Building
Transformed the categorical variables into dummy variables. Split the data into train and tests sets with a train size of 80%.

Tried three different models and evaluated them using Mean Absolute Error. Chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

Four different models were used:

Multiple Linear Regression – Baseline for the model.
Lasso Regression – Normalized regression like lasso would be effective.
Random Forest – With the sparsity associated with the data, this would be a good fit.
XGB - To improve accuracy tried gradient boosting model.
Model performance

The XGB model far outperformed the other approaches on the test and validation sets.

XGB : MAE = 8.18

Random Forest : MAE = 17.10

Ridge Regression: MAE = 19.89

Linear Regression: MAE = 20.30
