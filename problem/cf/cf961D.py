# Problem: D. Pair Of Lines
# Contest: Codeforces - Educational Codeforces Round 41 (Rated for Div. 2)
# URL: https://codeforces.com/contest/961/problem/D
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
PROBLEM = """https://codeforces.com/contest/961/problem/D

输入 n(≤1e5) 和 n 个点 (xi,yi)，范围在 [-1e9,1e9]，所有点都是不同的。
你能否画至多两条直线，覆盖所有点？输出 YES 或 NO。
输入
5
0 0
0 1
1 1
1 -1
2 2
输出 YES

输入
5
0 0
1 0
2 1
1 1
2 3
输出 NO
"""

"""
求导:
    (y1-y2)/(x1-x2) == (y1-y3)/(x1-x3)
    (y1-y2)(x1-x3) == (y1-y3)(x1-x2)

"""


#    155   ms
def solve():
    n, = RI()
    ps = []
    for _ in range(n):
        ps.append(RILST())
    if n <= 4:
        return print('YES')

    def is_line(a, b, c):
        return (a[1] - b[1]) * (a[0] - c[0]) == (a[1] - c[1]) * (a[0] - b[0])

    def f(a, b):
        other = []
        for c in ps:
            if not is_line(a, b, c):
                if len(other) < 2:
                    other.append(c)
                else:
                    if not is_line(other[0], other[1], c):
                        return False
        return True

    if f(ps[0], ps[1]) or f(ps[0], ps[2]) or f(ps[1], ps[2]):
        return print('YES')

    print('NO')


#     171  ms
def solve1():
    n, = RI()
    ps = []
    for _ in range(n):
        ps.append(RILST())
    if n <= 4:
        return print('YES')

    def f(ps):
        (x1, y1), (x2, y2) = ps[:2]
        other = []
        for x3, y3 in ps[2:]:
            if (y1 - y2) * (x1 - x3) != (y1 - y3) * (x1 - x2):
                if len(other) < 2:
                    other.append((x3, y3))
                else:
                    (a1, b1), (a2, b2) = other
                    if (b1 - b2) * (a1 - x3) != (b1 - y3) * (a1 - a2):
                        return False
        return True

    if f(ps):
        return print('YES')
    ps[:3] = ps[1:3] + ps[:1]
    if f(ps):
        return print('YES')
    ps[:3] = ps[1:3] + ps[:1]
    if f(ps):
        return print('YES')
    print('NO')


if __name__ == '__main__':
    solve()
