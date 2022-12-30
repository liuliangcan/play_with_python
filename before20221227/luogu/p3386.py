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
"""https://www.luogu.com.cn/problem/P3372
模板题，区间加，区间求和。
"""


#  	 ms
def solve(n, m, e, es):
    g = [[] for _ in range(n)]
    for u, v in es:
        g[u - 1].append(v - 1)

    ans = [-1] * m
    vis = [-1] * m

    def find(i, c):
        for j in g[i]:
            if vis[j] != c:
                vis[j] = c
                if ans[j] == -1 or find(ans[j], c):
                    ans[j] = i
                    return True
        return False

    cnt = 0
    for i in range(n):
        # vis = [-1]*m
        if find(i, i):
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    n, m, e = RI()
    es = []
    for _ in range(e):
        es.append(RILST())
    solve(n, m, e, es)
