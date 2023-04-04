# Problem: D2. Equalizing by Division (hard version)
# Contest: Codeforces - Codeforces Round #582 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1213/D2
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
PROBLEM = """https://codeforces.com/problemset/problem/1213/D2

输入 n k (1≤k≤n≤2e5) 和长为 n 的数组 a(1≤a[i]≤2e5)。

每次操作你可以让一个 a[i] 变为 floor(a[i]/2)。
要想得到至少 k 个相同的数，最少需要多少次操作？

进阶：你能想出一个时间复杂度为 O(max(a)) 的做法吗？
输入
5 3
1 2 2 4 5
输出 1

输入
5 3
1 2 3 4 5
输出 2

输入
5 3
1 2 3 3 3
输出 0
"""
"""https://codeforces.com/contest/1213/submission/193430181

设 U=max(a)。
O(Ulog^2U) 或者 O(UlogU) 的做法是把每个 a[i] 变成 a[i]/2^j 的次数 j 存到 x=a[i]/2^j 里面。每个 x 都有一个列表去存储次数 j。
然后对每个 1~U 的数 x，累加列表中最小的 k 个次数，最小的和就是答案。

O(U) 的做法是从 U~1 倒着考虑数 x，每个 x 都有一个列表，列表的第 j 项记录有多少个数可以通过操作 j 次变为 x。
如果无法得到到 k 个 x，那么就把这个列表左边插入个 0，然后合并到 x/2 的列表中。
时间复杂度看上去是 O(UlogU)，但是 x 越大，列表的长度越短，仔细计算可以得到所有列表长度之和其实是 O(U) 的。"""


#  795  ms
def solve3():
    n, k = RI()
    a = RILST()
    mx = max(a)
    p = [deque([0]) for _ in range(mx + 1)]
    for v in a:
        p[v][0] += 1
    ans = 1e9
    no = deque([0])
    for i in range(mx, 0, -1):
        b = p[i]
        if b == no:
            continue
        s, left = 0, k
        for j, c in enumerate(b):
            if left <= c:
                ans = min(ans, s + left * j)
                break
            s += c * j
            left -= c
        i2 = i // 2
        if p[i2] == no:
            b.appendleft(0)
            p[i2] = b
        else:
            for j, c in enumerate(b):
                if j + 1 == len(p[i2]):
                    # p[i2].extend(islice(b, j , len(b), 1))  # 686 ms
                    p[i2].extend(list(b)[j:])  # 623 ms
                    break
                p[i2][j + 1] += c
    print(ans)


#   623 ms
def solve5():
    n, k = RI()
    a = RILST()
    mx = max(a)
    p = [[] for _ in range(mx + 1)]
    for v in a:
        if not p[v]:
            p[v] = deque([1])
        else:
            p[v][0] += 1
    ans = 1e9
    for i in range(mx, 0, -1):
        b = p[i]
        if not b:
            continue
        s, left = 0, k
        for j, c in enumerate(b):
            if left <= c:
                ans = min(ans, s + left * j)
                break
            s += c * j
            left -= c
        i2 = i // 2
        if not p[i2]:
            b.appendleft(0)
            p[i2] = b
        else:
            for j, c in enumerate(b):
                if j + 1 == len(p[i2]):
                    # p[i2].extend(islice(b, j , len(b), 1))  # 686 ms
                    p[i2].extend(list(b)[j:])  # 623 ms
                    break
                p[i2][j + 1] += c
    print(ans)


#  280  ms
def solve4():
    n, k = RI()
    a = RILST()
    mx = max(a)
    p = [[] for _ in range(mx + 1)]
    for v in a:
        if not p[v]:
            p[v].append(1)
        else:
            p[v][0] += 1
    ans = 1e9
    for i in range(mx, 0, -1):
        b = p[i]
        if not b:
            continue
        s, left = 0, k
        for j, c in enumerate(b):
            if left <= c:
                ans = min(ans, s + left * j)
                break
            s += c * j
            left -= c
        i2 = i // 2
        if not p[i2]:
            p[i2] = [0] + b
        else:
            for j, c in enumerate(b):
                if j + 1 == len(p[i2]):
                    p[i2].extend(b[j:])
                    break
                p[i2][j + 1] += c
    print(ans)


#  264  ms
def solve():
    n, k = RI()
    a = RILST()
    mx = max(a)
    p = [[0] for _ in range(mx + 1)]
    for v in a:
        p[v][0] += 1
    no = [0]
    ans = 1e9
    for i in range(mx, 0, -1):
        b = p[i]
        if b == no:
            continue
        s, left = 0, k
        for j, c in enumerate(b):
            if left <= c:
                ans = min(ans, s + left * j)
                break
            s += c * j
            left -= c
        i2 = i // 2
        if p[i2] == no:
            p[i2].extend(b)
        else:
            for j, c in enumerate(b):
                if j + 1 == len(p[i2]):
                    p[i2].extend(b[j:])
                    break
                p[i2][j + 1] += c
    print(ans)


#   920    ms
def solve2():
    n, k = RI()
    a = RILST()
    p = [[] for _ in range(max(a) + 1)]
    for v in a:
        i = 0
        while v > 0:
            p[v].append(i)
            i += 1
            v //= 2
        p[v].append(i)
    ans = n * 32
    for x in p:
        if len(x) >= k:
            ans = min(ans, sum(sorted(x)[:k]))
    print(ans)


#    420   ms
def solve1():
    n, k = RI()
    a = RILST()
    a.sort()
    p = [[] for _ in range(max(a) + 1)]
    for v in a:
        i = 0
        while v > 0:
            p[v].append(i)
            i += 1
            v //= 2
        p[v].append(i)
    ans = n * 32
    for x in p:
        if len(x) >= k:
            ans = min(ans, sum(x[:k]))
    print(ans)


if __name__ == '__main__':
    solve()
