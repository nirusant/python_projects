import numpy as np
from matplotlib import pyplot as plt
from array import *
import time
import timeit


class Mandelbrot1(object):

    def __init__(self, numIt,pixelWidth, pixelHeight, xMinVal, xMaxVal, yMinVal, yMaxVal):
        self.numIt = numIt 
        self.pixelWidth = pixelWidth
        self.pixelHeight = pixelHeight
        self.xMinVal = xMinVal
        self.xMaxVal = xMaxVal
        self.yMinVal = yMinVal
        self.yMaxVal = yMaxVal 
    
    def mandelbrot(self,z,numIt):
        """
        mandelbrot():
        Given a complex number z and a user defined number of iterations(numIt), this function finds the number of iterations it can do before  the absoulute value of z is larger than 2.
        This function returns the number of iterations before it reached an absolute value over 2, or numIt if the function does not get an absolute value above 2 in the given number of iterations.  
        """
        c = z #The constant c that always is added to the number that is iterated on.  
        for n in range(numIt):
            if abs(z) > 2.0: #Assuming that every complex number with an absolute value over 2 is going to go to infinity 
                return n #If abs(z) is larger than 2, the function returns how many iterations it did befor reaching abs(z) > 2
            z = z**2 + c
        return numIt #If the function iterates to the maximum number of iterattions, the numIt is returned


    def makeMandelbrotSet(self):
        """
        MakeMandelbrotSet():
        This function makes a mandlebrot set based on the number of iterations and how much of the complex plane we are allowed to span. 
        numIt decides the number of iterations the function is allowed to iterate to.
        The variable pixelWidth decides the resolution/accuracy on the x-axis.
        
        This variable works in conjuctions with xMinVal and xMaxVal since those two variables decied how much of the real axis we are going to span.
        The variabel pixelHeight does the same thing as pixelWidth but this handles the accuracy/resolution on the y-axis.
        
        pixelHeight works in conjuction with yMinVal and yMaxVal as they span the imaginary axis.
        The function returns an 2D-array that spans the user defined complex plane. 
        """

        numIt = self.numIt   
        pixelWidth = self.pixelWidth 
        pixelHeight = self.pixelHeight  
        xMinVal = self.xMinVal  
        xMaxVal = self.xMaxVal  
        yMinVal = self.yMinVal  
        yMaxVal = self.yMaxVal   

        #When giving the mandelbrot function a real and complex number, we have to calculate how large the interval between two 
        #pixels should be. The next four lines of codes does this.   
        xstep = abs(xMinVal-xMaxVal)/pixelWidth 
        Re = xMinVal #The start point for the X-value    
        
        ystep = abs(yMinVal-yMaxVal)/pixelHeight
        Im = yMinVal #The start point for the Y-value

        img = [] #Empty list for adding arrays as the function tests different values
        for j in range(0,pixelHeight+1):
            line = [] #adding every real value for a given imaginary value 
            for i in range(0,pixelWidth+1):
                line.insert(i,self.mandelbrot(complex(Re,Im),numIt))
                Re += xstep

            img.append(line)#Appending every real value to a given imaginary value.
            Im += ystep
            Re = xMinVal
        return np.asmatrix(img, dtype=int)



if __name__ == '__main__':
    M = Mandelbrot1(100,1000,1000,-2,1,-1.5,1.5)
    for i in range(5):
        t0 = time.time()
        res = M.makeMandelbrotSet()
        t1 = time.time()
        total = t1-t0
        print(total)
    plt.imshow(np.asmatrix(res))
    plt.show()

