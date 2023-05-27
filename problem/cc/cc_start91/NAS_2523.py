# Problem: Odd GCD Permutation
# Contest: CodeChef - START91C
# URL: https://www.codechef.com/START91C/problems/NAS_2523
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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10**9 + 7
PROBLEM = """
"""


#       ms
def solve():
    n, = RI()
    if n%2==0:
        return print(*(list(range(1,n+1))[::-1]))
    else:
        print(-1)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
