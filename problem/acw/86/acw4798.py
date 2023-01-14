# Problem: 安全区域
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4798/
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
    n, m = RI()
    a = []
    for _ in range(m):
        a.append(RILST())
    rs, cs = set(), set()
    ans = n * n
    ret = []
    for x, y in a:
        if x not in rs:
            ans -= n - len(cs) - 1 + (y in cs)
        if y not in cs:
            ans -= n - len(rs) - 1 + (x in rs)
        ans -= (x not in rs and y not in cs)
        ret.append(ans)
        rs.add(x)
        cs.add(y)
    print(*ret)


if __name__ == '__main__':
    solve()
