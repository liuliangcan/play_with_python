# Created by Bob at 2023/02/18 22:30
# https://leetcode.cn/problems/minimum-impossible-or/
# https://leetcode.cn/contest/biweekly-contest-98/problems/minimum-impossible-or/

"""
6360. 最小无法得到的或值 (Medium)

给你一个下标从 **0** 开始的整数数组 `nums` 。

如果存在一些整数满足 `0 <= index₁ < index₂ < ... < indexₖ <
nums.length` ，得到 `nums[index₁] | nums[index₂] | ... |
nums[indexₖ] = x` ，那么我们说 `x` 是 **可表达的** 。换言之，如果一个整数能由 `nums`
的某个子序列的或运算得到，那么它就是可表达的。

请你返回 `nums` 不可表达的 **最小非零整数** 。

**示例 1：**

```
输入：nums = [2,1]
输出：4
解释：1 和 2 已经在数组中，因为 nums[0] | nums[1] = 2 | 1 = 3 ，所以 3
是可表达的。由于 4 是不可表达的，所以我们返回 4 。

```

**示例 2：**

```
输入：nums = [5,3,2]
输出：1
解释：1 是最小不可表达的数字。

```

**提示：**

- `1 <= nums.length <= 10⁵`
- `1 <= nums[i] <= 10⁹`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        s = set(nums)
        i = 1
        while i in nums:
            i *= 2
        return i
# @lc code=end
