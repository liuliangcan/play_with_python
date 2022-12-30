import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

# RI = lambda: map(int, sys.stdin.buffer.readline().split())
# RS = lambda: sys.stdin.readline().strip().split()
# RILST = lambda: list(RI())

# input = sys.stdin.buffer.readline
# RI = lambda: map(int, input().split())
# RS = lambda: map(bytes.decode, input().strip().split())
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())


MOD = 10 ** 9 + 7
"""http://codeforces.com/problemset/problem/543/A

输入 n (1≤n≤500) m (1≤m≤500) b (0≤b≤500) mod (1≤mod≤1e9+7) 和一个长为 n 的数组 a (0≤a[i]≤500)。

你接手了一个有很多祖传代码的老项目，该项目由 n 个程序员开发，目前有 m 行代码。
已知第 i 个程序员在一行代码中会产生 a[i] 个 bug。
你尚不知道每个程序员分别写了多少行代码，于是你思考：有多少种方案，能使项目的 bug 数量不超过 b 个？由于答案很大，你需要输出答案模 mod 的结果。

注意：两种方案不同，当且仅当某个程序员编写的行数不同。
可能有程序员一行代码都不写。
输入
3 3 3 100
1 1 1
输出 10

输入
3 6 5 1000000007
1 2 3
输出 0

输入
3 5 6 11
1 2 1
输出 0
"""
""" 背包
f[i][j][k] 前i个程序员写了j行代码，共产生k个bug的方案数
"""


# 2542 	 ms
def solve(n, m, b, mod, a):
    f = [[0] * (b + 1) for _ in range(m + 1)]
    f[0][0] = 1
    for v in a:
        for i in range(1, m + 1):
            for j in range(v, b + 1):
                f[i][j] = (f[i][j] + f[i - 1][j - v]) % mod
    print(sum(f[-1]) % mod)



if __name__ == '__main__':
    n, m, b, mod = RI()
    a = RILST()

    solve(n, m, b, mod, a)