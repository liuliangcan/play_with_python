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


"""
http://codeforces.com/problemset/problem/1368/D

输入 n(≤2e5) 和一个长为 n 的整数数组 a (0≤a[i]<2^20)。

每次操作，你可以选择两个数 a[i] 和 a[j]，分别记作 x 和 y，然后更新 a[i] = x AND y, a[j] = x OR y。AND 表示按位与，OR 表示按位或。
你可以执行该操作任意次。
输出 sum(a[i]*a[i]) 的最大值，即 a[0]*a[0] + a[1]*a[1] + ... + a[n-1]*a[n-1] 的最大值。
"""

"""
https://codeforces.com/contest/1368/submission/167929428

提示 1：操作不会改变 a[i]+a[j] 的值。

提示 2：思考一下题目的样例二，是操作前答案大，还是操作后答案大？你能提出一个更一般的猜想并证明吗？

提示 3：我们应该执行尽量多的操作，把 bit 1 都合并到一起。

提示 4：统计每个 bit 位上 1 的个数，然后从大往小构造 a[i]。

具体实现逻辑见代码。
"""


def solve(n, a):
    bits = [0] * 20
    for c in a:
        for i in range(20):
            if c & (1 << i):
                bits[i] += 1

    xs = [0] * n
    for i in range(20):
        for j in range(bits[i]):
            xs[j] |= 1 << i

    print(sum(x * x for x in xs))


if __name__ == '__main__':
    n, = RI()
    a = RILST()
    solve(n, a)
