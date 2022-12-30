import sys
from collections import *
from itertools import *
from math import sqrt, inf
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 998244353
"""https://atcoder.jp/contests/abc251/tasks/abc251_e

输入 n (2≤n≤3e5) 和长为 n 的数组 a (1≤a[i]≤1e9)，下标从 1 开始。
有 n 只动物围成一圈，你可以花费 a[i] 喂食动物 i 和 i+1。特别地，你可以花费 a[n] 喂食动物 n 和 1。
输出喂食所有动物需要的最小花费。
"""


#   337   ms  把最后一个数挪到最前边再dp一次
def solve1(n, a):
    def f(a):  # 无环情况计算，从第一开始喂
        # 定义：dp[i][0/1]为前i只狗都喂了的最小花费，0是没用a[i],1用了
        # 转移：当前不用的话，前一个必须用dp[i][0]=dp[i-1][1];当前用的话，前一个爱用不用dp[i][1]=a[i]+min(dp[i-1)
        # 初始: 第一个必须喂dp[0][1]=a[0];如果不喂，后续用的话花费是无限大dp[0][0]=inf
        # 答案: min(dp[-1]
        dp = [[inf, inf] for _ in range(n)]  #
        dp[0][1] = a[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = min(dp[i - 1]) + a[i]
        return min(dp[-1])

    print(min(f(a), f(a[n - 1:] + a[:n - 1])))


#    294   ms 滚动
def solve(n, a):
    def f(a):
        x, y = inf, a[0]
        for i in range(1, n):
            x, y = y, min(x, y) + a[i]
        return min(x, y)

    print(min(f(a), f(a[n - 1:] + a[:n - 1])))


if __name__ == '__main__':
    n, = RI()
    a = RILST()

    solve(n, a)
