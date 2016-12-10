#!/usr/bin/python

'''
	CIS 519 Project: Seizure Prediction
	Data plotter for PCA (pca.py); can be run as a script
	Author: Zheng Tian
'''

import numpy as np
import matplotlib.pyplot as plt
import timeit
from sklearn.decomposition import PCA, KernelPCA

'''
	plots explained variance as a f'n of number of primary components
	plots time taken to fit the model as a f'n of number of primary components
'''
def plot_info(filePath, n_components):
	file = open(filePath,'r')
	allData = np.loadtxt(file, delimiter=',')

	Xtrain = allData
	
	plt.figure()
	plt.subplot(1, 2, 1, aspect='equal')
	plt.title("Explained variance given desired principal components")
	start_times = [0]*n_components
	end_times = [0]*n_components
	# plot explained variance as a f'n of number of primary components
	for princ_c in range(n_components):
		pca = PCA(n_components=princ_c)

		start_times[princ_c] = time.clock() # time.clock measures cpu time on unix
		pca_model = pca.fit(Xtrain)
		end_times[princ_c] = time.clock()
		
		print princ_c, pca.explained_variance_
		plt.plot(princ_c, pca.explained_variance_)
	plt.xlabel("Principal components")
	plt.ylabel("Explained variance")

	plt.subplot(2, 2, 1, aspect='equal')
	plt.title("CPU time for PCA given desired principal components")
	plt.plot([(x + 1) for x in range(n_components)], end_times - start_times)
	plt.xlabel("Principal components")
	plt.ylabel("PCA CPU time")

	# TODO: maybe plot primary components as a f'n of desired explained variance?
	# would that be redundant since i plot them the other way around above?
	plt.show()


def main(argv):
	if len(argv) != 2:
		print "usage: [data file], [desired number of primary components]"
		return

	try:
		if int(argv[1]) > 0:
			print "given number of primary components is not a positive integer: ", argv[1]
			return
	except ValueError:
		print "given number of primary components is not an integer: ", argv[1]
		return

	filePath = argv[0]
	n_components = argv[1]
	plot_info(filePath, n_components)


if __name__ == "__main__":
   main(sys.argv[1:])