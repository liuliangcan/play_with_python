# Problem: B. Planets
# Contest: Codeforces - Codeforces Round 142 (Div. 1)
# URL: https://codeforces.com/contest/229/problem/B
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
from heapq import *
from math import sqrt, gcd, inf

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/229/problem/B

输入 n(2≤n≤1e5) m(0≤m≤1e5) 表示一个 n 点 m 边的无向图（节点编号从 1 开始）。
然后输入 m 条边，每条边包含 3 个数 a b c(1≤c≤1e4)，表示有一条边权为 c 的无向边连接 a 和 b，表示从 a 到 b 需要 c 秒。
保证无自环、无重边。
然后输入 n 行，每行第一个数 k 表示数组 t[i] 的长度，然后输入数组 t[i]。
数组 t[i] 是一个严格递增序列，0≤t[i][j]<1e9。
所有 k 之和 ≤1e5。

初始时间为 0。你从 1 出发，要去 n。
如果你在点 i，但是当前时间在数组 t[i] 中，那么你必须等待 1 秒。如果下一秒仍然在 t[i] 中，那么继续等待 1 秒。依此类推。
输出到达 n 的最早时间。
如果无法到达 n，输出 -1。

【易错题】
输入
4 6
1 2 2
1 3 3
1 4 8
2 3 4
2 4 5
3 4 3
0
1 3
2 3 4
0
输出 7

输入
3 1
1 2 3
0
1 3
0
输出 -1
"""
"""其实就是dij最短路，但每个节点都有一些时间不能走，那么到达这个节点后，看看最早什么时候能走即可。
由于dij只会访问每个节点一次，因此可以暴力递增，inc最多1e5次
也可以dp预处理每个ban时间下，最早什么时候可以走，倒序dp即可。显然t[-1]能走的时间是t[-1]+1.但预处理实际上也要1e5次，还得建哈希表，不如暴力。
"""

#    1184   ms
def solve():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = RI()
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    t = []
    for _ in range(n):
        _, *ban = RI()
        t.append(set(ban))
    h = [(0, 0)]
    dist = [inf] * n
    dist[0] = 0
    while h:
        d, u = heappop(h)
        if d > dist[u]:
            continue
        if u == n - 1:
            return print(d)
        while d in t[u]:  # 根据y总的说法，dij只会访问每个点1次，因此这里总复杂度不超过sum(k)<=1e5
            d += 1
        for v, w in g[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heappush(h, (d + w, v))
    print(-1)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
