# Problem: C - Gap Existence
# Contest: AtCoder - AtCoder Beginner Contest 296
# URL: https://atcoder.jp/contests/abc296/tasks/abc296_c
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

MOD = 10**9 + 7
PROBLEM = """https://atcoder.jp/contests/abc296/tasks/abc296_c
给你整数N(2<=N<=2e5)，X(-1e9<=X<=1e9)，和长为N的数组A。
请问A中是否存在两个数差值为X。这两个数可以是同一个数。
"""


#       ms
def solve():
    n, x = RI()
    a = set(RILST())
    for v in a:
        if v - x in a or v + x in a:
            return print('Yes')
    print('No')


if __name__ == '__main__':
    solve()
