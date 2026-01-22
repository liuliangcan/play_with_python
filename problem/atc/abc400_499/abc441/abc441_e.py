# Problem: E - A > B substring
# Contest: AtCoder - AtCoder Beginner Contest 441 (Promotion of Engineer Guild Fes)
# URL: https://atcoder.jp/contests/abc441/tasks/abc441_e
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

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
"""

class BinIndexTree:
    """    PURQ的最经典树状数组，每个基础操作的复杂度都是logn；如果需要查询每个位置的元素，可以打开self.a    """
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            # self.a = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            # self.a = [0 for _ in range(self.size + 5)]
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_point(i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始
        # self.a[i] += v
        while i <= self.size:
            self.c[i] += v
            i += i & -i

    # def set_point(self, i, v):  # 单点修改，下标从1开始 需要先计算差值，然后调用add
    #     self.add_point(i, v - self.a[i])
    #     self.a[i] = v

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            # i -= i&-i
            i &= i - 1
        return s
#       ms
def solve():
    n, = RI()
    s, = RS()
    pre = BinIndexTree(n*2+5)
    pre.add_point(0+n+1,1)
    p = 0
    ans = 0
    for c in s:
        if c =='A':
            p += 1
        elif c == 'B':
            p -= 1
        ans += pre.sum_prefix(p-1+n+1)
        pre.add_point(p+n+1,1)
    print(ans)



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
