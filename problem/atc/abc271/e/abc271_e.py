# Problem: E - Subsequence Path
# Contest: AtCoder - KYOCERA Programming Contest 2022（AtCoder Beginner Contest 271）
# URL: https://atcoder.jp/contests/abc271/tasks/abc271_e
# Memory Limit: 1024 MB
# Time Limit: 2000 ms
#
# Powered by CP Editor (https://cpeditor.org)

import sys
import heapq
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, inf
from array import *
from functools import lru_cache

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda x: sys.stderr.write(f'{str(x)}\n')

MOD = 10**9 + 7


def solve(n, m, k, es, a):
    # 实际上是按照a的顺序逐步加边，那么类似最短路去给距离松弛即可
    dis = [0, 0] + [inf] * n
    for i in a:
        u, v, w = es[i - 1]
        dis[v] = min(dis[v], dis[u] + w)
    # DEBUG(dis)
    if dis[n] < inf:
        print(dis[n])
    else:
        print(-1)


if __name__ == '__main__':
    n, m, k = RI()
    es = []
    for _ in range(m):
        es.append(RILST())

    a = RILST()
    solve(n, m, k, es, a)

# if __name__ == '__main__':
# n, m, _ = RI()
# es = []
# for _ in range(m):
# es.append(RILST())
# dis = [0,0] + [inf]*(n-1)
# for i in RI():
# u,v,w = es[i-1]
# x = dis[u] + w
# if dis[v] > x:
# dis[v] = x
# if dis[-1] < inf:
# print(dis[-1])
# else:
# print(-1)
"""https://atcoder.jp/contests/abc271/tasks/abc271_e

输入 n m k (≤2e5)，然后输入 m 条边，每条边输入两个点 x y（表示从 x 到 y 的一条有向边，点的编号 1~n）和一个值在 [1,1e9] 内的边权，每条边的编号 1~m。
图中没有自环，但可能有重边。
然后输入一个长为 k 的数组 a (1≤e[i]≤m)。
找到一条从 1 到 n 的路径，满足路径上的边的编号是 a 的子序列。
输出满足这个要求的路径的最短长度。如果不存在，输出 -1。
输入
3 4 4
1 2 2
2 3 2
1 3 3
1 3 5
4 2 1 2
输出 4

输入
3 2 3
1 2 1
2 3 1
2 1 1
输出 -1
"""
