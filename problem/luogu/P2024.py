# Problem: P2024 [NOI2001] 食物链
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P2024
# Memory Limit: 125 MB
# Time Limit: 1000 ms

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
from typing import Tuple

# Decimal(s) 实例化Decimal对象,一般使用字符串
# getcontext().prec=100 修改精度
# sys.setrecursionlimit(10**6) #调整栈空间
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """带权并查集
一共三种动物循环吃，那么x吃y可以认为y-x=1%3,
在模3上的mod相同则是同类，距离1则是吃。
"""


class DSUW:
    """带权并查集，维护每个节点到祖宗的距离"""

    def __init__(self, n):
        self.fa = list(range(n))
        self.w = [0] * n  # 到祖宗的距离

    def find(self, x):
        fa = self.fa
        w = self.w
        t = x
        s = 0
        while fa[x] != x:
            s += w[x]
            x = fa[x]
        while t != x:
            w[t], s = s, s - w[t]
            fa[t], t = x, fa[t]
        return x

    def union(self, x: int, y: int, z: int) -> tuple[bool, int]:  # 表示合并一个y-x=z的关系,返回是否成功合并，以及y-x的实际距离
        nx = self.find(x)
        ny = self.find(y)

        if nx == ny:
            return False, self.w[y] - self.w[x]  # 同组，返回实际距离
        self.w[ny] = self.w[x] - self.w[y] + z
        self.fa[ny] = nx

        return True, z


#       ms
def solve():
    n, k = RI()
    dsu = DSUW(n + 1)
    ans = 0
    for _ in range(k):
        t, x, y = RI()
        if x > n or y > n:
            ans += 1
            continue
        if t == 1:
            a, b = dsu.union(x, y, 0)
            if b % 3 != 0:
                ans += 1
        else:
            a, b = dsu.union(x, y, 1)
            if b % 3 != 1:
                ans += 1
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
