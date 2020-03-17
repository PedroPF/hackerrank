#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0] * n+1
    for start, stop, val in queries:
        array[start-1] += val
        array[stop] -= val

    max = 0
    count = 0
    for val in array:
        count += val
        if count >  max:
            max = count

    return max


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    print(arrayManipulation(n, queries))
