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
from curve_length import curve_length
from spectral_entropy import spectral_entropy
from energy_calcs import energy_calcs


X_test_1 = np.loadtxt('1_1_0_small.dat', delimiter= ',');
X_test_2 = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5]]);

#===============================================
# LOOP THROUGH ALL FILES IN A DIRECTORY
# ASSUMES THAT YOUR DATA FOLDER IS NEXT TO THE GITHUB DIRECTORY 
#===============================================

# Initialize the energy calcs object
energy_calc_obj = energy_calcs();

for filename in os.listdir('../Data/'):
    print filename;
    directory = '../Data/';
    X = np.loadtxt(directory + filename, delimiter= ',');
    print curve_length
    print curve_length(X);
    print spectral_entropy(X);
    print energy_calc_obj.nonlinear_energy(X, 0);


    