# -*- coding: utf-8 -*-
'''
	CIS 519 Project: Seizure Prediction
	Spectral Entropy Calculator
	Author: Tyrell McCurbin
'''

import math
import numpy as np

def spectral_entropy(X):
    
    # process the data
    num_data_pts = int(X.shape[0]);
    number_of_channels = int(X.shape[1]);
    spectral_entropy = np.zeros([1, number_of_channels]); # initialize final array
    
    # The following routine is based off of information found on Stack Exchange
    # 1. Calculate the Power SPectral Density
    PSD = np.zeros([num_data_pts, number_of_channels]);
    for channel in range (number_of_channels):
        for i in range(num_data_pts):
            PSD[i,channel] = (X[i, channel])**2 / num_data_pts;
    
    # 2. Convert the PSD into a probability density function (PDF)
    PDF = np.zeros([num_data_pts, number_of_channels]);
    sums = np.sum(PSD, axis=0);
    for channel in range (number_of_channels):
        for i in range(num_data_pts):
            PDF[i,channel] = (PSD[i, channel]) / sums[channel];
    
    # 3. Compute entropies. Each value corresponds to the channel's entropy
    for channel in range (0, number_of_channels):
        for i in range(1, num_data_pts): # START WITH THE SECOND DATA POINT
            spectral_entropy[0,channel] += - PDF[i][channel] * math.log(PDF[i][channel], 2);
    
    return spectral_entropy;