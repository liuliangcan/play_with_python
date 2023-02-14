# Problem: E1. Reading Books (easy version)
# Contest: Codeforces - Codeforces Round #653 (Div. 3)
# URL: https://codeforces.com/contest/1374/problem/E1
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/contest/1374/problem/E1

输入 n k (1≤k≤n≤2e5)，表示有 n 本书，然后输入 n 行，每行输入 t(1≤t≤1e4) a b，其中 a=0/1 表示 A 喜欢/不喜欢这本书，b=0/1 表示 B 喜欢/不喜欢这本书。

你需要选择一些书，使得其中至少有 k 本是 A 喜欢的，至少有 k 本是 B 喜欢的。
如果无法满足输出 -1，否则输出所选书的 t 之和的最小值。

进阶：如果要选恰好 m 本书呢？ （就是E2题，试了一下没做出来）
输入
8 4
7 1 1
2 1 1
4 0 1
8 1 1
1 0 1
1 1 1
1 0 1
3 0 0
输出 18
"""
"""贪心
先分类出仅a喜欢、仅b喜欢、都喜欢c的三种书。排序。
从c(都喜欢)入手讨论，优先从c中选，:
    1. 如果超过k本，那就选k本c。
        然后尝试把c中最大的移除，换成一本a和b。当然要满足a+b<c才能换。
        如果不满足则可以跳出了，后边怎么换都不会更优。
    2. 如果不超过k本，则全选，且再从a和b中各选出k-c本补充进来。
        然后执行同样的逻辑，尝试用a+b替换c。
"""


#   155    ms
def solve1():
    n, k = RI()
    a, b, c = [], [], []  # 仅a喜欢，仅b喜欢，都喜欢

    for _ in range(n):
        t, x, y = RI()
        if x == y == 1:
            c.append(t)
        elif x == 1:
            a.append(t)
        elif y == 1:
            b.append(t)
    both = len(c)

    if both + len(a) < k or both + len(b) < k:
        return print(-1)
    a.sort()
    b.sort()
    c.sort()
    if both >= k:
        ans = sum(c[:k])  # 从c中选k本
        both = k - 1  # c的指针指向末尾
        i = j = 0  # ab指针都从头
    else:
        ans = sum(c) + sum(a[:k - both]) + sum(b[:k - both])  # c选完，且用ab补充到k
        both -= 1  # c的指针指向末尾
        i = j = k - both  # ab指针只能从k-both
    while i < len(a) and j < len(b) and both >= 0 and a[i] + b[j] < c[both]:  # 可以替换
        ans += a[i] + b[j] - c[both]  # 替换
        i += 1
        j += 1
        both -= 1
    print(ans)


#   171    ms
def solve():
    n, k = RI()
    a, b, c = [], [], []  # 仅a喜欢，仅b喜欢，都喜欢

    for _ in range(n):
        t, x, y = RI()
        if x == y == 1:
            c.append(t)
        elif x == 1:
            a.append(t)
        elif y == 1:
            b.append(t)
    a.sort()
    b.sort()
    for x, y in zip(a, b):
        c.append(x + y)

    if len(c) < k:
        return print(-1)
    print(sum(nsmallest(k, c)))  # 421ms
    # c.sort()
    # print(sum(c[:k]))


#    171   ms
def solve2():
    n, k = RI()
    a, b, c = [], [], []  # 仅a喜欢，仅b喜欢，都喜欢

    for _ in range(n):
        t, x, y = RI()
        if x == y == 1:
            c.append(t)
        elif x == 1:
            a.append(t)
        elif y == 1:
            b.append(t)
    for x, y in zip(sorted(a), sorted(b)):
        c.append(x + y)

    if len(c) < k:
        return print(-1)

    print(sum(sorted(c)[:k]))


if __name__ == '__main__':
    solve()
