# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
'''
	CIS 519 Project: Seizure Prediction
	Generate X Array by Parsing All Feature Files in a Directory
	Author:   Tyrell McCurbin
'''

import os
import numpy as np

#===============================================
# SETUP
#===============================================
isTrainingData = 1; # Set to 1 if using training data 0 fot test data
if (isTrainingData):
    directory = '../train_features/';
else:
    directory = '../test_features/';
num_channels = 16;
num_features = 6;
num_files = len([f for f in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, f))])
if (isTrainingData):
    X = np.zeros([num_channels * num_features + 1, num_files])
else:
    X = np.zeros([num_channels * num_features, num_files]) # transpose at end

#===============================================
# LOOP THROUGH ALL FILES IN A DIRECTORY
#===============================================
i = 0;
for filename in os.listdir(directory):
    print (i);
    # Extract the data from the file    
    X[:,i] = np.loadtxt(directory + filename, delimiter= ',');
    i += 1;

X = np.transpose(X);
if (isTrainingData):
    np.savetxt('X_train.dat', X, delimiter=',');
else:
    np.savetxt('X_test.dat', X, delimiter=',');    