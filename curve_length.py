# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 14:46:26 2016

@author: Tyrell
"""

import numpy as np

# import and process the data
X = np.loadtxt('./Data/1_1_0_small.dat', delimiter=',');
num_data_pts = int(X.shape[0]);
number_of_channels = int(X.shape[1]);
curve_length = np.zeros([number_of_channels, 1]); # initialize final array

# Output a vector of curve lengths. Each value corresponds to the channel's CL
for channel in range (number_of_channels):
    for i in range(1, num_data_pts): # START WITH THE SECOND DATA POINT
        curve_length[channel,0] += abs(X[i - 1][channel] - X[i][channel]);

print curve_length;