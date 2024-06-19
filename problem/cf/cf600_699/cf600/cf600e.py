# Problem: E. Lomsat gelral
# Contest: Codeforces - Educational Codeforces Round 2
# URL: https://codeforces.com/problemset/problem/600/e
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
PROBLEM = """
"""


class HLD:
    def __init__(self, g, root):
        # 无论是点还是dfn\rank还是dep，都从1开始，默认0是无
        n = len(g) - 1
        self.g = g
        self.fa = fa = [0] * (n + 1)  # 父节点，0表示无父节点
        self.size = size = [1] * (n + 1)  # 子树大小
        self.dep = dep = [0] * (n + 1)  # 深度，根深度为1
        self.son = son = [0] * (n + 1)  # 重儿子，0表示无儿子
        self.dfn = dfn = [0] * (n + 1)  # dfs序，子树终点的dfs序是dfn[i]+size[i]-1
        self.top = top = list(range(n + 1))  # 所在重链起点，起点就是自己
        self.rank = rank = [0] * (n + 1)  # dfs序为i的节点编号
        # self.is_heavy = [0] * (n + 1)
        # self.is_heavy[root] = 1
        size[0] = 0
        st = [root]
        dep[root] = 1
        tot = 1
        while st:  # 第一次dfs：求fa\depth\size\hson
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
                # self.is_heavy[son[u]] = 1

        for u in rank[1:]:  # 自上而下更新链起点  第二次dfs：求top\优先访问重儿子的dfn\rank
            for v in g[u]:
                if v == son[u]: top[v] = top[u]
        st = [root]
        tot = 1
        while st:  # 重新计算以重儿子优先的dfn序（可能有用）
            u = st.pop()
            dfn[u] = tot
            rank[tot] = u
            tot += 1
            if son[u] == 0: continue  # 叶子
            for v in g[u]:
                if v != fa[u] and v != son[u]: st.append(v)
            st.append(son[u])

    def lca(self, u, v):  # 求u和v的最近公共祖先节点,复杂度lgn
        fa = self.fa
        dep = self.dep
        top = self.top
        while top[u] != top[v]:
            if dep[top[u]] > dep[top[v]]:
                u = fa[top[u]]
            else:
                v = fa[top[v]]
        return v if dep[u] > dep[v] else u

    def get_route(self, u, v):
        """获取简单路径u-v的重链剖分，返回不超过O(lgn)段区间[l,r],其中lr均为1~n,代表dfn[i]"""
        fa = self.fa
        dep = self.dep
        top = self.top
        dfn = self.dfn
        ans = []
        while top[u] != top[v]:
            if dep[top[u]] < dep[top[v]]: u, v = v, u
            ans.append((dfn[top[u]], dfn[u]))
            u = fa[top[u]]
        x, y = dfn[u], dfn[v]
        ans.append((x, y) if x <= y else (y, x))
        return ans

    def dis(self, u, v):
        dep = self.dep
        return dep[u] + dep[v] - 2 * dep[self.lca(u, v)]


#       ms
def solve():
    n, = RI()
    a = [0] + RILST()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)

    hld = HLD(g, 1)
    rank, fa, dfn, son, size = hld.rank, hld.fa, hld.dfn, hld.son, hld.size
    cnt = [0] * (n + 1)  # cnt 颜色计数
    mx = cur = 0  # 当前最多的颜色是谁
    ans = [0] * (n + 1)

    def add(u):
        nonlocal mx, cur
        c = a[u]
        cnt[c] += 1
        if cnt[c] > mx:
            mx = cnt[c]
            cur = c
        elif cnt[c] == mx:
            cur += c

    def delete(u):
        c = a[u]
        cnt[c] -= 1

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
                        add(rank[i])
            add(u)

            ans[u] = cur
            if not keep:  # 如果本子树是轻儿子，那就移除贡献
                for i in range(dfn[u], dfn[u] + size[u]):
                    delete(rank[i])
                mx = cur = 0
    print(*ans[1:])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
