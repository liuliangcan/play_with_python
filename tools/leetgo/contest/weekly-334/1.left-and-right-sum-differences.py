# Created by Bob at 2023/02/26 10:30
# https://leetcode.cn/problems/left-and-right-sum-differences/
# https://leetcode.cn/contest/weekly-contest-334/problems/left-and-right-sum-differences/

"""
6369. 左右元素和的差值 (Easy)

给你一个下标从 **0** 开始的整数数组 `nums` ，请你找出一个下标从 **0** 开始的整数数组
`answer` ，其中：

- `answer.length == nums.length`
- `answer[i] = |leftSum[i] - rightSum[i]|`

其中：

- `leftSum[i]` 是数组 `nums` 中下标 `i` 左侧元素之和。如果不存在对应的元素，
`leftSum[i] = 0` 。
- `rightSum[i]` 是数组 `nums` 中下标 `i` 右侧元素之和。如果不存在对应的元素，
`rightSum[i] = 0` 。

返回数组 `answer` 。

**示例 1：**

```
输入：nums = [10,4,8,3]
输出：[15,1,11,22]
解释：数组 leftSum 为 [0,10,14,22] 且数组 rightSum 为 [15,11,3,0] 。
数组 answer 为 [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] =
[15,1,11,22] 。

```

**示例 2：**

```
输入：nums = [1]
输出：[0]
解释：数组 leftSum 为 [0] 且数组 rightSum 为 [0] 。
数组 answer 为 [|0 - 0|] = [0] 。

```

**提示：**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10⁵`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        n = len(nums)
        ans = [0] *n
        p  = 0
        for i in range(n):
            s -= nums[i]
            ans[i] =  abs(p - s)
            p += nums[i]
        return ans


# @lc code=end
