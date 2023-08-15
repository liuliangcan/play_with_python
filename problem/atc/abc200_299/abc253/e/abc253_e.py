# Problem: E - Distance Sequence
# Contest: AtCoder - NOMURA Programming Contest 2022（AtCoder Beginner Contest 253）
# URL: https://atcoder.jp/contests/abc253/tasks/abc253_e
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
# MOD = 10**9 + 7
MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc253/tasks/abc253_e

输入 n(2≤n≤1000) m k(0≤k<m≤5000)。
输出有多少个长为 n 的数组，满足元素范围为 [1,m] 且 abs(a[i]-a[i+1]) >= k。
模 998244353。
输入 2 3 1
输出 6

输入 3 3 2
输出 2

输入 100 1000 500
输出 657064711
"""


#    201    ms
def solve():
    n, m, k = RI()
    if k == 0:  # 不特判wa2组
        return print(pow(m, n, MOD))
    f = [1] * m  # 1~m看做0~m-1
    for _ in range(n - 1):
        p = [0] + list(accumulate(f))
        f = [((i + k < m and (p[-1] - p[i + k])) + (i - k >= 0 and p[i - k + 1])) % MOD for i in range(m)]
    print(sum(f) % MOD)


#    248    ms
def solve1():
    n, m, k = RI()
    if k == 0:  # 不特判wa2组
        return print(pow(m, n, MOD))
    f = [1] * m  # 1~m看做0~m-1
    for _ in range(n - 1):
        p = [0] + list(accumulate(f))
        for i in range(m):
            f[i] = 0
            if i + k < m:  # 从i+k~m-1转移来
                f[i] += p[-1] - p[i + k]
            if i - k >= 0:  # 从0~i-k转移来
                f[i] += p[i - k + 1]
            f[i] %= MOD
    print(sum(f) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
