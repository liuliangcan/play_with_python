# Problem: C - PC on the Table
# Contest: AtCoder - AtCoder Beginner Contest 297
# URL: https://atcoder.jp/contests/abc297/tasks/abc297_c
# Memory Limit: 1024 MB
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
PROBLEM = """https://atcoder.jp/contests/abc297/tasks/abc297_c
"""


#       ms
def solve():
    h, w = RI()
    for _ in range(h):
        s, = RS()
        p = list(s)
        j = 0
        while j < w - 1:
            if s[j] == s[j + 1] == 'T':
                p[j] = 'P'
                p[j + 1] = 'C'
                j += 1
            j += 1
        print(*p, sep='')


if __name__ == '__main__':
    solve()
