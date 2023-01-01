# Problem: ygg的分数运算
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/49343/D
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

MOD = 10 ** 9 + 7


def solve():
    a, b, c = RI()
    if a == b:
        while c % a == 0:
            c //= a
        if c == 1:
            return print('YES')
        return print('NO')

    p = c
    x = y = 0
    while p % a == 0:
        p //= a
        x += 1
    while p % b == 0:
        p //= b
        y += 1
    if p == 1:
        return print('YES')
    print('NO')


if __name__ == '__main__':
    solve()
