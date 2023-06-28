# Problem: 所有情况的和
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/problem/14509
# Memory Limit: 2 MB
# Time Limit: 14509000 ms

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
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """期望dp，每种2选1，互相独立，那么可以都选除二。
令dp[i]为前i个的期望，那么选第i个时，dp[i] = (dp[i-1]*x +dp[i-1]*y)/2
"""


#       ms
def solve():
    n, = RI()
    ans = 1
    for _ in range(n):
        x, y = RI()
        ans = ans * (x + y) % MOD
    print(ans)


if __name__ == '__main__':
    while True:
        try:
            solve()
        except:
            break
