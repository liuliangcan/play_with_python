"""主席树，可持久化线段树， 可以O(lg)查询
1. 某个区间的kth
2. 某个区间<=X的数量以及求和

什么是可持久化：
1. 可持久化线段树，可以保存每个版本的线段树信息。
2. 这里每个版本指的是从数组从左向右遍历时，加到树里后的一颗线段树信息，那么下标i就是第i个版本。
3. 这样利用前缀和的思想，pre[r]-pre[l-1]就是 [l,r]的信息了。  注意：由于是前缀和，所以原数组不能修改
4. 要求kth，要建立一颗值域线段树，然后通过二分的思想，看左右两边的数字数量，来逼近kth是几，那么就要离散化一下。

解释一下如何持久化：
1. 想像一颗普通的线段树，对某一个节点修改时，自底向上，其实只修改了log个节点，即这颗叶子到根的链。
2. 即修改过程产生了一个新的根，而一个根其实就代表一棵树。
3. 那么我不动原来的节点（和根）， 直接把新的根代表新的状态，并且把新的节点连到对应的左右儿子上，会发现从根开始的树，均是完整的。 这样每个节点不止有一个父亲了，其实也就对应了它在多个版本上
4. 每次修改多log（树高）个节点，因此修改空间复杂度是O(nlogn)，加上初始树的空间复杂度是O(4n),最后创建26n其实就差不多了

打这个板子之前我以为小波矩阵就够了，结果这题小波矩阵卡在TLE边缘，还是线段树nb
例题：
    1. LC3762. 使数组元素相等的最小操作次数 https://leetcode.cn/problems/minimum-operations-to-equalize-subarrays/  要快速查询区间中位数，以及左右两边数字数量

"""

import bisect
from typing import List


class PersistentSegmentTree:

    def __init__(self, data: List[int]):
        self.n = len(data)

        self.sorted_b = sorted(list(set(data)))
        self.m = len(self.sorted_b)
        self.rank = {x: i for i, x in enumerate(self.sorted_b)}

        # 步骤2：预估最大节点数（n×26，覆盖n*4+n*21的最坏情况）
        self.max_nodes = self.n * 26
        # 提前初始化4个一维数组（长度=max_nodes，初始值0）
        self.left = [0] * self.max_nodes  # 左子树索引
        self.right = [0] * self.max_nodes  # 右子树索引
        self.count = [0] * self.max_nodes  # 元素个数
        self.sum_val = [0] * self.max_nodes  # 元素总和
        self.size = 1  # 记录当前已使用的节点数（索引0为默认空节点，从1开始分配）

        # 步骤3：构建前缀版本的主席树
        self.root = [0] * (self.n + 1)  # root[i]：前i个元素的根节点索引
        for i in range(1, self.n + 1):
            val = data[i - 1]
            r = self.rank[val]
            self.root[i] = self._update(self.root[i - 1], 0, self.m - 1, r, val)

    def _update(self, node_idx: int, l: int, r: int, pos: int, val: int) -> int:
        """更新：使用预分配数组，用self.size分配新节点"""
        # 1. 分配新节点（直接使用self.size作为索引）
        new_node_idx = self.size
        self.size += 1
        # 安全检查：避免预估节点数不足（题目约束下不会触发）
        assert self.size < self.max_nodes, "预估节点数不足，请增大max_nodes"

        # 2. 复制原节点的左/右子树索引
        self.left[new_node_idx] = self.left[node_idx]
        self.right[new_node_idx] = self.right[node_idx]
        # 更新当前节点的count和sum_val
        self.count[new_node_idx] = self.count[node_idx] + 1
        self.sum_val[new_node_idx] = self.sum_val[node_idx] + val

        # 3. 叶子节点直接返回
        if l == r:
            return new_node_idx

        # 4. 递归更新左/右子树（核心逻辑不变）
        mid = (l + r) // 2
        if pos <= mid:
            # 更新原节点的左子树，绑定到新节点
            child_idx = self._update(self.left[node_idx], l, mid, pos, val)
            self.left[new_node_idx] = child_idx
        else:
            # 更新原节点的右子树，绑定到新节点
            child_idx = self._update(self.right[node_idx], mid + 1, r, pos, val)
            self.right[new_node_idx] = child_idx

        return new_node_idx

    def query_kth(self, L: int, R: int, k: int) -> int:
        """查询区间[L, R]的第k小元素（0-based）"""
        left_root = self.root[L]
        right_root = self.root[R + 1]
        l_bound, r_bound = 0, self.m - 1

        while l_bound < r_bound:
            mid = (l_bound + r_bound) // 2
            left_count = self.count[self.left[right_root]] - self.count[self.left[left_root]]
            if left_count > k:
                right_root = self.left[right_root]
                left_root = self.left[left_root]
                r_bound = mid
            else:
                k -= left_count
                right_root = self.right[right_root]
                left_root = self.right[left_root]
                l_bound = mid + 1

        return self.sorted_b[l_bound]

    def query_count_sum(self, L: int, R: int, x: int) -> tuple:
        """查询区间[L, R]中<=x的元素个数和总和"""
        pos = bisect.bisect_right(self.sorted_b, x) - 1
        if pos < 0:
            return 0, 0
        left_root = self.root[L]
        right_root = self.root[R + 1]
        return self._query(pos, 0, self.m - 1, left_root, right_root)

    def _query(self, pos: int, l: int, r: int, left_root: int, right_root: int) -> tuple:
        """递归查询版本差"""
        if r <= pos:
            cnt = self.count[right_root] - self.count[left_root]
            sm = self.sum_val[right_root] - self.sum_val[left_root]
            return cnt, sm

        mid = (l + r) // 2
        total_cnt, total_sum = 0, 0

        # 查询左子树
        left_cnt, left_sum = self._query(pos, l, mid, self.left[left_root], self.left[right_root])
        total_cnt += left_cnt
        total_sum += left_sum

        # 查询右子树（需要时）
        if mid < pos:
            right_cnt, right_sum = self._query(pos, mid + 1, r, self.right[left_root], self.right[right_root])
            total_cnt += right_cnt
            total_sum += right_sum

        return total_cnt, total_sum
