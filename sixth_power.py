# -*- coding: utf-8 -*-
'''
	CIS 519 Project: Seizure Prediction
	Average Sixth Power Calculator
	Author: Tyrell McCurbin
'''

import numpy as np

def sixth_power(X):   
    
    return np.mean(X**6, axis = 0).reshape(1,16);