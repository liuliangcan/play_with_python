# Problem: C. Keshi in Search of AmShZ
# Contest: Codeforces - Codeforces Round 800 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1693/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
from heapq import *
from math import sqrt, gcd, inf

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1693/C

输入 n(2≤n≤1e5) m(1≤m≤2e5) 表示一个 n 点 m 边的有向图（节点编号从 1 开始）。
然后输入 m 条边。没有自环，可能有重边。

你初始在 1，要到达 n。（输入保证可以从 1 到 n。）
每次操作，要么永久删除一条边，要么从当前点随机移动到一个邻居上。

最小化最大操作次数。
输入
2 1
1 2
输出 1

输入
4 4
1 2
1 4
2 4
1 4
输出 2

输入
5 7
1 2
2 3
3 5
1 4
4 3
4 5
3 1
输出 4
"""
"""https://codeforces.com/contest/1693/submission/207136188

根据题意，从某个点移动时，我们实际上是走的一条「最差」的边，使得花费最多的操作次数到达终点。
注意在描述这个性质时，是用「到终点的操作次数」来描述的，因此以终点为主体来思考。
设从 i 到 n 的最短路长度为 dis[i]。

性质 1：对于一个点 v，假设它有邻居 w1,w2,w3，且 dis[w1] <= dis[w2] <= dis[w3]，那么删边时，肯定是优先删除最大的 v-w3 这条边。
性质 2：如果删除的多，那么总的操作次数也多。如果删除的少，那么走最差的边，总的操作次数也多。
那么干脆枚举删除了多少条边。
难道每次枚举都要重新计算吗？

设原图为 g，反图为 rg。
设原图上的点 i 的出度为 deg[i]。
借鉴 Dijkstra，在 rg 上，从 n 出发去计算最短路。
在 rg 上从 w1 到达 v 时（首次访问 v），那就相当于在 g 上的 v 删除了 deg[i]-1 条边，然后走剩下的那条边到达 w1。
在 rg 上从 w2 到达 v 时（第二次访问 v），那就相当于在 g 上的 v 删除了 deg[i]-2 条边，然后走剩下的花费时间最多的那条边到达 w2。
为什么这里只需要删除 deg[i]-2 条边呢？因为按照 Dijkstra 算法，在 rg 上从 w2 到达 v，那么走的这条边在 g 上一定是从 v 出发的所有边中第二短的（最短的之前枚举过了），所以只需要删除 deg[i]-2 条边。"""


#    592   ms
def solve():
    n, m = RI()
    rg = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(m):
        u, v = RI()
        deg[u - 1] += 1
        rg[v - 1].append(u - 1)

    dist = [inf] * n
    dist[n - 1] = 0

    h = [(0, n - 1)]
    while h:
        c, u = heappop(h)
        if c > dist[u]: continue
        for v in rg[u]:
            d = c + deg[v]
            if d < dist[v]:
                dist[v] = d
                heappush(h, (d, v))
            deg[v] -= 1
    print(dist[0])


if __name__ == '__main__':
    solve()
    # n, m = RI()
    # rg = [[] for _ in range(n)]
    # deg = [0] * n
    # for _ in range(m):
    #     u, v = RI()
    #     deg[u - 1] += 1
    #     rg[v - 1].append(u - 1)
    #
    # dist = [inf] * n
    # h = [(0, n - 1)]
    # while h:
    #     c, u = heappop(h)
    #     if c > dist[u]: continue
    #     for v in rg[u]:
    #         d = c + deg[v]
    #         if d < dist[v]:
    #             dist[v] = d
    #             heappush(h, (d, v))
    #         deg[v] -= 1
    # print(dist[0])
