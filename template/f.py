#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

# ---------------------------- template ends here ----------------------------

import numpy as np
from scipy import signal
# sig = np.random.randn(1000000)
# autocorr = signal.fftconvolve(sig, sig[::-1], mode='full')
# print(autocorr)


def solve_(arr, brr):
    # if len(arr) == len(brr):
    #     return sum(a != b for a,b in zip(arr,brr))
    if len(brr) == 1:
        return 1-int(brr in arr)

    lbrr = len(brr)
    # MOD = 998244353
    # your solution here
    arr = [1-2*int(x) for x in arr]
    brr = [1-2*int(x) for x in brr] + [0]*(len(arr)-len(brr))

    crr = signal.fftconvolve(arr[::-1], brr, mode='full')
    crr = crr
    # val = 3*10**6
    # crr = [x-MOD if x > val else x for x in crr]
    # log(crr)
    # log(crr[2])
    crr = [round(x) for x in crr]
    # log(crr[2])
    # log(crr)

    prefix = lbrr - 1
    expected = len(arr) - lbrr + 1
    relevant = crr[prefix:expected+prefix]

    # log(relevant)

    best = max(relevant)

    # log(crr)
    # log(relevant)

    return (lbrr-best)//2


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    arr = input().strip()
    brr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(arr, brr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)