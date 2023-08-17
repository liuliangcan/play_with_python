# Problem: E - Pac-Takahashi
# Contest: AtCoder - パナソニックグループプログラミングコンテスト2023（AtCoder Beginner Contest 301）
# URL: https://atcoder.jp/contests/abc301/tasks/abc301_e
# Memory Limit: 1024 MB
# Time Limit: 5000 ms

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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
MOD = 10 ** 9 + 7
PROBLEM = """给一个m行n列的矩阵，其中矩阵的每个位置：
'S' 代表起始位置
'G' 代表目标位置
'#' 代表墙
'.' 代表路
'o' 代表这个位置有糖果。题目保证最多有18个糖果。
1<=m,n<=300。
问在t步内，是否能到达终点。若能，最多能收集多少个糖果。
"""
"""据说是两个非常裸的典拼到一起。但第二个我真不会，这次算学学。
- 注意到糖果最多只有18个，考虑18次bfs/状态压缩。
- 然而这题这两步都要做。
- 容易想到，从起始位置尝试经过1个糖果，再去下一个糖果..最终到达目标位置。
- 这样就要先计算出每个糖果到彼此的距离，以及到终点的距离。
1. 把(所有糖果+起始位置)它们互相之间的距离都计算出来，这个可以算20次最短路。（朴素bfs即可，因为权是1.
2. 对这20个位置状压，进行一个状压DP
    - 定义:f[mask][j]代表在状态mask下，最终到达j点的最短步数。其中mask第i为是1代表去过i位置。
    - 转移:从小到大刷表，每次对mask的每一个1，尝试从这个1(第j位)到达一个不在mask中的位置k，则可以更新mask|k的状态为f[mask][j] + dis[j][k]
    - 初始:令第0位是起始，第1位是终点，那么f[1][0]=0,即访问过0位置，且在0位置需要的步数为0.
    - 答案:对每个状态，若它终点为1的步数<=t,则可以尝试这个方案，mask.bit_count()-2,因为有2个位置是起始结束。
"""


#   1378      ms
def solve():
    n, m, t = RI()
    g = []  # 存地图
    oo = []  # 存糖果位置
    st = en = None  # 存起止
    for i in range(n):
        s, = RS()
        g.append(s)
        for j, c in enumerate(s):
            if c == 'S':
                st = (i, j)
            elif c == 'G':
                en = (i, j)
            elif c == 'o':
                oo.append((i, j))
    co = [st, en] + oo  # 编码糖果和起止
    ln = len(co)  # 最多共20个位置
    dis = [[t+1] * ln for _ in range(ln)]  # 每个位置到互相的距离，邻接矩阵dis[i][j]代表从位置i到j的步数;inf可以用t+1代替

    def bfs(i):  # 计算第i个节点到其它节点最短路，计算20次，构建所有位置的理解矩阵
        x, y = co[i]
        d = [[t+1] * m for _ in range(n)]  # inf可以用t+1代替
        d[x][y] = 0
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            c = d[x][y] + 1
            for a, b in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= a < n and 0 <= b < m and g[a][b] != '#':
                    if c < d[a][b]:
                        d[a][b] = c
                        q.append((a, b))
        for j, (x, y) in enumerate(co):  # 给邻接矩阵赋值
            dis[i][j] = d[x][y]

    for i in range(ln):
        bfs(i)
    if dis[0][1] > t:  # t步到不了终点
        return print(-1)

    mask = 1 << ln
    f = [[t+1] * mask for _ in range(ln)]  # f[i][j]代表状态j时，最后到达节点i的最短步数
    f[0][1] = 0  # 起始在0，状态是1,  0步
    for i in range(1, mask):
        if not i & 1: continue
        ones, zeros = [], []
        for j in range(ln):  # 因为要从当前状态的一个结束为止转移到不在当前状态的位置里，为了避免ln*ln,把两种位置先拆出来。
            if i >> j & 1:
                ones.append(j)
            else:
                zeros.append(j)

        for j in ones:  # 从j出发，尝试到达其他位置
            # if f[j][i] < inf:  # 只有这个状态可达，才枚举从它向别的走：比如状态'11'，无法从位置0走
            if f[j][i] < t:  # 只有这个状态可达，才枚举从它向别的走：比如状态'11'，无法从位置0走;其实超过t后边的就不用讨论了哈哈
                for k in zeros:
                    f[k][i | (1 << k)] = min(f[k][i | (1 << k)], f[j][i] + dis[j][k])

    ans = 0
    for i in range(mask):  # 枚举所有状态里，结束位置是终点的，且它的最短路在t内，则答案就是状态里的糖果数
        if f[1][i] <= t:
            ans = max(ans, bin(i).count('1') - 2)  # 注意从i状态里减去起止位置
    print(ans)

#    4000   ms
def solve1():
    m, n, t = RI()
    g = []
    cnt = 2
    cc = {}
    for i in range(m):
        s, = RS()
        g.append(s)
        for j, c in enumerate(s):
            if c == 'S':
                sx, sy = i, j
            elif c == 'G':
                gx, gy = i, j
            elif c == 'o':
                cc[(i, j)] = cnt
                cnt += 1
    cc[(sx, sy)] = 0
    cc[(gx, gy)] = 1
    dis = [[inf] * cnt for _ in range(cnt)]

    # print(1)
    def inside(x, y):
        return 0 <= x < m and 0 <= y < n and g[x][y] != '#'

    def bfs(x, y):
        u = cc[x, y]
        dist = [[10**9] * n for _ in range(m)]
        dist[x][y] = 0
        q = deque([(x, y)])
        while q:
            # print(q)
            x, y = q.popleft()
            d = dist[x][y]
            if (x, y) in cc:
                v = cc[x, y]
                dis[u][v] = d
            d += 1
            for dx, dy in DIRS:
                a, b = x + dx, y + dy
                if inside(a, b) and dist[a][b] > d :
                    dist[a][b] = d
                    q.append((a, b))

    for x, y in cc:
        bfs(x, y)
    if dis[0][1] > t:
        return print(-1)
    # print(dis)
    # 有cnt个点，给出他们分别到达彼此的距离，问从0最终到1的每种方案的最短距离。
    f = [[10 ** 9] * (1 << cnt) for _ in range(cnt)]  # f[i][j] 代表在状态i最后位置是j需的步数
    f[0][1] = 0  # 一开始站在位置0上，这个状态是1。
    for i in range(1 << cnt):
        for j in range(cnt):  # i状态里有j这个点，尝试从j出发
            if i >> j & 1:
                for k in range(cnt):
                    if i >> k & 1: continue  # k不在i里，那么从j到k
                    f[k][i | (1 << k)] = min(f[k][i | (1 << k)], f[j][i] + dis[j][k])
    ans = 0
    for i in range(1 << cnt):
        if f[1][i] <= t:
            ans = max(ans, bin(i).count('1')-2)
    print(ans)


"""[
[0, 2, 1, 3],
[2, 0, 3, 1], 
[1, 3, 0, 4], 
[3, 1, 4, 0]
]"""
if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
