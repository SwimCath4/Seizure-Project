'''
	CIS 519 Project: Seizure Prediction
	Normalize
	Author: Catherine Yee
'''

from __future__ import division
import numpy as np

def norm(X):
	'''
	Returns normalized X
	NOT WORKING ATM because max and min values are too close together
	'''
	mean = np.mean(X, axis=0)
	max = np.amax(X, axis=0)
	min = np.amin(X, axis=0)
	print "mean.shape = ", mean.shape
	print "mean = ", mean
	print "max.shape = ", max.shape
	print "max = ", max
	print "min.shape = ", min.shape
	print "min = ", min
	print "max - min", np.subtract(max, min)
	return np.true_divide(np.subtract(X, min), max - min)

def standardize(X):
	'''
	Returns standardized X
	'''
	mean = np.mean(X, axis=0)
	stddev = np.std(X, axis=0)
	print "mean.shape = ", mean.shape
	print "mean = ", mean
	print "stddev.shape = ", stddev.shape
	print "stddev = ", stddev
	return np.true_divide(np.subtract(X, mean), stddev)
