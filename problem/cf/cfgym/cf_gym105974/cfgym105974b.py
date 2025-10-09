# Problem: B. Distinct Xor Subsequence Queries
# Contest: Codeforces - Introductory Problems: XOR Basis
# URL: https://codeforces.com/gym/105974/problem/B
# Memory Limit: 256 MB
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


class XorBasisGreedy:
    """贪心法构造线性基，基于每个高位计算；1.每个基的最高位不同。2.基中没有异或为0的子集"""

    def __init__(self, n):
        self.b = [0] * n
        self.gauss = False

    def insert(self, v):
        while v:
            i = v.bit_length() - 1
            if self.b[i] == 0:
                self.b[i] = v
                self.gauss = False
                break
            v ^= self.b[i]

    def can_present(self, v):
        while v:
            i = v.bit_length() - 1
            if self.b[i] == 0:
                return False
            v ^= self.b[i]
        return v == 0

    def find_max_xor(self):
        res = 0
        b = self.b
        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:
                res ^= b[i]
        return res

    def kth(self, k):  # 第k小,k从1数
        if not self.gauss:  # 需要消元,最多做len(b)次
            self.gauss = True
            for i, x in enumerate(self.b):
                if x:
                    for j in range(i + 1, len(self.b)):
                        if self.b[j] >> i & 1:
                            self.b[j] ^= x
        b = [v for v in self.b if v]
        if 1 << len(b) < k: return -1
        k -= 1
        ans = 0
        for i, x in enumerate(b):
            if k >> i & 1:
                ans ^= x
        return ans


class XorBasisQuick:
    """贪心法构造线性基，基于每个高位计算"""

    def __init__(self):
        self.b = []
        self.gauss = 0  # 前gauss个已经做过高斯消元

    def insert(self, x):
        for v in self.b:
            if x ^ v < x:
                x ^= v
        if x:
            self.b.append(x)

    def can_present(self, x):
        for v in self.b:
            x = min(x, x ^ v)
        return x == 0

    def find_max_xor(self):  # 这个很慢
        if self.gauss < len(self.b):
            self.do_gauss()
        res = 0
        for v in self.b:
            res ^= v
        return res

    def do_gauss(self):
        b = self.b
        n = len(b)
        for i in range(self.gauss, n):
            for j in range(i):
                # b[j] = min(b[j], b[j] ^ b[i])
                if b[j] ^ b[i] < b[j]:
                    b[j] ^=b[i]
        b.sort()
        self.gauss = n

    def kth(self, k):
        b = self.b
        if 1 << len(b) < k:
            return -1
        if self.gauss < len(b):
            self.do_gauss()
        k -= 1
        ans = 0
        for i, v in enumerate(b):
            if k >> i & 1:
                ans ^= v
        return ans


#   405   ms
def solve():
    q, = RI()
    xb = XorBasisQuick()
    for _ in range(q):
        t, x = RI()
        if t == 1:
            xb.insert(x)
        else:
            print(xb.kth(x))


#   483    ms
def solve1():
    q, = RI()
    xb = XorBasisGreedy(60)
    for _ in range(q):
        t, x = RI()
        if t == 1:
            xb.insert(x)
        else:
            print(xb.kth(x))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
