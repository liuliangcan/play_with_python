# Problem: A. Vacations
# Contest: Codeforces - Codeforces Round 363 (Div. 1)
# URL: https://codeforces.com/problemset/problem/698/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/698/A

输入 n(1≤n≤100) 和长为 n 的数组 a(0≤a[i]≤3)。
有 n 天，第 i 天的情况用 a[i]=0/1/2/3 表示，具体如下：

0：健身房关闭，比赛不进行； 
1：健身房关闭，比赛进行；
2：健身房开放，比赛不进行；
3：健身房开放，比赛进行。

在每一天，你可以休息、比赛 (如果比赛在这一天进行)，或者做运动 (如果健身房在这一天是开放的)。
但你不想连续两天做同样的活动，这意味着，你不会连续两天做运动，也不会连续两天参加比赛。
输出你休息的最少天数。
输入
4
1 3 2 0
输出 2

输入
7
1 3 3 2 1 2 3
输出 0

输入
2
2 2
输出 1
"""
"""线性dp
令f[i][0/1/2]为前i天，行为分别是休息/健身/比赛时，总共最少休息天数
那么只有这天可以健身/比赛时才能转移，否则是inf。
休息就都可以转移。
acwing用过：https://www.acwing.com/problem/content/4805/
"""

#    93   ms
def solve1():
    n, = RI()
    a = RILST()
    x = y = z = 0
    for v in a:
        i, j, k = min(x, y, z) + 1, inf, inf
        if v & 1:
            j = min(x, z)
        if v & 2:
            k = min(x, y)
        x, y, z = i, j, k
    print(min(x, y, z))


#       ms
def solve():
    n, = RI()
    a = RILST()
    x = y = z = 0
    for v in a:
        x, y, z = min(x, y, z) + 1, min(x, z) if v & 1 else inf, min(x, y) if v & 2 else inf

    print(min(x, y, z))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
