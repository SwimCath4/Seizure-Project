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

    return np.mean(np.power(X, 2), axis = 0).reshape(1,16);

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

    ## Define width and shift values for accumulated energy calculation ##    
    width = 10
    shift = 5

    ## Compute first energy calculation ##
    E_k = np.zeros([1,16])
    E_k = np.divide(energy(X[0:width]), width)
    acc_energy = E_k
    num_data_pts = len(X)

    ## Calculate m - number of times to update accumulated energy ##
    
    # Handle case in which number of instances is not divisible by 5
    if((num_data_pts / shift - 1)*shift + width > (num_data_pts + shift)):
            end = (num_data_pts / shift - 1)*shift + width
            decr = 1
            while end > num_data_pts:
                end = end - shift
                decr = decr + 1
            m = (num_data_pts / shift - decr)
    else:
        m = (num_data_pts / shift - 1)

    ## Output a vector of accumulated eneries. Each value corresponds to the channel's energy ##
    for i in range(1, m):
        #print "X[i*shift : i*shift + width] = ", X[i*shift : i*shift + width]
        #print "energy(X[i*shift : i*shift + width]) = ", energy(X[i*shift : i*shift + width])
        #print "[[np.divide(energy(X[i*shift : i*shift + width]), width)] = ", [np.divide(energy(X[i*shift : i*shift + width]), width)]
        acc_energy = np.add([np.divide(energy(X[i*shift : i*shift + width]), width)], [acc_energy])

    return acc_energy.reshape(1,16)
