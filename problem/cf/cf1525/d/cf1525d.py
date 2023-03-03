# Problem: D. Armchairs
# Contest: Codeforces - Educational Codeforces Round 109 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1525/problem/D
# Memory Limit: 512 MB
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
PROBLEM = """https://codeforces.com/contest/1525/problem/D

输入 n(≤5000) 和长为 n 的数组 a，其中只有 0 和 1。保证 1 的数量不超过 n/2。
a[i]=0 表示位置 i 处有一把椅子，a[i]=1 表示位置 i 处有一个人。

一把椅子只能坐一个人。
一个人从 i 移动到 j 的耗时为 abs(i-j)。
问所有人都坐到椅子上，所有人的耗时之和最小是多少？
输入
7
1 0 0 1 0 0 1
输出 3

输入
6
1 1 1 0 0 0
输出 9
"""
"""类似[最小移动距离](https://leetcode.cn/problems/minimum-total-distance-traveled/)
先拆出椅子和用户的位置，分别记录两个数组chairs、persons。
邻项交换考虑每个人坐下后的相对位置不会改变，即他们不会交叉移动。类似于上题的连续。
那么最右一个人坐的椅子一定在最右边，转移时，考虑最后一个人往右走或不动。
状态：f[i][j] 代表前i把椅子坐前j个人的最小代价;定义时右移一位。
转移：考虑第i把椅子和第j个人，这个人可能坐在前边，f[i-1][j]；也能坐在这,f[i-1][j-1]+abs(chairs[i]-person[j])。
初始：不管是几把椅子，坐0个人代价是0.即f[i][0]=0
答案：f[-1][-1]
实现时，由于f[i]只依赖前一层状态f[i-1],且j依赖更前的状态，可以参考01背包的倒序遍历滚动压缩掉第一个维度。
"""

#    202   ms
def solve1():
    n, = RI()
    a = RILST()
    chairs = []
    persons = []
    for i, v in enumerate(a):
        if v:
            persons.append(i)
        else:
            chairs.append(i)
    m, n = len(chairs), len(persons)
    f = [([0] + [inf] * n) for _ in range(m + 1)]  # f[i][j] 前i把椅子坐前j个人的最小代价

    for i in range(m):
        for j in range(min(i + 1, n)):
            f[i + 1][j + 1] = min(f[i][j + 1], f[i][j] + abs(chairs[i] - persons[j]))
    print(f[-1][-1])


#    124   ms
def solve():
    n, = RI()
    a = RILST()
    chairs = []
    persons = []
    for i, v in enumerate(a):
        if v:
            persons.append(i)
        else:
            chairs.append(i)
    m, n = len(chairs), len(persons)
    f = [0] + [inf] * n  # f[i][j] 前i把椅子坐前j个人的最小代价,类背包倒序滚动

    for i in range(m):
        for j in range(min(i, n - 1), -1, -1):
            f[j + 1] = min(f[j + 1], f[j] + abs(chairs[i] - persons[j]))
    print(f[-1])


if __name__ == '__main__':
    solve()
