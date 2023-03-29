# Problem: D. Book of Evil
# Contest: Codeforces - Codeforces Round 196 (Div. 2)
# URL: https://codeforces.com/problemset/problem/337/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/337/D

输入 n m(1≤m≤n≤1e5) d(0≤d≤n-1) 表示一棵 n 个节点的树，其中 m 个节点有怪物，这些怪物是由一个传送门生成的，传送门与任意怪物的距离不超过 d。
然后输入 m 个互不相同的数，表示怪物所在节点编号（从 1 开始）。
然后输入 n-1 行，每行两个节点编号，表示树的边。

输出可能存在传送门的节点的个数。注意传送门只有一个。
输入
6 2 3
1 2
1 5
2 3
3 4
4 5
5 6
输出 3
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


#    1246   ms
def solve1():
    n, m, d = RI()
    monsters = {v - 1 for v in RI()}
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    # down1[i]代表向下走最远的怪物距离i的最大值(在当前子树上的深度)
    up, down1, down2 = [-inf] * n, [-inf] * n, [-inf] * n

    @bootstrap
    def dfs(u, fa):
        if u in monsters:
            down1[u] = down2[u] = up[u] = 0
        for v in g[u]:
            if v == fa: continue
            yield dfs(v, u)
            c = down1[v] + 1
            if c > down1[u]:
                down2[u], down1[u] = down1[u], c
            elif c > down2[u]:
                down2[u] = c
        yield

    @bootstrap
    def reroot(u, fa):
        for v in g[u]:
            if v == fa: continue
            if down1[v] + 1 == down1[u]:  # 当前子节点v在父节点u的最长路径上，走次大路径
                up[v] = max(up[u], down2[u]) + 1
            else:
                up[v] = max(up[u], down1[u]) + 1
            yield reroot(v, u)
        yield

    dfs(0, -1)
    reroot(0, -1)
    print(sum(max(x, y) <= d for x, y in zip(down1, up)))


#  模板 934    ms
def solve3():
    from typing import Callable, Generic, List, TypeVar

    T = TypeVar("T")
    E = Callable[[int], T]
    """identify element of op, and answer of leaf"""
    Op = Callable[[T, T], T]
    """merge value of child node"""
    Composition = Callable[[T, int, int, int], T]
    """return value from child node to parent node"""

    class Rerooting(Generic[T]):
        __slots__ = ("g", "_n", "_decrement", "_root", "_parent", "_order")

        def __init__(self, n: int, decrement: int = 0, edges=None):
            """
            n: 节点个数
            decrement: 节点id可能需要偏移 (1-indexed则-1, 0-indexed则0)
            """
            self.g = g = [[] for _ in range(n)]
            self._n = n
            self._decrement = decrement
            self._root = None  # 一开始的根
            if edges:
                for u, v in edges:
                    u -= decrement
                    v -= decrement
                    g[u].append(v)
                    g[v].append(u)

        def add_edge(self, u: int, v: int):
            """
            无向树加边
            """
            u -= self._decrement
            v -= self._decrement
            self.g[u].append(v)
            self.g[v].append(u)

        def rerooting(
                self, e: E["T"], op: Op["T"], composition: Composition["T"], root=0
        ) -> List["T"]:
            """
            - e: 初始化每个节点的价值
              (root) -> res
              mergeの単位元
              例:求最长路径 e=0

            - op: 两个子树答案如何组合或取舍
              (childRes1,childRes2) -> newRes
              例:求最长路径 return max(childRes1,childRes2)

            - composition: 知道子子树答案和节点值，如何更新子树答案
              (from_res,fa,u,use_fa) -> new_res
              use_fa: 0表示用u更新fa的dp1,1表示用fa更新u的dp2
              例:最长路径return from_res+1

            - root: 可能要设置初始根，默认是0
            <概要> 换根DP模板,用线性时间获取以每个节点为根整颗树的情况。
            注意最终返回的dp[u]代表以u为根时，u的所有子树的最优情况(不包括u节点本身),因此如果要整颗子树情况，还要再额外计算。
            1. 记录dp1,dp2。其中:
                dp1[u] 代表 以u为根的子树，它的孩子子树的最优值,即u节点本身不参与计算。注意，和我们一般定义的f[u]代表以u为根的子树2情况不同。
                dp2[v] 代表 除了v以外，它的兄弟子树的最优值。依然注意，v不参与，同时u也不参与(u是v的父节点)。
                建议画图理解。
            2. dp2[v]的含义后边将进行一次变动,变更为v的兄弟、u的父过来的路径,merge上u节点本身最后得出来的值。即v以父亲为邻居向外延伸的最优值(不含v，但含父)。
            3. 同时dp1[u]的含义更新为目标的含义:以u为根，u的子节点们所在子树的最优情况。
            4. 这样dp1,dp2将分别代表u的向下子树的最优,u除了向下子树以外的最优(一定从父节点来，但父节点可能从兄弟来或祖宗来)
            <步骤>
            1. 先从任意root出发(一般是0),获取bfs层序。这里是为了方便dp，或者直接dfs树形DP其实也是可以的，但可能会爆栈。
            2. 自底向上dp,用自身子树情况更新dp1,除自己外的兄弟子树情况更新dp2。
            3. 自顶向下dp,变更dp2和dp1的含义。这时对于u来说存在三种子树(强烈建议画图观察):
                ① u本身的子树，它们的最优解已经存在于之前的dp1[u]。
                ② u的兄弟子树+fa,它们的最优解=composition(dp2[u],fa,u,use_fa=1)。
                ③ 连接到fa的最优子树+fa,最优解=composition(dp2[fa],fa,u,use_fa=1)。
                    注意这里的dp2含义已变更，由于我们是自顶向下计算，因此dp2[fa]已更新。
                    ②和③可以写一起来更新dp2[u]

            計算量 O(|V|) (Vは頂点数)
            参照 https://qiita.com/keymoon/items/2a52f1b0fb7ef67fb89e
            """
            # step1
            root -= self._decrement
            assert 0 <= root < self._n
            self._root = root
            g = self.g
            _fas = self._parent = [-1] * self._n  # 记录每个节点的父节点
            _order = self._order = [root]  # bfs记录遍历层序，便于后续dp
            q = deque([root])
            while q:
                u = q.popleft()
                for v in g[u]:
                    if v == _fas[u]:
                        continue
                    _fas[v] = u
                    _order.append(v)
                    q.append(v)

            # step2
            dp1 = [e(i) for i in range(self._n)]  # !子树部分的dp值,假设u是当前子树的根，vs是第一层儿子(它的非父邻居)，则dp1[u]=op(dp1(vs))
            dp2 = [e(i) for i in
                   range(
                       self._n)]  # !非子树部分的dp值,假设u是当前子树的根，vs={v1,v2..vi..}是第一层儿子(它的非父邻居),则dp2[vi]=op(dp1(vs-vi)),即他的兄弟们

            for u in _order[::-1]:  # 从下往上拓扑序dp
                res = e(u)
                for v in g[u]:
                    if _fas[u] == v:
                        continue
                    dp2[v] = res
                    res = op(res, composition(dp1[v], u, v, 0))  # op从下往上更新dp1
                # 由于最大可能在后边，因此还得倒序来一遍
                res = e(u)
                for v in g[u][::-1]:
                    if _fas[u] == v:
                        continue
                    dp2[v] = op(res, dp2[v])
                    res = op(res, composition(dp1[v], u, v, 0))
                dp1[u] = res

            # step3 自顶向下计算每个节点作为根时的dp1，dp2的含义变更为:dp2[u]为u的兄弟+父。这样对v来说dp1[u] = op(dp1[fa],dp1[u])

            for u in _order[1:]:
                fa = _fas[u]
                dp2[u] = composition(
                    op(dp2[u], dp2[fa]), fa, u, 1
                )  # op从上往下更新dp2
                dp1[u] = op(dp1[u], dp2[u])

            return dp1

    def e(root: int) -> int:
        # 转移时单个点不管相邻子树的贡献
        # 例:最も遠い点までの距離を求める場合 e=0
        return 0 if root in monsters else -inf

    def op(child_res1: int, child_res2: int) -> int:
        # 如何组合/取舍两个子树的答案
        # 例：求最长路径 return max(childRes1,childRes2)
        return max(child_res1, child_res2)

    def composition(from_res: int, fa: int, u: int, use_fa: int = 0) -> int:
        # 知道子树的每个子树和节点值，如何更新子树答案;
        # 例子:求最长路径 return from_res+1
        if use_fa == 0:  # cur -> parent
            return from_res + 1
        return from_res + 1

    n, m, d = RI()
    r = Rerooting(n)
    monsters = {v - 1 for v in RI()}
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        r.add_edge(u, v)

    print(sum(x <= d for x in r.rerooting(e, op, composition)))


#  bfs 654   ms
def solve():
    n, m, d = RI()
    up, down1, down2 = [-inf] * n, [-inf] * n, [-inf] * n
    for u in RI():
        up[u - 1] = down1[u - 1] = down2[u - 1] = 0
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    # down1[i]代表向下走最远的怪物距离i的最大值(在当前子树上的深度)
    fas = [-1] * n
    order = []
    q = deque([0])
    while q:
        u = q.popleft()
        order.append(u)
        for v in g[u]:
            if v == fas[u]: continue
            fas[v] = u
            q.append(v)
    for u in order[::-1]:
        for v in g[u]:
            if v == fas[u]: continue
            c = down1[v] + 1
            if c > down1[u]:
                down1[u], down2[u] = c, down1[u]
            elif c > down2[u]:
                down2[u] = c
    for u in order:
        for v in g[u]:
            if v == fas[u]: continue
            if down1[v] + 1 == down1[u]:
                up[v] = max(up[u], down2[u]) + 1
            else:
                up[v] = max(up[u], down1[u]) + 1

    print(sum(max(x, y) <= d for x, y in zip(down1, up)))


if __name__ == '__main__':
    solve()
