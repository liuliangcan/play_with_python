# Problem: B. Tolik and His Uncle
# Contest: Codeforces - Codeforces Round #569 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1179/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1179/B

输入 n m (n*m≤1e6)，表示一个 n 行 m 列的棋盘，行列编号从 1 开始。
初始时，你在 (1,1)。每一步，你可以使用一个方向向量 (dx,dy)，然后从当前位置 (x,y) 移动到 (x+dx,y+dy)。
你需要访问每个格子恰好一次，且每一步使用的方向向量互不相同。
如果存在这样的移动方案，输出任意一组符合要求的 n*m 个坐标，表示你每一步所在的位置。否则输出 -1。
输入
2 3
输出
1 1
1 3
1 2
2 2
2 3
2 1

输入
1 1
输出
1 1
"""
"""https://codeforces.com/contest/1179/submission/108111481

提示 1：方案一定存在。

提示 2：从左上角跳到右下角，这个方向向量以后绝不会再用到了。

提示 3：然后再从右下角跳到 (1,2)，这个方向向量以后也绝不会再用到了。"""


#   187    ms
def solve3():
    n, m = RI()

    a, b = 1, 1
    x, y = n, m
    while a < x or (a == x and b < y):
        sys.stdout.write(f'{a} {b}\n{x} {y}\n')
        if b < m:
            b += 1
        else:
            a += 1
            b = 1
        if y > 1:
            y -= 1
        else:
            x -= 1
            y = m

    if a == x and b == y:
        sys.stdout.write(f'{a} {b}')


#    545   ms
def solve2():
    n, m = RI()

    a, b = 1, 1
    x, y = n, m
    while a < x or (a == x and b < y):
        print(a, b)
        print(x, y)
        if b < m:
            b += 1
        else:
            a += 1
            b = 1
        if y > 1:
            y -= 1
        else:
            x -= 1
            y = m

    if a == x and b == y:
        print(a, b)


#   265    ms
def solve1():
    n, m = RI()

    a, b = 1, 1
    x, y = n, m
    ans = []
    while a < x or (a == x and b < y):
        ans.append(f'{a} {b}\n{x} {y}')
        if b < m:
            b += 1
        else:
            a += 1
            b = 1
        if y > 1:
            y -= 1
        else:
            x -= 1
            y = m

    if a == x and b == y:
        ans.append(f'{a} {b}')
    print('\n'.join(ans))


#     608  ms
def solve0():
    n, m = RI()

    a, b = 1, 1
    x, y = n, m
    ans = []
    while a < x or (a == x and b < y):
        ans.extend([(a, b), (x, y)])
        if b < m:
            b += 1
        else:
            a += 1
            b = 1
        if y > 1:
            y -= 1
        else:
            x -= 1
            y = m

    if a == x and b == y:
        ans.append((a, b))
    print('\n'.join(map(lambda x: ' '.join(map(str, x)), ans)))


#    202   ms
def solve4():
    n, m = RI()
    r1, r2 = 1, n
    while r1 < r2:
        for x, y in zip(range(1, m + 1), range(m, 0, -1)):
            sys.stdout.write(f'{r1} {x}\n{r2} {y}\n')
        r1 += 1
        r2 -= 1
    if r1 == r2:
        l, r = 1, m
        while l < r:
            sys.stdout.write(f'{r1} {l}\n{r2} {r}\n')
            l += 1
            r -= 1
        if l == r:
            sys.stdout.write(f'{r1} {l}\n')


#   202   ms
def solve5():
    n, m = RI()
    r1, r2 = 1, n
    while r1 < r2:
        for x in range(1, m + 1):
            sys.stdout.write(f'{r1} {x}\n{r2} {m - x + 1}\n')
        r1 += 1
        r2 -= 1
    if r1 == r2:
        l, r = 1, m
        while l < r:
            sys.stdout.write(f'{r1} {l}\n{r2} {r}\n')
            l += 1
            r -= 1
        if l == r:
            sys.stdout.write(f'{r1} {l}\n')


#   295   ms
def solve():
    n, m = RI()
    l, r = 0, n * m - 1
    while l <= r:
        sys.stdout.write(f'{l // m + 1} {l % m + 1}\n')
        if l < r:
            sys.stdout.write(f'{r // m + 1} {r % m + 1}\n')
        elif l == r:
            break
        l += 1
        r -= 1


if __name__ == '__main__':
    solve()
