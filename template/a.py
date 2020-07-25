import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr):  # fix inputs here
    console("----- solving ------")
        

    brr = [arr[0]]

    for a in arr[1:]:
        if a == brr[-1]:
            continue
        brr.append(a)

    brr = [999] + brr + [0]

    console(brr)

    pos = []
    neg = []
    
    for a,b,c in zip(brr, brr[1:], brr[2:]):
        if a < b and b > c:
            pos.append(b)
        elif a > b and b < c:
            neg.append(b)
        
    console(pos, neg)

    cash = 1000
    for n,p in zip(neg, pos):
        stock_bought = cash//n
        gains = stock_bought * (p-n)
        cash = cash + gains


    # return a string (i.e. not a list or matrix)
    return cash


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
