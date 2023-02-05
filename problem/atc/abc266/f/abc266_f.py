# Problem: F - Well-defined Path Queries on a Namori
# Contest: AtCoder - AtCoder Beginner Contest 266
# URL: https://atcoder.jp/contests/abc266/tasks/abc266_f
# Memory Limit: 1024 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://atcoder.jp/contests/abc266/tasks/abc266_f

输入 n (3≤n≤2e5) 和 n 条边，点的编号在 [1,n] 内，表示一个没有重边和自环的无向连通图。
然后输入 q(≤2e5) 表示有 q 个询问，每个询问输入两个数 x 和 y (1≤x<y≤n)。
对于每个询问，如果 x 和 y 之间只存在唯一的简单路径，则输出 Yes，否则输出 No。
输入
5
1 2
2 3
1 3
1 4
2 5
3
1 2
1 4
1 5
输出
No
Yes
No
"""


class DSU:
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1 for _ in range(n)]  # 本家族size
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
            return False
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.setCount -= 1
        return True


#       ms
def solve():
    """
    基环树解法,注意是n个节点n条边，因此只有一个环
    这个图可以看做1个环和他们身上的“树枝”
    先做拓扑排序，把树枝都找到，
    显然，”只存在一条简单路径“ 等价于 ”这俩数在同一个树枝上“ 或 ”这俩数在相邻的树枝上（他们都连接到环上的同一个节点）“
    可以思考一下，别的情况都不符合，比如任意一个在环上，或中间需要经过环上的多个节点。
    注意这里是无向基环树，因此建图时degree都要+1，拓扑时，判断是1的度继续遍历（树叶），注意出度入度都减去
    然后用并查集维护节点所在树枝的连通性
    """
    n, = RI()
    g = [[] for _ in range(n)]
    degree = [0] * n
    for _ in range(n):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        degree[u] += 1
        degree[v] += 1
    dsu = DSU(n)
    start = []
    for i, x in enumerate(degree):
        if x == 1:
            degree[i] -= 1
            start.append(i)

    q = deque(start)
    while q:
        u = q.popleft()
        for v in g[u]:
            dsu.union(u, v)
            degree[v] -= 1
            if degree[v] == 1:
                degree[v] -= 1
                q.append(v)

    q, = RI()
    for _ in range(q):
        x, y = RI()
        if dsu.find_fa(x - 1) == dsu.find_fa(y - 1):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    solve()
