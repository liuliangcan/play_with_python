# Problem: D. Robert Hood and Mrs Hood
# Contest: Codeforces - Codeforces Round 974 (Div. 3)
# URL: https://codeforces.com/problemset/problem/2014/D
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/2014/D

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(1≤n≤1e5) d(1≤d≤n) k(1≤k≤n) 和 k 个闭区间，左右端点范围在 [1,n] 中。

输出两个数：
选一个长为 d 的范围 [i,i+d-1]（左右端点必须是 [1,n] 中的整数），这个范围与尽量多的闭区间有交集（只有一个点也可以），输出满足该要求的最小 i。
选一个长为 d 的范围 [i,i+d-1]（左右端点必须是 [1,n] 中的整数），这个范围与尽量少的闭区间有交集（只有一个点也可以），输出满足该要求的最小 i。
注：最大化/最小化与范围相交的区间个数，而非长度。
输入
6
2 1 1
1 2
4 1 2
1 2
2 4
7 2 3
1 2
1 3
6 7
5 1 2
1 2
3 5
9 2 1
2 8
9 2 4
7 9
4 8
1 3
2 3
输出
1 1
2 1
1 4
1 1
1 1
3 4
"""


#       ms
def solve():
    n, d, k = RI()
    diff = [0] * (n + d + 2)
    for _ in range(k):
        l, r = RI()
        diff[l] += 1
        diff[r + d] -= 1

    mx = (0,)
    mn = (k + 1,)
    a = list(accumulate(diff))
    # print(a)
    for i in range(d, n + 1):
        mx = max(mx, (a[i], -(i - d + 1)))
        mn = min(mn, (a[i], i - d + 1))

    print(-mx[1], mn[1])


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
