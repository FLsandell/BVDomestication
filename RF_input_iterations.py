# Random Forest script for the publication: Variation analysis employing machine learning reveals domestication patterns and breeding trends in sugar beet
# this code is only a demonstration of the concept and not ready to use. This has to be adapted by adding input files of choice, output paths. Parameter ranges for hyperparameter optimization have to be selected with proper caution and have to be adapted depending on the input data set. 
# (c) Felix Sandell
# 1.7.2024

import pandas as pd
import numpy as np
import io
import os
import sys
import sklearn
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn.model_selection import train_test_split
from pandas import DataFrame


# read file
beets_snps = pd.read_csv('INPUTFILE',  sep = " ")

# Set index
beets_snps = beets_snps.set_index('ACC')
# .T
beets_snps = beets_snps.T

beets_snps = beets_snps.astype('int8')

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

beet_snps = beet_snps.loc[MarSug]


# create y table

beets_snps["Cultivated"] = np.where((beets_snps.index).isin(sugs_list), "Cultivated", "Wild")

# create X and y

y = beets_snps['Cultivated']
X = beets_snps.drop(['Cultivated'], axis=1)

for seed in range(42):

    # Set train set 
    
    X_train, X_test, y_train, y_test = train_test_split(X, y ,random_state = seed, stratify = y)
    
    # train the model with 5000 Estimators
    
    rf_fixed = RandomForestClassifier('PARAMETERS')
    
    U =rf_fixed.fit(X_train, y_train)
    
    # get classification score
    
    score = rf_fixed.score(X_test,y_test)
    
    joblib.dump(rf_fixed, "%s.model5000" % seed)
    
    with open("%s.score" % seed, 'w') as f:
        print(score, file=f)

    result = []

    feat=rf_fixed.feature_importances_

    for name,score in zip(beets_snps.columns.values, feat):
        result.append((name,score))
    
    # Create Dataframe
    df = DataFrame (result,columns=['1','2'])
    
    # Sort feature importance list
    feature_importance = df.sort_values(by=['2'], ascending = False)
    
    feature_importance.columns = ['SNP','Importance']
    feature_importance = feature_importance[feature_importance['Importance'] > 0]
                            
    feature_importance.to_csv("export_path" % seed, sep='\t')
