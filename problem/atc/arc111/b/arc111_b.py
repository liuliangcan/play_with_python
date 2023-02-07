# Problem: B - Reversible Cards
# Contest: AtCoder - AtCoder Regular Contest 111
# URL: https://atcoder.jp/contests/arc111/tasks/arc111_b
# Memory Limit: 1024 MB
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
PROBLEM = """https://atcoder.jp/contests/arc111/tasks/arc111_b

输入 n(≤2e5) 和一个 n 行 2 列的矩阵，矩阵元素范围 [1,4e5]。
从每行中恰好选一个数，你最多能选出多少个不同的数？
输入
4
1 2
1 3
4 2
2 3
输出
4

输入
2
111 111
111 111
输出
1
"""
"""https://atcoder.jp/contests/arc111/submissions/38552445

把每行的两个数当作图的一条边的两个端点。

对每个连通块分别统计。
如果连通块是树，那么答案是边数。
如果连通块不是树，那么答案是点数。"""
"""
无环的情况，树：
比如
1 2 
2 3
2是重叠的
1-2-3 一共两条边
每条边取一个点 最大化取点 
那么可以从任意叶子作为根出发，取每条边上远离根的那个点，由于没有重边和自环，取的点就不会重，ans=点数-1=边数

但是有环/重边的例子如
1 2
2 3
2 3
图是 1-2=3 （23之间两条边）
多出来的那条边就可以把根取到，因此可以取到所有点，ans=点数

对于有环的情况，可以这么分析：
环上的所有边可以保证每条边正好取到一个点；
不在环上的边，可以让每条边取远离环的那个点，因此一定可以取完所有点
"""


class DSU:
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.setCount = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            self.edge_size[y] += 1
            return False
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.setCount -= 1
        return True


#    441    ms
def solve1():
    n, = RI()
    s = set()
    dsu = DSU(4 * 10 ** 5 + 1)
    for _ in range(n):
        u, v = RI()
        s.add(u)
        s.add(v)
        dsu.union(u, v)
    ans = 0
    vis = set()
    for x in s:
        fa = dsu.find_fa(x)
        if fa in vis:
            continue
        vis.add(fa)
        if dsu.size[fa] == dsu.edge_size[fa] + 1:  # 本连通块点数==边数+1，则是树；否则有环
            ans += dsu.edge_size[fa]
        else:
            ans += dsu.size[fa]
    print(ans)


#    379    ms
def solve2():
    n, = RI()
    s = set()
    dsu = DSU(4 * 10 ** 5 + 1)
    for _ in range(n):
        u, v = RI()
        s.add(u)
        s.add(v)
        dsu.union(u, v)
    ans = 0
    vis = [0] * (4 * 10 ** 5 + 1)
    for x in s:
        fa = dsu.find_fa(x)
        if vis[fa]:
            continue
        vis[fa] = 1
        if dsu.size[fa] == dsu.edge_size[fa] + 1:  # 本连通块点数==边数+1，则是树；否则有环
            ans += dsu.edge_size[fa]
        else:
            ans += dsu.size[fa]
    print(ans)


#    293       ms
def solve():
    n, = RI()
    dsu = DSU(4 * 10 ** 5 + 1)
    for _ in range(n):
        u, v = RI()
        dsu.union(u, v)
    ans = 0

    # 并查集方法计算每个连通块的点数和边数，取小的那个(无环树取边数；有环取点数)
    # 并查集方法用py实现；dfs方法用go实现；bfs方法用rust实现；可移步查看
    for x in range(4 * 10 ** 5 + 1):
        fa = dsu.find_fa(x)
        if fa == x:
            if dsu.size[fa] == dsu.edge_size[fa] + 1:  # 本连通块点数==边数+1，则是树；否则有环
                ans += dsu.edge_size[fa]
            else:
                ans += dsu.size[fa]
    print(ans)


if __name__ == '__main__':
    solve()
