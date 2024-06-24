# Problem: G - Sum of Tree Distance
# Contest: AtCoder - UNIQUE VISION Programming Contest 2024 Summer (AtCoder Beginner Contest 359)
# URL: https://atcoder.jp/contests/abc359/tasks/abc359_g
# Memory Limit: 1024 MB
# Time Limit: 4000 ms

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


# 543ms
def solve():
    n, = RI()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)
    a = [0] + RILST()
    fa = [0] * (n + 1)  # 父节点，0表示无父节点
    size = [1] * (n + 1)  # 子树大小
    son = [0] * (n + 1)  # 重儿子，0表示无儿子
    dfn = [0] * (n + 1)  # dfs序，子树终点的dfs序是dfn[i]+size[i]-1
    rank = [0] * (n + 1)  # dfs序为i的节点编号
    depth = [0] * (n + 1)
    st = [(1, 0)]
    tot = 1
    d = [0] * (n + 1)
    while st:  # 第一次dfs：求fa\depth\size\hson
        u, p = st.pop()
        d[u] = p ^ a[u]
        dfn[u] = tot
        rank[tot] = u  # 临时算一个非重儿子优先的dfn序，用于自底向上计算size
        tot += 1
        for v in g[u]:
            if v == fa[u]: continue
            fa[v] = u  # 父节点
            depth[v] = depth[u] + 1
            st.append((v, d[u]))
    for u in rank[:0:-1]:  # 自底向上
        for v in g[u]:
            if v == fa[u]: continue
            size[u] += size[v]
            if size[v] > size[son[u]]: son[u] = v  # 更新重儿子
    cnt, deep = [0] * (n + 1), [0] * (n + 1)
    # c, d = Counter(), Counter()
    ans = 0
    st = [(1, False, True)]  # root,是否keep贡献(重儿子),入栈标记
    while st:
        u, keep, in_ = st.pop()
        if in_:
            st.append((u, keep, False))  # 注册自己的出栈动作
            if son[u]:
                st.append((son[u], True, True))  # 重儿子先入栈，后出栈处理
            for v in g[u]:
                if son[u] != v != fa[u]:
                    st.append((v, False, True))  # 轻儿子先处理
        else:
            for v in g[u]:  # 处理所有轻儿子的贡献
                if son[u] != v != fa[u]:
                    for i in range(dfn[v], dfn[v] + size[v]):
                        x = rank[i]
                        c = a[x]
                        ans += (depth[x] - depth[u]) * cnt[c] + (deep[c] - cnt[c] * depth[u])

                    for i in range(dfn[v], dfn[v] + size[v]):
                        x = rank[i]
                        c = a[x]
                        deep[c] += depth[x]
                        cnt[c] += 1
            c = a[u]
            ans += deep[c] - cnt[c] * depth[u]
            cnt[c] += 1
            deep[c] += depth[u]
            if not keep:
                for i in range(dfn[u], dfn[u] + size[u]):
                    x = rank[i]
                    c = a[x]
                    deep[c] -= depth[x]
                    cnt[c] -= 1

    print(ans)


#   1251    ms
def solve1():
    n, = RI()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)
    a = [0] + RILST()
    cnt, deep = [Counter() for _ in range(n + 1)], [Counter() for _ in range(n + 1)]

    st = [(1, 0, True, 0)]  # root,fa,入栈标记,节点深度
    ans = 0
    while st:
        u, fa, in_, depth = st.pop()
        if in_:
            st.append((u, fa, False, depth))  # 注册自己的出栈动作
            for v in g[u]:
                if v != fa:
                    st.append((v, u, True, depth + 1))  #
        else:
            cnt[u][a[u]] += 1
            deep[u][a[u]] += depth
            for v in g[u]:
                if v != fa:
                    if len(cnt[u]) < len(cnt[v]):
                        cnt[u], cnt[v] = cnt[v], cnt[u]
                        deep[u], deep[v] = deep[v], deep[u]
                    for x, y in deep[v].items():
                        ans += cnt[u][x] * (y - cnt[v][x] * depth) + cnt[v][x] * (deep[u][x] - cnt[u][x] * depth)
                        cnt[u][x] += cnt[v][x]
                        deep[u][x] += y

    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
