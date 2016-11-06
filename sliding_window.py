'''
	CIS 519 Project: Seizure Prediction
	Sliding Window Algorithm
	Author: Catherine Yee
'''

import numpy as np
from itertools import islice

def window(seq, n=100):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result    
    for elem in it:
        result = result[1:] + (elem,)
        yield result