'''
	CIS 519 Project: Seizure Prediction
	KNN Calculation
	Author: Catherine Yee
'''

import numpy as np

def compute_centroid(centroid_old, x):
    '''
    Returns updated centroid
    '''

    centroid_new = np.vstack((centroid_old, x))
    centroid_new = np.average(centroid_new, axis=0)

    return centroid_new