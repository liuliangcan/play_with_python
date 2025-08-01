# Problem: D - Pedometer
# Contest: AtCoder - AtCoder Beginner Contest 367
# URL: https://atcoder.jp/contests/abc367/tasks/abc367_d
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
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc367/tasks/abc367_d

输入 n(2≤n≤2e5) m(1≤m≤1e6) 和长为 n 的数组 a(1≤a[i]≤1e9)。下标从 1 开始。

一个环上有 n 个位置，顺时针编号从 1 到 n。
从 i 顺时针移动到 i+1，需要走 a[i] 步。
特别地，从 n 顺时针移动到 1，需要走 a[n] 步。

输出有多少对位置 (s,t)，满足 s≠t，且从 s 顺时针移动到 t 的最小步数是 m 的倍数。

输入
4 3
2 1 4 3
输出 4

输入
2 1000000
1 1
输出 0

输入
9 5
9 9 8 2 4 4 3 5 3
输出 11
"""


#       ms
def solve():
    n, m = RI()
    a = RILST()
    cnt = defaultdict(int)
    cnt[0] = 1
    ans = s = s1 = 0
    for i in range(2 * n - 1):
        s = (s + a[i % n]) % m
        if i >= n - 1:
            cnt[s1] -= 1
            s1 = (s1 + a[i - n + 1]) % m
        ans += cnt[s]
        if i < n-1:
            cnt[s] += 1
        # print(i,s,ans,cnt)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
