import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1286/A

输入 n(≤100) 和一个长为 n 的数组 p，p 原本是一个 1~n 的排列，但是有些数字丢失了，丢失的数字用 0 表示。
你需要还原 p，使得 p 中相邻元素奇偶性不同的对数最少。输出这个最小值。
输入
5
0 5 0 2 3
输出 2

输入
7
1 0 0 5 0 0 2
输出 1
"""


# 264  	 ms
def solve1(n, a):
    if n == 1:
        return print(0)
    even = n // 2  # 偶数
    ood = n - even  # 奇数
    for v in a:
        if not v:
            continue
        if v & 1:
            ood -= 1
        else:
            even -= 1
    # f[i][j][k][0] 前i个数，填了j个奇数，l个偶数时，且末位是偶数的情况
    # f[i][j][k][1] 前i个数，填了j个奇数，l个偶数时，且末位是奇数的情况
    f = [[[[inf] * 2 for _ in range(even + 1)] for _ in range(ood + 1)] for _ in range(n)]
    # f[0][0][0] = 0
    if a[0] == 0:
        f[0][1][0][1] = 0  # a[0]放奇数
        f[0][0][1][0] = 0  # a[0]放偶数
    else:
        if a[0] & 1:  # 奇数
            f[0][0][0][1] = 0
        else:
            f[0][0][0][0] = 0
    # print(ood,even)
    for i in range(1, n):
        if a[i] == 0:
            for j in range(ood + 1):
                for k in range(even + 1):
                    if k:
                        # a[i]放偶数，前一个是奇数就+1否则不+
                        f[i][j][k][0] = min(f[i][j][k][0], f[i - 1][j][k - 1][0])
                        f[i][j][k][0] = min(f[i][j][k][0], f[i - 1][j][k - 1][1] + 1)
                    if j:
                        # a[i]放奇数
                        f[i][j][k][1] = min(f[i][j][k][1], f[i - 1][j - 1][k][0] + 1)
                        f[i][j][k][1] = min(f[i][j][k][1], f[i - 1][j - 1][k][1])
        else:
            if a[i] & 1:
                for j in range(ood + 1):
                    for k in range(even + 1):
                        f[i][j][k][1] = min(f[i - 1][j][k][1], f[i - 1][j][k][0] + 1)

            else:
                for j in range(ood + 1):
                    for k in range(even + 1):
                        f[i][j][k][0] = min(f[i - 1][j][k][1] + 1, f[i - 1][j][k][0])
    # print(f)
    print(min(f[-1][-1][-1]))


# 155 ms
def solve2(n, a):
    if n == 1:
        return print(0)
    even = n // 2  # 偶数
    ood = n - even  # 奇数
    for v in a:
        if not v:
            continue
        if v & 1:
            ood -= 1
        else:
            even -= 1
    f = [[[inf] * 2 for _ in range(even + 1)] for _ in range(ood + 1)]
    # f[0][0][0] = 0
    if a[0] == 0:
        f[1][0][1] = 0  # a[0]放奇数
        f[0][1][0] = 0  # a[0]放偶数
    else:
        if a[0] & 1:  # 奇数
            f[0][0][1] = 0
        else:
            f[0][0][0] = 0
    # print(ood,even)

    for i in range(1, n):
        g = f
        f = [[[inf] * 2 for _ in range(even + 1)] for _ in range(ood + 1)]
        if a[i] == 0:
            for j in range(ood + 1):
                for k in range(even + 1):
                    if k:
                        # a[i]放偶数，前一个是奇数就+1否则不+
                        f[j][k][0] = min(f[j][k][0], g[j][k - 1][0])
                        f[j][k][0] = min(f[j][k][0], g[j][k - 1][1] + 1)
                    if j:
                        # a[i]放奇数
                        f[j][k][1] = min(f[j][k][1], g[j - 1][k][0] + 1)
                        f[j][k][1] = min(f[j][k][1], g[j - 1][k][1])
        else:
            if a[i] & 1:
                for j in range(ood + 1):
                    for k in range(even + 1):
                        f[j][k][1] = min(g[j][k][1], g[j][k][0] + 1)

            else:
                for j in range(ood + 1):
                    for k in range(even + 1):
                        f[j][k][0] = min(g[j][k][1] + 1, g[j][k][0])
    # print(f)
    print(min(f[-1][-1]))


# 93 ms
def solve3(n, a):
    if n == 1:
        return print(0)
    even = n // 2  # 偶数
    ood = n - even  # 奇数
    for v in a:
        if not v:
            continue
        if v & 1:
            ood -= 1
        else:
            even -= 1
    # f[i][j][0] 前i个数，填了j个偶数且末尾是偶数的情况
    f = [[inf] * 2 for _ in range(even + 1)]

    if a[0] == 0:
        f[0][1] = 0  # a[0]放奇数
        f[1][0] = 0  # a[0]放偶数
    else:
        if a[0] & 1:  # 奇数
            f[0][1] = 0
        else:
            f[0][0] = 0
    # print(ood,even)
    pos = 0 + (a[0] == 0)
    for i in range(1, n):
        g = f
        f = [[inf] * 2 for _ in range(even + 1)]
        if a[i] == 0:
            pos += 1
            for j in range(min(pos + 1, even + 1)):
                if j:
                    f[j][0] = min(g[j - 1][0], g[j - 1][1] + 1)
                f[j][1] = min(g[j][1], g[j][0] + 1)

        else:
            p = a[i] & 1
            for j in range(min(pos + 1, even + 1)):
                f[j][p] = min(g[j][p], g[j][p ^ 1] + 1)
            # if a[i] & 1:
            #     for j in range(min(pos + 1, ood + 1)):
            #         f[j][1] = min(g[j][1], g[j][0] + 1)
            # else:
            #     for j in range(min(pos + 1, ood + 1)):
            #         f[j][0] = min(g[j][1] + 1, g[j][0])
    # print(f)
    print(min(f[-1]))


# 93 ms
def solve(n, a):
    if n == 1:
        return print(0)
    even = n // 2  # 偶数
    for v in a:
        if not v:
            continue
        if v & 1 == 0:
            even -= 1
    f = [[inf] * 2 for _ in range(even + 1)]
    if a[0] == 0:
        f[0][1] = 0  # a[0]放奇数
        f[1][0] = 0  # a[0]放偶数
    else:
        f[0][a[0] & 1] = 0
    # print(ood,even)
    for i in range(1, n):
        g = f
        f = [[inf] * 2 for _ in range(even + 1)]
        if a[i] == 0:
            for j in range(even + 1):
                if j:
                    f[j][0] = min(g[j - 1][0], g[j - 1][1] + 1)
                f[j][1] = min(g[j][1], g[j][0] + 1)

        else:
            p = a[i] & 1
            for j in range(even + 1):
                f[j][p] = min(g[j][p], g[j][p ^ 1] + 1)

    print(min(f[-1]))


if __name__ == '__main__':
    n, = RI()
    a = RILST()

    solve(n, a)
