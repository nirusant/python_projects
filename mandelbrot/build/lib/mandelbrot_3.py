import numpy as np
from matplotlib import pyplot as plt
import time
from numba import jit

@jit(nopython=True)
def mandelbrot(z,numIt):
    """
    Same as in mandelbrot_1.py
    """
    c = z
    for n in range(numIt):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return numIt

@jit
def makeMandelbrotSet(numIt,pixelWidth, pixelHeight, xMinVal, xMaxVal, yMinVal, yMaxVal):
    """
    Combining elements from mandelbrot_1 and mandelbrot_2
    """
    #When giving the mandelbrot function a real and complex number, we have to calculate how large the interval between two 
    #pixels should be. The next four lines of codes does this.   
    xstep = abs(xMinVal-xMaxVal)/pixelWidth 
    Re = xMinVal #The start point for the X-value    
    ystep = abs(yMinVal-yMaxVal)/pixelHeight
    Im = yMaxVal #The start point for the Y-value

    img = np.zeros((pixelHeight,pixelWidth), dtype=int)
    for i in range(0,pixelHeight):
        for j in range(0,pixelWidth):
            img[i,j] = mandelbrot(complex(Re,Im),numIt)
            Re +=xstep    
        Im -=ystep
        Re = xMinVal
    return img


if __name__ == '__main__':
    xmin = -2
    xmax = 1
    ymin = -1.5
    ymax = 1.5

    for i in range(5):
        t0 = time.time()
        res = makeMandelbrotSet(100,1000,1000,xmin,xmax,ymin,ymax)
        t1 = time.time()
        total = t1-t0
        print(total)

    plt.imshow(res, extent=[xmin,xmax,ymin,ymax])
    plt.show()
