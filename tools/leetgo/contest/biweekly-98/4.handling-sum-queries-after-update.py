# Created by Bob at 2023/02/18 22:30
# https://leetcode.cn/problems/handling-sum-queries-after-update/
# https://leetcode.cn/contest/biweekly-contest-98/problems/handling-sum-queries-after-update/

"""
6358. 更新数组后处理求和查询 (Hard)

给你两个下标从 **0** 开始的数组 `nums1` 和 `nums2` ，和一个二维数组 `queries`
表示一些操作。总共有 3 种类型的操作：

1. 操作类型 1 为 `queries[i] = [1, l, r]` 。你需要将 `nums1` 从下标 `l`
到下标 `r` 的所有 `0` 反转成 `1` 或将 `1` 反转成 `0` 。 `l` 和 `r` 下标都从
**0** 开始。
2. 操作类型 2 为 `queries[i] = [2, p, 0]` 。对于 `0 <= i < n`
中的所有下标，令 `nums2[i] = nums2[i] + nums1[i] * p` 。
3. 操作类型 3 为 `queries[i] = [3, 0, 0]` 。求 `nums2` 中所有元素的和。

请你返回一个数组，包含所有第三种操作类型的答案。

**示例 1：**

```
输入：nums1 = [1,0,1], nums2 = [0,0,0], queries =
[[1,1,1],[2,1,0],[3,0,0]]
输出：[3]
解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1]
，所以第三个操作的答案为 3 。所以返回 [3] 。

```

**示例 2：**

```
输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
输出：[5]
解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。

```

**提示：**

- `1 <= nums1.length,nums2.length <= 10⁵`
- `nums1.length = nums2.length`
- `1 <= queries.length <= 10⁵`
- `queries[i].length = 3`
- `0 <= l <= r <= nums1.length - 1`
- `0 <= p <= 10⁶`
- `0 <= nums1[i] <= 1`
- `0 <= nums2[i] <= 10⁹`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


class IntervalTree:
    def __init__(self, size):
        self.size = size
        self.interval_tree = [0 for _ in range(size * 4)]
        self.lazys = [0 for _ in range(size * 4)]

    def give_lay_to_son(self, p, l, r):
        interval_tree = self.interval_tree
        lazys = self.lazys
        if lazys[p] == 0:
            return
        mid = (l + r) // 2
        interval_tree[p * 2] = mid - l + 1 - interval_tree[p * 2]
        interval_tree[p * 2 + 1] = r - mid - interval_tree[p * 2 + 1]
        lazys[p * 2] ^= 1
        lazys[p * 2 + 1] ^= 1
        lazys[p] = 0

    def update(self, p, l, r, x, y, val):
        """
        把[x,y]区域全变成val
        """
        if y < l or r < x:
            return
        interval_tree = self.interval_tree
        lazys = self.lazys
        if x <= l and r <= y:
            interval_tree[p] = r - l + 1 - interval_tree[p]
            lazys[p] ^= 1
            return
        self.give_lay_to_son(p, l, r)
        mid = (l + r) // 2
        if x <= mid:
            self.update(p * 2, l, mid, x, y, val)
        if mid < y:
            self.update(p * 2 + 1, mid + 1, r, x, y, val)
        interval_tree[p] = interval_tree[p * 2] + interval_tree[p * 2 + 1]

    def query(self, p, l, r, x, y):
        """
        区间求和      """

        if y < l or r < x:
            return 0
        if x <= l and r <= y:
            return self.interval_tree[p]
        self.give_lay_to_son(p, l, r)
        mid = (l + r) // 2
        s = 0
        if x <= mid:
            s += self.query(p * 2, l, mid, x, y)
        if mid < y:
            s += self.query(p * 2 + 1, mid + 1, r, x, y)
        return s


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        s = sum(nums2)
        tree = IntervalTree(n)
        for i, v in enumerate(nums1, start=1):
            if v:
                tree.update(1, 1, n, i, i, 1)
        ans = []
        for op, l, r in queries:
            if op == 1:
                tree.update(1, 1, n, l + 1, r + 1, 1)
            elif op == 2:
                s += l * tree.query(1, 1, n, 1, n)
            else:
                ans.append(s)
        return ans
# @lc code=end
