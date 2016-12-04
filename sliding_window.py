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

    def compute(self, X):
    	'''
    	Returns indices of a sliding window over data from the iterable
    	   s -> (s0,s1,...s[width-1]), (s0+shift,s1+shift,...,s[width-1]+shift), ...
    	'''
    	
    	n,d = X.shape

    	#print "(n / self.shift - 1)*self.shift + self.width", (n / self.shift - 1)*self.shift + self.width
        #print "n + self.shift = ", n + self.shift

        if((n / self.shift - 1)*self.shift + self.width > (n + self.shift)):
            end = (n / self.shift - 1)*self.shift + self.width
            #print "end = ", end
            decr = 1
            while end > n:
                end = end - self.shift
                decr = decr + 1
            num_windows = (n / self.shift - decr)

        else:
            num_windows = (n / self.shift - 1)

    	windows = np.zeros((num_windows, self.width))

    	for i in range(0, len(windows)):
            #print "window = ", xrange(i*self.shift, ((i*self.shift) + self.width), 1)
            #print "len(window) = ", len(xrange(i*self.shift, ((i*self.shift) + self.width), 1))
            windows[i,:] = xrange(i*self.shift, (i*self.shift) + self.width, 1)

    	return windows.astype(int)
