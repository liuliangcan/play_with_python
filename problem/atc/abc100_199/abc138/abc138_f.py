# Problem: F - Coincidence
# Contest: AtCoder - AtCoder Beginner Contest 138
# URL: https://atcoder.jp/contests/abc138/tasks/abc138_f
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
PROBLEM = """给出整数 L 和 R 。求的整数对 (x,y) (L≤x≤y≤R)   ，使得 y 除以 x 的余数等于 y XOR x 。
模为 1e9+7 
"""
"""
        x<=y且y%x == y^x 
等价于   x<=y<2x 且 y-x=y^x 
数位dp
枚举数位时，同时枚举两个数的位，满足：
    1. 置位上x<=y => y^x=y-x
    2. 限制y<2x, 想象把x左移1位，得有一个y上的位<2x对应的位才行
因此除了limit，还需多两个属性记录前一位的y和当前是否已经满足y<2x
"""


#       ms
def solve():
    L, R = RI()
    lo, hi = bin(L)[2:], bin(R)[2:]
    m, n = len(lo), len(hi)
    lo = '0' * (n - m) + lo
    lo = list(map(int, lo))
    hi = list(map(int, hi))

    @lru_cache(None)
    def f(i, down_limit1, up_limit1, down_limit2, up_limit2, less2x, prey):  # less2x：小于还是相等，前一位的y
        if i == n:
            return 0 if not less2x else 1
        up1 = hi[i] if up_limit1 else 1
        down1 = lo[i] if down_limit1 else 0
        up2 = hi[i] if up_limit2 else 1
        down2 = lo[i] if down_limit2 else 0
        ans = 0
        # for k in range(down2, up2 + 1):
        #     if not less2x and k < prey: continue
        #     for j in range(max(down1,k), up1 + 1):
        #         # if j >= k:
        #         ans += f(i + 1,
        #                  j == down1 and down_limit1, j == up1 and up_limit1,
        #                  k == down2 and down_limit2, k == up2 and up_limit2,
        #                  less2x or k > prey, j if not less2x else 0
        #                  )
        for k in range(down2, up2 + 1):
            if not less2x and k < prey: continue  # 跳过使y>2x的分支
            for j in range(down1, up1 + 1):
                if j >= k:
                    ans += f(i + 1,
                             j == down1 and down_limit1, j == up1 and up_limit1,
                             k == down2 and down_limit2, k == up2 and up_limit2,
                             less2x or k > prey, j if not less2x else 0
                             )
        return ans % MOD

    print(f(0, True, True, True, True, False, 0))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
