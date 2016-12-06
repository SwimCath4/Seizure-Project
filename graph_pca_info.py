'''
	CIS 519 Project: Seizure Prediction
	PCA
	Author: Zheng Tian
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, KernelPCA

def main(argv):
	if len(argv) > 1:
		print "only 1 argument should be given"
		return

	try:
		if type(argv[0]) == int and argv[0] > 0:
			print "given number of primary components is not a positive integer: ", argv[0]
			return
	except ValueError:
		print "given number of primary components is not an integer: ", argv[0]
		return

	n_comps = argv[0]

	# plot explained variance as a f'n of number of primary components
	for pc in range(n_comps):
		# TODO: do stuff
		return
	plt.xlabel("n_components")
	plt.ylabel("explained variance")


	# plot primary components as a f'n of desired explained variance
	for x in xrange(1,10):
		# TODO: do stuff
		return

	plt.show()

if __name__ == "__main__":
   main(sys.argv[1:])