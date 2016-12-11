'''
	CIS 519 Project: Seizure Prediction
	Normalize
	Author: Catherine Yee
'''

import numpy as np

def norm(X):
	'''
	Returns normalized X
	'''
	mean = np.mean(X, axis=0)
	stddev = np.std(X, axis=0)
	print "mean.shape = ", mean.shape
	print "mean = ", mean
	print "stddev.shape = ", stddev.shape
	print "stddev = ", stddev
	return np.divide(np.subtract(X, mean), stddev)