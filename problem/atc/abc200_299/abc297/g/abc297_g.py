# Problem: G - Constrained Nim 2
# Contest: AtCoder - AtCoder Beginner Contest 297
# URL: https://atcoder.jp/contests/abc297/tasks/abc297_g
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
PROBLEM = """https://atcoder.jp/contests/abc297/tasks/abc297_g
nim游戏2，输入n(<2e5) l r(l,r<1e9),和长为n的数组a(a[i]<1e9)。a[i]代表第i堆石子的数量
First和Second两名玩家做游戏，轮流从任意一堆石子中取走l~r个石子，不能完成操作的玩家失败。
最优操作下问谁赢。
"""
"""nim游戏可以用SG函数解决。
SG(x) = mex{SG(y)|y是局面x的所有后记局面}
SG定理：
    - g是总体局面，它可以分成n个互相独立的局面：在本题就是n堆石子。
    - g = g1+g2+g3_..+gn
    - SG(g) = SG(g1)^SG(g2)^..^SG(gn)
当SG(g)=0的时候，这个局面的玩家必败。
对一堆石子打表一下找规律，发现循环节是(l+r),且从0向上增长，每l个一跳，就再除以l。
"""


#  163 ms
def solve():
    n, l, r = RI()
    a = RILST()
    s = 0

    def sg(x):
        return x % (l + r) // l

    for v in a:
        s ^= sg(v)

    if s:
        print('First')
    else:
        print('Second')


if __name__ == '__main__':
    solve()
