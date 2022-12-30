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


"""
https://codeforces.com/problemset/problem/954/C

有一个 x 行 y 列的矩阵，你不知道 x 和 y 的大小，你只知道矩阵中的数字是从 1 开始连续递增的，即：
第一行是 1,2,3,...,y
第二行是 y+1,y+2,y+3,...,2y
……

定义矩阵上的一条路径为：从某一点出发，每一步往四个相邻格子走（不能出界），所走过的数字组成的序列。注意不能停在原地。

现在输入 n(≤2e5) 和一个长为 n 的路径 a (1≤a[i]≤1e9)。
如果存在某个矩阵能走出路径 a，且 x 和 y 均不超过 1e9，则输出 YES 和 x y，否则输出 NO。
如果有多个答案，输出任意一种。
"""


def RILST():
    return list(RI())


LIMIT = 10 ** 9
def print_x_y(x, y):
    if 1 <= x <= LIMIT and 1 <= y <= LIMIT:
        print(f'YES\n{x} {y}')
    else:
        print('NO')


def solve(n, a):
    mx = max(a)
    if n == 1:
        x = y = ceil(sqrt(mx))
        return print_x_y(x, y)

    # diff = sorted(list(set([abs(u - v) for u, v in pairwise(a)])))
    diff = sorted(list(set([abs(a[i] - a[i + 1]) for i in range(n - 1)])))
    if len(diff) > 2 or diff[0] == 0:
        return print('NO')

    if len(diff) == 1:
        y = diff[0]
        # if y == 1:
        #     x = y = ceil(sqrt(mx))
        #     return print_x_y(x, y)
        x = ceil(mx / y)
        return print_x_y(x, y)
    if len(diff) == 2:
        if diff[0] != 1:
            return print('NO')
        y = diff[1]
        for i, v in enumerate(a):
            if 0 == v % y:
                if (i < n - 1 and a[i + 1] == v + 1) or (i > 0 and a[i - 1] == v + 1):
                    return print('NO')
        x = ceil(mx / y)
        return print_x_y(x, y)


if __name__ == '__main__':
    n, = RI()
    a = RILST()
    solve(n, a)
