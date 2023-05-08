# Problem: B. LuoTianyi and the Table
# Contest: Codeforces - Codeforces Round 872 (Div. 2)
# URL: https://codeforces.com/contest/1825/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """输入t组数据，每组：
输入n,m和n*m个数。
构造一个n*m的矩阵，最大化:
sum(每个从左上角到(i,j)的矩阵中max-min)
"""
"""
尝试把最大值放左上角，最小和次小放它旁边；
尝试把最小值放左上角，最大和次大放它旁边。
"""


#       ms
def solve():
    n, m = RI()
    b = RILST()
    b.sort()

    mx = b[-1] * n * m - b[-1]
    x, y = b[0], b[1]
    ans = mx - x * n * (m - 1) - y * (n - 1)
    ans = max(ans, mx - x * m * (n - 1) - y * (m - 1))

    mn = -b[0] * n * m + b[0]
    x, y = b[-1], b[-2]
    ans = max(ans, mn + x * m * (n - 1) + y * (m - 1))
    ans = max(ans, mn + x * n * (m - 1) + y * (n - 1))
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
