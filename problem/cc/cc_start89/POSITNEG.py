# Problem: Positive or Negative Subarrays
# Contest: CodeChef - START89B
# URL: https://www.codechef.com/START89B/problems/POSITNEG
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
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf
if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10**9 + 7
PROBLEM = """a数组,a[i]=2^i
给出b数组 b[i]只存在-1 +1
c数组 c[i] = a[i]*b[i]
问c数组里的子数组，有几个和严格>0，几个严格<0,做差。
"""
"""由于每个c[i]都是2^i，那么以i为右端点的子数组，正负性一定只和i相关。因为前边的绝对值加起来也没有它大。
"""


#       ms
def solve():
    n, = RI()
    b = RILST()
    x = y = 0
    for i,v in enumerate(b):
        if v > 0:
            y += i + 1
        else:
            x += i + 1
    print(abs(x-y))


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
