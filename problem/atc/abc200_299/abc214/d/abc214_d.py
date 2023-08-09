# Problem: D - Sum of Maximum Weights
# Contest: AtCoder - AtCoder Beginner Contest 214
# URL: https://atcoder.jp/contests/abc214/tasks/abc214_d
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc214/tasks/abc214_d

输入 n(2≤n≤1e5) 和一棵树的 n-1 条边（节点编号从 1 开始），每条边包含 3 个数 a b c，表示有一条边权为 c(1≤c≤1e7) 的边连接 a 和 b。
定义 f(x,y) 表示从 x 到 y 的简单路径上的最大边权。
输出所有 f(i,j) 的和，其中 i<j。

相似题目：
2421. 好路径的数目
https://codeforces.com/problemset/problem/915/F
输入
3
1 2 10
2 3 20
输出 50
解释 f(1,2)+f(2,3)+f(1,3)=10+20+20=50

输入
5
1 2 1
2 3 2
4 2 5
3 5 14
输出 76
"""


#    437    ms
def solve():
    n, = RI()
    es = []
    for _ in range(n - 1):
        u, v, c = RI()
        es.append((c, u - 1, v - 1))
    es.sort()
    ans = 0
    fa = list(range(n))
    size = [1] * n

    def find(x):
        t = x
        while fa[x] != x:
            x = fa[x]
        while t != x:
            fa[t], t = x, fa[t]
        return x

    for c, u, v in es:
        x, y = find(u), find(v)
        ans += c * size[x] * size[y]
        size[y] += size[x]
        fa[x] = y
    print(ans)


#    443    ms
def solve1():
    n, = RI()
    es = []
    for _ in range(n - 1):
        u, v, c = RI()
        es.append((c, u - 1, v - 1))
    es.sort()
    ans = 0
    fa = list(range(n))
    size = [1] * n

    def find(x):
        t = x
        while fa[x] != x:
            x = fa[x]
        while t != x:
            fa[t], t = x, fa[t]
        return x

    def union(x, y):
        if x == y:
            return False
        x = find(x)
        y = find(y)
        size[y] += size[x]
        fa[x] = y
        return True

    for c, u, v in es:
        x, y = find(u), find(v)
        ans += c * size[x] * size[y]
        union(x, y)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
