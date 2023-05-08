# Problem: H. Don't Blame Me
# Contest: Codeforces - Codeforces Round 871 (Div. 4)
# URL: https://codeforces.com/contest/1829/problem/H
# Memory Limit: 256 MB
# Time Limit: 2000 ms

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
PROBLEM = """输入t组数据，每组数据
输入n,k和一个长度为n的数据a。(0<=a[i]<=63)
问a中有多少个子序列，他们的位于结果里，有k个1。
"""
"""看起来可以背包，但是查表法有些麻烦，由于a[i]范围64，可以刷表法，直接尝试所有转移。
"""


#       ms
def solve():
    n, k = RI()
    a = RILST()
    f = [0] * 64

    for v in a:
        g = f[:]
        f[v] += 1
        for i, x in enumerate(g):
            f[v & i] += x
            f[v & i] %= MOD
    ans = 0
    for i, v in enumerate(f):
        if bin(i).count('1') == k:
            ans = (ans + v) % MOD

    print(ans % MOD)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
