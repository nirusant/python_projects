cimport numpy as np
import numpy as np
from matplotlib import pyplot as plt
import time
import cython

cdef int mandelbrot(double re, double im, int numIt):
    """
    The logic is same as in mandelbrot_1.py.
    The difference is that instead of using the pythons abs function normal arithmetic is used 
    This makes the code more c-heavy and by that hopefully quicker
    """
    cdef:
        double re_c = re
        double im_c = im
        double tmpRe  
        double tmpIm 
        int n
    
    for n in range(numIt):
        if(re*re+ im*im) > 4.0:
            return n
        """
        (a+bj)(c+dj) = ac + adj +bcj-bd = (ac-bd)+(ad+bc)j
        (a+bj)(a+bj) = aa + abj + abj+(-bb) = (aa-bb) + 2(ab)j   
        """
        tmpRe = (re*re - im*im) + re_c
        tmpIm = 2*(re*im) + im_c
        re = tmpRe
        im = tmpIm
    return numIt

@cython.boundscheck(False) 
@cython.wraparound(False)
cpdef np.ndarray c_makeMandelbrotSet(int numIt, int pixelWidth, int pixelHeight, double xMinVal, double xMaxVal, double yMinVal, double yMaxVal):
    """
    Combining elements from mandelbrot_1 and mandelbrot_2
    """
    cdef:
        np.ndarray img = np.zeros((pixelHeight,pixelWidth), np.int)
        double[:] Re = np.linspace(xMinVal,xMaxVal,pixelWidth, dtype = np.double)
        double[:] Im = np.linspace(yMinVal,yMaxVal,pixelHeight, dtype = np.double)
        int i
        int j 
              
    for i in range(0,pixelHeight):
        for j in range(0,pixelWidth):
            img[i,j] = mandelbrot(Re[j],Im[i],numIt)
    return img

