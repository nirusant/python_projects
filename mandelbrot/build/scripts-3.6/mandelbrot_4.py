import os
import numpy as np
from matplotlib import pyplot as plt
import time
from mandelbrot_4_1 import c_makeMandelbrotSet

def cython_mandelbrot(max_esc_t, nx, ny, xmin, xmax, ymin, ymax):
	"""
	This function interfaces with mandelbrot_4_1.pyx. 
	The reason for doing this is that I wanted to keep the cython part seperate from the more ordinary python implementation. 
	This affords me some flexibility when doing tests and interfacing with other pure python programs  
	"""
	return np.asarray(c_makeMandelbrotSet(max_esc_t, nx, ny, xmin, xmax, ymin, ymax),dtype = int)


if __name__ == '__main__':
	for i in range(5):
		t0 = time.time()
		res = c_makeMandelbrotSet(100,1000,1000,-2,1,-1.5,1.5)
		t1 = time.time()
		total = t1-t0
		print(total)
	plt.imshow(res)
	plt.show()

