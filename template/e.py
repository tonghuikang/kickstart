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


# https://codeforces.com/blog/entry/80158?locale=en
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


@bootstrap
def recurse(n):
    if n <= 0:
        yield 0
    yield (yield recurse(n-1)) + 2



def build_graph(edges, bidirectional=False, costs=None):
    g = defaultdict(list)
    if costs:
        for (a,b),cost in zip(edges, costs):
            g[a].append((b,cost))
            if bidirectional:
                g[b].append((a,cost))
    else:
        for a,b in edges:
            g[a].append(b)
            if bidirectional:
                g[b].append(a)
    return g



def solve_(edges, queries):
    # your solution here

    vertices = [0 for _ in range(len(edges) + 1)]
    edges_one = [0 for _ in edges]
    edges_two = [0 for _ in edges]

    edge_map_one = {(a,b):i for i,(a,b) in enumerate(edges)}
    edge_map_two = {(b,a):i for i,(a,b) in enumerate(edges)}

    for i,e,x in queries:
        if i == 1:
            edges_one[e] += x
        else:
            edges_two[e] += x

    del queries

    g = build_graph(edges, bidirectional=True)

    del edges

    visited = set([0])

    @bootstrap
    def dfs(cur, addn):
        log("a", cur, addn)
        vertices[cur] += addn
        bddn = 0
        for nex in g[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            if (nex,cur) in edge_map_one:
                idx = edge_map_one[nex,cur]
                x = edges_one[idx]
                y = edges_two[idx]
            else:
                idx = edge_map_two[nex,cur]
                x = edges_two[idx]
                y = edges_one[idx]
            # x,y = y,x
            bddn += yield dfs(nex, addn+x)
            bddn += y
        vertices[cur] += bddn
        log("b", cur, bddn)
        yield bddn

    dfs(0, 0)
    
    return vertices




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

for case_num in [1]:  # no loop over test case
# for case_num in range(int(input())):

    # read line as a string
    # strr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()

    # read line as an integer
    n = int(input())
    nrr = read_matrix(n-1)
    
    q = int(input())
    qrr = read_matrix(q)

    nrr = [(x-1, y-1) for x,y in nrr]
    qrr = [(t,e-1,x) for t,e,x in qrr]

    # read one line and parse each word as an integer
    # n,k = list(map(int,input().split()))

    # read multiple rows
    # arr = read_strings(k)

    res = solve(nrr, qrr)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    for r in res:
        print(r)
    # print(len(res))  # if printing length of list
    # print(*res)  # if printing a list