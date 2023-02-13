# Problem: 找数字
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4810/
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


#       ms
def solve():
    m, s = RI()
    if s == 0 and m == 1:
        return print('0 0')
    if s < 1 or 9 * m < s:
        return print('-1 -1')
    t = s

    a = [0] * m
    i = 0
    while t:
        x = min(t, 9)
        a[i] = x
        t -= x
        i += 1
    mx = ''.join(map(str, a))
    if a[-1] == 0:
        for i in range(m - 1, -1, -1):
            if a[i]:
                a[-1] += 1
                a[i] -= 1
                break
    print(''.join(map(str, a[::-1])), mx)


if __name__ == '__main__':
    solve()
