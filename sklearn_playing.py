#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn import tree
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from xgboost import XGBClassifier

wines = load_wine(as_frame=True)

# This is the series of target values
wines.target

# This is the feature array
wines.data

# Do some simple EDA here.
wines.data.shape

# Are there any NAs in any feature?
wines.data.columns
np.count_nonzero(np.isnan(wines.data), axis=0)

# What is the distribution of data for each feature?
df = wines.data
df.plot(subplots=True)

# What is the distribution of the target?
wines.target.plot.hist(bins=10, alpha=0.5)

# How balanced are the classes? Fairly balanced
pd.DataFrame(wines.target).value_counts()

# These are on pretty different scales. If we end up doing a regression we should conver them to z scores to compare
# beta coefficients.
# For classification without a lot of feature interrogation, we can use the data as they are.

# Lets do a 70/30 test/train split
x_train, x_test, y_train, y_test = train_test_split(
    df, wines.target, test_size=0.3, shuffle=True, random_state = 66)

print(x_train.shape)
print(x_test.shape)

# Lets try a decision tree
model = tree.DecisionTreeClassifier()
model.fit(x_train, y_train)
predicted = model.predict(x_test)
print(metrics.classification_report(y_test, predicted, target_names=wines.target_names))
print(metrics.confusion_matrix(y_test, predicted))

# Extratrees uses whole dataset and randomly chooses when to make splits, it is faster than RF, but may lead to more
# bias bc irrelevant features are included.
model = ExtraTreesClassifier()
model.fit(x_train, y_train)

#predict
predicted = model.predict(x_test)

print(metrics.classification_report(y_test, predicted, target_names=wines.target_names))
print(metrics.confusion_matrix(y_test, predicted))

# Lets try XGBoost
model = XGBClassifier(objective='binary:logistic')
model.fit(x_train, y_train)

#predict
predicted = model.predict(x_test)

print(metrics.classification_report(y_test, predicted, target_names=wines.target_names))
print(metrics.confusion_matrix(y_test, predicted))
