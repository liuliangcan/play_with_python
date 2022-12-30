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

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve1(n, m, k, a):
    pre = list(accumulate(a, initial=0))
    f = [[0] * k for _ in range(n)]  # f[i][j] 前i个数，取j+1组的最大值
    for i in range(m - 1, n):
        f[i][0] = max(f[i - 1][0], pre[i + 1] - pre[i - m + 1])

    for i in range(m, n):
        for j in range(1, min((i + 1) // m, k)):
            f[i][j] = max(f[i - 1][j], pre[i + 1] - pre[i - m + 1] + f[i - m][j - 1])
    print(f[-1][k - 1])


def solve2(n, m, k, a):
    pre = list(accumulate(a, initial=0))
    f = [[0] * n for _ in range(k)]  # f[i][j] 前j个数，取i+1组的最大值
    for i in range(m - 1, n):
        f[0][i] = max(f[0][i - 1], pre[i + 1] - pre[i - m + 1])
    for i in range(1, k):
        f[i][(i + 1) * m - 1] = pre[(i + 1) * m]
        for j in range((i + 1) * m, n):
            f[i][j] = max(f[i][j - 1], f[i - 1][j - m] + pre[j + 1] - pre[j - m + 1])
    print(f[-1][-1])


def solve3(n, m, k, a):
    pre = list(accumulate(a, initial=0))
    f = [0] * n  # f[i][j] 前j个数，取i+1组的最大值
    for i in range(m - 1, n):
        f[i] = max(f[i - 1], pre[i + 1] - pre[i - m + 1])
    for i in range(1, k):  # 空间优化但正逆向遍历两次
        for j in range(n - 1, (i + 1) * m - 1, -1):
            f[j] = f[j - m] + pre[j + 1] - pre[j - m + 1]

        f[(i + 1) * m - 1] = pre[(i + 1) * m]
        for j in range((i + 1) * m, n):
            f[j] = max(f[j - 1], f[j])
    print(f[-1])


def solve4(n, m, k, a):
    pre = list(accumulate(a, initial=0))
    f = [0] * n  # f[i][j] 前j个数，取i+1组的最大值
    for i in range(m - 1, n):
        f[i] = max(f[i - 1], pre[i + 1] - pre[i - m + 1])
    for i in range(1, k):  # 空间优化+但拷贝临时状态数组
        g = f[:]
        g[(i + 1) * m - 1] = pre[(i + 1) * m]
        for j in range((i + 1) * m, n):
            g[j] = max(g[j - 1], f[j - m] + pre[j + 1] - pre[j - m + 1])
        f = g

    print(f[-1])


def solve(n, m, k, a):  # 过不了 爆栈
    pre = list(accumulate(a, initial=0))
    sys.setrecursionlimit(10**9)

    # 前j个数取i组的最大值
    @lru_cache(None)
    def dfs(i, j):
        if j + 1 == i * m:
            return pre[j + 1]
        if i == 1:
            return max(dfs(1, j - 1), pre[j + 1] - pre[j - m + 1])
        return max(dfs(i, j - 1), dfs(i - 1, j - m) + pre[j + 1] - pre[j - m + 1])

    if n > 3000 and k >= 2:
        for i in range(0, min(k + 1, n // 2 // m)):
            dfs(n // 2, i)
    print(dfs(k, n - 1))



if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))

    solve(n, m, k, a)
