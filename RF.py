# Trains random forest hyperparameters for predictive models based on sequencing data
# Code lines to be adapted are marked with e.g. "# insert path to input file".
# (c) Felix Sandell
# 1.7.2024

# Import libraries

import pandas as pd
import numpy as np
import io
import os
import sys
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split

# read file
CHR_input = pd.read_csv('# insert path to input file',  sep = " ")
# Set index
CHR_input = CHR_input.set_index('# insert column name of phenotypes')
# .T
CHR_input = CHR_input.T

# Reduce file size to save memory

CHR_input = CHR_input.astype('int8')

# creates lists for groups (example BETA_MARITIMA, SUGAR BEET)
# MARs
MARs = open("# insert path to accession list", "r")
content = MARs.read()
MARs_list = content.split("\n")
del MARs_list[-1]
MARs.close()

# SUGs
SUGs = open("# insert path to accession list", "r")
content = SUGs.read()
SUGs_list = content.split("\n")
del SUGs_list[-1]
MARs.close()

# Combine groups
MarSug = SUGs_list + MARs_list

CHR_input = CHR_input.loc[MarSug]

# Create input 

CHR_input['MAR'] = CHR_input.index.isin(MARs_list)

y = CHR_input['MAR'].values
X = CHR_input.drop(['MAR'], axis=1).values

# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y ,random_state = 42, stratify = y)

# Parameter Selection

# Number of trees in random forest
n_estimators = [# insert PARAMETER_RANGE]
# Number of features to consider at every split
max_features = [# insert PARAMETER_RANGE]
# Maximum number of levels in tree
max_depth = [# insert PARAMETER_RANGE]
# Minimum number of samples required to split a node
min_samples_split = [# insert PARAMETER_RANGE]
# Minimum number of samples required at each leaf node
min_samples_leaf = [# insert PARAMETER_RANGE]
# Method of selecting samples for training each tree
bootstrap = [True, False]# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}

# Train hyperparameters

rf = RandomForestClassifier()
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose = 2 ,  random_state=38, n_jobs = 90)

# Fit the best model

rf_random.fit(X_train, y_train)

# output best parameter combination

rf_random.best_params_

# test accuracy of your model

rf_random.best_estimator_.score(X_test,y_test)



