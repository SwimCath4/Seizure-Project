'''
	CIS 519 Project: Seizure Prediction
	PCA
	Author: Zheng Tian
'''

import numpy as np
from sklearn.decomposition import PCA, KernelPCA

class pca:
	'''
		There are two options for this class:
		1. numComponents is a positive integer for the number of desired principal
			components; explainedVariance will be ignored.
		2. numComponents is None; explainedVariance is a real value between 0 and 1
			that is the minimum percent of data that must be explained.
	'''
	def __init__(self, numComponents, explainedVariance):
		self.numComponents = numComponents
		self.explainedVariance = explainedVariance

		# Decide whether option 1 or 2 is desired
		# if type(numComponents) == int and numComponents > 0:
		# 	# option 1
		# 	componentsPca()
		# elif numComponents == None and 0 < explainedVariance < 1:
		# 	# option 2
		# 	explainedVarPca()
		# else:
		# 	print "given arguments not valid: ", numComponents, explainedVariance

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
		