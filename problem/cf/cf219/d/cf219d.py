# Problem: D. Choosing Capital for Treeland
# Contest: Codeforces - Codeforces Round 135 (Div. 2)
# URL: https://codeforces.com/problemset/problem/219/D
# Memory Limit: 256 MB
# Time Limit: 3000 ms

import sys
from collections import *
from types import GeneratorType

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """
https://codeforces.com/problemset/problem/219/D

输入 n(2≤n≤2e5) 和 n-1 条边 v w，表示一条 v->w 的有向边。（节点编号从 1 开始）
保证输入构成一棵树。

定义 f(x) 表示以 x 为根时，要让 x 能够到达任意点，需要反向的边的数量。
输出 min(f(x))，以及所有等于 min(f(x)) 的节点编号（按升序输出）。
输入
3
2 1
2 3
输出
0
2 

输入
4
1 4
2 4
3 4
输出
2
1 2 3 
"""
"""换根DP，类似双周赛T4
先求以0为根时，反边数量
然后求以其它为根时反边数量。
一对邻居分别作根时，状态的差别只跟这条边有关，因此可以按次序求出每个节点为根时的状态。
想象以0为根时状态已求出，0-1有边，揪住1向上提，让1做根。
发现0的其它子树状态不变，1的其它子树状态也不变，只有0-1这条边变了。
以此类推。
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


#     2526  ms
def solve1():
    n, = RI()
    g = [[] for _ in range(n)]
    s = set()
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        s.add((u, v))
    f = [0] * n

    @bootstrap
    def dfs(u, fa):
        for v in g[u]:
            if v == fa: continue
            if (v, u) in s:
                f[0] += 1
            yield dfs(v, u)
        yield

    @bootstrap
    def reroot(u, fa):
        for v in g[u]:
            if v == fa: continue
            f[v] = f[u] - int((v, u) in s) + int((u, v) in s)
            yield reroot(v, u)
        yield

    dfs(0, -1)
    reroot(0, -1)
    mn = min(f)
    ans = [i + 1 for i, v in enumerate(f) if v == mn]
    print(mn)
    print(*ans)


#   1526    ms
def solve2():
    n, = RI()
    g = [[] for _ in range(n)]
    s = set()
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        s.add((u, v))
    f = [0] * n
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
            f[u] += f[v] + int((v, u) in s)
    for u in order:
        for v in g[u]:
            if v == fas[u]: continue
            f[v] = f[u] + int((u, v) in s) - int((v, u) in s)
    # print(f)
    mn = min(f)
    ans = [i + 1 for i, v in enumerate(f) if v == mn]
    print(mn)
    print(*ans)


#    1402   ms
def solve3():
    n, = RI()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append((v, 1))  # 邻居和方向
        g[v].append((u, -1))  # 反边
    f = [0] * n
    fas = [-1] * n
    order = []
    q = deque([0])
    while q:
        u = q.popleft()
        order.append(u)
        for v, _ in g[u]:
            if v == fas[u]: continue
            fas[v] = u
            q.append(v)

    for u in order[::-1]:
        for v, d in g[u]:
            if v == fas[u]: continue
            # f[u] += f[v] + (d < 0)  # 如果是反边则+1
            f[u] += f[v] + ((-d + 1) >> 1)  # 如果是反边则+1 1402
    for u in order:
        for v, d in g[u]:
            if v == fas[u]: continue
            # f[v] = f[u] + (d > 0) - (d < 0)  # uv是正边的话，根从u->v则数量+1，反边则-1
            f[v] = f[u] + d  # uv是正边的话，根从u->v则数量+1，反边则-1
    # print(f)
    mn = min(f)
    ans = [i + 1 for i, v in enumerate(f) if v == mn]
    print(mn)
    print(*ans)


#   1714    ms
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
    r = Rerooting(n)
    s = set()
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        s.add((u, v))
        r.add_edge(u, v)

    def e(root: int) -> int:
        # 转移时单个点不管相邻子树的贡献
        # 例:最も遠い点までの距離を求める場合 e=0
        return 0

    def op(child_res1: int, child_res2: int) -> int:
        # 如何组合/取舍两个子树的答案
        # 例：求最长路径 return max(childRes1,childRes2)
        return child_res1 + child_res2

    def composition(from_res: int, fa: int, u: int, use_fa: int = 0) -> int:
        # 知道子树的每个子树和节点值，如何更新子树答案;
        # 例子:求最长路径 return from_res+1
        if use_fa == 0:  # cur -> parent 用子节点更新父节点
            return from_res + int((u, fa) in s)  # 计算反边数量
        return from_res + int((fa, u) in s)  # 反过来把子节点当父的话，u->fa才是正边。

    f = r.rerooting(e, op, composition)

    # print(f)
    mn = min(f)
    ans = [i + 1 for i, v in enumerate(f) if v == mn]
    print(mn)
    print(*ans)


if __name__ == '__main__':
    solve()
