# Problem: D. Yet Another Yet Another Task
# Contest: Codeforces - Educational Codeforces Round 88 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1359/problem/D
# Memory Limit: 512 MB
# Time Limit: 1500 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/1359/problem/D

输入 n(1≤n≤1e5) 和长为 n 的数组 a(-30≤a[i]≤30)。
设 b 为 a 的一个非空连续子数组。
输出 sum(b)-max(b) 的最大值。
输入
5
5 -2 10 -1 4
输出 6

输入
8
5 2 5 3 -30 -30 6 9
输出 10

输入
3
-10 6 -15
输出 0
https://codeforces.com/contest/1359/submission/95405228

注意值域很小。

枚举 max(b)，把 > max(b) 的去掉，分裂出每个子段都求一遍最大子段和（力扣 53 题）再减去枚举的 max(b)。
所有结果的最大值即为答案。
"""


#   124   ms
def solve():
    n, = RI()
    a = RILST()
    ans = 0
    for mx in range(1, 31):
        i = 0
        while i < n:
            while i < n and a[i] > mx:
                i += 1
            if i == n:
                break
            s = a[i]
            i += 1
            while i < n and a[i] <= mx:
                s = max(s + a[i], a[i])
                ans = max(ans, s - mx)
                i += 1

    print(ans)


#   140   ms
def solve1():
    n, = RI()
    a = RILST()
    ans = 0
    for mx in range(1, 31):
        i = 0
        while i < n:
            while i < n and a[i] > mx:
                i += 1
            if i == n:
                break
            s = mx_s = a[i]
            i += 1
            while i < n and a[i] <= mx:
                s = max(s + a[i], a[i])
                mx_s = max(mx_s, s)
                i += 1
            ans = max(ans, mx_s - mx)

    print(ans)


if __name__ == '__main__':
    solve()
