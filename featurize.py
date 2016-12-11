# -*- coding: utf-8 -*-
'''
	CIS 519 Project: Seizure Prediction
	Feature Characterization Script For Seizure Data Analysis
	Author:   Tyrell McCurbin
'''
import os
import numpy as np
from sixth_power import sixth_power
from curve_length import curve_length
from spectral_entropy import spectral_entropy
from energy_calcs import energy, nonlinear_energy, accumulated_energy


#===============================================
# SETUP
#===============================================
isTrainingData = 0; # Set to 1 if using training data
if (isTrainingData):
    directory = 'F://KaggleData/Python/Train_1/';
else:
    directory = 'F://KaggleData/Python/Test_1/';
num_channels = 16;
num_features = 6;
num_files = len([f for f in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, f))])


#===============================================
# LOOP THROUGH ALL FILES IN A DIRECTORY
#===============================================
i = 0;
for filename in os.listdir(directory):
    print (i);
    # Extract the data from the file    
    data = np.loadtxt(directory + filename, delimiter= ',');
    # Calculate the features for the file     
    sp = sixth_power(data)[0];
    cl = curve_length(data)[0];
    se = spectral_entropy(data);
    e = energy(data)[0];
    ne = nonlinear_energy(data);
    ae = accumulated_energy(data)[0,:];
    if (isTrainingData):
        label = np.array([int(filename[-5])]); # Extract label from file name
        # Concatenate features into row vector
        instance = np.concatenate((sp, cl, se, e, ne, ae, label));
    else:
        instance = np.concatenate((sp, cl, se, e, ne, ae));
    i += 1;
    np.savetxt(filename[:-4] + '_feat.dat', instance, delimiter=',');