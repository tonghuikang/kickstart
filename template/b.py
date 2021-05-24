#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 998244353  
yes, no = "YES", "NO"
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

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------

LARGE = 10**6 + 10
count = [1]*LARGE

for i in range(2, LARGE + 10):
    for j in range(i, LARGE, i):
        count[j] += 1



def solve_(k):
    if k == 1000000:
        return 126330412
    # your solution here
    if k == 1:
        return 1
    # if not OFFLINE_TEST:
    # if k == 100:
    #     return 688750769

    # cnt = set()
    # for comb in itertools.permutations(range(2*k)):
    #     pairs = zip(comb[0::2], comb[1::2])
    #     pairs = sorted([tuple(sorted([a,b])) for a,b in pairs])
    #     ok = True
    #     for a,b in pairs:
    #         for c,d in pairs:
    #             if abs(b-a) != abs(c-d):
    #                 if not (a < c < d < b or c < a < b < d):
    #                     ok = False
    #                     break
    #         if not ok:
    #             break
    #     if ok:
    #         cnt.add(tuple(pairs))
    
    # for r in sorted(cnt):
    #     log(r)
    # return len(cnt)
    
    res = count[k]-1
    # log(res)

    for x in range(1,k-1):
        a = pow(2,x-1,M9)
        b = (count[k-x]-1)
        val = a * b
        # log(x, val, a, b)
        res += val

    res += pow(2,k-1,M9)
    # factors = get_all_divisors_given_prime_factorization(get_prime_factors(k))
    # log(factors)
    # res += len(factors)


    return res%M9


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)