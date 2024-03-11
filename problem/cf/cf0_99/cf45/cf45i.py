# Problem: I. TCMCF+++
# Contest: Codeforces - School Team Contest 3 (Winter Computer School 2010/11)
# URL: https://codeforces.com/problemset/problem/45/I
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import random
from operator import imul
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
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/45/I

输入 n(1≤n≤100) 和长为 n 的数组 a(-100≤a[i]≤100)。
你需要从 a 中选择若干个数（至少一个），最大化所选数字的乘积。
输出你选的数字。如果答案不唯一，输出任意一个。
输入
5
1 2 -3 3 3
输出 3 1 2 3

输入
13
100 100 100 100 100 100 100 100 100 100 100 100 100
输出 100 100 100 100 100 100 100 100 100 100 100 100 100

输入
4
-2 -2 -2 -2
输出 -2 -2 -2 -2
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    if len(a) == 1: return print(*a)
    neg = sorted([v for v in a if v < 0])
    pos = [v for v in a if v > 0]
    if len(neg) == 1 and not pos and len(neg) < n or not neg and not pos:return print(0)

    print(*(neg[:-1] + pos if len(neg) & 1 else neg+pos))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
