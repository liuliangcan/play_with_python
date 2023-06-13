"""倍增法求LCA：灵神文字版 https://leetcode.cn/problems/kth-ancestor-of-a-tree-node/solution/mo-ban-jiang-jie-shu-shang-bei-zeng-suan-v3rw/"""

class BinLiftingLCA:
    """倍增法求LCA，这是离线的过程，本质是DP。预处理O(nlogn),查询O(logn)"""
    def __init__(self, edges: list[list[int]]):
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y in edges:  # 节点编号从 0 开始
            g[x].append(y)
            g[y].append(x)

        depth = [0] * n
        pa = [[-1] * m for _ in range(n)]  # pa[x][i]代表x节的第2^i个祖先

        def dfs(x: int, fa: int) -> None:  # 预处理每个节的深度，顺便计算每个节点直接父亲
            pa[x][0] = fa
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dfs(y, x)

        dfs(0, -1)

        # 刷表法，一般地,pa[x][i+1]=pa[pa[x][i]][i]。如果pa[x][i]=-1,则pa[x][i+1]=-1
        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]
        self.depth = depth
        self.pa = pa

    def get_kth_ancestor(self, node: int, k: int) -> int:
        """获取node的第k个祖先，思路是把k二进制分解，然后走倍增的路径。
            注:若不保证node的第k个祖先必在树上，即可能比根还高，那么逆序遍历位可以更快的遇到-1退出；但在lca里其实不需要这样，而且这里优化很小"""
        for i in range(k.bit_length()):
            if (k >> i) & 1:  # k 二进制从低到高第 i 位是 1
                node = self.pa[node][i]
                # if node<0:break
        return node


    def get_lca(self, x: int, y: int) -> int:
        """返回 x 和 y 的最近公共祖先（节点编号从 0 开始）
            思路是先让x,y处于同一层，通过kth跳。
            然后尝试迈大步(2^i步),若迈完发现变成同节点就不迈了，尝试2^(i-1)步。
            最后答案pa[x][0],即x、y一定在lca的直接儿子上，"""
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使 y 和 x 在同一深度
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时上跳 2**i 步
        return self.pa[x][0]
