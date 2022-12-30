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

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

# RI = lambda: map(int, sys.stdin.buffer.readline().split())
# RS = lambda: sys.stdin.readline().strip().split()
# RILST = lambda: list(RI())

# input = sys.stdin.buffer.readline
# RI = lambda: map(int, input().split())
# RS = lambda: map(bytes.decode, input().strip().split())
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/38/E

输入 n(≤3000)，表示在一维数轴上有 n 颗大小忽略不计的弹珠。
然后输入 n 对数字，每对数字表示这颗弹珠在数轴上的位置 xi，以及把这颗弹珠固定在 xi 上的花费 ci，数据范围均在 [-1e9,1e9] 之间，且 xi 互不相同。注意 ci 可以为负。

选择若干弹珠固定后，所有未固定的弹珠向左滚动，直到碰到固定住的弹珠。
总花费 = 固定弹珠的花费之和 + 所有未固定的弹珠的滚动距离之和。
输出总花费的最小值。
注：根据题意，最左边的弹珠一定要固定。
输入
3
2 3
3 4
1 2
输出 5

输入
4
1 7
3 1
5 10
6 1
输出 11
"""


#  310	 ms
def solve1(n, ac):
    ac.sort()
    # print(ac)
    f = [[inf, inf] for _ in range(n)]  # f[i][0]:第i个球不固定时,s[:i+1]总费用;f[i][1]:第i个球固定时,s[:i+1]总费用
    f[0][1] = ac[0][1]
    for i in range(1, n):
        f[i][1] = ac[i][1] + min(f[i - 1])
        # 如果撞到j停下，那么值为(i-j)+(i-1-j)+...(j+1-j)=sum(j+1..i)-len(j+1..i)*j,用s累计被减数，
        # 这里其实可以预处理前缀和,但为了求min依然遍历，就途中累计即可。
        s = ac[i][0]
        for j in range(i - 1, -1, -1):
            f[i][0] = min(f[i][0], s - ac[j][0] * (i - j) + f[j][1])
            s += ac[j][0]

    print(min(f[-1]))


# 372 ms 用前缀和优化变慢了！
def solve2(n, ac):
    ac.sort()
    # print(ac)
    f = [[inf, inf] for _ in range(n)]  # f[i][0]:第i个球不固定时,s[:i+1]总费用;f[i][1]:第i个球固定时,s[:i+1]总费用
    f[0][1] = ac[0][1]
    pre = [0] + list(accumulate([x[0] for x in ac]))
    for i in range(1, n):
        f[i][1] = ac[i][1] + min(f[i - 1])
        # 如果撞到j停下，那么值为(i-j)+(i-1-j)+...(j+1-j)=sum(j+1..i)-len(j+1..i)*j,发现被减数是区间和，用前缀和。
        for j in range(i - 1, -1, -1):
            f[i][0] = min(f[i][0], pre[i + 1] - pre[j + 1] - ac[j][0] * (i - j) + f[j][1])
        # print(f)
    print(min(f[-1]))


# 248 ms
def solve3(n, ac):
    ac.sort()
    # print(ac)
    f = [inf] * n  # f[i]:第i个球固定时,s[:i+1]总费用
    f[0] = ac[0][1]
    g = inf  # 当前球不固定
    pre = [0] + list(accumulate([x[0] for x in ac]))
    for i in range(1, n):
        f[i] = ac[i][1] + min(f[i - 1], g)
        g = inf
        # 如果撞到j停下，那么值为(i-j)+(i-1-j)+...(j+1-j)=sum(j+1..i)-len(j+1..i)*j,发现被减数是区间和，用前缀和。
        for j in range(i - 1, -1, -1):
            g = min(g, pre[i + 1] - pre[j + 1] - ac[j][0] * (i - j) + f[j])
        # print(f)
    print(min(f[-1], g))


# 248 ms
def solve(n, ac):
    ac.sort()
    # print(ac)
    f = [inf] * n  # f[i]:第i个球固定时,s[:i+1]总费用
    f[0] = ac[0][1]
    g = inf  # 当前球不固定
    for i in range(1, n):
        f[i] = ac[i][1] + min(f[i - 1], g)
        g = inf
        s = ac[i][0]
        # 如果撞到j停下，那么值为(i-j)+(i-1-j)+...(j+1-j)=sum(j+1..i)-len(j+1..i)*j,发现被减数是区间和，用s累计被减数。
        for j in range(i - 1, -1, -1):
            g = min(g, s - ac[j][0] * (i - j) + f[j])
            s += ac[j][0]
        # print(f)
    print(min(f[-1], g))

if __name__ == '__main__':
    n, = RI()
    ac = []
    for _ in range(n):
        ac.append(RILST())

    solve(n, ac)
