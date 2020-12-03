import sys, os, getpass
import heapq as hq
import math, random, functools, itertools
from collections import Counter, defaultdict, deque
input = sys.stdin.readline

# available on Google, AtCoder Python3
# not available on Codeforces
# import numpy as np
# import scipy

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
def log(*args):  
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)


def solve_1_(lst):
    # your solution here

    low, high = lst[0].split("-")
    low, high = int(low), int(high)
    alpha = lst[1][0]
    password = lst[2]

    c = Counter(password)

    if low <= c[alpha] <= high:
        return 1

    return 0

def solve_2_(lst):
    # your solution here

    low, high = lst[0].split("-")
    low, high = int(low)-1, int(high)-1
    alpha = lst[1][0]
    password = lst[2]

    if (password[low] == alpha) + (password[high] == alpha) == 1:
        return 1

    return 0


def solve_1(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_1_(*args)

def solve_2(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_2_(*args)


def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]


overall_res = 0

for case_num in range(1000):  # no loop over test case
# for case_num in [1]:  # no loop over test case
# for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    lst = input().split()
    
    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read multiple rows
    # mrr = read_matrix(k)
    # arr = read_strings(k)

    res = solve_1(lst)  # please change
    # res = solve_2(lst)  # please change
    
    overall_res += res
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list

print(overall_res)