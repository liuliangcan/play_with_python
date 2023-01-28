# Problem: 下一个
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4803/
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
from math import sqrt, gcd, inf
# ACW没有comb
# from math import sqrt, gcd, inf, comb
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

#       ms
def solve():
    n, = RI()
    n += 1
    while True:
        s = str(n)
        if len(s) == len(set(s)):
            return print(n)
        n += 1


if __name__ == '__main__':
    # t, = RI()
    # for _ in range(t):
    #     solve()
    solve()
