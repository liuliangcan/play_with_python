# Created by Bob at 2023/04/04 11:24
# https://leetcode.cn/problems/minimum-cost-to-merge-stones/

"""
1000. 合并石头的最低成本 (Hard)
有 `N` 堆石头排成一排，第 `i` 堆中有 `stones[i]` 块石头。

每次移动（move）需要将 **连续的** `K` 堆石头合并为一堆，而这个移动的成本为这 `K` 堆石头的总数。

找出把所有石头合并成一堆的最低成本。如果不可能，返回 `-1` 。

**示例 1：**

```
输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。

```

**示例 2：**

```
输入：stones = [3,2,4,1], K = 3
输出：-1
解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.

```

**示例 3：**

```
输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。

```

**提示：**

- `1 <= stones.length <= 30`
- `2 <= K <= 30`
- `1 <= stones[i] <= 100`
"""

from bisect import *
from collections import *
from functools import cache
from heapq import *
from itertools import *
from math import inf
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1
        pre = [0] + list(accumulate(stones))

        @cache
        def dfs(l, r, p):  # [l,r]区间变成p组的最小代价
            d = r - l + 1  # 计算区间长度
            if d < p:  # 如果这个区间根本不够p个数，无法变p组
                return inf
            elif d == p:  # 如果正好p个数，不用变
                return 0
            if p == 1 and d == k:  # 如果是k个数变一组就是加起来
                return pre[r + 1] - pre[l]
            ans = inf
            if p == 1:  # 如果目标一组，那只能是1组+k-1组，增加合成代价
                for i in range(l, r):  # 枚举最左边那组的位置
                    ans = min(ans, dfs(l, i, 1) + dfs(i + 1, r, k - 1) + pre[r + 1] - pre[l])
            else:  # 目标超过1组，则是1组+p-1组
                for i in range(l, r):  # 枚举最左边那组的位置，不用跟后边的合成
                    ans = min(ans, dfs(l, i, 1) + dfs(i + 1, r, p - 1))

            return ans

        return dfs(0, n - 1, 1)

# @lc code=end
