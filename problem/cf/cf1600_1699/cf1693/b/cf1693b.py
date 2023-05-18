# Problem: B. Fake Plastic Trees
# Contest: Codeforces - Codeforces Round 800 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1693/B
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
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1693/B

输入 T(≤1e3) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(2≤n≤2e5) 表示一棵 n 个节点的树，编号从 1 开始，1 为根节点。
然后输入 p[2],p[3],...,p[n]，其中 p[i] 表示 i 的父节点。
然后输入 n 行，其中第 i 行输入两个数 l 和 r，表示第 i 个节点值的目标范围 [l,r]。 1<=l<=r<=1e9

初始时，所有节点值均为 0。
每次操作你可以选择一条从 根 开始的路径，把路径上的每个节点值都加上一个非负数p[j]。
要求这些数按p照路径的顺序，形成一个递增序列。（可以相等，可以等于 0，例如 [0,0,1,3,3]）
要使所有节点值都在对应的范围内，至少要操作多少次？
"""
"""输入
4
2
1
1 5
2 9
3
1 1
4 5
2 4
6 10
4
1 2 1
6 9
5 6
4 5
2 4
5
1 2 3 4
5 5
4 4
3 3
2 2
1 1
输出
1
2
2
5"""
"""https://codeforces.com/contest/1693/submission/206072426

自底向上思考。

每个叶子由于下界 >=1，所以一定要操作，由于序列是递增的，那么尽量取范围的上界，祖先节点的增量可以没叶子这么多。

对于一个非叶节点，累加所有子节点的增量。如果小于下界，那么必须操作一次，变成上界。如果大于上界则免费调整为上界。"""


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


#    514   ms
def solve1():
    n, = RI()
    p = RILST()
    g = [[] for _ in range(n)]
    for i, v in enumerate(p, start=1):
        g[v - 1].append(i)
    ls, rs = [], []
    for _ in range(n):
        l, r = RI()
        ls.append(l)
        rs.append(r)

    change = [0] * n
    ans = 0

    @bootstrap
    def dfs(u):
        nonlocal ans
        if not g[u]:
            ans += 1
            change[u] = rs[u]
        else:
            s = 0
            for v in g[u]:
                yield dfs(v)
                s += change[v]
            if s >= rs[u]:
                change[u] = rs[u]
            elif s >= ls[u]:
                change[u] = s
            else:
                change[u] = rs[u]
                ans += 1
        yield

    dfs(0)
    # print(g)
    # print(ls)
    # print(rs)
    # print(change)
    print(ans)


#  390     ms
def solve2():
    n, = RI()
    p = RILST()
    g = [[] for _ in range(n)]
    for i, v in enumerate(p, start=1):
        g[v - 1].append(i)
    ls, rs = [], []
    for _ in range(n):
        l, r = RI()
        ls.append(l)
        rs.append(r)

    order = []
    q = deque([0])
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            q.append(v)

    change = [0] * n
    ans = 0
    for u in order[::-1]:
        if not g[u]:
            ans += 1
            change[u] = rs[u]
        else:
            for v in g[u]:
                change[u] += change[v]
            if change[u] >= rs[u]:
                change[u] = rs[u]
            elif change[u] < ls[u]:
                change[u] = rs[u]
                ans += 1
    print(ans)


#   202     ms
def solve():
    n, = RI()
    p = [0] + RILST()

    ls, rs = [], []
    for _ in range(n):
        l, r = RI()
        ls.append(l)
        rs.append(r)

    change = [0] * n
    ans = 0
    for u in range(n - 1, -1, -1):
        if not change[u]:
            ans += 1
            change[u] = rs[u]
        else:
            if change[u] >= rs[u]:
                change[u] = rs[u]
            elif change[u] < ls[u]:
                change[u] = rs[u]
                ans += 1
        change[p[u] - 1] += change[u]
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
