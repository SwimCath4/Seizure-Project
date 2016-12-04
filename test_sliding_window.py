"""
	CIS 519 Project: Seizure Prediction
	Sliding Window Algorithm TEST
	Author: Catherine Yee
"""
print(__doc__)
import numpy as np
from sliding_window import slidingWindow
from energy_calcs import compute_energy, compute_nonlinear_energy, compute_accumulated_energy

#width = 100;

filePath = "1_1_0_small.dat"
file = open(filePath,'r')
allData = np.loadtxt(file, delimiter=',')

Xtrain = allData
# Ytrain = 

#n,d = Xtrain.size
print "Xtrain.shape = ", Xtrain.shape

test_sw1 = slidingWindow(width=100, shift=50)
test_indices1 = test_sw1.compute(Xtrain)

print "indices 1 = ", test_indices1

test_sw2 = slidingWindow(width=100, shift=25)
test_indices2 = test_sw2.compute(Xtrain)

print "indices 2 = ", test_indices2

test_sw3 = slidingWindow(width=200, shift=100)
test_indices3 = test_sw3.compute(Xtrain)

print "indices 3 = ", test_indices3

test_sw4 = slidingWindow(width=50, shift=25)
test_indices4 = test_sw4.compute(Xtrain)

print "indices 4 = ", test_indices4

