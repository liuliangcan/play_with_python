# Problem: 前缀和序列
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4792/
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


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


if __name__ == '__main__':
    n, = RI()
    a = RILST()
    aa = [0] + list(accumulate(a))
    bb = [0] + list(accumulate(sorted(a)))


    def calc(p, l, r):
        return p[r + 1] - p[l]


    m, = RI()
    for _ in range(m):
        t, l, r = RI()
        p = aa if t == 1 else bb
        print(calc(p, l - 1, r - 1))
