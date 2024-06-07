"""
分块通常可以用O(n)时间预处理，使得做到O(sqrt(n))的查询、修改。并且常数较低，有时可以莽过一些题。
区间加区间求和：https://leetcode.cn/problems/coin-bonus/
另有一道分块题：
楼房重建，大意是每次修改一个数组值，问从左边能看到的单调序列长度。
    - 分块后，每块维护一个快内的单调序列。
    - 修改时，直接重建这个分块。
    - 查询时，从左向右处理，每块的有效数量是超过premax的数量，这可以二分。
    - 复杂度 O(q*sqrt(n)*lg(sqrt(n)))
"""
MOD = 10 ** 9 + 7


class FenKuai:
    """分块求和"""

    def __init__(self, nums):  # 树状数组,区间加区间求和，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        n = len(nums)
        self.block_size = max(1, isqrt(n))
        self.blocks = []
        self.f = []
        for i in range(0, n, self.block_size):
            self.blocks.append((i, min(i + self.block_size - 1, n - 1)))
            s = 0
            for j in range(i, min(i + self.block_size, n)):
                s += nums[j]
            self.f.append(s)
        self.lazy = [0] * len(self.blocks)
        self.nums = nums

    def add(self, l, r, v):
        x, y = l // self.block_size, r // self.block_size
        if x == y:
            for i in range(l, r + 1):
                self.nums[i] += v
                self.f[x] += v
        else:
            for i in range(l, self.blocks[x][1] + 1):
                self.nums[i] += v
                self.f[x] += v
            for i in range(self.blocks[y][0], r + 1):
                self.nums[i] += v
                self.f[y] += v
            for i in range(x + 1, y):
                self.lazy[i] += v
                # self.f[i] += v*(self.blocks[i][1]-self.blocks[i][0]+1)

    def query(self, l, r):
        s = 0
        x, y = l // self.block_size, r // self.block_size
        if x == y:
            s += (r - l + 1) * self.lazy[x]
            for i in range(l, r + 1):
                s += self.nums[i]
        else:
            s += (self.blocks[x][1] - l + 1) * self.lazy[x]
            for i in range(l, self.blocks[x][1] + 1):
                s += self.nums[i]
            s += (r - self.blocks[y][0] + 1) * self.lazy[y]
            for i in range(self.blocks[y][0], r + 1):
                s += self.nums[i]
            for i in range(x + 1, y):
                s += self.lazy[i] * (self.blocks[i][1] - self.blocks[i][0] + 1) + self.f[i]
        return s


def get_dfs_order(g, n, start=0):
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
    return dfs_order, dfs_order_pos, size


class Solution:
    def bonus(self, n: int, leadership: List[List[int]], operations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n + 1)]
        for u, v in leadership:
            g[u].append(v)
        dfs_order, dfs_order_pos, size = get_dfs_order(g, n + 1, 1)
        fk = FenKuai([0] * n)
        ans = []
        for op in operations:
            if op[0] == 1:
                l = r = dfs_order_pos[op[1]]
                fk.add(l, r, op[2])
            elif op[0] == 2:
                l = dfs_order_pos[op[1]]
                r = l + size[op[1]] - 1
                fk.add(l, r, op[2])
            else:
                l = dfs_order_pos[op[1]]
                r = l + size[op[1]] - 1
                # print(fk.nums,fk.lazy,fk.blocks,l,r)
                ans.append(fk.query(l, r) % MOD)
        return ans


