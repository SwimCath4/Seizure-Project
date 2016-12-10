'''
	CIS 519 Project: Seizure Prediction
	Energy Feature Calculation - 
        Energy, Nonlinear energy, Accumulated energy
'''

import numpy as np

def energy(X):
    '''
    Returns energy feature calculation
    Author: Catherine
    '''
    
    #num_data_pts = int(X.shape[0]);
    #number_of_channels = int(X.shape[1]);
    #energy = np.zeros([1, number_of_channels]); # initialize final array
    
    # Output a vector of eneries. Each value corresponds to the channel's energy
    #for channel in range (number_of_channels):
    #    for i in range(1, num_data_pts - 1): # START WITH THE SECOND DATA POINT
    #        energy[0, channel] += (X[i][channel])**2;
    #    energy[0, channel] = (energy[0, channel]) / num_data_pts;
    
    #return energy

    return np.mean(X**2, axis = 0).reshape(1,16);

def nonlinear_energy(X):
    '''
    Returns nonlinear energy feature calculation
    Author: Tyrell
    '''
    
    num_data_pts = int(X.shape[0]);
    X1 = X[1:-1,:]**2;
    X2 = X[0:-2,:];
    X3 = X[2:,:];
    
    return np.sum(X1 - np.multiply(X2, X3), axis=0) / float(num_data_pts - 2);

def accumulated_energy(X):
    '''
    Returns accumulated energy feature calculation
    Author: Catherine
    '''
    
    num_data_pts = int(X.shape[0]);
    number_of_channels = int(X.shape[1]);
    accumulated_energy = np.zeros([1, number_of_channels]); # initialize final array
    
    # Output a vector of eneries. Each value corresponds to the channel's energy
    for channel in range (number_of_channels):
        for i in range(1, num_data_pts - 1): # START WITH THE SECOND DATA POINT
            accumulated_energy[0, channel] += (X[i][channel])**2;
    
    return accumulated_energy