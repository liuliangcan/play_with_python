# Problem: E. Tree Painting
# Contest: Codeforces - Educational Codeforces Round 67 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1187/E
# Memory Limit: 256 MB
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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1187/E

输入 n(2≤n≤2e5) 表示一棵有 n 个节点的无向无根树，然后输入这棵树的 n-1 条边（节点编号从 1 开始）。

一开始，所有节点都是白色的。
第一回合，你可以随便选一个节点，并把它涂成黑色，得到 n 分。
在接下来的 n-1 个回合中，每回合，选择一个与黑色节点相邻的白色节点。设该白色节点所在的白色连通块的大小为 k，你会先得到 k 分，然后把该白色节点涂成黑色。

输出最大得分和。
输入
9
1 2
2 3
2 5
2 6
1 4
4 9
9 7
9 8
输出 36

输入
5
1 2
1 3
2 4
2 5
输出 14
"""


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


#    1111   ms
def solve1():
    n, = RI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    cnt = [1] * n
    down = [0] * n

    @bootstrap
    def dfs(u, fa):
        for v in g[u]:
            if v == fa: continue
            yield dfs(v, u)
            cnt[u] += cnt[v]
            down[u] += down[v]
        down[u] += cnt[u]
        yield

    dfs(0, -1)

    @bootstrap
    def reroot(u, fa):
        for v in g[u]:
            if v == fa: continue
            down[v] = down[u] - cnt[v] + n - cnt[v]
            yield reroot(v, u)
        yield

    reroot(0, -1)
    print(max(down))


#  514     ms
def solve():
    n, = RI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    fa = [-1] * n
    order = []
    q = [0]
    while q:
        u = q.pop()
        order.append(u)
        for v in g[u]:
            if v == fa[u]:
                continue
            fa[v] = u
            q.append(v)

    cnt = [1] * n
    down = [0] * n

    for u in order[::-1]:
        for v in g[u]:
            if v == fa[u]: continue
            cnt[u] += cnt[v]
            down[u] += down[v]
        down[u] += cnt[u]

    for u in order:
        for v in g[u]:
            if v == fa[u]: continue
            down[v] = down[u] - cnt[v] + n - cnt[v]

    print(max(down))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
