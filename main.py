# -*- coding: utf-8 -*-
'''
	CIS 519 Project: Seizure Prediction
	Main Function For Seizure Data Analysis
	Authors:     Tyrell McCurbin
                 Catherine Yee
                 Elaida Dimwamwa
                 Zheng Tian
'''

import numpy as np
from knn import compute_centroid, predict
import dim_red
from normalize import norm, standardize
from sklearn import metrics
from pprint import pprint

# import Xtrain and Xtest data #

filePath = "X.dat"
file = open(filePath,'r')
allData = np.loadtxt(file, delimiter=',')
Xtrain = allData[0:int(len(allData)/2),:]
Xtrain[:,0:-1] = standardize(Xtrain[:,0:-1])
ytrain = allData[0:int(len(allData)/2),-1]

# dimensionality reduction; change the method for whichever method
dim_red_method = dim_red.lle(9)
dim_red_method.fit_transform(Xtrain[:,0:-1], ytrain)

Xtest = allData[int(len(allData)/2) + 1:, :]
Xtest[:,0:-1] = standardize(Xtest[:,0:-1])
dim_red_method.transform(Xtest[:,0:-1])
ytest = allData[int(len(allData)/2) + 1:, -1]

n_train, d = Xtrain.shape
n_test = Xtest.shape[0]

centroid_0 = np.zeros((1,n_train-1))
centroid_1 = np.zeros((1,n_train-1))
predicted_labels = np.zeros(n_test)

# booleans for determining whether first centroid has been initialized #
centroid_0_init = 0
centroid_1_init = 0

## Compute centroids for training data ##

for i in range(0, n_train):
    if(ytrain[i] == 0.0):
        if(centroid_0_init == 0):
            centroid_0 = Xtrain[i,:-1]
            centroid_0_init = 1
            #print "centroid_0 first = ", centroid_0
        else:
            centroid_0 = compute_centroid(centroid_0, Xtrain[i,:-1])

    elif(ytrain[i] == 1.0):
        if(centroid_1_init == 0):
            centroid_1 = Xtrain[i,:-1]
            centroid_1_init = 1
            #print "centroid_1 first = ", centroid_1
        else:
            centroid_1 = compute_centroid(centroid_1, Xtrain[i,:-1])

#print "centroid_0 = ", centroid_0
#print "centroid_1 = ", centroid_1

## Predict testing data ##
for i in range(0, n_test):
    predicted_labels[i] = predict(centroid_0, centroid_1, Xtest[i,:-1])

print "predicted_labels = ", predicted_labels

print "LLE & KNN accuracy = "
pprint(metrics.accuracy_score(ytest, predicted_labels))
print "LLE & KNN precision = "
pprint(metrics.precision_score(ytest, predicted_labels))
print "LLE & KNN recall = "
pprint(metrics.recall_score(ytest, predicted_labels))
