# Problem: C - AtCoder Cards
# Contest: AtCoder - パナソニックグループプログラミングコンテスト2023（AtCoder Beginner Contest 301）
# URL: https://atcoder.jp/contests/abc301/tasks/abc301_c
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
PROBLEM = """给两个字符串s和t，只含小写字母和'@'。
其中'@'可以替换成任意'atcoder'几个字符中的一个。
开始前，你可以重排t。问是否能使s和t完全相同。
"""
"""计数每个字符，计算差异。最终看看差异的字符能否用对方行的'@'补回来即可。
"""

#       ms
def solve():
    s, = RS()
    t, = RS()
    cnt = Counter()
    x = y = 0
    for a, b in zip(s, t):
        if a == '@':
            x += 1
        else:
            cnt[a] += 1
        if b == '@':
            y += 1
        else:
            cnt[b] -= 1
    # print(cnt, x, y)
    for k, v in cnt.items():
        if v == 0:
            continue
        if k not in 'atcoder':
            return print('No')
        if v > 0 and y >= v:
            y -= v
        elif v < 0 and x >= -v:
            x += v
        else:
            return print('No')

    print('Yes')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
