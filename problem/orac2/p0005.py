"""https://orac2.info/problem/fario08climbing/"""
import heapq
import os.path
import sys
from math import inf, comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
INFILE = ''
OUTFILE = ''
if INFILE and os.path.exists(INFILE):
    sys.stdin = open(INFILE, 'r')
if INFILE and os.path.exists(INFILE):
    sys.stdout = open(OUTFILE, 'w')
"""攀岩，给出n(<=50)个坐标(x,y)。(-1000<=x,y<=1000)
你每次需要勾住三个点，然后松开一个点，勾到附近一个点上。每次操作要保证3个点不能有一个太远：每个点要到其中一个距离不超过R(<=6)。
因此，勾住的点状态一共有C(50,3)=19600个,每次状态转移，枚举松开的点是哪个，然后新点从另外两个点的邻居里出，
每个点的邻居都是半径R,因此不会很多，(最多<=n=50个),那么每次找新状态大概50*3。
于是直接dij。
剩下的就是考验码力了：
1. 预处理邻居 n^2，用set存，方便合并
2. 三维状态。
3. 扩展邻居封装一个方法，枚举要松开的点
4. 判断合法状态，利用set
"""


def solve():
    n, r = RI()
    a, b, c = RI()
    g = []
    for _ in range(n):
        x, y = RI()
        g.append((x, y))
    a -= 1
    b -= 1
    c -= 1

    def manh(i, j):
        return abs(g[i][0] - g[j][0]) + abs(g[i][1] - g[j][1])

    reach = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if manh(i, j) <= r:
                reach[i].add(j)
                reach[j].add(i)
    start = sorted((a, b, c))
    a, b, c = start
    vis = [[[inf] * n for _ in range(n)] for _ in range(n)]
    vis[a][b][c] = 0
    q = [(0, a, b, c)]

    while q:
        od, a, b, c = heapq.heappop(q)

        if od > vis[a][b][c]:
            continue
        if c == n - 1:
            return print(vis[a][b][c])
        x, y, z = reach[a], reach[b], reach[c]
        d = vis[a][b][c]

        def f(from_, b, c, y, z):
            rc = y | z
            for a in rc:
                if a == from_ or a == b or a == c:continue
                # if a not in rc :continue
                if b not in reach[a] and b not in reach[c]:continue
                if c not in reach[a] and c not in reach[b]:continue

                v = sorted((a, b, c))
                di = manh(a, from_)
                i, j, k = v
                if d + di < vis[i][j][k]:
                    vis[i][j][k] = d + di
                    heapq.heappush(q, (d + di, i, j, k))

        f(a, b, c, y, z)
        f(b, a, c, x, z)
        f(c, a, b, x, y)
    print(-1)


solve()

sys.stdout.close()
