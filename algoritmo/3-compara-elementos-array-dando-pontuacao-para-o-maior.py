#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):

    scoreBoard = [0, 0]

    if(a and b is not None):
        if(len(a) == len(b)):

            for i in range(len(a)):
                if a[i] > b[i]:
                    scoreBoard[0] += 1
                elif a[i] < b[i]: 
                    scoreBoard[1] += 1
                elif a[i] == b[i]: 
                    pass
                else:
                    return
        
            return scoreBoard 
        
        else:

            return

if __name__ == '__main__':

    arrayMaria = [1,10,6]
    arrayfb = [100,9,8]

    compareTriplets(arrayMaria,arrayfb)