"""树链剖分 https://oi-wiki.org/graph/hld/
可以把一颗树完整剖分成一些链，树上任意简单路径u->v都可以分解成至多O(lgn)条链，且这些链内在dfn序上是连续的，因此可以用数据结构优化。
树剖一般指重链剖分，即重儿子是指子树最大的那个，且dfn序时，优先访问重儿子。这保证了一条重链上的节点在dfn上是连续的。
观察一条链，从lca(u,v)向下思考任意一边：
    若走重边，那么更容易一次走较远的链。
    若走轻边，可能一直切链，这时子树大小至少除2。
    因此：如果一直走重边，那么一次就下来了；否则切轻边，最多切O(lgn)次
实现：
    两次dfs:(py拿栈+递推代替)
    - 第一次dfs求出 fa\dep\size\hson(自底向上)
    - 第二次dfs求出 top(自顶向下，依赖hson)\dfn\rank

应用：
    - 求lca。可以从depth[top[u]]考虑，更低的那个向上跳到上边的链。uv共链时，高的那个即是答案。
    - 树上差分，主要是用lca。
    - 树上路径操作，转化为区间问题，依然是向上跳的动作，最多跳O(lgn)次(常数小，跑不满，除非完全二叉树)。那么用数组区间数据结构优化，通常查询可以变成O(q*lgn*lgn)
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
