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

modinv = lambda A,n,s=1,t=0,N=0: (n < 2 and t%N or modinv(n, A%n, t, s-A//n*t, N or n),-1)[n<1]
def invmod(a,b): return 0 if a==0 else 1 if b%a==0 else b - invmod(b%a,a)*b//a

def chinese_remainder_theorem(divisors, remainders):
    log(divisors, remainders)
    sum = 0
    prod = functools.reduce(lambda a, b: a*b, divisors)
    for n_i, a_i in zip(divisors, remainders):
        p = prod // n_i
        sum += a_i * modinv(p, n_i) * p
    return sum % prod


def solve_(x,y,p,q):
    # your solution here

    minres = math.inf

    # find minimum m*(2x+2y)+a == n*(p+q)+b
    # find minimum m*(2x+2y) - n*(p+q) = b-a
    

    for a in range(x,x+y):
        for b in range(p,p+q):
            # cur = chinese_remainder_theorem([2*(x+y), p+q], [a, b])
            div = (2*(x+y))
            mod = p+q
            rem = b-a
            # log(mod, div, rem, rem%mod, div%mod)

            # cur = modinv(rem*div, mod)
            cur = modinv(div, mod)
            # cur = modinv(rem, mod)%mod * modinv(div, mod)%mod

            if cur >= 0:
                # cur = modinv(rem, mod)
                time = (rem*cur)%mod*div + a
                # log(cur, time, a, div)
                minres = min(minres, time)

            # cur = chinese_remainder_theorem([2*(x+y), p+q], [a, b])
            div = p+q
            mod = (2*(x+y))
            rem = a-b
            # log(mod, div, rem, rem%mod, div%mod)

            # cur = modinv(rem*div, mod)
            cur = modinv(div, mod)
            # cur = modinv(rem, mod)%mod * modinv(div, mod)%mod

            if cur >= 0:
                # cur = modinv(rem, mod)
                time = (rem*cur)%mod*div + b
                # log(cur, time, a, div)
                minres = min(minres, time)


    if str(minres) == "inf":
        return "infinity"

    return minres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    a,b,c,d = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(a,b,c,d)  # include input here
    
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