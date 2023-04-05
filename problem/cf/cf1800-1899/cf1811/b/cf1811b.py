# Problem: B. Conveyor Belts
# Contest: Codeforces - Codeforces Round 863 (Div. 3)
# URL: https://codeforces.com/contest/1811/problem/B
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://codeforces.com/contest/1811/problem/B
输入t(<=2e5)表示t组数据，每组数据：
输入n(偶数且<=1e9),x1,x2,y1,y2 (均<=n)。
其中n表示一个边长n的正放心栅格，栅格是由n//2个旋转运行的传送带组成。
你可以花费1点能量跳到相邻传送带，问从x1y1到x2y2最少花费几能量。
"""
"""其实就是计算两个传送带的距离，设计一下传送带编号即可：越靠近外边编号越小，那么尝试x到上下边界最小值和y到上下边界最小值就是传送带编号"""


#       ms
def solve():
    n, x1, y1, x2, y2 = RI()
    d1 = min(x1, n - x1 + 1, y1, n - y1 + 1)
    d2 = min(x2, n - x2 + 1, y2, n - y2 + 1)
    print(abs(d1 - d2))


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
