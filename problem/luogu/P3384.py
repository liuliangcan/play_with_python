# Problem: P3384 【模板】重链剖分/树链剖分
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P3384
# Memory Limit: 128 MB
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


class BinIndexTreeRURQ:
    """树状数组的RURQ模型"""

    def __init__(self, size_or_nums):  # 树状数组,区间加区间求和，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.d = [0 for _ in range(self.size + 5)]
            self.d2 = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.d = [0 for _ in range(self.size + 5)]
            self.d2 = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_interval(i + 1, i + 1, v)

    def _add_point(self, c, i, v):  # 单点增加,下标从1开始;不支持直接调用，这里增加的是差分数组的单点,同步修改c2
        while i <= self.size:
            c[i] += v
            c[i]%=MOD
            i += -i & i

    def _sum_prefix(self, c, i):  # 前缀求和，下标从1开始；不支持直接调用，这里求和的是差分数组的前缀和;传入c决定怎么计算，但是不要直接调用 无视吧
        s = 0
        while i >= 1:
            s += c[i]
            s %= MOD
            i -= -i & i
        return s

    def add_interval(self, l, r, v):  # 区间加，下标从1开始，把[l,r]闭区间都加v
        self._add_point(self.d, l, v)
        self._add_point(self.d, r + 1, -v)
        self._add_point(self.d2, l, (l - 1) * v)
        self._add_point(self.d2, r + 1, -v * r)

    def sum_interval(self, l, r):  # 区间求和，下标从1开始，返回闭区间[l,r]上的求和
        return self._sum_prefix(self.d, r) * r - self._sum_prefix(self.d2, r) - self._sum_prefix(self.d, l - 1) * (
                l - 1) + self._sum_prefix(self.d2, l - 1)

    def query_point(self, i):  # 单点询问值，下标从1开始，返回i位置的值
        return self._sum_prefix(self.d, i)

    def lowbit(self, x):
        return x & -x


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
    n, m, r, p = RI()
    global MOD
    MOD = p
    a = RILST()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)
    hld = HLD(g, r)
    size = hld.size
    dfn = hld.dfn

    bit = BinIndexTreeRURQ(n)
    for i, v in enumerate(a, start=1):
        bit.add_interval(dfn[i], dfn[i], v)
    for _ in range(m):
        t, *op = RI()
        if t == 1:
            x, y, z = op
            for l, r in hld.get_route(x, y):
                bit.add_interval(l, r, z)
        elif t == 2:
            s = 0
            x, y = op
            for l, r in hld.get_route(x, y):
                s += bit.sum_interval(l, r)
            print(s%MOD)
        elif t == 3:
            x, z = op
            bit.add_interval(dfn[x], dfn[x] + size[x] - 1, z)
        else:
            x = op[0]
            print(bit.sum_interval(dfn[x], dfn[x] + size[x] - 1)%MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
