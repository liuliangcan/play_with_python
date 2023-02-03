# Problem: F - Transportation
# Contest: AtCoder - TOYOTA MOTOR CORPORATION Programming Contest 2022(AtCoder Beginner Contest 270)
# URL: https://atcoder.jp/contests/abc270/tasks/abc270_f
# Memory Limit: 1024 MB
# Time Limit: 4000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import sys
import heapq
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

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7


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


class MST:
    def __init__(self, es, n, key=lambda x: x[3]):
        self.es = sorted(es, key=key)
        self.n = n

    def kruskal(self):
        dsu = DSU(self.n + 1)
        ans = 0
        for u, v, w in self.es:
            if dsu.union(u, v):
                ans += w
        return ans


class UnionFind:
    def __init__(self, n: int):
        self.parent = [x for x in range(n)]
        self.size = [1 for _ in range(n)]  # 本家族size
        self.n = n
        self.setCount = n  # 共几个家族

    def find_fa(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find_fa(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find_fa(x)
        root_y = self.find_fa(y)
        if root_x == root_y:
            return False
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.setCount -= 1
        return True


#    2956   ms
def solve1(n, m, airs, ports, es):
    a, p = n + 1, n + 2
    ae = [(u, a, w) for u, w in enumerate(airs, start=1)]  # 机场到超级源点
    pe = [(u, p, w) for u, w in enumerate(ports, start=1)]  # 港口到超级源点

    def calc(es, ok=1):  # 讨论建机场或港口的必能联通省去一层O(n)判断
        # Kruskal 先加小边
        es.sort(key=lambda x: x[2])
        dsu = UnionFind(n + 3)
        ans = 0
        for u, v, w in es:
            if dsu.union(u, v):
                ans += w
        f = dsu.find_fa(1)
        return ans if ok or all(dsu.find_fa(x) == f for x in range(2, n + 1)) else inf

    print(min(calc(es + ae), calc(es + pe), calc(es + ae + pe), calc(es, 0)))


#   2966    ms
def solve(n, m, airs, ports, es):
    a, p = n + 1, n + 2
    ae = [(u, a, w) for u, w in enumerate(airs, start=1)]  # 机场到超级源点
    pe = [(u, p, w) for u, w in enumerate(ports, start=1)]  # 港口到超级源点

    def calc(es):  # 讨论建机场或港口的必能联通省去一层O(n)判断
        # Kruskal 先加小边
        es.sort(key=lambda x: x[2])
        dsu = DSU(n + 3)
        ans = 0
        for u, v, w in es:
            if dsu.union(u, v):
                ans += w
                # if dsu.size[dsu.find_fa(1)] >= n:
                #     break
        return ans if dsu.size[dsu.find_fa(1)] >= n else inf

    print(min(calc(es + ae), calc(es + pe), calc(es + ae + pe), calc(es)))


if __name__ == '__main__':
    n, m = RI()
    airs = RILST()
    ports = RILST()
    es = []
    for _ in range(m):
        es.append(RILST())

    solve(n, m, airs, ports, es)

PROBLEM = """https://atcoder.jp/contests/abc270/tasks/abc270_f

输入 n m (≤2e5)。有 n 个岛屿。
输入 n 个数，表示在第 i 个岛屿上修建机场的花费(≤1e9)。如果两个岛都有机场，则可以互相到达。
输入 n 个数，表示在第 i 个岛屿上修建港口的花费(≤1e9)。如果两个岛都有港口，则可以互相到达。
输入 m 条边，每条边输入 a b z 表示在岛屿 a 和 b 造桥的花费为 z(≤1e9)。
输出使得任意两个岛可以互相到达的最小花费。
输入
4 2
1 20 4 7
20 2 20 3
1 3 5
1 4 6
输出 16

输入
3 1
1 1 1
10 10 10
1 2 100
输出 3
"""
"""最小生成树（Minimum Spanning Tree，MST）的Kruskal算法，把边排序，从小到大加边，如果当前边两边的点已经联通则放弃这条边；注意原图必须是联通的才有MST。
本题如果要用机场、港口，则分别建立超级源点；然后分别讨论是否用机场、港口共4种情况。
"""
