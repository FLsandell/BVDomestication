# Summs up feature importances along the chromosomes using a sliding window in order to determine genetic regions of interest. 
# Code lines to be adapted are marked with e.g. "# insert path to input file".
# (c) Felix Sandell
# 1.7.2024

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import file

chr_lengths = pd.read_csv('# insert path to input file', sep = '\t')
df = pd.read_csv('# insert path to input file', sep = '\t')

# remove unasigned scaffolds
# in our case they where names as "un" chromosomes. If the assembly is chromosome scale, simply skip this step

df = df[~df['Scaffold'].str.contains('un')]
chr_lengths = chr_lengths[~chr_lengths['Sca'].str.contains('un')]

# definde functions to sum up features

def sliding_window_feats(sca_length, window_size, step_size, scaffold):
    sca = df[df['Scaffold'].str.contains(scaffold)]
    sliding_list=[]
    lst = list(range(1,sca_length+1))
    for i in range(len(lst))[::step_size]:
        feats = sca.loc[(df['Position'] >= i) & (sca['Position'] <= i+window_size)].Importance.sum()
        feats_list = feats.tolist()
        sliding_list.append(feats_list)
    return sliding_list

def sliding_window_counts(sca_length, window_size, step_size, scaffold):
    sca = df[df['Scaffold'].str.contains(scaffold)]
    sliding_list=[]
    lst = list(range(1,sca_length+1))
    for i in range(len(lst))[::step_size]:
        counts = pd.cut(sca.Position, [i ,i+window_size]).value_counts()
        counts_list = counts.tolist()
        sliding_list.extend(counts_list)
    return sliding_list

# iterate through all and plot the sliding window
sig_windows = pd.DataFrame()

for index, row in chr_lengths.iterrows(): 
    print(row['Sca'])
    sliding_list_feats = sliding_window_feats(row['length'], 5000, 2500, row['Sca'])
    
    df = pd.DataFrame()

    df['chr'] = row['Sca']
    df['feats'] = sliding_list_feats
    df['loc'] = range(1,row['length'],2500)
    #q = df['feats'].quantile(0.99)
    #print(q)
    #df.loc[(df['feats'] >= 0.01)]
    #sig_windows = sig_windows.append(df, ignore_index=True)
    
    
    plt_1 = plt.figure(figsize=(15, 5))
    # name the labels
    plt.xlabel('Position')
    plt.ylabel('Counts')
    plt.title(row['Sca'])
    plt.ylim(0, 0.06)

    plt.plot(range(1,row['length'],2500), sliding_list_feats)
