import sys
import numpy as np
from matplotlib import pyplot as plt
import time

"""
Importing the different mandelbrot implementations
"""
from mandelbrot_1 import Mandelbrot1
from mandelbrot_2 import Mandelbrot2
from mandelbrot_3 import makeMandelbrotSet
from mandelbrot_4 import cython_mandelbrot

def help_win():
    """
    If the user uses the --help flag this function is going to run. 
    """
    print('Help screen for mandelbrot.py:')
    print('When running this program please be ready to provide:')
    print('\t-xmin: Starting value in the x/real-domain')
    print('\t-xmax: Stoping value in the x/real-domain')
    print('\t-ymin: Starting value in the y/imaginary-plane')
    print('\t-ymax: Stoping value in the y/imgainary-plane')
    print('\t-Nx: The interval between the minimum value and maximum value in the x/real-direction')
    print('\t-Ny: The interval between the minimum value and maximum value in the y/imaginary-direction')
    print('\t-max_esc_t: The maximum number of iterations')
    print('\t-Type of implementation:')
    print('\t\t* python (Mandelbrot implemented with native python functions)')
    print('\t\t* numpy (Mandelbrot implemented with the use of the numpy library)')
    print('\t\t* numba (Mandelbrot implemented with the use of the numba library)')
    print('\t\t* cython (Mandelbrot implemented with the use of the cython library)')
    print('\t-Name of the output image: If you don\'t want an image write, None ')
    sys.exit()

def get_arguments():
    """
    If the user decides to run only run mandelbrot.py the user interface is going to be run.
    This funtion only uses python's input function to get arguments and do the proper datatype casts.
    Returns the set of parameters necesarry to run rest of the program 
    """
    xmin = -2.0
    xmin = np.double(input("xmin: "))
         
    xmax = 2.0
    xmax = np.double(input("xmax: "))
        
    ymin = -1.5
    ymin = np.double(input("ymin: "))
 
    ymax = 1.5
    ymax = np.double(input("ymax: "))

    nx = 100
    nx = int(input("Nx: "))

    ny = 100
    ny = int(input("Ny: "))

    max_esc_t = 100
    max_esc_t = int(input("max_esc_time: "))

    imp = ''
    imp = input("Type of implementation(python, numpy, numba, cython): ")  

    img_name = 'None'
    img_name = input("Name of the output image: ")
    if(img_name == 'None'):
        img_name = None
 
    return xmin, xmax, ymin, ymax, nx, ny, max_esc_t, imp, img_name  

def select_from_ui(xmin, xmax, ymin, ymax, nx, ny, max_esc_t, imp, img_name):
    """
    Based on the users preferance on how to calculate the mandelbrot set, this functions runs the appropriate
    function
    Then the function calls a function to save or display the generated image
    """
    if(imp == 'python'):
        M = Mandelbrot1(max_esc_t, nx, ny, xmin, xmax, ymin, ymax)
        res = M.makeMandelbrotSet()

    elif(imp == 'numpy'):
        M = Mandelbrot2(max_esc_t, nx, ny, xmin, xmax, ymin, ymax)
        res = M.makeMandelbrotSet()

    elif(imp == 'numba'):
        res = makeMandelbrotSet(max_esc_t, nx, ny, xmin, xmax, ymin, ymax)

    elif(imp == 'cython'):
        res = cython_mandelbrot(max_esc_t, nx, ny, xmin, xmax, ymin, ymax)

    else:
        print('Invalid name of desired implementation, please use the flag --help for more information')
        sys.exit()
    
    img_maker(res,img_name,xmin,xmax,ymin,ymax)

def img_maker(res,img_name,xmin,xmax,ymin,ymax):
    """
    Generates an image of the mandelbrot set based on the input res
    if img_name = None  the image only gets displayed and not saved
    """
    if(img_name != None):
        obj = plt.imshow(np.asmatrix(res),extent=[xmin,xmax,ymin,ymax])
        img_name +='.eps' 
        plt.savefig(img_name, format='eps')
        print('Image created: '+img_name)
    else:
        plt.imshow(np.asmatrix(res),extent=[xmin,xmax,ymin,ymax])
        plt.show();

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time = 1000, plot_filename = None):
    """
    This is the function is the intended function to use when importing mandelbrot whereevere on the computer.
    The description on how to implement this was somewhat ambigious so this is based on my own interpretation of the assignment text.
    
    The first step is to check if the user defined area in the complex-space is an are that is a part of the mandebrotset.
    This is done by finding the absoulute value of each point in the complex space.
    If every single one of them has an absoulte value larger than 2 this function simply returns a zero-matrix.
    The user that is also provided with a message telling them that the chosen area is outside the mandelbrotset.

    After passing this test I have opted to use the cython implementation, since that implementation is the fastes one. 
    
    Finally the function checks if the user wants an image or not         
    """
    ReIm1 = np.sqrt(xmin**2 + ymin**2)
    ReIm2 = np.sqrt(xmin**2 + ymax**2)
    ReIm3 = np.sqrt(xmax**2 + ymin**2)
    ReIm4 = np.sqrt(xmax**2 + ymax**2)   
    if (ReIm1 > 2 and ReIm2 > 2 and ReIm3 > 2 and ReIm4 > 2 ):
        print('The given values are outside the mandelbrotset')
        return np.zeros((Nx,Ny))    
    t0 = time.time()
    res = cython_mandelbrot(max_escape_time, Nx, Ny, xmin, xmax, ymin, ymax)        
    t1 = time.time()
    total = t1-t0
    print('Seconds used: ', total)
    if(plot_filename == 'None'): 
        img_maker(res,None,xmin,xmax,ymin,ymax)
    else:
        img_maker(res,plot_filename,xmin,xmax,ymin,ymax)         
    return res

def make_art():
    """
    Function made for the art contest
    """
    xmin = -2
    xmax = 0.75
    ymin = 1.25
    ymax = -1.25
    Nx = 6000
    Ny = 6000
    max_escape_time = 100
    img_name = 'contest_img'
    res = cython_mandelbrot(max_escape_time, Nx, Ny, xmin, xmax, ymin, ymax)
    above = res > max_escape_time*0.90
    res[above] = 0
    plt.imshow(np.asmatrix(res),extent=[xmin,xmax,ymin,ymax],cmap = 'nipy_spectral')
    plt.show()

if __name__ == '__main__':
    """
    When only mandelbrot.py is ran
    """
    if(len(sys.argv) > 1):
        if(sys.argv[1] == '--help'):
            help_win()
        if(sys.argv[1] == '--art' ):
            make_art()
            sys.exit()
        else:
            print('Invalid flag, valid flag is --help')
            sys.exit()
 
    xmin, xmax, ymin, ymax, nx, ny, max_esc_t, imp, img_name = get_arguments() 
    select_from_ui(xmin, xmax, ymin, ymax, nx, ny, max_esc_t, imp, img_name)


