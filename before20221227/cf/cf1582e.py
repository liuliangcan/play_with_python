import os
import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import re

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
else:
    input = sys.stdin.buffer.readline
MOD = 10 ** 9 + 7


def RI():
    return map(int, input().split())


def RILST():
    return list(RI())


def solve1(n, a):
    a = a[::-1]  # 逆序，题目转化成：子数组长度+1递增，但求和递减
    # print(a)
    pre = list(accumulate(a, initial=0))
    # print(pre)
    m = int((1 + 8 * n) ** 0.5 - 1) // 2
    f = [[0] * (n + 1) for _ in range(m + 2)]  # f[i][j]代表 从以j为结尾的前缀里，选出i个子数组，最后一组数组的最大和（ij均从1开始）
    f[0] = [inf] * (n + 1)
    ans = 1
    # print(f,m)
    for i in range(1, m + 1):
        if ans < i - 1:
            return print(ans)
        for j in range(i * (i + 1) // 2, n + 1):
            f[i][j] = f[i][j - 1]
            s = pre[j] - pre[j - i]
            if s < f[i - 1][j - i]:
                ans = i
                f[i][j] = max(f[i][j], s)
        # print(f)

    print(ans)


def solve2(n, a):
    a = a[::-1]  # 逆序，题目转化成：子数组长度+1递增，但求和递减
    pre = list(accumulate(a, initial=0))
    # print(pre)
    m = int((1 + 8 * n) ** 0.5 - 1) // 2
    f = [0] * (n + 1)  # f[i][j]代表 从以j为结尾的前缀里，选出i个子数组，最后一组数组的最大和（ij均从1开始）
    f = [inf] * (n + 1)
    g = [0] * (n + 1)
    ans = 1
    # print(f,m)
    for i in range(1, m + 1):
        if ans < i - 1:
            return print(ans)
        g[i * (i + 1) // 2 - 1] = 0
        for j in range(i * (i + 1) // 2, n + 1):
            g[j] = g[j - 1]
            s = pre[j] - pre[j - i]
            if s < f[j - i]:
                ans = i
                g[j] = max(g[j], s)
        f, g = g, f
        # print(f,g)

    print(ans)


def solve(n, a):
    # 逆序，题目转化成：子数组长度+1递增，但求和递减
    pre = list(accumulate(a[::-1], initial=0))
    m = int((1 + 8 * n) ** 0.5 - 1) // 2  # 长度为n的数组最多能选出m组
    # f[i][j]代表 从以j为结尾的前缀里，选出i个子数组，最后一组数组的最大和（ij均从1开始）
    f = [inf] * (n + 1)  # f[0][j]都置INF，因为长度为1的数组无求和上限要求,认为长度0的数组求和都是inf
    g = [0] * (n + 1)  # 实测滚动数组时间优化一小半

    ans = 1
    for i in range(1, m + 1):
        g[i * (i + 1) // 2 - 1] = 0  # 长度不够选不出来，结尾段求和置0，方便转移
        for j in range(i * (i + 1) // 2, n + 1):
            g[j] = g[j - 1]  # 从前缀转移
            s = pre[j] - pre[j - i]
            if g[j] < s < f[j - i]:  # 本段符合要求，尝试以它结尾（作为第i个子段）
                ans = i
                g[j] = s

        if not g[n]:
            break
        f, g = g, f

    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        n, = RI()
        a = RILST()
        solve(n, a)
