"""虚树 https://oi-wiki.org/graph/virtual-tree/
https://atcoder.jp/contests/abc359/submissions/54735916
当询问是问部分散点（可非连续），且总的询问数和n同阶，可以使用虚树优化成nlogn+q. log在lca。
原理是：
    - 发现每次询问m个点时，树上很多其他点是没用的。考虑生成一颗”浓缩的小树“，且小树里亲代关系不变。
    - 那么只需要把所有询问点和他们的lca放到树里即可。
    - 这样每颗虚树的点有2m个，级别是m的。

注意：
    - 注意如果有边权，注意u-lca链接时，这里如何合并（除了相加，还有从头可以顺下来的情况，如前缀min）
然而很多虚树的题可以用启发式合并水过。
目前板子是0-indexed，待改造
"""

def solve():
    n = int(input())
    edge = [[] for i in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        edge[u].append(v)
        edge[v].append(u)

    a = list(map(lambda x: int(x) - 1, input().split()))
    col = [[] for i in range(n)]
    for i in range(n):
        col[a[i]].append(i)

    depth = [-1] * n
    depth[0] = 0
    todo = [0]
    while todo:
        v = todo.pop()
        for u in edge[v]:
            if depth[u] == -1:
                depth[u] = depth[v] + 1
                todo.append(u)
    T = AuxiliaryTree(n, edge)
    ans = 0
    dp = [0] * n
    for c in range(n):
        if len(col[c]) <= 1:
            continue
        s = len(col[c])
        root = T.query(col[c])
        todo = [~root, root]
        while todo:
            v = todo.pop()
            if v >= 0:
                dp[v] = 0
                for u in T.G[v]:
                    todo += [~u, u]
            else:
                v = ~v
                for u in T.G[v]:
                    ans += (s - dp[u]) * dp[u] * (depth[u] - depth[v])
                    dp[v] += dp[u]
                if a[v] == c:
                    dp[v] += 1
    print(ans)


class AuxiliaryTree:
    def __init__(self, n, edge, root=0):
        self.n = n
        self.edge = edge
        self.eular = [-1] * (2 * n - 1)
        self.first = [-1] * n
        self.depth = [-1] * n
        self.lgs = [0] * (2 * n)
        for i in range(2, 2 * n):
            self.lgs[i] = self.lgs[i >> 1] + 1
        self.st = []
        self.G = [[] for i in range(n)]  # 構築結果

        self.dfs(root)
        self.construct_sparse_table()

    def dfs(self, root):
        stc = [root]
        self.depth[root] = 0
        num = 0
        while stc:
            v = stc.pop()
            if v >= 0:
                self.eular[num] = v
                self.first[v] = num
                num += 1
                for u in self.edge[v][::-1]:
                    if self.depth[u] == -1:
                        self.depth[u] = self.depth[v] + 1
                        stc.append(~v)
                        stc.append(u)
            else:
                self.eular[num] = ~v
                num += 1

    def construct_sparse_table(self):
        self.st.append(self.eular)
        sz = 1
        while 2 * sz <= 2 * self.n - 1:
            prev = self.st[-1]
            nxt = [0] * (2 * self.n - 2 * sz)
            for j in range(2 * self.n - 2 * sz):
                v = prev[j]
                u = prev[j + sz]
                if self.depth[v] <= self.depth[u]:
                    nxt[j] = v
                else:
                    nxt[j] = u
            self.st.append(nxt)
            sz *= 2

    def lca(self, u, v):
        x = self.first[u]
        y = self.first[v]
        # if x > y : x , y = y , x
        d = self.lgs[y - x + 1]
        return (
            self.st[d][x]
            if self.depth[self.st[d][x]] <= self.depth[self.st[d][y - (1 << d) + 1]]
            else self.st[d][y - (1 << d) + 1]
        )

    def query(self, vs):
        """
        vs: 仮想木の頂点
        self.G: 仮想木における子
        返り値: 仮想木の根
        """

        k = len(vs)
        if k == 0:
            return -1
        vs.sort(key=self.first.__getitem__)
        stc = [vs[0]]
        self.G[vs[0]] = []

        for i in range(k - 1):
            w = self.lca(vs[i], vs[i + 1])
            if w != vs[i]:
                last = stc.pop()
                while stc and self.depth[w] < self.depth[stc[-1]]:
                    self.G[stc[-1]].append(last)
                    last = stc.pop()

                if not stc or stc[-1] != w:
                    stc.append(w)
                    vs.append(w)
                    self.G[w] = [last]
                else:
                    self.G[w].append(last)
            stc.append(vs[i + 1])
            self.G[vs[i + 1]] = []

        for i in range(len(stc) - 1):
            self.G[stc[i]].append(stc[i + 1])

        return stc[0]


from sys import stdin

input = lambda: stdin.readline().rstrip()

solve()
