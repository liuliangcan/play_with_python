# Problem: 二维费用的背包问题
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/8/
# Memory Limit: 64 MB
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

# 二维费用背包模板题
if __name__ == '__main__':
    N, V, M = RI()
    f = [[0] * (M + 1) for _ in range(V + 1)]
    for _ in range(N):
        v, m, w = RI()
        for j in range(V, v - 1, -1):
            for k in range(M, m - 1, -1):
                f[j][k] = max(f[j][k], f[j - v][k - m] + w)
    print(f[-1][-1])
