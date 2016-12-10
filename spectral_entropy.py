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
    
    # The following routine is based off of information found on Stack Exchange
    # 1. Calculate the frequency spectrum of the signal
    fourier = np.fft.fft(X, axis=0);
    
    # 2. Calculate the Power Spectral Density
    P = np.abs(fourier)**2 / float(num_data_pts);
    
    # 3. Convert the PSD into a probability density function (PDF)
    p = P / (P.sum(axis=0)).astype(float);
    
    # 4. Compute entropies. Each value corresponds to the channel's entropy    
    return -np.sum(np.multiply(p, np.log(p)), axis=0) / float(num_data_pts);