# Problem: F - Exactly K Steps
# Contest: AtCoder - NEC Programming Contest 2022 (AtCoder Beginner Contest 267)
# URL: https://atcoder.jp/contests/abc267/tasks/abc267_f
# Memory Limit: 1024 MB
# Time Limit: 2000 ms
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
from types import GeneratorType

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc267/tasks/abc267_f

输入 n(≤2e5) 和一棵树的 n-1 条边（节点编号从 1 开始）。
然后输入 q(≤2e5) 和 q 个询问，每个询问输入 u 和 k。
输出到 u 的距离为 k 的任意一个点。如果这个点不存在则输出 -1。
距离指两点最短路上的边的数目。
输入
5
1 2
2 3
3 4
3 5
3
2 2
5 3
3 3
输出
4
1
-1
"""
"""https://atcoder.jp/contests/abc267/submissions/37595672

求出树的任意一条直径，设直径端点为 x 和 y。

从 x 出发 dfs，同时记录 dfs 路径上的点。
如果点 u 的深度 d >= k，那么 dfs 路径上的第 d-k 个点就是答案。

一次 dfs 不一定能满足所有点，再从 y 出发 dfs 一次就能保证所有点都有答案（除了 k 非常大的）。
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


# 1629 ms
if __name__ == '__main__':
    n, = RI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    q, = RI()
    qs = defaultdict(list)
    for i in range(q):
        u, d = RI()
        qs[u - 1].append([i, d])
    ans = [-1] * q

    leaf = mx = 0
    path = [-1] * n


    @bootstrap
    def dfs(u, fa, d=0):
        path[d] = u
        global leaf, mx
        if d > mx:
            leaf = u
            mx = d
        for i, k in qs[u]:
            if d >= k:
                ans[i] = path[d - k] + 1
        for v in g[u]:
            if v != fa:
                yield dfs(v, u, d + 1)
        yield


    for _ in range(3):
        dfs(leaf, -1)

    print('\n'.join(map(str, ans)))

# # 1423 ms
# if __name__ == '__main__':
#     n, = RI()
#     g = [[] for _ in range(n)]
#     for _ in range(n - 1):
#         u, v = RI()
#         g[u - 1].append(v - 1)
#         g[v - 1].append(u - 1)
#
#
#     def get_tree_diameter(g, root=0):  # bfs两次找直径的端点
#         if not g[root]:
#             return root, root
#
#         def bfs(start):
#             q = deque([(start, -1)])
#             while q:
#                 u, fa = q.popleft()
#                 for v in g[u]:
#                     if v != fa:
#                         q.append((v, u))
#             return u
#
#         x = bfs(root)
#         y = bfs(x)
#         return x, y
#
#
#     x, y = get_tree_diameter(g)
#
#     q, = RI()
#     qs = defaultdict(list)
#     for i in range(q):
#         u, d = RI()
#         qs[u - 1].append([i, d])
#     # print(qs)
#     ans = [-1] * q
#     path = [0] * n  # 当前深度链接到根的路径
#
#
#     @bootstrap
#     def dfs(u, fa, d=0):
#         path[d] = u
#         for i, k in qs[u]:
#             if d >= k:
#                 ans[i] = path[d - k] + 1
#         for v in g[u]:
#             if v != fa:
#                 yield dfs(v, u, d + 1)
#         yield
#
#
#     dfs(x, -1)
#     dfs(y, -1)
#     print('\n'.join(map(str, ans)))

# # 1892ms
# if __name__ == '__main__':
#     n, = RI()
#     g = [[] for _ in range(n)]
#     for _ in range(n - 1):
#         u, v = RI()
#         g[u - 1].append(v - 1)
#         g[v - 1].append(u - 1)
#
#
#     def get_tree_diameter(g, root=0):
#         ans = (0, root, root)
#         if not g[root]:
#             return ans
#
#         dp = {}
#
#         @bootstrap
#         def dfs(u, fa, depth=0):  # 返回树高以及最深的叶子
#             if len(g[u]) == 1 and u != root:  # 没有子节点了，它就是一个端点（叶子），高度1
#                 dp[u] = (1, u)
#                 yield
#
#             hs = []
#             for v in g[u]:
#                 if v != fa:
#                     yield dfs(v, u, depth + 1)
#                     h, o = dp[v]
#                     if len(hs) < 2:
#                         heapq.heappush(hs, (h, o))
#                     else:
#                         heapq.heappushpop(hs, (h, o))
#
#             if len(hs) == 2:
#                 l, r = max((depth, root), hs[0]), hs[1]
#             else:
#                 l, r = (depth, root), hs[0]
#             p = (l[0] + r[0], l[1], r[1])
#             # print(p)
#             nonlocal ans
#             if p > ans:
#                 ans = p
#             dp[u] = (hs[-1][0] + 1, hs[-1][1])
#             yield
#
#         dfs(root, -1)
#         return ans
#
#
#     d, x, y = get_tree_diameter(g)
#
#     q, = RI()
#     qs = defaultdict(list)
#     for i in range(q):
#         u, d = RI()
#         qs[u - 1].append([i, d])
#     # print(qs)
#     ans = [-1] * q
#     path = [0] * n  # 当前深度链接到根的路径
#
#
#     @bootstrap
#     def dfs(u, fa, d=0):
#         path[d] = u
#         for i, k in qs[u]:
#             if d >= k:
#                 ans[i] = path[d - k] + 1
#         for v in g[u]:
#             if v != fa:
#                 yield dfs(v, u, d + 1)
#         yield
#
#
#     dfs(x, -1)
#     dfs(y, -1)
#     print('\n'.join(map(str, ans)))
