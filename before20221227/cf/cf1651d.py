import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1651/D

输入 n(≤2e5) 和 n 个二维平面上的互不相同的整点，坐标范围 [1,2e5]。
对每个整点，输出离它曼哈顿距离最近的，且不在输入中的整点。
两点的曼哈顿距离=横坐标之差的绝对值+纵坐标之差的绝对值。
输入
6
2 2
1 2
2 1
3 2
2 3
5 5
输出
1 1
1 1
2 0
3 1
2 4
5 4

输入
8
4 4
2 4
2 2
2 3
1 4
4 2
1 3
3 3
输出
4 3
2 5
2 1
2 5
1 5
4 1
1 2
3 2
"""

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


#  1279	 ms
def solve(n, xy):
    s = {(x, y) for x, y in xy}
    vis = {}
    for i, (x, y) in enumerate(xy):
        for dx, dy in DIRS:
            a, b = x + dx, y + dy
            if (a, b) not in s:
                vis[(x, y)] = (a, b)
                break
    q = deque(vis.keys())
    while q:
        x, y = q.popleft()
        nr = vis[(x, y)]
        for dx, dy in DIRS:
            a, b = x + dx, y + dy
            if (a, b) not in s or (a, b) in vis:
                continue
            vis[(a, b)] = nr
            q.append((a, b))

    # def ans(p):
    #     z = vis[tuple(p)]
    #     return f'{z[0]} {z[1]}'
    #
    # print('\n'.join(map(ans, xy)))
    for x, y in xy:
        print(*vis[x, y])


if __name__ == '__main__':
    n, = RI()
    a = []
    for _ in range(n):
        a.append(RILST())

    solve(n, a)
