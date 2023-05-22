# Problem: D. Mr. Kitayuta's Colorful Graph
# Contest: Codeforces - Codeforces Round 286 (Div. 1)
# URL: https://codeforces.com/contest/506/problem/D
# Memory Limit: 256 MB
# Time Limit: 4000 ms

import sys
from bisect import bisect_left
from collections import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，实测这个快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/506/problem/D
输入 n(2≤n≤1e5) m(1≤m≤1e5) 表示一个 n 点 m 边的无向图，节点编号从 1 到 n。
然后输入 m 条边，每条边输入 v w c(1≤c≤m)，表示有条颜色为 c 的边连接 v 和 w。
然后输入 q(1≤q≤1e5) 和 q 个询问，每个询问输入 v w，你需要输出有多少种颜色 c 满足：从 v 到 w 存在一条路径，这条路径上的边均为颜色 c。

输入
4 5
1 2 1
1 2 2
2 3 1
2 3 3
2 4 3
3
1 2
3 4
1 4
输出
2
1
0
"""


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


class DSU:
    """基于数组的并查集"""

    def __init__(self, n):
        self.fathers = list(range(n))

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

        self.fathers[x] = y
        return True


# 3244  47.95 MB
def solve4():
    n, m = RI()
    es = [[] for _ in range(m)]
    for _ in range(m):
        u, v, c = RI()
        if u > v:
            u, v = v, u
        es[c - 1].append((u - 1, v - 1))
    st = int(m ** 0.5)
    q, = RI()
    qs = []
    dsu = list(range(n))

    def find_fa(x):
        t = x
        while dsu[x] != x:
            x = dsu[x]
        while t != x:
            dsu[t], t = x, dsu[t]
        return x

    ans = {}
    for _ in range(q):
        u, v = RI()
        if u > v:
            u, v = v, u
        qs.append((u - 1, v - 1))
        ans[(u - 1, v - 1)] = 0
    s = list(set(qs))

    for ee in es:
        if not ee:
            continue

        if len(ee) >= st:  # 这种颜色最多有√m种
            dsu = list(range(n))
            for u, v in ee:
                u, v = find_fa(u), find_fa(v)
                dsu[u] = v
            for u, v in s:  # O(q)
                if find_fa(u) == find_fa(v):
                    ans[u, v] += 1
        else:  # 2 * √m个点，直接排序暴力预处理
            for u, v in ee:  # 只重置要用到的节点，由于是遍历边，重置总次数2*m
                dsu[u] = u
                dsu[v] = v
            ps = []
            for u, v in ee:  # 只重置要用到的节点，由于是遍历边，重置总次数2*m
                ps.append(u)
                ps.append(v)
            for u, v in ee:
                u, v = find_fa(u), find_fa(v)
                dsu[u] = v
            ps = sorted(set(ps))
            ln = len(ps)
            for i in range(ln - 1):
                u = ps[i]
                fu = find_fa(u)
                for j in range(i + 1, ln):
                    v = ps[j]
                    if fu == find_fa(v) and (u, v) in ans:
                        ans[u, v] += 1

    for u, v in qs:
        print(ans[u, v])


# 3135  47.95 MB
def solve():
    n, m = RI()
    es = [[] for _ in range(m)]
    for _ in range(m):
        u, v, c = RI()
        if u > v:
            u, v = v, u
        es[c - 1].append((u - 1, v - 1))
    st = int(m ** 0.5)
    q, = RI()
    qs = []
    dsu = list(range(n))

    def find_fa(x):
        t = x
        while dsu[x] != x:
            x = dsu[x]
        while t != x:
            dsu[t], t = x, dsu[t]
        return x

    ans = {}
    for _ in range(q):
        u, v = RI()
        if u > v:
            u, v = v, u
        qs.append((u - 1, v - 1))
        ans[(u - 1, v - 1)] = 0
    s = list(set(qs))

    for ee in es:
        if not ee:
            continue
        for u, v in ee:  # 只重置要用到的节点，由于是遍历边，重置总次数2*m
            dsu[u] = u
            dsu[v] = v

        if len(ee) >= st:  # 这种颜色最多有√m种
            for u, v in s:  # 由于这里会查询不在这个颜色里的点，因此也重置他们
                dsu[u] = u
                dsu[v] = v
            for u, v in ee:
                u, v = find_fa(u), find_fa(v)
                dsu[u] = v
            for u, v in s:  # O(q)
                if find_fa(u) == find_fa(v):
                    ans[u, v] += 1
        else:  # 2 * √m个点，直接排序暴力预处理
            ps = []
            for u, v in ee:  # 只重置要用到的节点，由于是遍历边，重置总次数2*m
                ps.append(u)
                ps.append(v)
            for u, v in ee:
                u, v = find_fa(u), find_fa(v)
                dsu[u] = v
            ps = sorted(set(ps))
            ln = len(ps)
            for i in range(ln - 1):
                u = ps[i]
                fu = find_fa(u)
                for j in range(i + 1, ln):
                    v = ps[j]
                    if fu == find_fa(v) and (u, v) in ans:
                        ans[u, v] += 1

    for u, v in qs:
        print(ans[u, v])


# 3369  46.39mb
def solve3():
    n, m = RI()
    es = [[] for _ in range(m)]
    for _ in range(m):
        u, v, c = RI()
        if u > v:
            u, v = v, u
        es[c - 1].append((u - 1, v - 1))
    st = int(m ** 0.5) // 2
    q, = RI()
    qs = []

    ans = {}
    for _ in range(q):
        u, v = RI()
        if u > v:
            u, v = v, u
        qs.append((u - 1, v - 1))
        ans[(u - 1, v - 1)] = 0
    s = list(set(qs))

    for ee in es:
        if not ee:
            continue

        if len(ee) >= st:  # 这种颜色最多有√m种
            dsu = DSU(n)
            for u, v in ee:
                dsu.union(u, v)
            for u, v in s:  # O(q)
                if dsu.find_fa(u) == dsu.find_fa(v):
                    ans[u, v] += 1
        else:  # 2 * √m个点，直接排序暴力预处理
            ps = []
            for u, v in ee:
                ps.append(u)
                ps.append(v)
            ps = sorted(set(ps))
            ln = len(ps)
            dsu = DSU(ln)
            for u, v in ee:
                dsu.union(bisect_left(ps, u), bisect_left(ps, v))
            for i in range(ln - 1):
                u = ps[i]
                fu = dsu.find_fa(bisect_left(ps, u))
                for j in range(i + 1, ln):
                    v = ps[j]
                    if fu == dsu.find_fa(bisect_left(ps, v)) and (u, v) in ans:
                        ans[u, v] += 1
    for u, v in qs:
        print(ans[u, v])


# TLE
def solve2():
    n, m = RI()
    es = [[] for _ in range(m)]
    for _ in range(m):
        u, v, c = RI()
        if u > v:
            u, v = v, u
        es[c - 1].append((u - 1, v - 1))
    st = int(m ** 0.5) // 2
    q, = RI()
    qs = []

    ans = {}
    for _ in range(q):
        u, v = RI()
        if u > v:
            u, v = v, u
        qs.append((u - 1, v - 1))
        ans[(u - 1, v - 1)] = 0
    s = list(set(qs))

    for ee in es:
        if not ee:
            continue
        dsu = UnionFind()
        for u, v in ee:
            dsu.union(u, v)
        if len(ee) >= st:  # 这种颜色最多有√m种
            for u, v in s:  # O(q)
                if dsu[u] == dsu[v]:
                    ans[u, v] += 1
        else:  # 2 * √m个点，直接排序暴力预处理
            ps = []
            for u, v in ee:
                ps.append(u)
                ps.append(v)
            ps = sorted(set(ps))

            for i in range(len(ps) - 1):
                u = ps[i]
                fu = dsu[u]
                for j in range(i + 1, len(ps)):
                    v = ps[j]
                    if fu == dsu[v] and (u, v) in ans:
                        ans[u, v] += 1
    for u, v in qs:
        print(ans[u, v])


#    TLE   ms
def solve1():
    n, m = RI()
    dsu = defaultdict(lambda: UnionFind())
    color = defaultdict(set)
    for _ in range(m):
        u, v, c = RI()
        dsu[c - 1].union(u - 1, v - 1)
        color[u - 1].add(c - 1)
        color[v - 1].add(c - 1)
    f = Counter()
    half = int(m ** 0.5) + 1  # u的颜色超过half，则预处理product它的连通集；否则可以暴力枚举它的边
    for d in dsu.values():
        for s in d.to_sets():
            p = []
            for u in s:
                if len(color[u]) >= half:
                    p.append(u)
            if len(p) > 1:
                p.sort()
                for i in range(len(p) - 1):
                    for j in range(i + 1, len(p)):
                        f[(p[i], p[j])] += 1

    def ask(u, v):
        if (u, v) in f:
            return f[(u, v)]
        ans = 0
        if len(color[u]) > len(color[v]):
            u, v = v, u

        vc = color[v]
        for c in color[u]:
            if c in vc:
                if dsu[c][u] == dsu[c][v]:
                    ans += 1
        if u > v:
            u, v = v, u
        f[(u, v)] = ans
        return ans

    q, = RI()
    for _ in range(q):
        u, v = RI()
        u -= 1
        v -= 1
        if u > v:
            u, v = v, u

        # print(ask(u, v))
        if (u, v) in f:
            print(f[(u, v)])
            continue
        ans = 0
        if len(color[u]) > len(color[v]):
            u, v = v, u

        vc = color[v]
        for c in color[u]:
            if c in vc:
                if dsu[c][u] == dsu[c][v]:
                    ans += 1
        if u > v:
            u, v = v, u
        f[(u, v)] = ans
        print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
