# Problem: 七夕
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/63746/B
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """链接：https://ac.nowcoder.com/acm/contest/63746/B

七夕节左近，楚楚想去见女朋友，可是他最近和女朋友吵架了，女朋友躲着他，不知道会出现在哪座城市里。楚楚心知肚明女朋友是在赌气，所以无论自己在哪座城市，女朋友在哪座城市，
他一定要在七夕节见到她。城市之间用铁路或者城际公交中的一种相连通，虽然并不是任意两个城市都直接相连，但是保证可以通过这两种交通方式从任一城市出发到另一任意城市。
由于楚楚的特殊身份，他可以免费乘坐城际公交，那么他最少需要买多少张火车票才能保证见到女朋友呢？
输入描述:
第一行三个整数n，k，m，表示共n个城市，编号从1到n，k条城际，m条铁路。
接下来k行，每行两个整数u、v，表示城市u、v之间有城际。
再接下来m行，每行两个整数u、v，表示城市u、v之间有铁路。

输出描述:
一个整数表示还需要的票数。
输入
6 3 4
1 2
2 3
4 5
1 3
3 4
4 6
5 6

输出
2
"""


#       ms
def solve():
    n, k, m = RI()
    fa = list(range(n))

    def find(x):
        t = x
        while x != fa[x]:
            x = fa[x]
        while t != x:
            t, fa[t] = fa[t], x
        return x

    for _ in range(k):  # 读k个城际，缩点
        u, v = RI()
        u, v = find(u - 1), find(v - 1)
        fa[u] = v

    g = [[] for _ in range(n)]
    for _ in range(m):  # 读m个铁道，给代表元建图；重边和自环都不管，直接建
        u, v = RI()
        u, v = find(u - 1), find(v - 1)
        g[u].append(v)
        g[v].append(u)

    def bfs(st):  # 层序遍历
        q = [st]
        vis = [0] * n
        vis[st] = 1
        step = 0
        while q:
            nq = []
            step += 1
            for u in q:
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = 1
                        nq.append(v)
            q = nq
        return u, step - 1  # 两次bfs求图的直径，就是max(最短路)

    st, _ = bfs(find(0))  # 第一次bfs求直径的一段
    _, ans = bfs(st)  # 第二次bfs求直径长度
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
