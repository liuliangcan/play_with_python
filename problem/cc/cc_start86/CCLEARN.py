# Problem: CodeChef Learn Problem Solving
# Contest: CodeChef - START86D
# URL: https://www.codechef.com/START86D/problems/CCLEARN
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
PROBLEM = """
"""


#       ms
def solve():
    n, = RI()
    print(n*2)


if __name__ == '__main__':
    # t, = RI()
    # for _ in range(t):
    #     solve()
    solve()
