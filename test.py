from typing import List, Tuple, Optional
from collections import defaultdict, Counter
from sortedcontainers import SortedList

MOD = int(1e9 + 7)
INF = int(1e20)

# 给你一个 n 个节点的无向无根图，节点编号为 0 到 n - 1 。给你一个整数 n 和一个长度为 n - 1 的二维整数数组 edges ，其中 edges[i] = [ai, bi] 表示树中节点 ai 和 bi 之间有一条边。

# 每个节点都有一个价值。给你一个整数数组 price ，其中 price[i] 是第 i 个节点的价值。

# 一条路径的 价值和 是这条路径上所有节点的价值之和。

# 你可以选择树中任意一个节点作为根节点 root 。选择 root 为根的 开销 是以 root 为起点的所有路径中，价值和 最大的一条路径与最小的一条路径的差值。

# 请你返回所有节点作为根节点的选择中，最大 的 开销 为多少。


from typing import Callable, Generic, List, TypeVar

T = TypeVar("T")

E = Callable[[int], T]
"""identify element of op, and answer of leaf"""

Op = Callable[[T, T], T]
"""merge value of child node"""

Composition = Callable[[T, int, int, int], T]
"""return value from child node to parent node"""


class Rerooting(Generic[T]):
    __slots__ = ("g", "_n", "_decrement", "_root", "_parent", "_order", "_directed")

    def __init__(self, n: int, decrement: int = 0, directed=False):
        """
        n: 节点个数
        decrement: 定点可能需要便宜 (1-indexed则1, 0-indexed则0)
        """
        self.g = [[] for _ in range(n)]
        self._n = n
        self._decrement = decrement
        self._directed = directed
        self._root = None  # 一番最初に根とする頂点

    def addEdge(self, u: int, v: int):
        """
        加边u->v，如果无向边则加两条
        """
        u -= self._decrement
        v -= self._decrement
        self.g[u].append(v)
        if not self._directed:
            self.g[v].append(u)

    def rerooting(
            self, e: E["T"], op: Op["T"], composition: Composition["T"], root=0
    ) -> List["T"]:
        """
        - e: 初始化每个节点的价值
          (root) -> res
          mergeの単位元
          例:求最长路径 e=0

        - op: 子树的merge方法
          (childRes1,childRes2) -> newRes

          例:求最长路径 return max(childRes1,childRes2)

        - composition: 頂点の値を更新する関数
          (fromRes,parent,cur,direction) -> newRes
          direction: 0表示用cur更新parent的dp1,1表示用parent更新cur的dp2
          dpをmergeする前段階で実行する演算
          例:最も遠い点までの距離を求める場合 return fromRes+1

        - root: 根とする頂点

        <概要>
        1. rootを根としてまず一度木構造をbfsで求める 多くの場合rootは任意 (0)
        2. 自身の部分木のdpの値をdp1に、自身を含まない兄弟のdpの値のmergeをdp2に入れる
          木構造が定まっていることからこれが効率的に求められる。 葉側からボトムアップに実行する
        3. 任意の頂点を新たに根にしたとき、部分木は
          ①元の部分木 ②兄弟を親とした部分木 ③元の親を親とした(元の根の方向に伸びる)部分木の三つに分かれる。
          ①はstep2のdp1であり、かつdp2はstep3において、②から②と③をmergeした値へと更新されているので
          ②も③も分かっている。 根側からトップダウンに実行する(このことが上記の更新において重要)

        計算量 O(|V|) (Vは頂点数)
        参照 https://qiita.com/keymoon/items/2a52f1b0fb7ef67fb89e
        """
        # step1
        root -= self._decrement
        assert 0 <= root < self._n
        self._root = root
        g = self.g
        _fas = self._parent = [-1] * self._n  # 记录每个节点的父节点
        _order = self._order = [root]  # 用栈遍历记录dfs序
        stack = [root]
        while stack:
            u = stack.pop()
            for v in g[u]:
                if v == _fas[u]:
                    continue
                _fas[v] = u
                _order.append(v)
                stack.append(v)

        # step2
        dp1 = [e(i) for i in range(self._n)]  # !子树部分的dp值,假设u是当前子树的根，vs是第一层儿子(它的非父邻居)，则dp1[u]=op(dp1(vs))
        dp2 = [e(i) for i in
               range(self._n)]  # !非子树部分的dp值,假设u是当前子树的根，vs={v1,v2..vi..}是第一层儿子(它的非父邻居),则dp2[vi]=op(dp1(vs-vi)),即他的兄弟们
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

        # step3 自顶向下计算每个节点作为根时的dp1，dp2的含义变更为:dp2[u]为u的兄弟+父。这样对v来说dp1[v] = op(dp1[u],dp1[v])
        for newRoot in _order[1:]:  #
            parent = _fas[newRoot]
            dp2[newRoot] = composition(
                op(dp2[newRoot], dp2[parent]), parent, newRoot, 1
            )  # op从上往下更新dp2
            dp1[newRoot] = op(dp1[newRoot], dp2[newRoot])
        return dp1


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:

        def e(root: int) -> int:
            # mergeの単位元
            # 例:最も遠い点までの距離を求める場合 e=0
            return 0

        def op(childRes1: int, childRes2: int) -> int:
            # モノイドの性質を満たす演算を定義する それが全方位木DPをする条件
            # 例:最も遠い点までの距離を求める場合 return max(childRes1,childRes2)
            return max(childRes1, childRes2)

        def composition(fromRes: int, fa: int, u: int, direction: int) -> int:
            # dpをmergeする前段階で実行する演算
            # 例:最も遠い点までの距離を求める場合 return res+1
            if direction == 0:  # cur -> parent
                return fromRes + price[u]
            return fromRes + price[fa]

        R = Rerooting(n)
        for u, v in edges:
            R.addEdge(u, v)
        res = R.rerooting(e, op, composition)
        return max(res)
