# Problem: C. The Values You Can Make
# Contest: Codeforces - Codeforces Round 360 (Div. 1)
# URL: https://codeforces.com/problemset/problem/687/C
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
PROBLEM = """https://codeforces.com/problemset/problem/687/C

输入正整数 n(≤500) k(≤500) 和长为 n 的数组 c(1≤c[i]≤500)。

从 c 中选择若干个数，组成数组 A，满足 sum(A) = k。
从 A 中再选择若干个数，组成数组 B（可以为空）。
你需要计算 sum(B) 的所有可能的值。
输出这些值的个数 q，然后按升序输出这 q 个数。
输入
6 18
5 6 1 10 12 2
输出
16
0 1 2 3 5 6 7 8 10 11 12 13 15 16 17 18 

输入
3 50
25 25 50
输出
3
0 25 50 
"""
"""https://codeforces.com/problemset/submission/687/197390629

提示 1：问题转换成，能否从 c 中选出两个不相交的子集，其中一个和为 x，另一个和为 k-x。（求所有 x）

提示 2：相当于一个二维体积的 0-1 背包问题。
每个 c[i] 要么不选，要么放入一种体积，要么放入另一种体积。

所以
f[i][j1][j2] = f[i-1][j1][j2] || f[i-1][j1-c[i]][j2] || f[i-1][j1][j2-c[i]]

代码实现时第一个维度可以优化掉（倒序循环）

答案就是所有 f[x][k-x] 为 true 的 x。"""


#    982   ms
def solve3():
    n, k = RI()
    c = RILST()

    f = [[0] * (k + 1) for _ in range(k + 1)]  # f[x][i][j] 代表 从前x个物品里选，能组合成体积i+j的方案是否存在
    f[0][0] = 1
    for v in c:
        for i in range(k, -1, -1):
            for j in range(k, -1, -1):
                if i >= v:
                    f[i][j] |= f[i - v][j]
                if j >= v:
                    f[i][j] |= f[i][j - v]

    ans = [i for i in range(k + 1) if f[i][k - i]]
    print(len(ans))
    print(*ans)


#    1013   ms
def solve4():
    n, k = RI()
    c = RILST()

    f = [[0] * (k + 1) for _ in range(k + 1)]  # f[x][i][j] 代表 从前x个物品里选，能组合成体积i+j的方案是否存在
    f[0][0] = 1
    for v in c:
        for i in range(k, v - 1, -1):
            for j in range(k, v - 1, -1):
                f[i][j] |= f[i - v][j]
                f[i][j] |= f[i][j - v]
        for i in range(v - 1, -1, -1):
            for j in range(k, v - 1, -1):
                f[i][j] |= f[i][j - v]
        for i in range(k, v - 1, -1):
            for j in range(v - 1, -1, -1):
                f[i][j] |= f[i - v][j]

    ans = [i for i in range(k + 1) if f[i][k - i]]
    print(len(ans))
    print(*ans)


#    109   ms
def solve5():
    n, k = RI()
    c = RILST()

    f = [0] * (k + 1)  # f[i][j] 是个二进制的编码，其第x位上是1代表从前i个物品里选，能组合成体积j的方案里，是否存在体积x
    f[0] = 1
    for v in c:
        for i in range(k, v - 1, -1):
            f[i] |= f[i - v] | (f[i - v] << v)

    ans = [i for i in range(k + 1) if (f[-1] >> i) & 1]
    print(len(ans))
    print(*ans)


#    1512   ms
def solve6():
    n, k = RI()
    c = RILST()

    f = [[0] * (k + 1) for _ in range(k + 1)]  # f[x][i][j] 代表 从前x个物品里选，能组合成体积i+j的方案是否存在
    f[0][0] = 1
    for v in c:
        for i in range(k, -1, -1):
            for j in range(k, -1, -1):
                f[i][j] |= (i >= v and f[i - v][j]) | (j >= v and f[i][j - v])

    ans = [i for i in range(k + 1) if f[i][k - i]]
    print(len(ans))
    print(*ans)


#    1574   ms
def solve():
    n, k = RI()
    c = RILST()

    f = [[0] * (k + 1) for _ in range(k + 1)]  # f[x][i][j] 代表 从前x个物品里选，能组合成体积i+j的方案是否存在
    f[0][0] = 1
    s = 0
    for v in c:
        s += v
        if s > k: s = k
        for i in range(s, -1, -1):
            for j in range(s, -1, -1):
                if i >= v:
                    f[i][j] |= f[i - v][j]
                if j >= v:
                    f[i][j] |= f[i][j - v]

    ans = [i for i in range(k + 1) if f[i][k - i]]
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    solve()
