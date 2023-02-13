# Problem: 首字母大写
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4809/
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


#       ms
def solve():
    s, = RS()
    print(s[0].upper() + s[1:])



if __name__ == '__main__':
    # t, = RI()
    # for _ in range(t):
    #     solve()
    solve()
