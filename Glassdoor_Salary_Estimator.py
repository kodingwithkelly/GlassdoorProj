#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 13:34:58 2021

@author: kellylam
"""

import pandas as pd 
import numpy as np 

df = pd.read_csv('/Users/kellylam/Glassdoor/Data/Glassdoor_w_Seniority.csv')

df_model = df[['Rating', 'State', 'Average Salary (Thousands)', 'Size', 'Industry', 'Seniority']]

## Replace NaN values. Rating, State, Size, and Industry all have Nans.
from sklearn.impute import SimpleImputer 
# Replace Size and Industry NaN with mode
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer.fit(df_model.iloc[:, 3:5])
df_model.iloc[:, 3:5] = imputer.transform(df_model.iloc[:, 3:5])

# Replace State NaN with mode
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer.fit(df_model.iloc[:, 1:2])
df_model.iloc[:, 1:2] = imputer.transform(df_model.iloc[:, 1:2])

# Replace Rating NaN with mean
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(df_model.iloc[:, 0:1])
df_model.iloc[:, 0:1] = imputer.transform(df_model.iloc[:, 0:1])

# Get dummy vars
df_dum = pd.get_dummies(df_model)

# Split into training and testing set 
from sklearn.model_selection import train_test_split

X = df_dum.drop('Average Salary (Thousands)', axis =1)
y = df_dum['Average Salary (Thousands)'].values # Get data as array

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# Support Vector Regression
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVR
svr = SVR(kernel = 'rbf')
svr.fit(X_train, y_train)
np.mean(cross_val_score(svr, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3)) # Split into smaller sets

# Random Forest 
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
np.mean(cross_val_score(rf, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))

# Decision Tree
from sklearn.tree import DecisionTreeRegressor
dt = DecisionTreeRegressor(random_state = 0)
dt.fit(X_train, y_train)
np.mean(cross_val_score(dt, X_train, y_train, scoring = 'neg_mean_absolute_error', cv = 3))

# Predicting
tpred_svr = svr.predict(X_test)
tpred_dt = dt.predict(X_test)
tpred_rf = rf.predict(X_test)

# Get MAE 
from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_svr)
mean_absolute_error(y_test,tpred_dt)
mean_absolute_error(y_test,tpred_rf)

mean_absolute_error(y_test,(tpred_svr+tpred_rf)/2)
