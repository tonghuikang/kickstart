import sys, os
import heapq as hq
import functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

# def dijkstra_with_preprocessing(map_from_node_to_nodes_and_costs, source, target):

    # return costs[idxs[target]]


def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    weights = [math.inf]*n
    path = [None]*n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights


def console(*args):  
    # print on terminal in different color
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
# if os.path.exists('input.txt'):
#     ONLINE_JUDGE = True

# if ONLINE_JUDGE:
#     sys.stdin = open("input.txt","r")
#     sys.stdout = open("output.txt","w")

#     def console(*args):
#         pass


# def solve(*args):
#     # screen input
#     # if not ONLINE_JUDGE:
#     #     console("----- solving ------")
#     #     console(*args)
#     #     console("----- ------- ------")
#     return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.readlines())
    input = lambda: next(inp)
# else:
    # if memory is a constraint
# input = sys.stdin.readline


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    nrows,_ = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(input().strip())
    #     grid.append(list(map(int,input().split())))

    # res = solve(grid)  # please change
    

    grid = ["#"*len(grid[0])] + grid + ["#"*len(grid[0])]
    grid = [["#"] + list(row) + ["#"] for row in grid]

    # locations
    g = defaultdict(list)

    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            val = grid[i][j]
            # if val == "#":
            #     continue
            if val != ".":
                # g[(i,j)].append((val,1))
                g[val].append((i,j))

    # print("check1")
    start = g["S"][0]
    end = g["G"][0]

    # console(g)
    # del grid

    if len(g) == 2:
        print(abs(start[0] - end[0]) + abs(start[1] - end[1]))
        continue

    c = Counter()
    dxy = [(1,0),(-1,0),(0,-1),(0,1)]
    visited = set([start])
    stack = collections.deque([(start,0)])
    while stack:
        (x,y),dist = stack.popleft()
        # print(dist)
        # c[dist] += 1
        val = grid[x][y]
        for dx,dy in dxy:
            xx,yy = x+dx, y+dy
            # print(x,dx, y,dy, xx,yy)
            if grid[xx][yy] == "#":
                continue
            if (xx,yy) in visited:
                continue
            visited.add((xx,yy))
            stack.append(((xx,yy), dist+1))
        if val in g:
            # print(val)
            for i,j in g[val]:
                if (i,j) in visited:
                    continue
                stack.append(((i,j), dist+1))
                visited.add((xx,yy))
            del g[val]
            # print(g)
        if end in visited:
            break
    # print(c)
    # print("results")
    # print(visited)
    if end in visited:
        while stack:
            loc, dist = stack.pop()
            if loc == end:
                print(dist)
                break
    else:
        print(-1)



    # Codeforces - no case number required
    # print(res)
    # print(*res)  # if printing a list