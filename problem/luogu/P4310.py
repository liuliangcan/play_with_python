# Problem: P4310 绝世好题
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P4310
# Memory Limit: 512 MB
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
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://www.luogu.com.cn/problem/P4310

输入 n(1≤n≤1e5) 和长为 n 的数组 a(0≤a[i]≤1e9)。

找一个 a 的子序列 b，满足 b 中任意相邻元素的 AND 不等于 0。
输出 b 的最长长度。
注：长为 1 的 b 一定满足要求。
"""
"""状态机DP
定义：f[i][j]为前i个数里，含二进制1的末尾数字最长长度
转移：当前数字是v，那么从前序状态的相同二进制1的位转移过来；然后这个数字可以刷新所有v为1的状态；由于是子序列，还要继承
初始值：用滚动压缩，因此初始全是0
答案：max(f[-1]),注意至少是1
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    f = [0] * 30
    for v in a:
        p = 0
        for i in range(30):
            if v >> i & 1 and f[i] > p:
                p = f[i]
        p += 1
        for i in range(30):
            if v >> i & 1:
                f[i] = p


    print(max(max(f), 1))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
