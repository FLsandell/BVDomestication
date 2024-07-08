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

# Groups for Filtering
#ALL sugs
sugs_full = open("/DEFINELIST", "r")
content = sugs_full.read()
sugs_full_list = content.split("\n")
del sugs_full_list[-1]
sugs_full.close()
#MarMash Accs
MarMash_ACCs = open("/DEFINELIST", "r")
content = MarMash_ACCs.read()
MarMash_ACCs_list = content.split("\n")
del MarMash_ACCs_list[-1]
MarMash_ACCs.close()
# MARs
MARs = open("/DEFINELIST", "r")
content = MARs.read()
MARs_list = content.split("\n")
del MARs_list[-1]
MARs.close()
MedMARs = open("/DEFINELIST", "r")
content = MedMARs.read()
MedMARs_list = content.split("\n")
del MedMARs_list[-1]
MedMARs.close()

#beets_snps = beets_snps.loc[MarMash_ACCs_list]
Dom_Mar_list = sugs_full_list + MedMARs_list
beets_snps = beets_snps.loc[Dom_Mar_list]


# create y table

beets_snps["Cultivated"] = np.where((beets_snps.index).isin(sugs_full_list), "Cultivated", "Wild")

# create X and y

y = beets_snps['Cultivated']
X = beets_snps.drop(['Cultivated'], axis=1)

for seed in range(42):

    # Set train set 
    
    X_train, X_test, y_train, y_test = train_test_split(X, y ,random_state = seed, stratify = y)
    
    # train the model with 5000 Estimators
    
    rf_fixed = RandomForestClassifier(PARAMETERS)
    
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

