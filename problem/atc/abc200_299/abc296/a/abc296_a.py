# Problem: A - Alternately
# Contest: AtCoder - AtCoder Beginner Contest 296
# URL: https://atcoder.jp/contests/abc296/tasks/abc296_a
# Memory Limit: 1024 MB
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
PROBLEM = """https://atcoder.jp/contests/abc296/tasks/abc296_a
给你整数n和长为n的字符串s
s由M/F两种字母组成代表男女。
检测s是否是男女交替的。
"""


#       ms
def solve():
    n, = RI()
    s, = RS()
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            return print('No')
    print('Yes')


if __name__ == '__main__':
    solve()
