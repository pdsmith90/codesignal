#!/bin/python3

from numpy import multiply
def adjacentElementsProduct(inputArray):
    arrayMult = multiply(inputArray[:-1], inputArray[1:])
    arrayMult.sort()
    return int(arrayMult[-1:])
