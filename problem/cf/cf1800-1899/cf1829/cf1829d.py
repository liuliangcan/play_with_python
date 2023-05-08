# Problem: D. Gold Rush D. Gold Rush
# Contest: Codeforces - Codeforces Round 871 (Div. 4)
# URL: https://codeforces.com/contest/1829/problem/D
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/contest/1829/problem/D
输入t表示t组数据，每组数据：
输入n,m。n表示你有初始n个金块堆成一堆。
每次操作你需要选一堆金块，分成两堆数量分别是x,y。满足x=2*y。
请问是否可以通过任意次操作得到一堆金块数量是m。
"""
"""只有3的倍数才能继续操作，直接用dfs模拟，不需要记忆化"""

#       ms
def solve():
    n, m = RI()
    if m == n:
        return print('YES')

    # @lru_cache(None)  # 其实不需要记忆化
    def ok(x):
        if x == m:
            return True
        if x % 3 == 0:
            return ok(x // 3) or ok(x // 3 * 2)
        return False

    if ok(n):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
