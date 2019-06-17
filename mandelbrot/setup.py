from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

"""
To install this module, enter this in the terminal:
sudo python setup.py install

Controlling the installation destination
python setup.py install --prefix=$HOME/install

To call module
from mandelbrot import compute_mandelbrot
"""
name='mandelbrot'
setup(name=name,version='0.1',py_modules=[name],scripts=[name + '.py'])

name='mandelbrot_1'
setup(name=name,version='0.1',py_modules=[name],scripts=[name + '.py'])

name='mandelbrot_2'
setup(name=name,version='0.1',py_modules=[name],scripts=[name + '.py'])

name='mandelbrot_3'
setup(name=name,version='0.1',py_modules=[name],scripts=[name + '.py'])

setup(ext_modules = cythonize("mandelbrot_4_1.pyx"))
name='mandelbrot_4'
setup(name=name,version='0.1',py_modules=[name],scripts=[name + '.py'])



