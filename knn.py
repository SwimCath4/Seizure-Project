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

def predict(centroid_0, centroid_1, x):
    '''
    Returns predicted label
    '''

    #print "len(centroid_0) = ", len(centroid_0)
    #print "len(centroid_1) = ", len(centroid_1)
    #print "len(x) = ", len(x)

    distance_0 = np.linalg.norm(x - centroid_0)
    distance_1 = np.linalg.norm(x - centroid_1)

    if(distance_0 < distance_1):
    	return 0
    elif(distance_0 > distance_1):
        return 1
    else:
        print "Equal distances. Predicting 0."
        return 0
