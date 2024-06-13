"""
dfs序，把树上子树问题变成数组的区间问题
发 LeetCoin ,dfs序+rurq https://leetcode.cn/problems/coin-bonus/description/
"""

MOD = 10 ** 9 + 7


class BinIndexTreeRURQ:
    """树状数组的RURQ模型"""

    def __init__(self, size_or_nums):  # 树状数组,区间加区间求和，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.d = [0 for _ in range(self.size + 5)]
            self.d2 = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.d = [0 for _ in range(self.size + 5)]
            self.d2 = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_interval(i + 1, i + 1, v)

    def _add_point(self, c, i, v):  # 单点增加,下标从1开始;不支持直接调用，这里增加的是差分数组的单点,同步修改c2
        while i <= self.size:
            c[i] += v
            c[i] %= MOD
            i += -i & i

    def _sum_prefix(self, c, i):  # 前缀求和，下标从1开始；不支持直接调用，这里求和的是差分数组的前缀和;传入c决定怎么计算，但是不要直接调用 无视吧
        s = 0
        while i >= 1:
            s += c[i]
            s %= MOD
            i -= -i & i
        return s

    def add_interval(self, l, r, v):  # 区间加，下标从1开始，把[l,r]闭区间都加v
        self._add_point(self.d, l, v)
        self._add_point(self.d, r + 1, -v)
        self._add_point(self.d2, l, (l - 1) * v)
        self._add_point(self.d2, r + 1, -v * r)

    def sum_interval(self, l, r):  # 区间求和，下标从1开始，返回闭区间[l,r]上的求和
        return self._sum_prefix(self.d, r) * r - self._sum_prefix(self.d2, r) - self._sum_prefix(self.d, l - 1) * (
                l - 1) + self._sum_prefix(self.d2, l - 1)

    def query_point(self, i):  # 单点询问值，下标从1开始，返回i位置的值
        return self._sum_prefix(self.d, i)

    def lowbit(self, x):
        return x & -x


def get_dfs_order(g, n, start=0):  # 每个节点位置是dfs_order_pos[u],子树管辖范围[_pos[u],_pos[u]+size[u]-1]
    dfs_order = []
    fa = [-1] * n
    st = [start]
    while st:
        u = st.pop()
        dfs_order.append(u)
        for v in g[u]:
            if v == fa[u]: continue
            fa[v] = u
            st.append(v)
    size = [1] * n
    for u in dfs_order[::-1]:
        for v in g[u]:
            if v == fa[u]: continue
            size[u] += size[v]
    dfs_order_pos = [0] * n
    for i, v in enumerate(dfs_order):
        dfs_order_pos[v] = i
    return dfs_order, dfs_order_pos, size  # dfs序，每个节点在序里的位置，节点子树大小


class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n + 1)]
        for u, v in leadership:
            g[u].append(v)
        dfs_order, dfs_order_pos, size = get_dfs_order(g, n + 1, 1)
        bit = BinIndexTreeRURQ(n)
        ans = []
        for op in operations:
            if op[0] == 1:
                l = r = dfs_order_pos[op[1]] + 1
                bit.add_interval(l, r, op[2])
            elif op[0] == 2:
                l = dfs_order_pos[op[1]] + 1
                r = l + size[op[1]] - 1
                bit.add_interval(l, r, op[2])
            else:
                l = dfs_order_pos[op[1]] + 1
                r = l + size[op[1]] - 1
                ans.append(bit.sum_interval(l, r) % MOD)
        return ans


