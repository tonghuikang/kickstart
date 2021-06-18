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

M9 = 10**9 + 7  # 998244353
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
        assert solve_(*args) == solve_old(*args)
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


def z_function(S):
    """
    Z Algorithm in O(n)
    :param S: text string to process
    :return: the Z array, where Z[i] = length of the longest common prefix of S[i:] and S
    """

    n = len(S)
    Z = [0] * n
    l = r = 0

    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and S[z] == S[i + z]:
                z += 1

            l, r = i, i + z

        Z[i] = z

    Z[0] = n
    return Z

def solve_(srr, k):
    # your solution here

    if srr[0] == "a":
        return "a"*k

    abc = {x:i for i,x in enumerate("abcdefghijklmnopqrstuvwxyz")}

    start = srr[0]
    for i,x in enumerate(srr):
        if x > start:
            srr = srr[:i]
            break


    # log(srr)
    lensrr = len(srr)
    z = z_function(srr)
    # log(z)
    best_prefix = srr
    srr += srr[0]
    for i,x in enumerate(z):
        if x > 0:
            if srr[x] < srr[i+x]:
                best_prefix = srr[:i]
                break
    
    res = (best_prefix*(k//len(best_prefix) + 1))[:k]
    log(res)
    return res



def solve_old(srr, k):
    # your solution here

    abc = {x:i for i,x in enumerate("abcdefghijklmnopqrstuvwxyz")}

    res = (srr*(k//len(srr) + 1))[:k]
    assert len(res) == k
    for i in range(1,len(srr)+1):
        candidate = (srr[:i]*(k//i + 1))[:k]
        assert len(candidate) == k
        if candidate < res:
            res = candidate
    return res


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    n,k = list(map(int,input().split()))
    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))
    # lst = minus_one(lst)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)