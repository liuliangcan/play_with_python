"""
@File       :   DSU.py

        fa = list(range(n))

        def find(x):
            t = x
            while x != fa[x]:
                x = fa[x]
            while t != x:
                fa[t], t = x, fa[t]
            return x
- 并查集（Disjoint Set Union），有时命名为UnionFind。是一种家族合并算法。
- 并查集的基本结构:一个数组fa:fa[i]代表i的父亲(祖宗)节点是谁。有了父节点信息可以一直向下查找到祖宗。
- 路径压缩的并查集，合并和查询的复杂都是均摊约O(1)。有论证说最坏情况下平均复杂度上O(lgn)。
    - 方法是在每个家族选出代表元（祖宗节点）。这个家族的所有属性储存在代表元的位置上。
    - 讨论每个节点的合并及家族时，转为讨论代表元：
        - 合并x,y: 转为合并他们的代表元。
        - 查询x所在家族的size： size[fa(x)]。
        - 查询x所在家族的边数： edge_size[fa(x)]。
    - 按轶合并/启发式合并的话，复杂度是O(logn)。方法是每次都把小集合合并到大集合。
- 因此关键是如何用O(1)找到x家族的代表元。即find_fa(x)的实现。
    - 若find_fa(x) != x，继续寻找，并把路径上的点的父节点设为最终找到的代表元。
        - 显然这个一直向下找，最终再返回来处理每个节点的结构非常适合递归。
        - 但py递归深度超过1000就会RE，在atc有时可以通过设置sys.setrecursionlimit()的方法做。但在cf容易MLE。
        - 于是改为迭代，由于路径是唯一的，储存出发点，找到终点后，再从出发点走一遍修改这些点。
            - 这里也可以用一个数组记录路径，最后遍历数组即可，实测没有链快。
---

- 除了数组实现，另外还有基于defaultdict的写法，对字符串/坐标/大数字/输入无法确定..等不适合开数组的数据友好，但常数较大，优先选择离散化。
- 另外python3有个神奇的库：from networkx.utils import UnionFind。在atc的python3上实测可用，注意pypy用不了
    - 用[]操作作为find。union可以批量。
    - 无需初始化，基于字典而不是数组
    - 按轶合并
---
- 应用：
- 家族合并:家族数、每个家族大小、边数
- 检查图的连通性
- 在一些max/min相关的题目里，离线排序节点/边，然后(双指针/按大小)逐条边合并，递推性质。
    - 通常按边权是并查集，如最小生成树Kruskal；按点权更适合用heap。但也不尽然，比如可以用两个端点的最大/小值作为这个边的权
- 链式并查集，可以用来删除连续的点，然后查找残余的最近的点。（这种题目有时可以用链表/有序集合)
- 种类并查集：敌人的敌人是朋友。敌人的敌人是朋友[种类并查集](https://zhuanlan.zhihu.com/p/97813717)。
    - 维护n*2长度的并查集。
    - 若ab是敌人，则合并(a,n+b)和(b,n+a)
    - 如果有其他关系，如剪刀石头布(克制与被克),可以维护n*3长度
---
- 目前不会的：
- 可以删除的并查集
- 交错树
- 奇环
---
- [[python刷题模板] 并查集](https://blog.csdn.net/liuliangcan/article/details/124990864)
"""

class DSU:
    """基于数组的并查集"""
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.set_count = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            self.edge_size[y] += 1
            return False
        # if self.size[x] > self.size[y]:  # 注意如果要定向合并x->y，需要干掉这个；实际上上边改成find_fa后，按轶合并没必要了，所以可以常关
        #     x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.set_count -= 1
        return True




class UnionFind:
    """from networkx.utils import UnionFind"""

    def __init__(self, elements=None):

        if elements is None:
            elements = ()
        self.parents = {}
        self.weights = {}
        for x in elements:
            self.weights[x] = 1
            self.parents[x] = x

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def to_sets(self):
        """Iterates over the sets stored in this structure.

        For example::

            >>> partition = UnionFind("xyz")
            >>> sorted(map(sorted, partition.to_sets()))
            [['x'], ['y'], ['z']]
            >>> partition.union("x", "y")
            >>> sorted(map(sorted, partition.to_sets()))
            [['x', 'y'], ['z']]

        """
        # Ensure fully pruned paths
        for x in self.parents.keys():
            _ = self[x]  # Evaluated for side-effect only

        from collections import defaultdict

        one_to_many = defaultdict(set)
        for v, k in self.parents.items():
            one_to_many[k].add(v)

        yield from dict(one_to_many).values()

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        # Find the heaviest root according to its weight.
        roots = iter(
            sorted(
                {self[x] for x in objects}, key=lambda r: self.weights[r], reverse=True
            )
        )
        try:
            root = next(roots)
        except StopIteration:
            return

        for r in roots:
            self.weights[root] += self.weights[r]
            self.parents[r] = root

# if __name__ == '__main__':
#
#     uf = UnionFind(range(10))
#     print(list(uf.to_sets()))
#     uf.union(1,2)
#     print(uf.weights[uf[1]])
#     uf.union(1,2)
#     print(uf.weights[uf[1]])
#     print(list(uf.to_sets()))

