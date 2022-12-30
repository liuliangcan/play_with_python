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


def RI():
    return map(int, input().split())


def RS():
    return input().strip().split()


def RILST():
    return list(RI())


"""https://codeforces.com/problemset/problem/1249/E

输入正整数 n(2≤n≤2e5) 和 c(≤1000)，以及长度均为 n-1 的整数数组 a 和 b，数组元素范围均为 [1,1000]。

走楼梯从 i 层到 i+1 层需要 a[i] 秒。
坐电梯从 i 层到 i+1 层需要 b[i] 秒。
如果你要从某一层开始坐电梯，你需要额外等待 c 秒。

输出从第 1 层走楼梯或者坐电梯到每一层，分别最少需要多少秒。
"""


# dp空间O(n), 249 ms
def solve1(n, c, a, b):
    f = [[0] * 2 for _ in range(n)]
    f[0][1] = c
    for i in range(1, n):
        f[i][0] = min(f[i - 1]) + a[i - 1]
        f[i][1] = min(f[i - 1][0] + c + b[i - 1], f[i - 1][1] + b[i - 1])
    print(' '.join(map(lambda r: str(min(r)), f)))


# dp滚动，答案记录字符串数组空间O(n), 202 ms
def solve2(n, c, a, b):
    r, e = 0, c
    ans = ['0']
    for i in range(1, n):
        r, e = min(r, e) + a[i - 1], min(r + c, e) + b[i - 1]
        ans.append(str(min(r, e)))
    print(' '.join(ans))


# 答案数组空间O(n), 218 ms
def solve3(n, c, a, b):
    r, e = 0, c
    ans = [0]
    for i in range(1, n):
        r, e = min(r, e) + a[i - 1], min(r + c, e) + b[i - 1]
        ans.append(min(r, e))
    print(' '.join(map(str, ans)))


# 空间O(1),直接打印 311 ms，辣鸡
def solve4(n, c, a, b):
    r, e = 0, c
    print(0, end=' ')
    for i in range(1, n):
        r, e = min(r, e) + a[i - 1], min(r + c, e) + b[i - 1]
        print(min(r, e), end=' ')


# 187ms
def solve5(n, c, a, b):
    r, e = 0, c
    ans = [0] * n
    for i in range(1, n):
        r, e = min(r, e) + a[i - 1], min(r + c, e) + b[i - 1]
        ans[i] = min(r, e)
    print(' '.join(map(str, ans)))


# 218 ms
def solve6(n, c, a, b):
    r, e = 0, c
    ans = ['0'] * n
    for i in range(1, n):
        r, e = min(r, e) + a[i - 1], min(r + c, e) + b[i - 1]
        ans[i] = str(min(r, e))
    print(' '.join(ans))


# 202 ms
def solve7(n, c, a, b):
    r, e = 0, c
    ans = [''] * n
    ans[0] = '0'
    for i in range(1, n):
        r, e = min(r, e) + a[i - 1], min(r + c, e) + b[i - 1]
        ans[i] = str(min(r, e))
    print(' '.join(ans))


#
def solve(n, c, a, b):
    r, e = 0, c
    print('0', end=' ')

    def f(i):
        nonlocal r, e
        r, e = min(r, e) + a[i - 1], min(r + c, e) + b[i - 1]
        print(min(r, e), end=' ')

    list(map(f, range(1, n)))


if __name__ == '__main__':
    n, c = RI()
    a, b = RILST(), RILST()
    solve(n, c, a, b)
