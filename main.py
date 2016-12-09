# -*- coding: utf-8 -*-
'''
	CIS 519 Project: Seizure Prediction
	Main Function For Seizure Data Analysis
	Authors:   Tyrell McCurbin
                 Catherine Yee
                 Elaida Dimwamwa
                 Zheng Tian
'''
import os
import numpy as np
from sixth_power import sixth_power
from curve_length import curve_length
from spectral_entropy import spectral_entropy
from energy_calcs import energy, nonlinear_energy


X_test_1 = np.loadtxt('1_1_0_small.dat', delimiter= ',');
X_test_2 = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5]]);


#===============================================
# GENERATE THE X ARRAY FOR THE TRAINING DATA
#===============================================
# Count the number of files in the directory
directory = '../Data/';
num_channels = 16;
num_features = 5;
num_files = len([f for f in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, f))])
X = np.zeros([num_files, num_features * num_channels + 1]); # ADD A COL FOR LABEL


#===============================================
# LOOP THROUGH ALL FILES IN A DIRECTORY
# ASSUMES THAT YOUR DATA FOLDER IS NEXT TO THE GITHUB DIRECTORY 
#===============================================
i = 0;
for filename in os.listdir('../Data/'):
    # Extract the data from the file    
    data = np.loadtxt(directory + filename, delimiter= ',');
    # Calculate the features for the file 
    print 'SIXTH POWER';    
    sp = sixth_power(data)[0];
    print sp
    print 'CURVE LENGTH';
    cl = curve_length(data)[0];
    print cl
    print 'SPECTRAL ENTROPY';
    se = spectral_entropy(data)[0];
    print se;
    print 'ENERGY: '
    e = energy(data)[0];
    print e;
    print 'NONLINEAR ENERGY'
    ne = nonlinear_energy(data)[0];
    print ne
    print 'LABEL'
    label = np.array([int(filename[-5])]); # Extract label from file name
    print label  
    # Concatenate features into row vector
    instance = np.concatenate((sp, cl, se, e, ne, label));
    X[i,:] = instance;
    i += 1;
print 'X'    
print X


    