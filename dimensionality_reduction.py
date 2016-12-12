#!/usr/bin/python

'''
	CIS 519 Project: Seizure Prediction
	PCA
	Author: Zheng Tian
'''

import sys
import numpy as np
import pca
import graph_pca_info

'''
	currently only uses PCA; no way to use kernel PCA from here
	arguments:
		the data to perform PCA on
		number of principal components
		whether to plot info from graph_pca_info
			Note: if you want to plot info, pca with the number of principal components
				will be run twice. This should be fine, since PCA is deterministic.
'''
def main(argv):
	if len(argv) != 3:
		print "usage: [data], [# of principal components], [whether to plot]"

	try:
		if int(argv[1]) < 1:
			print "given number of desired primary components is not a positive integer: ", argv[1]
			return
	except ValueError:
		print "given number of desired primary components is not an integer: ", argv[1]
		return

	n_components = int(argv[1])
	data = argv[0]

	if argv[2]:
		graph_pca_info.plot_info(data, n_components)

	return pca_model

if __name__ == "__main__":
   main(sys.argv[1:])