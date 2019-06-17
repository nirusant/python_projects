import numpy as np #importing numpy
import sys #import sys
from numba import jit #importing jit from numba

class test():

    def do_local():
        print('Hi')

"""
This is a
multiline
comment
"""

#This tests as in comments
# This is a comment
print("this") #This comments print-statement

a = False
b = True
c = None

@jit(nopython=True)
def test():
    """
    A function using jit and for loops

    Input:    
        none

    Output:
        none
    """
    for a in range(5):
        for b in range(4): #for
            if a == b: #if test
                print(a)
            elif a>b: # elif-test
                print(b)
            else:
                print(a,b) #else-test

count = 0
while count < 5: #testing while loop
   print(count, " is  less than 5")
   count = count + 1

print(count, " is not less than 5")
