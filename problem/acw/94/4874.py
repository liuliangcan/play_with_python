# Problem: 最早时刻
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4874/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
from heapq import *
from math import inf

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')


#    4330   ms
def solve1():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = RI()
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    gogo = []
    for _ in range(n):
        _, *b = RI()
        can = {}
        if b:
            go = b[-1] + 1
            can[b[-1]] = go
            for i in range(len(b) - 2, -1, -1):
                if b[i] + 1 != b[i + 1]:
                    go = b[i] + 1
                can[b[i]] = go
        gogo.append(can)

    vis = [inf] * n
    vis[0] = 0
    h = [(0, 0)]
    while h:
        d, u = heappop(h)
        if u == n - 1:
            return print(d)
        ban = gogo[u]
        go = ban.get(d, d)

        for v, w in g[u]:
            nd = go + w
            if vis[v] > nd:
                vis[v] = nd
                heappush(h, (nd, v))
    # if n - 1 in vis:
    #     return print(vis[n - 1])
    print(-1)


#    4330   ms
def solve():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = RI()
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    ban = []
    for _ in range(n):
        _, *b = RI()
        ban.append(b)

    vis = [inf] * n
    vis[0] = 0
    h = [(0, 0)]
    while h:
        d, u = heappop(h)
        if u == n - 1:
            return print(d)
        if d > vis[u]:continue
        b = ban[u]
        for c in b:
            if c == d:
                d += 1
            elif c > d:
                break

        for v, w in g[u]:
            nd = d + w
            if vis[v] > nd:
                vis[v] = nd
                heappush(h, (nd, v))
    # if n - 1 in vis:
    #     return print(vis[n - 1])
    print(-1)


if __name__ == '__main__':
    solve()
