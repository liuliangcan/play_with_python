"""https://orac2.info/problem/seln04jogging/"""
import heapq
import os.path
import sys
from collections import deque
from math import inf, comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
INFILE = 'jogin.txt'
OUTFILE = 'jogout.txt'
if INFILE and os.path.exists(INFILE):
    sys.stdin = open(INFILE, 'r')
if INFILE and os.path.exists(INFILE):
    sys.stdout = open(OUTFILE, 'w')
"""有向无环图，问任意节点到任意节点的最大边权和，可以不动
直接topsort+dp

"""


def solve():
    n, = RI()
    g = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    while True:
        u, v, w = RI()
        if u == v == w == 0:
            break
        g[u].append((v, w))
        degree[v] += 1
    q = [u for u in range(1, n + 1) if degree[u] == 0]
    f = [0] * (n + 1)
    while q:
        u = q.pop()
        for v, w in g[u]:
            f[v] = max(f[v], w + f[u])
            degree[v] -= 1
            if degree[v] == 0:
                q.append(v)

    print(max(f))


solve()

sys.stdout.close()
