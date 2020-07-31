#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'treeConstruction' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. LONG_INTEGER X
#

def treeConstruction(N, X):
    if X < N-1:
        return [[-1, -1]]
    if X > ((N-1)*N)//2:
        return [[-1, -1]]

    # distributable
    
    flood = ((N)*(N-1))//2
    fill = X
    
    missing = flood - fill
    
    guess = int(math.sqrt(missing))
    guesses = [guess-1, guess, guess+1, guess+2]
    
    # print(guesses)
    
    for guess in guesses:
        if (guess*(guess+1))//2 > missing:
            break
            
    height = N-guess
    
    print("flood", flood)
    print("fill", fill)
    print("guess", guess)
    print("height", height)
    # Write your code here
    
    # N-2, guess, remainder
    
    res = []
    for i in range(height):
        # print("main")
        res.append([i+1, i+2])
    
    remaining_nodes = N - height - 1
    remaining_score = fill - (height*(height+1)//2) - remaining_nodes
    
    print(remaining_nodes)
    print(remaining_score)
    
    for i in range(height, N-1):
        assign = min(remaining_score, height-1)
        remaining_score = remaining_score - (assign)
        res.append([assign+1, i+2])
                
    # print(res)
    return res
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        first_multiple_input = input().rstrip().split()

        N = int(first_multiple_input[0])

        X = int(first_multiple_input[1])

        result = treeConstruction(N, X)

        fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
        fptr.write('\n')

    fptr.close()