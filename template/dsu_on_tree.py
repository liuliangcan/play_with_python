"""树上启发式合并
一般用来解决不带修（可离线）的子树内询问，复杂度一般是O(q+nlogn)

dsu on tree 名字很离谱其实和并查集没有关系。
指的是小集合向大集合暴力合并：
    用一个信息集维护大集合(重儿子)的信息。小集合(轻儿子们)的信息用完了删掉。
    这样保证每个节点被暴力合并的次数不超过O(logn)次。因此总复杂度做到O(nlogn)
需要用到重链剖分的轻重儿子性质，以及dfn序（不用dfn序也可以，轻儿子贡献时直接递归）

步骤：
1. 先重链剖分，求出rank、dfn序、fa、son等信息
2. 自底向上处理：
    - 对每个子树，先处理轻儿子（会删除信息），再处理重儿子（不删）
    - 处理完儿子，当前信息集会保留重儿子的信息，然后暴力遍历所有轻儿子的子树上每个节点，向信息集贡献。然后贡献点u，计算当前子树答案。
    - 计算完子树答案，看看本子树是否需要移除（即u是别人的轻儿子），如果需要移除，则暴力遍历移除。
    - 以上暴力过程，可以dfs，也可以在dfn序上搞。
    - py的话全过程用栈模拟，因此能用dfn序的都用dfn序。

-- 由于根节点到任意节点的路径上，轻边不超过O(logn)条，因此每个节点被暴力合并的次数不会超过O(logn)。
-- 每次clear其实都会把所有数据清空,但为了时间，依然是通过遍历节点移除贡献；但全局性的属性比如mx等可以直接重置
-- 同上条，由于清空动作的存在，每次贡献答案时，其实当前信息集储存的就是'本子树',并未储存其他任何兄弟子树或者其它。

例题：
    - cf375d 算是模板，离线查询子树上有多少种颜色超过k个：Tree and Queries  https://codeforces.com/problemset/problem/375/D
    - CF741D
    - CF600E 模板 通过这个发现，每次clear其实都会把所有数据清空,但为了时间，依然是通过遍历节点移除贡献  lomsat gelral  https://codeforces.com/problemset/problem/600/E
    - CF1709E XOR TREE  利用树上前缀xor推公式，但有操作要移除整颗子树的点集，以后都不再贡献，因此可以在dfn上用链式并查集合并连续区间  https://codeforces.com/problemset/problem/1709/E
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
        # self.is_heavy = [0] * (n + 1)
        # self.is_heavy[root] = 1
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
                # self.is_heavy[son[u]] = 1

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
    n, m = RI()
    a = [1] + RILST()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)
    qs = [[] for _ in range(n + 1)]
    for i in range(m):
        u, k = RI()
        qs[u].append((i, k))
    hld = HLD(g, 1)
    rank, fa, dfn, son, size = hld.rank, hld.fa, hld.dfn, hld.son, hld.size
    cnt = [0] * (10 ** 5 + 1)
    cs = [0] * (10 ** 5 + 1)
    ans = [0] * m

    def dfs(u, keep):  # py dfs跑不过，改用栈模拟
        for v in g[u]:
            if son[u] != v != fa[u]:
                dfs(v, False)
        if son[u]: dfs(son[u], True)
        for v in g[u]:
            if son[u] != v != fa[u]:
                for i in range(dfn[v], dfn[v] + size[v]):
                    c = a[rank[i]]
                    cnt[c] += 1
                    cs[cnt[c]] += 1
        c = a[u]
        cnt[c] += 1
        cs[cnt[c]] += 1
        for i, k in qs[u]:
            ans[i] = cs[k]
        if not keep:
            for i in range(dfn[u], dfn[u] + size[u]):
                c = a[rank[i]]
                cs[cnt[c]] -= 1
                cnt[c] -= 1

    # dfs(1,True)

    st = [(1, False, True)]  # root,是否keep贡献(重儿子),入栈标记
    while st:
        u, keep, in_ = st.pop()
        if in_:
            st.append((u, keep, False))  # 注册自己的出栈动作
            if son[u]:
                st.append((son[u], True, True))  # 重儿子先入栈，后出栈处理
            for v in g[u]:
                if son[u] != v != fa[u]:
                    st.append((v, False, True))  # 轻儿子先处理
        else:
            for v in g[u]:  # 处理所有轻儿子的贡献
                if son[u] != v != fa[u]:
                    for i in range(dfn[v], dfn[v] + size[v]):
                        c = a[rank[i]]
                        cnt[c] += 1
                        cs[cnt[c]] += 1
            c = a[u]  # 三行本节点贡献答案
            cnt[c] += 1
            cs[cnt[c]] += 1
            for i, k in qs[u]:
                ans[i] = cs[k]
            if not keep:  # 如果本子树是轻儿子，那就移除贡献
                for i in range(dfn[u], dfn[u] + size[u]):
                    c = a[rank[i]]
                    cs[cnt[c]] -= 1
                    cnt[c] -= 1

    print(*ans, sep='\n')
