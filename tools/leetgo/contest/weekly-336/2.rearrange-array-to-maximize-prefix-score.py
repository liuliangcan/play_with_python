# Created by Bob at 2023/03/12 10:30
# https://leetcode.cn/problems/rearrange-array-to-maximize-prefix-score/
# https://leetcode.cn/contest/weekly-contest-336/problems/rearrange-array-to-maximize-prefix-score/

"""
6316. 重排数组以得到最大前缀分数 (Medium)

给你一个下标从 **0** 开始的整数数组 `nums` 。你可以将 `nums` 中的元素按 **任意顺序**
重排（包括给定顺序）。

令 `prefix` 为一个数组，它包含了 `nums` 重新排列后的前缀和。换句话说， `prefix[i]` 是
`nums` 重新排列后下标从 `0` 到 `i` 的元素之和。 `nums` 的 **分数** 是 `prefix`
数组中正整数的个数。

返回可以得到的最大分数。

**示例 1：**

```
输入：nums = [2,-1,0,1,-3,3,-3]
输出：6
解释：数组重排为 nums = [2,3,1,-1,-3,0,-3] 。
prefix = [2,5,6,5,2,2,-1] ，分数为 6 。
可以证明 6 是能够得到的最大分数。

```

**示例 2：**

```
输入：nums = [-2,-3,0]
输出：0
解释：不管怎么重排数组得到的分数都是 0 。

```

**提示：**

- `1 <= nums.length <= 10⁵`
- `-10⁶ <= nums[i] <= 10⁶`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        p = list(accumulate(nums))
        return sum(x>0 for x in p )

# @lc code=end
