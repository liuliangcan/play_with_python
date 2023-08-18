# Problem: F - Knapsack for All Segments
# Contest: AtCoder - AtCoder Beginner Contest 159
# URL: https://atcoder.jp/contests/abc159/tasks/abc159_f
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
PROBLEM = """https://atcoder.jp/contests/abc159/tasks/abc159_f

输入 n(1≤n≤3000) s(1≤s≤3000) 和长为 n 的数组 a(1≤a[i]≤3000)。
定义 f(L,R) 等于：在子数组 a[L],a[L+1],...,a[R] 中，元素和恰好等于 s 的子序列的个数。
输出所有 f(L,R) 的和，其中 0≤L≤R<n。
模 998244353。
输入 
3 4
2 2 4
输出 5

输入 
5 8
9 9 9 9 9
输出 0

输入
10 10
3 1 4 1 5 9 2 6 5 3
输出 152
"""
"""下标从 0 开始。

定义 f[i][j] 表示子数组右端点为 i（左端点任意），子序列和为 j 的方案数。
本题要求的答案就是 f[0][s]+f[1][s]+...+f[n-1][s]。

考虑 a[i] 选或不选，有
f[i][j] = f[i-1][j] + f[i-1][j-a[i]]

初始值：f[i][0] = i+1。例如 f[1][0] 表示子数组 {a[1]} 中有 1 个子序列和为 0，子数组 {a[0],a[1]} 中有 1 个子序列和为 0，所以 f[1][0]=2。

https://atcoder.jp/contests/abc159/submissions/44666661"""


#   179    ms
def solve1():
    n, s = RI()
    a = RILST()
    f = [0] + [0] * s
    ans = 0
    for v in a:
        f[0] += 1
        for j in range(s, v - 1, -1):
            f[j] = (f[j] + f[j - v]) % MOD
        ans += f[-1]
    print(ans % MOD)


#     305   ms
def solve():
    n, s = RI()
    a = RILST()
    f = [[0] * (n + 1) for _ in range(s + 1)]
    f[0] = range(1, n + 2)

    for i, v in enumerate(a, start=1):
        for j in range(s, 0, -1):
            f[j][i] = (f[j][i - 1] + (j >= v and f[j - v][i - 1])) % MOD
    # print(f)
    print(sum(f[-1]) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
