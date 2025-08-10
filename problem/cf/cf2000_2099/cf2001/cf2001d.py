# Problem: D. Longest Max Min Subsequence
# Contest: Codeforces - Codeforces Round 967 (Div. 2)
# URL: https://codeforces.com/problemset/problem/2001/D
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
PROBLEM = """https://codeforces.com/problemset/problem/2001/D

输入 T(≤5e4) 表示 T 组数据。所有数据的 n 之和 ≤3e5。
每组数据输入 n(1≤n≤3e5) 和长为 n 的数组 a(1≤a[i]≤n)。

从 a 中选择一个子序列 b，满足：
1. b 包含 a 中的所有元素，无重复元素。（相当于把 a 去重）
2. （b 的下标从 1 开始）如果把 b 的奇数下标的元素乘以 -1，得到的新序列 c 的字典序是最小的。

输出 b 的长度，以及 b。
输入
4
4
3 2 1 3
4
1 1 1 1
9
3 2 1 3 2 1 3 2 1
1
1
输出
3
3 2 1
1
1
3
3 1 2
1
1

输入
10
2
1 2
10
5 2 1 7 9 7 2 5 5 2
2
1 2
10
2 2 8 7 7 9 8 1 9 6
9
9 1 7 5 8 5 6 4 1
3
3 3 3
6
1 6 4 4 6 5
6
3 4 4 5 3 3
10
4 1 4 5 4 5 10 1 5 1
7
1 2 1 3 2 4 6
输出
2
1 2
5
5 1 9 7 2
2
1 2
6
2 7 9 8 1 6
7
9 1 7 5 8 6 4
1
3
4
1 4 6 5
3
4 5 3
4
5 4 10 1
5
2 1 3 4 6
"""


#   406    ms
def solve():
    n, = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    vis = [0] * (n + 1)
    st = []
    for v in a:
        cnt[v] -= 1
        if not vis[v]:
            while st and cnt[st[-1]] and ((-v if len(st) & 1 else v) < (-st[-1] if len(st) & 1 else st[-1]) or
                                          len(st) >= 2 and cnt[st[-2]] and (v if len(st) & 1 else -v) < (
                                                  st[-2] if len(st) & 1 else -st[-2])):
                vis[st.pop()] = 0
            vis[v] = 1
            st.append(v)
        # print(v,st)
    print(len(st))
    print(*st)


#   359    ms
def solve1():
    n, = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    vis = [0] * (n + 1)
    st = []
    for v in a:
        cnt[v] -= 1
        if not vis[v]:
            while True:
                if st and cnt[st[-1]] and (-v if len(st) & 1 else v) < (-st[-1] if len(st) & 1 else st[-1]):
                    vis[st.pop()] = 0
                elif len(st) >= 2 and cnt[st[-1]] and cnt[st[-2]] and (v if len(st) & 1 else -v) < (
                        st[-2] if len(st) & 1 else -st[-2]):
                    vis[st.pop()] = 0
                    vis[st.pop()] = 0
                else:
                    break
            vis[v] = 1
            st.append(v)
        # print(v,st)
    print(len(st))
    print(*st)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
