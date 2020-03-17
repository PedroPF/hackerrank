#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    visited = set()
    count = 0
    for pos, val in enumerate(arr):
        if(pos in visited): # already visited this position, so ignore
            continue
        visited.add(pos)
        if(pos+1 == val): # no swap needed
            continue
        i = arr[pos]-1
        while(i != pos): # runs the whole cycle counting the number of swaps
            visited.add(i)
            count += 1
            i = arr[i]-1
    return count

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(minimumSwaps(arr))
