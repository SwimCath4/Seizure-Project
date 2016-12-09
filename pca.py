'''
	CIS 519 Project: Seizure Prediction
	PCA
	Author: Zheng Tian
'''

import numpy as np
from sklearn.decomposition import PCA, KernelPCA

class pca:
	'''
		componentsPca takes a positive integer
			as the number of desired principal components.
		explainedVarPca takes a real value between 0 and 1
			as the minimum percent of data that must be "explained" by the model.
	'''
	def __init__(self):

	def componentsPca(numComponents):
		if not (type(numComponents) == int and numComponents > 0):
			print "given numComponents is not a positive integer: ", numComponents
			return

		return PCA(n_components=numComponents)

	def explainedVarPca(explainedVariance):
		if not (0 < explainedVariance < 1):
			print "given explainedVariance is not between 0 and 1: ", explainedVariance
			return

		return PCA(n_components=explainedVariance, svd_solver='full')
		

class kernelPca:
	
	def __init__(self, numComponents, ):
		self.numComponents = numComponents

	def kpca(numComponents):
		return KernelPCA(n_components=numComponents)
		