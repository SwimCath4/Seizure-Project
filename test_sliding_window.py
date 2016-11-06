"""
	CIS 519 Project: Seizure Prediction
	Sliding Window Algorithm TEST
	Author: Catherine Yee
"""
print(__doc__)
import numpy as np
from sliding_window import slidingWindow

#width = 100;

filePath = "1_1_0_small.dat"
file = open(filePath,'r')
allData = np.loadtxt(file, delimiter=',')

Xtrain = allData
# Ytrain = 

n,d = Xtrain.size
print "Xtrain.size = ", Xtrain.size

test_sw = slidingWindow(width=100, shift=50)
test_indices = test_sw.window_idx(Xtrain)

for i in range(0, 5):
	print "indices = ", test_indices[i,:]