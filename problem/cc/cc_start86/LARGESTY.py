# Problem: Largest Y
# Contest: CodeChef - START86D
# URL: https://www.codechef.com/START86D/problems/LARGESTY
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
from functools import lru_cache, reduce
from operator import ior, iand
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
PROBLEM = """
"""


def solve():
    n, x = RI()
    a = RILST()
    c = reduce(ior, a)
    d = reduce(iand, a)
    e = c - d
    if (x & e) != e:
        return print(x)
    for i in range(31):
        if e >> i & 1:
            x -= x % (1 << i)
            return print(x - 1)


def solve1():
    n, x = RI()
    a = RILST()
    ans = 0
    for i in range(31):
        p = set()
        for v in a:
            z = (v >> i) & 1
            p.add(z)
            if len(p) == 2:
                if (x >> i) & 1:
                    ans = max(ans, (x ^ (1 << i)) | ((1 << i) - 1))
                    break
                else:
                    return print(x)
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
