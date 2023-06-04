# Problem: B - Discord
# Contest: AtCoder - NS Solutions Corporation Programming Contest 2023（AtCoder Beginner Contest 303）
# URL: https://atcoder.jp/contests/abc303/tasks/abc303_b
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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10**9 + 7
PROBLEM = """
"""


#       ms
def solve():
    n,m = RI()
    s = set()
    for i in range(1,n):
        for j in range(i+1,n+1):
            s.add((i,j))
    for _ in range(m):
        a = RILST()
        for i in range(1,n):
            x,y = a[i-1],a[i]
            if x>y:
                x,y = y,x
            s.discard((x,y))
    print(len(s))



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
