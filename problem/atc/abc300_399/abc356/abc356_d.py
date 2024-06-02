# Problem: D - Masked Popcount
# Contest: AtCoder - AtCoder Beginner Contest 356
# URL: https://atcoder.jp/contests/abc356/tasks/abc356_d
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
# MOD = 10 ** 9 + 7
MOD = 998244353
PROBLEM = """
"""


#       ms
def solve():
    n, m = RI()

    s = bin(n)[2:]
    s2 = bin(m)[2:]
    if len(s) < len(s2):
        s2 = s2[len(s2) - len(s):]
    elif len(s) > len(s2):
        s2 = '0' * (len(s) - len(s2)) + s2

    @lru_cache(None)
    def f(i: int, cnt1: int, is_limit: bool) -> int:
        if i == len(s):
            return cnt1
        res = 0
        up = int(s[i]) if is_limit else 1
        for d in range(up + 1):  # 枚举要填入的数字 d
            res += f(i + 1, cnt1 + (d == 1 and s2[i] == '1'), is_limit and d == up)
            res %= MOD
        return res

    print(f(0, 0, True))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
