'''
	CIS 519 Project: Seizure Prediction
	Energy Feature Calculation - 
        Energy, Nonlinear energy, Accumulated energy
	Author: Catherine Yee
'''

import numpy as np

class energy_calcs:

    def __init__(self, width=100, shift=50):
        '''
        Constructor
        '''
        self.width = width
        self.shift = shift

    def energy(self, X):
    	'''
    	Returns energy feature calculation
    	'''
    	return 0

    def nonlinear_energy(self, X):
        '''
        Returns nonlinear energy feature calculation
        '''
        return 0

    def accumulated_energy(self, X):
        '''
        Returns accumulated energy feature calculation
        '''
        return 0