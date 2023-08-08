# Problem: D - I Hate Non-integer Number
# Contest: AtCoder - AtCoder Beginner Contest 262
# URL: https://atcoder.jp/contests/abc262/tasks/abc262_d
# Memory Limit: 1024 MB
# Time Limit: 2500 ms

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
PROBLEM = """https://atcoder.jp/contests/abc262/tasks/abc262_d

输入 n(1≤n≤100) 和长为 n 的数组 a(1≤a[i]≤1e9)。
如果一个非空子序列的平均值是整数，那么称其为漂亮的。
输出 a 的漂亮子序列的个数，模 998244353。
注：子序列不一定连续。
输入
3
2 6 2
输出 6

输入 
5
5 5 5 5 5
输出 31
"""
"""
f[i][j][k]   表示前i个数取j个数模m为k的情况数
"""
"""枚举子序列的长度。

考虑子序列长度固定为 m 时，有多少个平均值为整数的子序列。
相当于子序列的元素和模 m 为 0。

用选或不选来思考。
定义 f[i][j][k] 表示从前 i 个数中选 j 个数，元素和模 m 为 k 的方案数。

为方便计算取模，用刷表法（用查表法的话，需要算 (k-a[i])%m，可能会算出负数）：
f[i][j][(k+a[i])%m] = f[i-1][j][(k+a[i])%m] + f[i-1][j-1][k]

答案为 f[n][m][0]。

代码实现时，第一个维度可以去掉，然后像 0-1 背包那样倒序循环 j。初始值 f[0][0] = 1。

https://atcoder.jp/contests/abc262/submissions/44370034"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    ans = n
    for m in range(2, n + 1):
        f = [[0] * m for _ in range(n + 1)]
        f[0][0] = 1
        for i, v in enumerate(a, start=1):
            for j in range(min(i - 1, m - 1), -1, -1):  # 前i个数最多选出i个数，且不需要考虑超过m的情况
                for k in range(m - 1, -1, -1):  # 模只能在0~m-1
                    f[j + 1][(k + v) % m] = (f[j + 1][(k + v) % m] + f[j][k]) % MOD
                    # f[j + 1][(k + v) % m] += f[j][k]  # 最多加100w次，最后在取模吧
        ans += f[m][0]  # 只执行100次，最后再取模吧
    print(ans % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
