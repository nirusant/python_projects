import unittest 
import numpy as np

from mandelbrot import compute_mandelbrot
class TestMandelbrot(unittest.TestCase):

	def test_if_outside_set(self):
		"""
		Tests if the user defined area is entirely outside of the mandelbrotset. 	
		"""
		xmin = 3
		xmax = 4
		ymin = 3
		ymax = 4
		Nx = 1000
		Ny = 1000
		max_escape_time = 100
		plot_filename = 'None'
		truth = np.zeros((Nx,Ny))
		test = compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time , plot_filename)
		self.assertTrue((truth==test).all(),True)
	
	def test_if_inside_set(self):
		"""
		Tests if the user defined area is entirely inside of the mandelbrotset. 	
		"""
		xmin = -0.1
		xmax = 0.1
		ymin = -0.1
		ymax = 0.1
		Nx = 1000
		Ny = 1000
		max_escape_time = 100
		plot_filename = 'None'
		truth = np.ones((Nx,Ny))*max_escape_time
		test = compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time , plot_filename)
		self.assertTrue((truth == test).all(),True)
				

if __name__ == '__main__':
	unittest.main()
