# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 16:16:24 2016

@author: Tyrell
"""

import numpy as np

# import and process the data
X = np.loadtxt('./Data/1_1_0_small.dat', delimiter=',');
num_data_pts = int(X.shape[0]);
number_of_channels = int(X.shape[1]);
nonlinear_energy = np.zeros([number_of_channels, 1]); # initialize final array

# Output a vector of eneries. Each value corresponds to the channel's energy
for channel in range (number_of_channels):
    for i in range(1, num_data_pts - 1): # START WITH THE SECOND DATA POINT
        nonlinear_energy[channel,0] += (X[i][channel])**2 - (X[i - 1][channel] * X[i + 1][channel]);

print nonlinear_energy;