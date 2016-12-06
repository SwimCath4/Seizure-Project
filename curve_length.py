# -*- coding: utf-8 -*-
'''
	CIS 519 Project: Seizure Prediction
	Curve Length Calculator
	Author: Tyrell McCurbin
'''

import numpy as np

class curve_length:
    def __init__(self):
        '''
        Constructor
        '''
        
    def compute(self, X):
        
        # Process the data
        num_data_pts = int(X.shape[0]);
        number_of_channels = int(X.shape[1]);
        curve_length = np.zeros([number_of_channels, 1]); # initialize final array
        
        # Output a vector of curve lengths. Each value corresponds to the channel's CL
        for channel in range (number_of_channels):
            for i in range(1, num_data_pts): # START WITH THE SECOND DATA POINT
                curve_length[channel,0] += abs(X[i - 1][channel] - X[i][channel]);
        
        return curve_length;