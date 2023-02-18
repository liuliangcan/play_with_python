# Problem: 浇花
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4865/
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

MOD = 10 ** 9 + 7


#   3529     ms
def solve():
    n, m = RI()
    a = [0] * (n + 2)
    for _ in range(m):
        x, y = RI()
        a[x] += 1
        a[y + 1] -= 1
    s = 0
    for i in range(1,n+1):
        s += a[i]
        if s != 1:
            return print(i,s)
    print('OK')



#    3424   ms
def solve1():
    n, m = RI()
    a = []
    for _ in range(m):
        a.append(RILST())
    a.sort()
    i = 0
    ans = -1
    for x, y in a:
        if x <= i:
            ans = x
            break
        if x > i + 1:
            ans = i + 1
            break
        i = y
    else:
        if i < n:
            ans = i + 1
    if ans == -1:
        print('OK')
    else:
        s = sum(x <= ans <= y for x, y in a)
        print(ans, s)


if __name__ == '__main__':
    solve()
