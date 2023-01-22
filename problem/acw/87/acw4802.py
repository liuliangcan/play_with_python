# Problem: 最远距离
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4802/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
# ACW没有comb
# from math import sqrt, gcd, inf, comb
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """我们规定，如果一个无向连通图满足去掉其中的任意一条边都会使得该图变得不连通，则称该图为有效无向连通图。

给定一个 n 个点 m 条边的有效无向连通图，点的编号为 1∼n，所有边的长度均为 1。

两点之间的距离定义为两点之间的最短距离。

请你计算，给定图中距离最远的两个点之间的距离。

输入格式
第一行包含两个整数 n,m。

接下来 m 行，每行包含两个整数 a,b，表示点 a 和点 b 之间存在一条无向边。

输出格式
一个整数，表示给定图中距离最远的两个点之间的距离。

数据范围
前三个测试点满足 1≤n,m≤10。
所有测试点满足 1≤n,m≤105，1≤a,b≤n，a≠b。

输入样例1：
4 3
1 2
1 3
1 4
输出样例1：
2
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


#    4994    ms
def solve2():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    start = 0
    ans = 0
    for _ in range(2):
        @bootstrap
        def dfs(u, fa, depth=0):
            nonlocal ans, start
            if depth > ans:
                start = u
                ans = depth
            for v in g[u]:
                if v != fa:
                    yield dfs(v, u, depth + 1)
            yield

        dfs(start, -1)

    print(ans)


#   3618    ms
def solve1():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    start = 0
    ans = 0
    for _ in range(2):
        q = deque([start])
        fas = [-1] * n
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                u = q.popleft()
                start = u
                for v in g[u]:
                    fas[v] = u
                    if v != fas[u]:
                        q.append(v)
        ans = max(ans, step)
    print(ans - 1)


#    3917     ms
def solve3():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    def get_tree_diameter(g, root=0):  # bfs两次找直径的端点
        """
        求树的直径，g是0-indexed，默认第一次root是从0
        返回某条直径的两个端点u,v，以及直径值d(边数而不是点数)
        简述:求树的直径时，可以通过树形DP做，也可以通过两次遍历找最远的点(bfs或dfs都可以)
            第二次的起始点就是某条直径的端点
        """
        if not g[root]:
            return root, root, 0

        def bfs(start):
            q = deque([(start, -1)])
            step = -1
            while q:
                step += 1
                for _ in range(len(q)):
                    u, fa = q.popleft()
                    for v in g[u]:
                        if v != fa:
                            q.append((v, u))
            return u, step

        x, _ = bfs(root)
        y, d = bfs(x)
        return x, y, d

    _, _, ans = get_tree_diameter(g)

    print(ans)


#   3918     ms
def solve4():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    def get_tree_diameter(g, root=0):  # bfs两次找直径的端点
        """
        求树的直径，g是0-indexed，默认第一次root是从0
        返回直径值(边数而不是点数)
        简述:树形dp,树的直径一定是以某个端点为根的子树，它的左右两条最长的简单路径求和。那么转移时提前和最大兄弟节点加一下即可。
        """
        if not g[root]:
            return 0
        ans = 0
        f = [0] * n  # f[u]是以u为根节点的子树的高(最大深度)

        @bootstrap
        def dfs(u, fa):
            nonlocal ans
            mx = 0
            for v in g[u]:
                if v != fa:
                    yield dfs(v, u)
                    cur = f[v]
                    if ans < cur + mx:
                        ans = cur + mx
                    if mx < cur:
                        mx = cur
            f[u] = mx + 1
            yield

        dfs(root, -1)
        return ans

    def get_tree_diameter_dfs(g, root=0):  # bfs两次找直径的端点
        """
        求树的直径，g是0-indexed，默认第一次root是从0
        返回直径值(边数而不是点数)
        简述:树形dp,树的直径一定是以某个端点为根的子树，它的左右两条最长的简单路径求和。那么转移时提前和最大兄弟节点加一下即可。
        """
        if not g[root]:
            return 0
        ans = 0

        def dfs(u, fa):
            nonlocal ans
            mx = 0
            for v in g[u]:
                if v != fa:
                    cur = dfs(v, u)
                    ans = max(ans, cur + mx)
                    mx = max(mx, cur)
            return mx + 1

        dfs(root, -1)
        return ans

    print(get_tree_diameter_dfs(g))


#  换根dp   4122    ms
def solve():
    n, m = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    def get_tree_diameter(g, root=0):  # bfs两次找直径的端点
        """ ms
        求树的直径，g是0-indexed，默认第一次root是从0
        返回直径值(边数而不是点数)
        简述:换根dp，假设直径两端是u,v，那么以u为树根，v一定是最远节点，求最大树高即可。
        """
        if not g[root]:
            return 0
        down1, down2, up = [0] * n, [0] * n, [0] * n  # 初始化向下最大/次大树高、向上树高(其实不是树高，是最远简单路径)
        order = []  # dp序
        fas = [-1] * n  # 记录父节点
        q = deque([root])  # bfs求order
        while q:
            u = q.popleft()
            order.append(u)
            for v in g[u]:
                if v != fas[u]:
                    fas[v] = u
                    q.append(v)

        for u in order[::-1]:  # 第一遍，自底向上求每个子树的最大/次大树高
            for v in g[u]:
                if v == fas[u]:
                    continue
                h = down1[v] + 1  # 高度
                if h > down1[u]:
                    down1[u], down2[u] = h, down1[u]
                elif h > down2[u]:
                    down2[u] = h
        for u in order:
            for v in g[u]:
                if v == fas[u]:
                    continue
                if down1[u] == down1[v] + 1:  # v在u的最大路径上，则往上的路径应该可能从次大走
                    up[v] = max(down2[u], up[u]) + 1
                else:  # 否则一定从最大走
                    up[v] = max(down1[u], up[u]) + 1

        return max(max(x, y) for x, y in zip(down1, up))

    print(get_tree_diameter(g))


if __name__ == '__main__':
    solve()
