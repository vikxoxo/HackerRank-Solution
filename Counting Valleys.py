#https://www.hackerrank.com/challenges/counting-valleys/problem
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    s = list(s)
    count = 0
    V=M=0
    for e in s:
        if e=='U':
            count= count+1
        else:
            count = count - 1
        if count==0:
            if e=='U':
                V = V+1
            elif e=='D':
                M = M+1
    return V



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
