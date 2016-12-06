'''
	CIS 519 Project: Seizure Prediction
	Energy Feature Calculation - 
        Energy, Nonlinear energy, Accumulated energy
'''

import numpy as np

class energy_calcs:

    def __init__(self):
        '''
        Constructor
        '''

    def energy(self, X, sliding_window):
    	'''
    	Returns energy feature calculation
        Author: Catherine
    	'''

        num_data_pts = int(X.shape[0]);
        number_of_channels = int(X.shape[1]);
        energy = np.zeros([1, number_of_channels]); # initialize final array

    	return 0

    def nonlinear_energy(self, X, sliding_window):
        '''
        Returns nonlinear energy feature calculation
        Author: Tyrell
        '''
        num_data_pts = int(X.shape[0]);
        number_of_channels = int(X.shape[1]);
        nonlinear_energy = np.zeros([1, number_of_channels]); # initialize final array

        # Output a vector of eneries. Each value corresponds to the channel's energy
        for channel in range (number_of_channels):
            for i in range(1, num_data_pts - 1): # START WITH THE SECOND DATA POINT
                nonlinear_energy[0, channel] += (X[i][channel])**2 - (X[i - 1][channel] * X[i + 1][channel]);

        return nonlinear_energy

    def accumulated_energy(self, X, sliding_window):
        '''
        Returns accumulated energy feature calculation
        Author: Catherine
        '''
        return 0