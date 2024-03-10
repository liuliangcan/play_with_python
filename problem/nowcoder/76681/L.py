# Problem: 删边游戏
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/76681/L
# Memory Limit: 524288 MB
# Time Limit: 6000 ms

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
PROBLEM = """找割边，然后缩点，然后用割边建树，然后dfs子树和
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

class Tarjan:
    def __init__(self):
        return

    @staticmethod
    def get_scc(n: int, edge):
        assert all(i not in edge[i] for i in range(n))
        assert all(len(set(edge[i])) == len(edge[i]) for i in range(n))
        dfs_id = 0
        order, low = [inf] * n, [inf] * n
        visit = [0] * n
        out = []
        in_stack = [0] * n
        scc_id = 0
        # nodes list of every scc_id part
        scc_node_id = []
        # index if original node and value is scc_id part
        node_scc_id = [-1] * n
        parent = [-1] * n
        for node in range(n):
            if not visit[node]:
                stack = [[node, 0]]
                while stack:
                    cur, ind = stack[-1]
                    if not visit[cur]:
                        visit[cur] = 1
                        order[cur] = low[cur] = dfs_id
                        dfs_id += 1
                        out.append(cur)
                        in_stack[cur] = 1
                    if ind == len(edge[cur]):
                        stack.pop()
                        if order[cur] == low[cur]:
                            while out:
                                top = out.pop()
                                in_stack[top] = 0
                                while len(scc_node_id) < scc_id + 1:
                                    scc_node_id.append(set())
                                scc_node_id[scc_id].add(top)
                                node_scc_id[top] = scc_id
                                if top == cur:
                                    break
                            scc_id += 1

                        cur, nex = parent[cur], cur
                        if cur != -1:
                            low[cur] = low[cur] if low[cur] < low[nex] else low[nex]
                    else:
                        nex = edge[cur][ind]
                        stack[-1][-1] += 1
                        if not visit[nex]:
                            parent[nex] = cur
                            stack.append([nex, 0])
                        elif in_stack[nex]:
                            low[cur] = low[cur] if low[cur] < order[nex] else order[nex]

        # new graph after scc
        new_dct = [set() for _ in range(scc_id)]
        for i in range(n):
            for j in edge[i]:
                a, b = node_scc_id[i], node_scc_id[j]
                if a != b:
                    new_dct[a].add(b)
        new_degree = [0] * scc_id
        for i in range(scc_id):
            for j in new_dct[i]:
                new_degree[j] += 1
        assert len(scc_node_id) == scc_id
        return scc_id, scc_node_id, node_scc_id

    @staticmethod
    def get_pdcc(n: int, edge):

        dfs_id = 0
        order, low = [inf] * n, [inf] * n
        visit = [False] * n
        out = []
        parent = [-1] * n
        # number of group
        group_id = 0
        # nodes list of every group part
        group_node = []
        # index is original node and value is group_id set
        # cut node belong to two or more group
        node_group_id = [set() for _ in range(n)]
        child = [0] * n
        for node in range(n):
            if not visit[node]:
                stack = [[node, 0]]
                while stack:
                    cur, ind = stack[-1]
                    if not visit[cur]:
                        visit[cur] = True
                        order[cur] = low[cur] = dfs_id
                        dfs_id += 1

                    if ind == len(edge[cur]):
                        stack.pop()
                        cur, nex = parent[cur], cur
                        if cur != -1:
                            low[cur] = low[cur] if low[cur] < low[nex] else low[nex]
                            # cut node with rooted or not-rooted
                            if (parent == -1 and child[cur] > 1) or (parent != -1 and low[nex] >= order[cur]):
                                while out:
                                    top = out.pop()
                                    while len(group_node) < group_id + 1:
                                        group_node.append(set())
                                    group_node[group_id].add(top[0])
                                    group_node[group_id].add(top[1])
                                    node_group_id[top[0]].add(group_id)
                                    node_group_id[top[1]].add(group_id)
                                    if top == (cur, nex):
                                        break
                                group_id += 1
                            # We add all the edges encountered during deep search to the stack
                            # and when we find a cut point
                            # Pop up all the edges that this cutting point goes down to
                            # and the points connected by these edges are a pair of dots
                    else:
                        nex = edge[cur][ind]
                        stack[-1][-1] += 1
                        if nex == parent[cur]:
                            continue
                        if not visit[nex]:
                            parent[nex] = cur
                            out.append((cur, nex))
                            child[cur] += 1
                            stack.append([nex, 0])
                        elif low[cur] > order[nex]:
                            low[cur] = order[nex]
                            out.append((cur, nex))
            if out:
                while out:
                    top = out.pop()
                    group_node[group_id].add(top[0])
                    group_node[group_id].add(top[1])
                    node_group_id[top[0]].add(group_id)
                    node_group_id[top[1]].add(group_id)
                group_id += 1
        return group_id, group_node, node_group_id

    def get_edcc(self, n: int, edge):
        _, cutting_edges = self.get_cut(n, [list(e) for e in edge])
        for i, j in cutting_edges:
            edge[i].discard(j)
            edge[j].discard(i)
        # Remove all cut edges and leaving only edge doubly connected components
        # process the cut edges and then perform bfs on the entire undirected graph
        visit = [0] * n
        edcc_node_id = []
        for i in range(n):
            if visit[i]:
                continue
            stack = [i]
            visit[i] = 1
            cur = [i]
            while stack:
                x = stack.pop()
                for j in edge[x]:
                    if not visit[j]:
                        visit[j] = 1
                        stack.append(j)
                        cur.append(j)
            edcc_node_id.append(cur[:])

        # new graph after edcc
        edcc_id = len(edcc_node_id)
        node_edcc_id = [-1]*n
        for i, ls in enumerate(edcc_node_id):
            for x in ls:
                node_edcc_id[x] = i
        new_dct = [[] for _ in range(edcc_id)]
        for i in range(n):
            for j in edge[i]:
                a, b = node_edcc_id[i], node_edcc_id[j]
                if a != b:
                    new_dct[a].append(b)
        new_degree = [0] * edcc_id
        for i in range(edcc_id):
            for j in new_dct[i]:
                new_degree[j] += 1
        return edcc_node_id

    @staticmethod
    def get_cut(n: int, edge):
        order, low = [inf] * n, [inf] * n
        visit = [0] * n
        cutting_point = set()
        cutting_edge = []
        child = [0] * n
        parent = [-1] * n
        dfs_id = 0
        for i in range(n):
            if not visit[i]:
                stack = [[i, 0]]
                while stack:
                    cur, ind = stack[-1]
                    if not visit[cur]:
                        visit[cur] = 1
                        order[cur] = low[cur] = dfs_id
                        dfs_id += 1
                    if ind == len(edge[cur]):
                        stack.pop()
                        cur, nex = parent[cur], cur
                        if cur != -1:
                            pa = parent[cur]
                            low[cur] = low[cur] if low[cur] < low[nex] else low[nex]
                            if low[nex] > order[cur]:
                                cutting_edge.append((cur, nex) if cur < nex else (nex, cur))
                            if pa != -1 and low[nex] >= order[cur]:
                                cutting_point.add(cur)
                            elif pa == -1 and child[cur] > 1:
                                cutting_point.add(cur)
                    else:
                        nex = edge[cur][ind]
                        stack[-1][-1] += 1
                        if nex == parent[cur]:
                            continue
                        if not visit[nex]:
                            parent[nex] = cur
                            child[cur] += 1
                            stack.append([nex, 0])
                        else:
                            low[cur] = low[cur] if low[cur] < order[nex] else order[nex]
        return cutting_point, cutting_edge

#       ms
def solve():
    n, m = RI()
    a = RILST()
    s = sum(a)

    es = []
    for _ in range(m):
        x, y = RI()
        if x > y:
            x, y = y, x
        es.append((x - 1, y - 1))
    g = [[] for _ in range(n)]
    for u, v in es:
        g[u].append(v)
        g[v].append(u)

    ge = set()
    # print(Tarjan.get_cut(n, g))
    for u, v in Tarjan.get_cut(n, g)[-1]:
        if u > v:
            u, v = v, u
        ge.add((u, v))

    if not ge:  # 没有割边，那么删任意边两端都链接全部
        return print(s * s, s * s)

    fa = list(range(n))
    sm = a[:]  # 缩点之后的价值

    def find(x):
        t = x
        while fa[x] != x:
            x = fa[x]
        while t != x:
            fa[t], t = x, fa[t]
        return x

    mx = 0
    for u, v in es:  # 割边以外的点缩起来
        if (u, v) in ge: continue
        u, v = find(u), find(v)
        if u != v:
            fa[v] = u
            sm[u] += sm[v]
            sm[v] = 0
        mx = s * s  # 有非割边，mx就是s*s

    mn = inf
    g = [[] for _ in range(n)]
    for u, v in ge:  # 用割边建树
        u, v = find(u), find(v)
        g[u].append(v)
        g[v].append(u)
        start = u  # 起点

    f = [0] * n

    @bootstrap
    def dfs(u, fa):
        f[u] = sm[u]
        nonlocal mn, mx
        for v in g[u]:
            if v == fa:
                continue
            yield dfs(v, u)
            mn = min(mn, f[v] * (s - f[v]))
            mx = max(mx, f[v] * (s - f[v]))
            f[u] += f[v]
        yield

    dfs(start, -1)
    print(mn, mx)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
