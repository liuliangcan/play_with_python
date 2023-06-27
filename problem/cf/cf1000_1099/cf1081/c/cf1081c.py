# Problem: C. Colorful Bricks
# Contest: Codeforces - Avito Cool Challenge 2018
# URL: https://codeforces.com/problemset/problem/1081/C
# Memory Limit: 256 MB
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

MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1081/C

输入 n m(1≤n,m≤2000) k(0≤k≤n-1)。
n 块砖排成一排，把每块砖涂成 m 种颜色中的一种，要求恰好有 k 块砖的颜色与其左边相邻砖的颜色不同（第一块砖不能在这 k 块砖内）。
输出涂色方案数，模 998244353。
输入 3 3 0
输出 3

输入 3 2 1
输出 4
"""
"""https://codeforces.com/problemset/submission/1081/211192029

定义 f[i][j] 表示前 i 块砖，有 j 块砖的颜色与其左边相邻砖的颜色不同，此时的涂色方案数。
第一块砖随便涂色，f[0][0] = m。
考虑第 i 块砖「选或不选」，也就是：
颜色相同：f[i][j] = f[i-1][j]
颜色不同：f[i][j] = f[i-1][j-1] * (m-1)
相加得 f[i][j] = f[i-1][j] + f[i-1][j-1] * (m-1)
答案为 f[n-1][k]。
代码实现时可以用滚动数组优化。

另一种思路是从 n-1 块砖中选 k 块砖，颜色和左边不一样，
所以方案数是 C(n-1,k) * m * (m-1)^k，预处理阶乘可以做到 O(n)。"""


#   109    ms
def solve1():
    n, m, k = RI()
    f = [0] * (k + 1)
    f[0] = m

    for _ in range(n - 1):
        g = [0] * (k + 1)
        for j, v in enumerate(f):
            g[j] = (g[j] + v) % MOD
            if j < k:
                g[j + 1] = (g[j + 1] + v * (m - 1)) % MOD
        f = g
    print(f[k])


#     93  ms
def solve2():
    n, m, k = RI()
    f = [m] + [0] * k
    for _ in range(n - 1):
        for j in range(k, 0, -1):
            f[j] = (f[j] + f[j - 1] * (m - 1)) % MOD
    print(f[-1])


#       ms
def solve():
    n, m, k = RI()
    print(comb(n - 1, k) % MOD * m * (m - 1) ** k % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
