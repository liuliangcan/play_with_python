# Problem: 健身
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4797/
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
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7


#       ms
def solve():
    n, = RI()
    a = RILST()
    c = Counter()
    ans = 0
    for i, v in enumerate(a):
        p = i % 3
        c[p] += v
        if c[p] > c[ans]:
            ans = p
    print(['chest', 'biceps', 'back'][ans])


if __name__ == '__main__':
    solve()
