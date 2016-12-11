# -*- coding: utf-8 -*-
'''
	CIS 519 Project: Seizure Prediction
	Main Function For Seizure Data Analysis
	Authors:   Tyrell McCurbin
                 Catherine Yee
                 Elaida Dimwamwa
                 Zheng Tian
'''

import numpy as np

filePath = "X_train.dat"
file = open(filePath,'r')
allData = np.loadtxt(file, delimiter=',')

Xtrain = allData

filePath = "X_test.dat"
file = open(filePath,'r')
allData = np.loadtxt(file, delimiter=',')

Xtest = allData

print "Xtrain.shape = ", Xtrain.shape
print "Xtest.shape = ", Xtest.shape

n, d = Xtrain.shape

centroid_0 = np.zeros((1,96))
centroid_1 = np.zeros((1,96))

centroid_0_init = 0
centroid_1_init = 0

## Generate centroids ##

for i in range(0, n):
    if(Xtrain[i,d-1] == 0.0):
        if(centroid_0_init == 0):
            centroid_0 = Xtrain[i,:-1]
            centroid_0_init = 1
        else:
            centroid_0 = compute_centroid(centroid_0, Xtrain[i,:-1])

    elif(Xtrain[i,d-1] == 1.0):
        if(centroid_1_init == 0):
            centroid_1 = Xtrain[i,:-1]
            centroid_1_init = 1
        else:
            centroid_1 = compute_centroid(centroid_1, Xtrain[i,:-1])