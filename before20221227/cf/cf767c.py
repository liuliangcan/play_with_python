import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *
from types import GeneratorType

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/767/C

输入 n(3≤n≤1e6)，表示一颗有 n 个节点的有根树，节点编号从 1 开始。
每行输入两个数，表示当前节点的父节点编号（如果是 0 表示当前节点是根节点），以及节点的点权，范围在 [-100,100]。
例如节点 1 的父节点为 2，则表示一条 2->1 的边。

你需要删除两条边，将这棵树分成三个连通块，且每个连通块的点权和相等。
假设删除的边是 a->b 和 c->d，你需要输出 b 和 d。如果有多种方案，输出任意一种。
如果无法做到，输出 -1。
输入
6
2 4
0 5
4 2
2 1
1 1
4 2
输出 1 4
解释 见右图

输入
6
2 4
0 6
4 2
2 1
1 1
4 2
输出 -1
"""


#  1871 	 ms
def solve1(n, g, ws, root):
    total = sum(ws)
    if total % 3:
        return print(-1)
    target = total // 3
    order = []
    q = deque([root])
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            q.append(v)

    ans = []
    f = ws[:]
    for u in order[::-1]:
        for v in g[u]:
            if f[v] != target:
                f[u] += f[v]
        if f[u] == target and u != root:
            ans.append(u)
            if len(ans) == 2:
                return print(ans[0] + 1, ans[1] + 1)
    print(-1)


#   1715	 ms
def solve2(n, g, f, root):
    total = sum(f)
    if total % 3:
        return print(-1)
    target = total // 3
    ans = []
    order = []
    q = deque([root])
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            q.append(v)
    for u in order[::-1]:
        for v in g[u]:
            if f[v] != target:
                f[u] += f[v]
        if f[u] == target and u != root:
            ans.append(u)
            if len(ans) == 2:
                return print(ans[0] + 1, ans[1] + 1)
    print(-1)


#   1590  	 ms
def solve(n, g, f, root):
    total = sum(f)
    if total % 3:
        return print(-1)
    target = total // 3
    ans = []
    q = [root]
    i = 0
    while i < len(q):
        u = q[i]
        for v in g[u]:
            q.append(v)
        i += 1
    for i in range(len(q) - 1, -1, -1):
        u = q[i]
        for v in g[u]:
            if f[v] != target:
                f[u] += f[v]
        if f[u] == target and u != root:
            ans.append(u)
            if len(ans) == 2:
                return print(ans[0] + 1, ans[1] + 1)
    print(-1)


if __name__ == '__main__':
    n, = RI()
    g = [[] for _ in range(n)]
    ws = [0] * n
    root = -1
    for v in range(n):
        u, w = RILST()
        if u == 0:
            root = v
        else:
            g[u - 1].append(v)
        ws[v] = w

    solve(n, g, ws, root)
