# Problem: F - Must Buy
# Contest: AtCoder - AtCoder Beginner Contest 441 (Promotion of Engineer Guild Fes)
# URL: https://atcoder.jp/contests/abc441/tasks/abc441_f
# Memory Limit: 1024 MB
# Time Limit: 2500 ms

import sys

from types import GeneratorType
import bisect
import io, os
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from contextlib import redirect_stdout
from itertools import accumulate, combinations, permutations
# combinations(a,k)a序列选k个 组合迭代器
# permutations(a,k)a序列选k个 排列迭代器
from array import *
from functools import lru_cache, reduce
from heapq import heapify, heappop, heappush
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from random import randint, choice, shuffle, randrange
# randint(a,b)从[a,b]范围随机选择一个数
# choice(seq)seq可以是一个列表,元组或字符串,从seq中随机选取一个元素
# shuffle(x)将一个可变的序列x中的元素打乱
from string import ascii_lowercase, ascii_uppercase, digits
# 小写字母，大写字母，十进制数字
from decimal import Decimal, getcontext

# Decimal(s) 实例化Decimal对象,一般使用字符串
# getcontext().prec=100 修改精度
# sys.setrecursionlimit(10**6) #调整栈空间
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
# DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')  # cf突然编不过这行了
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
可删除背包：
两种方法
    分治背包
    前后缀分解
"""


#       ms
def solve1():
    n, m = RI()
    a = []
    for _ in range(n):
        v, w = RI()
        a.append((v, w))
    ans = ['C'] * n
    f = [0] + [-inf] * m

    for i, (v, w) in enumerate(a):
        if v > m:
            ans[i] = 3  # 必不能选
            continue
        for j in range(m, v - 1, -1):
            f[j] = max(f[j], f[j - v] + w)
    mx = max(f)

    dp = [0] * (m + 1)

    def f(l, r):
        nonlocal dp
        if l == r:
            if dp[-1] < mx:
                ans[r] = 'A'  # 必选
            else:
                v, w = a[r]
                if v <= m and dp[m - v] + w == mx:
                    ans[r] = "B"
            return
        mid = (l + r) // 2
        tmp = dp[:]
        # 01 背包左边，递归右边
        for i in range(l, mid + 1):
            v, w = a[i]
            for j in range(m, v - 1, -1):
                dp[j] = max(dp[j], dp[j - v] + w)
        f(mid + 1, r)
        dp = tmp
        # 01背包右边，递归左边
        for i in range(mid + 1, r + 1):
            v, w = a[i]
            for j in range(m, v - 1, -1):
                dp[j] = max(dp[j], dp[j - v] + w)
        f(l, mid)

    f(0, n - 1)
    print(''.join(ans))


#       ms
def solve():
    n, m = RI()
    a = []
    for _ in range(n):
        v, w = RI()
        a.append((v, w))

    f = [0] *(m+1)
    pre = []

    for i, (v, w) in enumerate(a):
        pre.append(f[:])
        for j in range(m, v - 1, -1):
            f[j] = max(f[j], f[j - v] + w)
        # pre.append(f[:])
    suf = []
    f = [0] * (m + 1)
    for i in range(n-1,-1,-1):
        suf.append(f[:])
        v,w = a[i]
        for j in range(m, v - 1, -1):
            f[j] = max(f[j], f[j - v] + w)
    suf = suf[::-1]
    mx = f[-1]
    ans = ['C'] * n
    for i, (v, w) in enumerate(a):
        left =pre[i]
        right = suf[i]
        s = 0
        for l in range(m+1):
            s = max(s, left[l] + right[m-l])
        if s < mx:
            ans[i] = 'A'
        else:
            if v <= m:
                k = m- v
                s= 0
                for l in range(k+1):
                    s = max(s, left[l]+right[k-l])
                if s + w == mx:
                    ans[i] = 'B'


    # dp = [0] * (m + 1)
    #
    # def f(l, r):
    #     nonlocal dp
    #     if l == r:
    #         if dp[-1] < mx:
    #             ans[r] = 'A'  # 必选
    #         else:
    #             v, w = a[r]
    #             if v <= m and dp[m - v] + w == mx:
    #                 ans[r] = "B"
    #         return
    #     mid = (l + r) // 2
    #     tmp = dp[:]
    #     # 01 背包左边，递归右边
    #     for i in range(l, mid + 1):
    #         v, w = a[i]
    #         for j in range(m, v - 1, -1):
    #             dp[j] = max(dp[j], dp[j - v] + w)
    #     f(mid + 1, r)
    #     dp = tmp
    #     # 01背包右边，递归左边
    #     for i in range(mid + 1, r + 1):
    #         v, w = a[i]
    #         for j in range(m, v - 1, -1):
    #             dp[j] = max(dp[j], dp[j - v] + w)
    #     f(l, mid)
    #
    # f(0, n - 1)
    print(''.join(ans))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
