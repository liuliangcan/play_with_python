# Problem: A - Overall Winner
# Contest: AtCoder - パナソニックグループプログラミングコンテスト2023（AtCoder Beginner Contest 301）
# URL: https://atcoder.jp/contests/abc301/tasks/abc301_a
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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """给一个只有A、T组成的字符串s，
谁多谁赢，一样多就从左到右看，谁先达到这个数。
"""
"""计数，一样多就看最后一个数是谁谁输"""

#       ms
def solve():
    n, = RI()
    s, = RS()
    cnt = Counter(s)
    # print(cnt)
    if cnt['T'] > cnt['A']:
        print('T')
    elif cnt['T'] < cnt['A']:
        print('A')
    else:
        if s[-1] == 'T':
            print('A')
        else:
            print('T')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
