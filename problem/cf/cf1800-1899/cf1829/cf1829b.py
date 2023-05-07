# Problem: B. Blank Space
# Contest: Codeforces - Codeforces Round 871 (Div. 4)
# URL: https://codeforces.com/contest/1829/problem/B
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
PROBLEM = """https://codeforces.com/contest/1829/problem/B
输入t组数据。
每组数据输入n和长为n的数组a，0<=a[i]<=1。
找到最长的连续0
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    f = [0] * n
    if a[0] == 0:
        f[0] = 1
    for i in range(1, n):
        if a[i] == 0:
            f[i] = f[i - 1] + 1
    print(max(f))


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
