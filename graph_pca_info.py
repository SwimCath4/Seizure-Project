#!/usr/bin/python

'''
	CIS 519 Project: Seizure Prediction
	Data plotter for PCA (pca.py); can be run as a script
	Author: Zheng Tian
'''

import sys
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.decomposition import PCA, KernelPCA

# test with iris data
# from sklearn.datasets import load_iris

'''
	plots explained variance as a f'n of number of primary components
	plots time taken to fit the model as a f'n of number of primary components
'''
def plot_pca_info(data, n_components):
	print "data: ", data
	plt.figure(figsize=(16, 8))
	plt.subplot(1, 2, 1, aspect='equal')
	plt.title("Explained variance given desired principal components")
	start_times = [0]*n_components
	end_times = [0]*n_components
	# plot explained variance as a f'n of number of primary components
	for i in range(n_components):
		princ_c = i + 1
		# change this to try diff things
		pca = PCA(n_components=princ_c)

		start_times[i] = time.clock() # time.clock measures cpu time on unix
		pca.fit_transform(data)
		end_times[i] = time.clock()
		
		print "princip. comp.s, explained var.: ", princ_c, sum(pca.explained_variance_ratio_)
		plt.plot(princ_c, sum(pca.explained_variance_ratio_), "ko", linestyle='None')
	plt.xlabel("Principal components")
	plt.ylabel("Explained variance")

	plt.subplot(1, 2, 2, aspect='equal')
	plt.title("CPU time for PCA given desired principal components")
	# list comprehension is cool, just wanted to say
	plt.plot([(x + 1) for x in range(n_components)], np.multiply([end_times[y] - start_times[y] for y in range(n_components)], 1000))
	plt.xlabel("Principal components")
	plt.ylabel("CPU time (milliseconds)")

	# TODO: maybe plot primary components as a f'n of desired explained variance?
	# would that be redundant since i plot them the other way around above?
	plt.tight_layout()
	plt.show()


def main(argv):
	if len(argv) != 2:
		print "usage: [data file], [desired number of primary components]"
		return

	try:
		if int(argv[1]) < 1:
			print "given number of primary components is not a positive integer: ", argv[1]
			return
	except ValueError:
		print "given number of primary components is not an integer: ", argv[1]
		return

	filePath = argv[0]
	file = open(filePath,'r')
	data = np.loadtxt(file, delimiter=',')
	n_components = int(argv[1])
	plot_pca_info(data, n_components)


if __name__ == "__main__":
   main(sys.argv[1:])