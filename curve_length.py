# -*- coding: utf-8 -*-
'''
	CIS 519 Project: Seizure Prediction
	Curve Length Calculator
	Author: Tyrell McCurbin
'''

import numpy as np

'''
class curve_length:
    def __init__(self):
        
        # Constructor
        
        
    def compute(self, X):
        
        # Process the data
        num_data_pts = int(X.shape[0]);
        number_of_channels = int(X.shape[1]);
        curve_length = np.zeros([1, number_of_channels]); # initialize final array
        
        # Output a vector of curve lengths. Each value corresponds to the channel's CL
        for channel in range (number_of_channels):
            for i in range(1, num_data_pts): # START WITH THE SECOND DATA POINT
                curve_length[0, channel] += abs(X[i - 1][channel] - X[i][channel]);
        
        return curve_length;
'''

def curve_length(X):
    # Process the data
    #num_data_pts = int(X.shape[0]);
    #number_of_channels = int(X.shape[1]);
    #curve_length = np.zeros([1, number_of_channels]); # initialize final array
    
    # Output a vector of curve lengths. Each value corresponds to the channel's CL
    #for channel in range (number_of_channels):
    #    for i in range(1, num_data_pts): # START WITH THE SECOND DATA POINT
    #        curve_length[0, channel] += abs(X[i - 1][channel] - X[i][channel]);
    #return curve_length / num_data_pts;
    
    
    X_k_minus_one = np.delete(X, (len(X)-1), axis=0)
    X = np.delete(X, 0, axis=0)

    return (X_k_minus_one - X).sum(axis=0).reshape(1,16)
