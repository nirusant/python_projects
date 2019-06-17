import numpy as np
from matplotlib import pyplot as plt
import time
import timeit

class Mandelbrot2(object):

    def __init__(self, numIt,pixelWidth, pixelHeight, xMinVal, xMaxVal, yMinVal, yMaxVal):
        self.numIt = numIt 
        self.pixelWidth = pixelWidth
        self.pixelHeight = pixelHeight
        self.xMinVal = xMinVal
        self.xMaxVal = xMaxVal
        self.yMinVal = yMinVal
        self.yMaxVal = yMaxVal 


    def mandelbrot(self,c, numIt):
        """
        Recieves two variables:
            - c: A matrixcontaining complex values, spaning a selected area of the complex plane.
            - numIt: an integer telling the function how long to iterate. 
        Using the fact that an operation on a matrix, means that we do an operation on every entry we can more or less use the same logic as used before.
        The difference is that we have to keep track of the parts of the matrix that can be multiplied.
        The function returns a matrix consisting of ints  
        """
        z = np.zeros(c.shape, dtype=np.complex64)
        img = np.zeros(c.shape, dtype = int) #The final image

        for n in range(numIt):
            active = (z.real*z.real + z.imag*z.imag) < 4.0 #Checking if any of the elements are less than 4.0
            img[active] += 1; # Every element that is smaller than 4.0 is added to the matrix
            z[active] = z[active]**2+c[active] #Only the elements that are smaller than 4.0 is multiplied, this prevents overflow 
        return img



    def makeMandelbrotSet(self):
        """
        The function is similar to the function in mandelbrot_1.py.
        The difference is that the function creates a matrix that spans a selected area of the complex plane and sends it to the mandelbrot function 
        The return value is an 2D-matrix with integer values 
        """

        numIt = self.numIt   
        pixelWidth = self.pixelWidth 
        pixelHeight = self.pixelHeight  
        xMinVal = self.xMinVal  
        xMaxVal = self.xMaxVal  
        yMinVal = self.yMinVal  
        yMaxVal = self.yMaxVal  

        Re = np.linspace(xMinVal, xMaxVal, pixelWidth)
        Im = np.linspace(yMinVal, yMaxVal, pixelHeight)
        img = np.zeros((pixelWidth,pixelHeight), dtype = int) 

        x,y = np.meshgrid(Re,Im)
        cplane = x + -1*y*1j    
        img = self.mandelbrot(cplane, numIt)
        return img


if __name__ == '__main__':
    M = Mandelbrot2(100,1000,1000,-2,1,-1.5,1.5)
    for i in range(5):
        t0 = time.time()
        res = M.makeMandelbrotSet()
        t1 = time.time()
        total = t1-t0
        print(total)
    plt.imshow(res)
    plt.show()
