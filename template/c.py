import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst,a,b):  # fix inputs here
    console("----- solving ------")

    lst = [-1] + [a-1 for a in lst]
    arr = [0 for _ in lst]
    brr = [0 for _ in lst]

    for cur in range(len(lst)):
        cooldown = 0
        while cur != -1:
            if cooldown == 0:
                arr[cur] += 1  # diff
                cooldown = a  # diff
            cooldown -= 1
            cur = lst[cur]

    for cur in range(len(lst)):
        cooldown = 0
        while cur != -1:
            if cooldown == 0:
                brr[cur] += 1  # diff
                cooldown = b  # diff
            cooldown -= 1
            cur = lst[cur]

    crr = [1-(1-x/len(lst))*(1-y/len(lst)) for x,y in zip(arr,brr)]

    console(arr)
    console(brr)
    console(crr)

    # return a string (i.e. not a list or matrix)
    return round(sum(crr),10)


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    _,a,b = list(map(int,input().split()))
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst,a,b)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
