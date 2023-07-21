# Problem: D. Road Improvement
# Contest: Codeforces - Codeforces Round 302 (Div. 1)
# URL: https://codeforces.com/problemset/problem/543/D
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
PROBLEM = """https://codeforces.com/problemset/problem/543/D

输入 n(2≤n≤2e5) 和 n-1 个数 p2,p3,...,pn，表示一棵 n 个节点的无根树，节点编号从 1 开始，i 与 pi(1≤pi≤i-1) 相连。
定义 a(x) 表示以 x 为根时的合法标记方案数，模 1e9+7。其中【合法标记】定义为：对树的某些边做标记，使得 x 到任意点的简单路径上，至多有一条边是被标记的。
输出 a(1),a(2),...,a(n)。
输入
3
1 1
输出
4 3 3

输入
5
1 2 3 4
输出
5 8 9 8 5
"""
"""换根 DP。不了解的同学请看右边的链接。

先来计算 a(1)，此时 1 为树根。
定义 f(i) 表示子树 i 的合法标记方案数。
对于 i 的儿子 j，考虑 i-j 这条边是否标记：
- 标记：那么子树 j 的所有边都不能标记，方案数为 1。
- 不标记：那么方案数就是 f(j)。
i 的每个儿子互相独立，所以根据乘法原理有 
f(i) = (f(j1)+1) * (f(j2)+1) * ... * (f(jm)+1)
其中 j1,j2,...,jm 是 i 的儿子。

然后来计算其余 a(i)。
考虑把根从 i 换到 j：
对于 j 来说，方案数需要在 f(j) 的基础上，再乘上【父亲 i】这棵子树的方案数，即 a(i) / (f(j)+1)。 
所以 a(j) = f(j) * (a(i)/(f(j)+1) + 1)

本题的一个易错点是，f(j)+1 可能等于 M=1e9+7，取模会变成 0，但是 0 没有逆元。
处理方式有很多，我的做法是定义二元组 (k,x) 表示 M^k * x % M，在这基础上定义：
- 乘法运算：(k1, x1) * (k2, x2) = (k1+k2, x1*x2%M)
- 除法运算：(k1, x1) / (k2, x2) = (k1-k2, x1*inv(x2)%M)  这里 k1>=k2
- 加一运算：请读者思考（需要分类讨论，具体见代码）

当 k>0 时，(k,x) 的实际值为 0；当 k=0 时，(k,x) 的实际值为 x。

https://codeforces.com/contest/543/submission/214621886"""


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


#   451    ms
def solve():
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

    n, = RI()
    a = RILST()
    r = Rerooting(n)
    for i, p in enumerate(a, start=1):
        r.add_edge(i, p - 1)

    def e(root: int) -> int:
        # 转移时单个点不管相邻子树的贡献
        # 例:最も遠い点までの距離を求める場合 e=0
        return 1

    def op(child_res1: int, child_res2: int) -> int:
        # 两个com(的贡献如何计算
        # 例：求最长路径 return max(childRes1,childRes2)
        return (child_res1) * (child_res2) % MOD

    def composition(from_res: int, fa: int, u: int, use_fa: int = 0) -> int:
        # from_res这个值向外计算时，如何进行贡献;
        # 例子:求最长路径 return from_res+1
        return (1 + from_res) % MOD

    ans = r.rerooting(e, op, composition)
    print(' '.join(map(str, ans)))



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
