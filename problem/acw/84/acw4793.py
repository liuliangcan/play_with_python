# Problem: 买可乐
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4793/
# Memory Limit: 256 MB
# Time Limit: 1000 ms
#
# Powered by CP Editor (https://cpeditor.org)

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


def solve():
    c, d = RI()
    n, m = RI()
    k, = RI()
    t = m * n
    if k >= t:
        return print(0)
    if d * n <= c:
        return print(d * (t - k))
    diff = t - k
    x, y = divmod(diff, n)
    a = x * c + y * d
    b = (x + 1) * c
    print(min(a, b))


if __name__ == '__main__':
    solve()
