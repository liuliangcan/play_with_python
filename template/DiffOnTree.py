"""树上差分
处理树上路径问题，要结合lca
点差分 u~v简单路上所有点权+=x, o=lca(u,v), p = parent[o]
diff[u]+=x,
diff[v]+=x,
diff[o]-=x,
diff[p]-=x;

边差分 u~v简单路上所有边权+=x, o=lca(u,v),每条边两端深度较大的节点存储该边的差分数组
diff[u]+=x,diff[v]+=x,diff[o]-=2*x;
"""


class HLD:
    def __init__(self, g, root):
        # 无论是点还是dfn还是dep，都从1开始，默认0是无
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

    def dis(self, u, v):
        dep = self.dep
        return dep[u] + dep[v] - 2 * dep[self.lca(u, v)]


class DiffOnTreePoint:
    """点差分 u~v简单路上所有边权+=x, o=lca(u,v), p = parent[o]
    diff[u]+=x,
    diff[v]+=x,
    diff[o]-=x,
    diff[p]-=x;"""

    def __init__(self, g, root=1, lca=None, a=None):  # 注意节点编号是1-indexed
        self.n = n = len(g) - 1
        self.lca = lca or HLD(g, root)  # 不传就重新算
        self.diff = [0] * (n + 1)  # 树上差分,用0作为根的父节点
        self.a = a[:] if a else [0] * (n + 1)  # 传了就用它初始化；默认不修改，去掉切片则直接改
        self.rank = self.lca.rank
        self.fa = self.lca.fa  # 用0作为根的父节点
        self.g = g

    def add_route(self, u, v, w):
        """把u~v简单路径上的所有点权+w"""
        self.diff[u] += w
        self.diff[v] += w
        o = self.lca.lca(u, v)
        self.diff[o] -= w
        self.diff[self.fa[o]] -= w

    def get_all_point_w(self):  #
        d = self.diff[:]
        for u in self.rank[:0:-1]:
            for v in self.g[u]:
                if v == self.fa[u]: continue
                d[u] += d[v]
            self.a[u] += d[u]
        # print(self.a)
        return self.a  # self.a[u]表示u的点权


class DiffOnTreeEdge:
    """边差分 u~v简单路上所有边权+=x, o=lca(u,v),每条边两端深度较大的节点存储该边的差分数组
    diff[u]+=x,diff[v]+=x,diff[o]-=2*x;"""

    def __init__(self, g, root=1, lca=None):  # 外部传进来lca或者自己重新算
        n = len(g) - 1
        self.lca = lca or HLD(g, root)
        self.diff = [0] * (n + 1)  # 树上差分
        self.a = [0] * (n + 1)
        self.rank = self.lca.rank
        self.fa = self.lca.fa  # 用0作为根的父节点
        self.g = g

    def add_route(self, u, v, w):
        """把u~v简单路径上的所有边权+w"""
        self.diff[u] += w
        self.diff[v] += w
        self.diff[self.lca.lca(u, v)] -= w * 2

    def get_all_edges_w(self):
        d = self.diff[:]
        for u in self.rank[:0:-1]:
            for v in self.g[u]:
                if v == self.fa[u]: continue
                d[u] += d[v]
            self.a[u] += d[u]

        return self.a  # self.a[u]表示以u为更低层的边权
