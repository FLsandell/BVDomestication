# Random Forest script for the publication: Variation analysis employing machine learning reveals domestication patterns and breeding trends in sugar beet
# this code is only a demonstration of the concept and not ready to use. This has to be adapted by adding input files of choice, output paths. Parameter ranges for hyperparameter optimization have to be selected with proper caution and have to be adapted depending on the input data set. 
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
CHR_input = pd.read_csv('INPUT_FILE',  sep = " ")
# Set index
CHR_input = CHR_input.set_index('ACC')
# .T
CHR_input = CHR_input.T

# Reduce file size to save memory

CHR_input = CHR_input.astype('int8')

# creates lists for groups (example BETA_MARITIMA, SUGAR BEET)
# MARs
MARs = open("PATH_TO_ACESSION_LIST", "r")
content = MARs.read()
MARs_list = content.split("\n")
del MARs_list[-1]
MARs.close()

# SUGs
SUGs = open("PATH_TO_ACESSION_LIST", "r")
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
n_estimators = [PARAMETER_RANGE]
# Number of features to consider at every split
max_features = [PARAMETER_RANGE]
# Maximum number of levels in tree
max_depth = [PARAMETER_RANGE]
# Minimum number of samples required to split a node
min_samples_split = [PARAMETER_RANGE]
# Minimum number of samples required at each leaf node
min_samples_leaf = [PARAMETER_RANGE]
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



