# Problem: 小d和孤独的区间
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/53366/D
# Memory Limit: 524288 MB
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
PROBLEM = """
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    p = Counter([0])
    s = ans = 0
    for v in a:
        s += v
        ans += p[s - 1]
        p[s] += 1
    print(ans)


if __name__ == '__main__':
    solve()
