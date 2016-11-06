'''
	CIS 519 Project: Seizure Prediction
	Sliding Window Algorithm TEST
	Author: Catherine Yee
'''

import numpy as np
from sliding_window import window

filePath = ".dat"
file = open(filePath,'r')
allData = np.loadtxt(file, delimiter=',')

Xtrain = allData

print "Xtrain.size = ", Xtrain.size

windows = 