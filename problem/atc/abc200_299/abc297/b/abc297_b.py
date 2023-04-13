# Problem: B - chess960
# Contest: AtCoder - AtCoder Beginner Contest 297
# URL: https://atcoder.jp/contests/abc297/tasks/abc297_b
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
PROBLEM = """https://atcoder.jp/contests/abc297/tasks/abc297_b
"""


#       ms
def solve():
    s, = RS()
    d = defaultdict(list)
    for i, c in enumerate(s):
        d[c].append(i)
    k = d['K'][0]
    x, y = d['R']
    if not x < k < y:
        return print('No')
    x, y = d['B']
    if x % 2 == y % 2:
        return print('No')
    print('Yes')


if __name__ == '__main__':
    solve()
