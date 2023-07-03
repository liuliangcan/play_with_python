# Problem: B. The Number of Products
# Contest: Codeforces - Codeforces Round 585 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1215/B
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/1215/B

输入 n(1≤n≤2e5) 和长为 n 的数组 a(-1e9≤a[i]≤1e9,a[i]≠0)。
输出两个数：
1. 有多少个非空连续子数组，乘积是负数？
2. 有多少个非空连续子数组，乘积是正数？

思考：如果数组中有 0 要怎么做？如果要数乘积为 0 的子数组个数呢？
思考：如果改成子序列呢？
输入
5
5 -3 3 -1 1
输出 8 7

输入
10
4 2 -4 3 1 2 -4 3 2 3
输出 28 27

输入
5
-1 -2 -3 -4 -5
输出 9 6
"""
"""dp
f[i][0/1]为以i为右端点的所有子段中，有多少个子段乘积为正/负数。
那么f[i]可以从f[i-1]转移而来，注意添加自己的单独子段。
实现时可以滚动优化省去第一层。
"""

#       ms
def solve():
    n, = RI()
    a = RILST()

    x, y = int(a[0] > 0), int(a[0] < 0)
    p, n = x, y
    for v in a[1:]:
        if v > 0:
            x, y = x + 1, y
        else:
            x, y = y, x + 1
        p += x
        n += y
    print(n, p)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
