# Calculates trained models with different train/test splits
# Code lines to be adapted are marked with e.g. "# insert path to input file".
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
beets_snps = pd.read_csv('# insert path to input file',  sep = " ")

# Set index
beets_snps = beets_snps.set_index('# insert column name of phenotypes')
# .T
beets_snps = beets_snps.T

# reduces file size to save memory

beets_snps = beets_snps.astype('int8')

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
                            
    feature_importance.to_csv("# insert path to output" % seed, sep='\t')
