# Problem: D - Ki
# Contest: AtCoder - AtCoder Beginner Contest 138
# URL: https://atcoder.jp/contests/abc138/tasks/abc138_d
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
PROBLEM = """https://atcoder.jp/contests/abc138/tasks/abc138_d

输入 n(2≤n≤2e5) q(1≤q≤2e5) 表示一个 n 个点的树（节点编号从 1 开始，根节点为 1）。
然后输入 n-1 条边（每行两个数）。
然后输入 q 个操作，每个操作输入 p(1≤p≤n) x(1≤x≤1e4)，表示把子树 p 内的所有节点值都加 x。（一开始所有节点值均为 0）
输出最终每个节点的节点值。（按节点编号从小到大输出）
输入
4 3
1 2
2 3
2 4
2 10
1 100
3 1
输出 100 110 111 110

输入
6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10
输出 20 20 20 20 20 20
"""



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
#       ms
def solve():
    n, q = RI()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)
    a = [0] * (n + 1)
    for _ in range(q):
        p, x = RI()
        a[p] += x

    @bootstrap
    def dfs(u, fa):
        a[u] += a[fa]
        for v in g[u]:
            if v != fa:
                yield dfs(v, u)
        yield
    dfs(1, 0)
    print(*a[1:])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
