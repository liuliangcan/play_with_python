# Problem: 构造字符串
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4811/
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




def prefix_function(s):
    """计算s的前缀函数,复杂度o(n)"""
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi
#       ms
def solve1():
    n, k = RI()
    t, = RS()
    mx = 0
    for i in range(1, n):
        if t[:i] == t[-i:]:
            mx = i
    if mx == 0:
        return print(t * k)
    suf = t[mx:]
    print(t + suf * (k - 1))
#       ms
def solve():
    n, k = RI()
    t, = RS()
    mx = prefix_function(t)[-1]

    if mx == 0:
        return print(t * k)
    suf = t[mx:]
    print(t + suf * (k - 1))


if __name__ == '__main__':
    solve()
