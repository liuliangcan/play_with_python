# Problem: E. Two Platforms
# Contest: Codeforces - Codeforces Round #667 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1409/E
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
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1409/E

输入 t(≤2e4) 表示 t 组数据，每组数据输入 n(≤2e5) k(≤1e9) 和长为 n 的数组 a(1≤a[i]≤1e9) 和数组 b。所有数据的 n 之和不超过 2e5。

把 a[i] 标记到数轴上，问两条长为 k 的线段，最多可以覆盖多少 a[i]（线段端点可以覆盖 a[i]）。
注意：数组 b 是没用的，但是你要读入它。

扩展：有 m 条线段：2209. 用地毯覆盖后的最少白色砖块
https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/
输入
4
7 1
1 5 2 3 1 5 4
1 3 6 7 2 5 4
1 1
1000000000
1000000000
5 10
10 7 5 15 8
20 199 192 219 1904
10 10
15 19 8 17 20 10 9 2 10 19
12 13 6 17 1 14 7 9 19 3
输出
6
1
5
10
解释 对于第一组数据，你可以覆盖 1,1,2,4,5,5
"""


#   218    ms
def solve():
    n, k = RI()
    a = RILST()
    RI()
    a.sort()
    if a[-1] - a[0] <= 2 * k:
        return print(n)
    pre = [1] * (n + 1)  # 截止到a[:i+1]的最大覆盖,则ans = max(r-l+1+pre[l-1])
    ans = 1
    j = 0  # 双指针
    for i, v in enumerate(a):
        while v - a[j] > k:
            j += 1
        pre[i + 1] = pre[i] if i - j + 1 < pre[i] else i - j + 1
        p = i - j + 1 + pre[j]
        if p > ans:
            ans = p
    print(ans)


#     233  ms
def solve3():
    n, k = RI()
    a = RILST()
    RI()
    a.sort()
    if a[-1] - a[0] <= 2 * k:
        return print(n)
    pre = [1] * n  # 截止到a[:i+1]的最大覆盖,则ans = max(r-l+1+pre[l-1])
    ans = 1
    j = 0  # 双指针
    for i, v in enumerate(a):
        while v - a[j] > k:
            j += 1
        pre[i] = pre[i - 1] if i and i - j + 1 < pre[i - 1] else i - j + 1
        p = i - j + 1 + (pre[j - 1] if j else 0)
        if p > ans:
            ans = p
    print(ans)


#     233  ms
def solve2():
    n, k = RI()
    a = RILST()
    RI()
    a.sort()
    if a[-1] - a[0] <= 2 * k:
        return print(n)
    l, r = [1] * n, [1] * n  # 求以i为左/右端点的窗口覆盖，答案就是max(r[i]+l[i+1])，边界不用单独讨论，因为不会取到
    j = 0  # 双指针
    for i, v in enumerate(a):
        while v - a[j] > k:
            j += 1
        r[i] = l[j] = i - j + 1
    r = list(accumulate(r, max))  # 前缀最大值
    l = list(accumulate(l[::-1], max))[::-1]  # 后缀最大值

    print(max([r[i] + l[i + 1] for i in range(n - 1)], default=1))


#     265  ms
def solve1():
    n, k = RI()
    a = RILST()
    b = RI()
    l, r = [1] * n, [1] * n
    a.sort()
    q = deque()
    for i, v in enumerate(a):
        q.append(i)
        while v - a[q[0]] > k:
            q.popleft()
        r[i] = l[q[0]] = len(q)
    for i in range(1, n):
        if r[i] < r[i - 1]:
            r[i] = r[i - 1]
    for i in range(n - 2, -1, -1):
        if l[i] < l[i + 1]:
            l[i] = l[i + 1]
    ans = 1
    for i in range(n - 1):
        p = r[i] + l[i + 1]
        if ans < p:
            ans = p
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
