#!/usr/bin/env python
# coding: utf-8

import numpy as np
import random
from sklearn.model_selection import train_test_split
from scipy.sparse import coo_matrix
import pandas as pd


def error_check(sample):
    
    if(len(sample) != 113):
        return 0
    if(np.max(sample) > 1 or np.min(sample[1:])<0):
        oobx = np.argmax(sample)
        oobn = np.argmin(sample)
        return 0
    if(sample[0] != -1 and sample[0] != 1):
        return 0

    return 0.995


Y_train = pd.read_csv("train_Y.csv", header= None).to_numpy()
X_unformat = pd.read_csv("train_X.csv", header= None).to_numpy()

Xrows = X_unformat[:,0] -1
Xcols = X_unformat[:,1] -1
Xvals = X_unformat[:,2]

X_train = coo_matrix((Xvals,(Xrows, Xcols))).toarray()
X_train, X_test, Y_train, Y_test =  train_test_split(X_train, Y_train, test_size=0.1, random_state=0)

X_proper = []
Y_proper = []


#check if input is proper


for i in range(len(Y_train)):
    sample = np.concatenate([Y_train[i],X_train[i]], axis=0)
    if (error_check(sample) + random.random()) > 1:
        X_proper.append(sample[1:])
        Y_proper.append(sample[:1])
print("Number of Training Samples:", len(X_proper))
X_proper = np.array(X_proper)
Y_proper = np.array(Y_proper)
