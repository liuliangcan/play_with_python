# Problem: F2. Same Sum Blocks (Hard)
# Contest: Codeforces - Codeforces Round #547 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1141/F2
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1141/F2

输入 n(≤1500) 和长为 n 的数组 a(-1e5≤a[i]≤1e5)，下标从 1 开始。

你需要从 a 中选出尽量多的非空连续子数组，这些子数组不能重叠，且元素和相等。
输出子数组的个数 k，然后输出 k 行，每行两个数表示子数组的左右端点。
可以按任意顺序输出，多种方案可以输出任意一种。
"""
"""https://codeforces.com/contest/1141/submission/192610240

暴力统计每个子数组的和，用哈希表把和相同的子数组左右端点记录下来。
对于每一组，问题变成最多不重叠线段个数。
这是个经典贪心，按照右端点从小到大排序+遍历，一旦遇到左端点大于上一个记录的右端点，答案加一，更新右端点。"""


#   1091    ms  暴力+右端点排序+贪心 n^2lgn
def solve1():
    n, = RI()
    a = RILST()
    d = defaultdict(list)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            d[s].append((i + 1, j + 1))
    ans = []

    for lst in d.values():
        if len(lst) <= len(ans):
            continue
        lst.sort(key=lambda x: x[1])
        t = []
        r0 = 0
        for l, r in lst:
            if l > r0:
                t.append((l, r))
                r0 = r
        if len(t) > len(ans):
            ans = t

    print(len(ans))
    print('\n'.join(map(lambda x: f'{x[0]} {x[1]}', ans)))


#  1122    ms   暴力+左端点排序(省去)+贪心 n^2
def solve2():
    n, = RI()
    a = RILST()
    d = defaultdict(list)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            d[s].append((i + 1, j + 1))

    ans = []
    for lst in d.values():
        if len(lst) <= len(ans):
            continue
        t = []
        l1 = 10 ** 6
        for l, r in lst[::-1]:
            if r < l1:
                t.append((l, r))
                l1 = l
        if len(t) > len(ans):
            ans = t

    print(len(ans))
    print('\n'.join(map(lambda x: f'{x[0]} {x[1]}', ans)))


#   1075  ms   一趟处理,直接存贪心结果
def solve():
    n, = RI()
    a = [0] + RILST()
    d = defaultdict(list)
    mx = 0
    for r in range(1, n + 1):
        s = 0
        for l in range(r, 0, -1):
            s += a[l]
            if not d[s] or d[s][-1][1] < l:
                d[s].append((l, r))
                if len(d[mx]) < len(d[s]):
                    mx = s

    print(len(d[mx]))
    print('\n'.join(map(lambda x: f'{x[0]} {x[1]}', d[mx])))


if __name__ == '__main__':
    solve()
