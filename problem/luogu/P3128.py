# Problem: P3128 [USACO15DEC] Max Flow P
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P3128
# Memory Limit: 125 MB
# Time Limit: 1000 ms

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
PROBLEM = """
"""

class HLD:
    def __init__(self, g, root):
        # 无论是点还是dfn还是dep，都从1开始，默认0是无
        n = len(g)-1
        self.g = g
        self.fa = fa = [0] * (n + 1)  # 父节点，0表示无父节点
        self.size = size = [1] * (n + 1)  # 子树大小
        self.dep = dep = [0] * (n + 1)  # 深度，根深度为1
        self.son = son = [0] * (n + 1)  # 重儿子，0表示无儿子
        self.dfn = dfn = [0] * (n + 1)  # dfs序，子树终点的dfs序是dfn[i]+size[i]-1
        self.top = top = list(range(n + 1))  # 所在重链起点，起点就是自己
        self.rank = rank = [0] * (n + 1)  # dfs序为i的节点编号
        size[0] = 0
        st = [root]
        dep[root] = 1
        tot = 1
        while st:
            u = st.pop()
            rank[tot] = u  # 临时算一个非重儿子优先的dfn序，用于自底向上计算size
            tot += 1
            for v in g[u]:
                if v == fa[u]: continue
                fa[v] = u  # 父节点
                dep[v] = dep[u] + 1  # 深度
                st.append(v)
        for u in rank[:0:-1]:  # 自底向上
            for v in g[u]:
                if v == fa[u]: continue
                size[u] += size[v]
                if size[v] > size[son[u]]: son[u] = v  # 更新重儿子

        for u in rank[1:]:  # 自上而下更新链起点
            for v in g[u]:
                if v == son[u]: top[v] = top[u]
        st = [root]
        tot = 1
        while st:  # 重新计算以重儿子优先的dfn序
            u = st.pop()
            dfn[u] = tot
            rank[tot] = u
            tot += 1
            if son[u] == 0: continue  # 叶子
            for v in g[u]:
                if v != fa[u] and v != son[u]: st.append(v)
            st.append(son[u])


    def lca(self, u, v):  # 求u和v的最近公共祖先节点
        fa = self.fa
        size = self.size
        dep = self.dep
        son = self.son
        dfn = self.dfn
        top = self.top
        rank = self.rank
        while top[u] != top[v]:
            if dep[top[u]] > dep[top[v]]:
                u = fa[top[u]]
            else:
                v = fa[top[v]]
        return v if dep[u] > dep[v] else u

    def dis(self, u, v):
        dep = self.dep
        return dep[u] + dep[v] - 2 * dep[self.lca(u, v)]




class DiffOnTreePoint:
    """点差分 u~v简单路上所有边权+=x, o=lca(u,v), p = parent[o]
    diff[u]+=x,
    diff[v]+=x,
    diff[o]-=x,
    diff[p]-=x;"""

    def __init__(self, g, root=1, lca=None, a=None):  # 注意节点编号是1-indexed
        self.n = n = len(g)-1
        self.lca = lca or HLD(g, root)  # 不传就重新算
        self.diff = [0] * (n + 1)  # 树上差分,用0作为根的父节点
        self.a = a[:] if a else [0] * (n+1)  # 传了就用它初始化；默认不修改，去掉切片则直接改
        self.rank = lca.rank
        self.fa = lca.fa  # 用0作为根的父节点
        self.g = g


    def add_route(self, u, v, w):
        """把u~v简单路径上的所有点权+w"""
        self.diff[u] += w
        self.diff[v] += w
        o = self.lca.lca(u, v)
        self.diff[o] -= w
        self.diff[self.fa[o]] -= w

    def get_all_point_w(self):  #
        d = self.diff[:]
        for u in self.rank[:0:-1]:
            for v in self.g[u]:
                if v == self.fa[u]: continue
                d[u] += d[v]
            self.a[u] += d[u]
        # print(self.a)
        return self.a  # self.a[u]表示u的点权


#       ms
def solve():
    n, k = RI()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)
    diff = DiffOnTreePoint(g, 1, HLD(g, 1))
    for _ in range(k):
        u, v = RI()
        diff.add_route(u, v, 1)
    ans = max(diff.get_all_point_w())

    print(ans)


def solve2():
    n, k = RI()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)
    hld = HLD(g, 1)

    fa = hld.fa
    diff = [0] * (n + 1)
    for _ in range(k):
        u, v = RI()
        diff[u] += 1
        diff[v] += 1
        o = hld.lca(u, v)
        diff[o] -= 1
        diff[fa[o]] -= 1

    for u in hld.rank[:0:-1]:
        for v in g[u]:
            if v == fa[u]: continue
            diff[u] += diff[v]

    print(max(diff))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
