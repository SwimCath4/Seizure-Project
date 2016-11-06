'''
	CIS 519 Project: Seizure Prediction
	Sliding Window Algorithm
	Author: Catherine Yee
'''

import numpy as np
from itertools import islice

class slidingWindow:

    def __init__(self, width=100, shift=50):
   	    '''
        Constructor
        '''
        self.width = width
        self.shift = shift

	def window_idx(self, X):
    	"Returns indices of a sliding window over data from the iterable"
    	"   s -> (s0,s1,...s[width-1]), (s1,s2,...,s_width), ..."
    	"(n/shift) x width"
    	
    	n,d = X.shape

    	seq = xrange(n)
    	
    	it = iter(seq)
    	result = tuple(islice(it, self.width))
    	
    	if len(result) == self.width:
        	yield result    
    	for i in range(0: len(seq)/self.shift)
    		result = result[self.shift:] + tuple(islice(iter(seq(i*self.shift:))), self.width)
        	yield result

    def window_dat(self, X):
    	"Returns (n/shift) x (width x d) with Xtrain data"

    	n,d = X.shape

    	indices = self.window_idx(X)
    	data_windows = np.zeros(len(indices), self.width, d)
