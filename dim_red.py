'''
	CIS 519 Project: Seizure Prediction
	PCA
	Author: Zheng Tian
'''

import numpy as np
from sklearn.decomposition import PCA, KernelPCA
from sklearn.manifold import LocallyLinearEmbedding

'''
	componentsPca takes a positive integer
		as the number of desired principal components.
	explainedVarPca takes a real value between 0 and 1
		as the minimum percent of data that must be "explained "by the model.
'''
def componentsPca(numComponents):
	if type(numComponents) != int or numComponents < 1:
		print "given numComponents is not a positive integer: ", numComponents
		return

	return PCA(n_components=numComponents)

def explainedVarPca(explainedVariance):
	if not (0 < explainedVariance < 1):
		print "given explainedVariance is not between 0 and 1: ", explainedVariance
		return

	return PCA(n_components=explainedVariance, svd_solver='full')
	
# use the RBF kernel for now; we're aiming to use CV to find the best kernel later
def kpca(numComponents, coef0=1):
	# let gamma be the default value
	return KernelPCA(n_components=numComponents, kernel='rbf', coef0=coef0)
		

def lle(numComponents, neighbors=5, hessian=False):
	# if there's time we can try changing n_neighbors
	if hessian:
		return LocallyLinearEmbedding(n_neighbors=neighbors, n_components=numComponents, method='hessian')
	else:
		return LocallyLinearEmbedding(n_neighbors=neighbors, n_components=numComponents)