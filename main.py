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
import dim_red
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from graph_pca_info import plot_pca_info
from normalize import norm, standardize
from sklearn import metrics
from pprint import pprint
from sklearn.metrics import roc_curve, auc
from matplotlib.backends.backend_pdf import PdfPages
import time
import matplotlib.pyplot as plt

# import training and testing data #

filePath = "X.dat"
file = open(filePath,'r')
allData = np.loadtxt(file, delimiter=',')
Xtrain = allData[0:int(len(allData)/2), 0:-1]
Xtrain = standardize(Xtrain)
# the labels are in the last column
ytrain = allData[0:int(len(allData)/2), -1]

# n_components for dimensionality reduction, chosen from graph_pca_info plots
n_components = 40
# n_neighbors for knn; sklearn's default value is 5
knn_neighbors = 5

# dimensionality reduction; change the method for whichever method you choose

# lle(n_components, neighbors=(n_components * (n_components + 3) / 2) + 1, hessian=True)
# lle(n_components, neighbors=(n_components * (n_components + 3) / 2) + 1)
# componentsPca(n_components)
# kpca(n_components)
start_time = time.clock()
dim_red_method = dim_red.componentsPca(n_components)
reducedXTrain = dim_red_method.fit_transform(Xtrain, ytrain)

Xtest = allData[int(len(allData)/2) + 1:, 0:-1]
Xtest = standardize(Xtest)
reducedXTest = dim_red_method.transform(Xtest)
ytest = allData[int(len(allData)/2) + 1:, -1]

# comment this in for no dimensionality reduction
reducedXTrain = Xtrain
reducedXTest = Xtest

n_train, d = reducedXTrain.shape
n_test = Xtest.shape[0]

knn = KNeighborsClassifier(n_neighbors=knn_neighbors, p=2)
knn.fit(reducedXTrain, ytrain)
predicted_labels = knn.predict(reducedXTest)

end_time = time.clock()

print "time from dim_red_method instantiation to prediction output: ", end_time - start_time

# print "predicted_labels = ", predicted_labels

# print "precision = "
# pprint(metrics.precision_score(ytest, predicted_labels))
# print "recall = "
# pprint(metrics.recall_score(ytest, predicted_labels))
# print "accuracy = "
# pprint(metrics.accuracy_score(ytest, predicted_labels))

plot_pca_info(Xtrain[:,0:-1], n_components)
exit()

# k-fold cross validation over the entire dataset
k_folds = 10
# data should be shuffled
dataCopy = allData
np.random.shuffle(dataCopy)

X = dataCopy[:, 0:-1]
y = dataCopy[:, -1]

# scores = cross_val_score(knn, X, y=y, scoring='precision', cv=k_folds)
# print "CV fold precision scores: ", scores

# scores = cross_val_score(knn, X, y=y, scoring='recall', cv=k_folds)
# print "CV fold recall scores: ", scores

# scores = cross_val_score(knn, X, y=y, scoring='accuracy', cv=k_folds)
# print "CV fold accuracy scores: ", scores


# Compute the ROC curves and ROC areas
fpr_knn = dict()
tpr_knn = dict()
roc_auc_knn = dict()
fpr_knn, tpr_knn, _ = roc_curve(ytest, predicted_labels)
# print "fpr_knn = ", fpr_knn
# print "tpr_knn = ", tpr_knn
roc_auc_knn = auc(fpr_knn, tpr_knn)

# knn with pca
dim_red_method = dim_red.componentsPca(n_components)
reducedXTrain = dim_red_method.fit_transform(Xtrain[:,0:-1], ytrain)
reducedXTest = dim_red_method.transform(Xtest[:,0:-1])
n_train, d = reducedXTrain.shape
n_test = Xtest.shape[0]
knn = KNeighborsClassifier(p=2)
knn.fit(reducedXTrain, ytrain)
predicted_labels = knn.predict(reducedXTest)
# print "precision = "
# pprint(metrics.precision_score(ytest, predicted_labels))
# print "recall = "
# pprint(metrics.recall_score(ytest, predicted_labels))
# print "accuracy = "
# pprint(metrics.accuracy_score(ytest, predicted_labels))
fpr_knn_pca = dict()
tpr_knn_pca = dict()
roc_auc_knn_pca = dict()
fpr_knn_pca, tpr_knn_pca, _ = roc_curve(ytest, predicted_labels)
# print "fpr_knn_pca = ", fpr_knn_pca
# print "tpr_knn_pca = ", tpr_knn_pca
roc_auc_knn_pca = auc(fpr_knn_pca, tpr_knn_pca)

# knn with kpca
dim_red_method = dim_red.kpca(n_components)
reducedXTrain = dim_red_method.fit_transform(Xtrain[:,0:-1], ytrain)
reducedXTest = dim_red_method.transform(Xtest[:,0:-1])
n_train, d = reducedXTrain.shape
n_test = Xtest.shape[0]
knn = KNeighborsClassifier(p=2)
knn.fit(reducedXTrain, ytrain)
predicted_labels = knn.predict(reducedXTest)
# print "precision = "
# pprint(metrics.precision_score(ytest, predicted_labels))
# print "recall = "
# pprint(metrics.recall_score(ytest, predicted_labels))
# print "accuracy = "
# pprint(metrics.accuracy_score(ytest, predicted_labels))
fpr_knn_kpca = dict()
tpr_knn_kpca = dict()
roc_auc_knn_kpca = dict()
fpr_knn_kpca, tpr_knn_kpca, _ = roc_curve(ytest, predicted_labels)
# print "fpr_knn_kpca = ", fpr_knn_kpca
# print "tpr_knn_kpca = ", tpr_knn_kpca
roc_auc_knn_kpca = auc(fpr_knn_kpca, tpr_knn_kpca)

# knn with lle
dim_red_method = dim_red.lle(n_components, neighbors=(n_components * (n_components + 3) / 2) + 1)
reducedXTrain = dim_red_method.fit_transform(Xtrain[:,0:-1], ytrain)
reducedXTest = dim_red_method.transform(Xtest[:,0:-1])
n_train, d = reducedXTrain.shape
n_test = Xtest.shape[0]
knn = KNeighborsClassifier(p=2)
knn.fit(reducedXTrain, ytrain)
predicted_labels = knn.predict(reducedXTest)
# print "precision = "
# pprint(metrics.precision_score(ytest, predicted_labels))
# print "recall = "
# pprint(metrics.recall_score(ytest, predicted_labels))
# print "accuracy = "
# pprint(metrics.accuracy_score(ytest, predicted_labels))
fpr_knn_lle = dict()
tpr_knn_lle = dict()
roc_auc_knn_lle = dict()
fpr_knn_lle, tpr_knn_lle, _ = roc_curve(ytest, predicted_labels)
# print "fpr_knn_lle = ", fpr_knn_lle
# print "tpr_knn_lle = ", tpr_knn_lle
roc_auc_knn_lle = auc(fpr_knn_lle, tpr_knn_lle)

# knn with hlle
dim_red_method = dim_red.lle(n_components, neighbors=(n_components * (n_components + 3) / 2) + 1, hessian=True)
reducedXTrain = dim_red_method.fit_transform(Xtrain[:,0:-1], ytrain)
reducedXTest = dim_red_method.transform(Xtest[:,0:-1])
n_train, d = reducedXTrain.shape
n_test = Xtest.shape[0]
knn = KNeighborsClassifier(p=2)
knn.fit(reducedXTrain, ytrain)
predicted_labels = knn.predict(reducedXTest)
# print "precision = "
# pprint(metrics.precision_score(ytest, predicted_labels))
# print "recall = "
# pprint(metrics.recall_score(ytest, predicted_labels))
# print "accuracy = "
# pprint(metrics.accuracy_score(ytest, predicted_labels))
fpr_knn_hlle = dict()
tpr_knn_hlle = dict()
roc_auc_knn_hlle = dict()
fpr_knn_hlle, tpr_knn_hlle, _ = roc_curve(ytest, predicted_labels)
# print "fpr_knn_hlle = ", fpr_knn_hlle
# print "tpr_knn_hlle = ", tpr_knn_hlle
roc_auc_knn_hlle = auc(fpr_knn_hlle, tpr_knn_hlle)

# Compute micro-average ROC curve and ROC area
#fpr_knn["micro"], tpr_knn["micro"], _ = roc_curve(ytest.ravel(), predicted_labels.ravel())
#roc_auc_knn["micro"] = auc(fpr_knn["micro"], tpr_knn["micro"])

# Save plot to pdf
with PdfPages('ROC_nocrossval.pdf') as pdf:
    #pp = PdfPages("graphTextClassifierROC.pdf")
    fig1 = plt.figure()
    lw = 2

    plt.plot(fpr_knn, tpr_knn, lw=lw, label='KNN ROC Curve without Dimensionality Reduction (area = %0.2f)' % roc_auc_knn)
    plt.plot(fpr_knn_pca, tpr_knn_pca, lw=lw, label='KNN with PCA ROC Curve (area = %0.2f)' % roc_auc_knn_pca)
    plt.plot(fpr_knn_kpca, tpr_knn_kpca, lw=lw, label='KNN with RBF Kernel PCA ROC Curve (area = %0.2f)' % roc_auc_knn_kpca)
    plt.plot(fpr_knn_lle, tpr_knn_lle, lw=lw, label='KNN with LLE ROC Curve (area = %0.2f)' % roc_auc_knn_lle)
    plt.plot(fpr_knn_hlle, tpr_knn_hlle, lw=lw, label='KNN with Hessian LLE ROC Curve (area = %0.2f)' % roc_auc_knn_hlle)


    plt.plot([0,1], [0,1], lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curves')
    plt.legend(loc="lower right")
    plt.show()
    pdf.savefig(fig1)
    #plt.savefig(pp, format='pdf')
    plt.close()

# Things we can try to do to get better results/plots:
# figure out a way to use gridsearch to find the best parameters for knn,
#   and possibly for the dimensionality reduction methods
# change kpca kernel type
# change kernel parameters of the kpca kernel
# change number of neighbors for LLE
# change number of neighbors for knn