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
# from knn import compute_centroid, predict
from sklearn.neighbors import KNeighborsClassifier
import dim_red
from graph_pca_info import plot_pca_info
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

# n_components for dimensionality reduction, chosen from graph_pca_info plots
n_components = 20
# n_neighbors for knn; default value is 5
n_neighbors = 5

# dimensionality reduction; change the method for whichever method you choose

# lle(n_components, neighbors=(n_components * (n_components + 3) / 2) + 1, hessian=True)
# lle(n_components, neighbors=(n_components * (n_components + 3) / 2) + 1)
# componentsPca(n_components)
# kpca(n_components)
dim_red_method = dim_red.lle(n_components, neighbors=(n_components * (n_components + 3) / 2) + 1, hessian=True)
reducedXTrain = dim_red_method.fit_transform(Xtrain[:,0:-1], ytrain)

Xtest = allData[int(len(allData)/2) + 1:, :]
Xtest[:,0:-1] = standardize(Xtest[:,0:-1])
reducedXTest = dim_red_method.transform(Xtest[:,0:-1])
ytest = allData[int(len(allData)/2) + 1:, -1]

n_train, d = reducedXTrain.shape
n_test = Xtest.shape[0]

knn = KNeighborsClassifier(p=2)
knn.fit(reducedXTrain, ytrain)
predicted_labels = knn.predict(reducedXTest)
# print "predicted_labels = ", predicted_labels

print "precision = "
pprint(metrics.precision_score(ytest, predicted_labels))
print "recall = "
pprint(metrics.recall_score(ytest, predicted_labels))
print "accuracy = "
pprint(metrics.accuracy_score(ytest, predicted_labels))

# plot_pca_info(Xtrain[:,0:-1], n_components)