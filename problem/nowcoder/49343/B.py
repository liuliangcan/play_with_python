# Problem: 分赃
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/49343/B
# Memory Limit: 524288 MB
# Time Limit: 2000 ms
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

MOD = 10**9 + 7

def solve():
    n, = RI()
    a = RILST()

    c = Counter(a)
    c = Counter(c.values())
    if c[1] & 1 == 0:
        return print('YES')
    del c[1]
    del c[2]
    if c:
        return print('YES')
    print('NO')

if __name__ == '__main__':
    solve()
