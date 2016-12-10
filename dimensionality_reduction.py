#!/usr/bin/python

'''
	CIS 519 Project: Seizure Prediction
	PCA
	Author: Zheng Tian
'''

import pca
import graph_pca_info

'''
	currently only uses PCA; no way to use kernel PCA from here
	arguments:
		filename of the data file to perform PCA on
		number of principal components
		whether to plot info from graph_pca_info
			Note: if you want to plot info, pca with the number of principal components
				will be run twice. This should be fine, since PCA is deterministic.
'''
def main(argv):
	if len(argv) != 3:
		print "usage: [data file], [# of principal components], [whether to plot]"

	try:
		if int(argv[1]) > 0:
			print "given number of desired primary components is not a positive integer: ", argv[1]
			return
	except ValueError:
		print "given number of desired primary components is not an integer: ", argv[1]
		return

	n_components = argv[1]
	file = open(argv[0],'r')
	data = np.loadtxt(file, delimiter=',')
	pca_model = pca.componentsPca(n_components)
	pca_model.fit(data)

	if argv[2]:
		graph_pca_info.plot_info(argv[0], argv[1])

	return pca_model

if __name__ == "__main__":
   main(sys.argv[1:])