# Created by Bob at 2023/01/30 08:23
# https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

"""
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面 (Easy)

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。
**示例：**
```
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
```
**提示：**
1. `0 <= nums.length <= 50000`
2. `0 <= nums[i] <= 10000`
"""

# @lc code=begin
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] % 2 == 1:
                l += 1
            while l < r and nums[r] % 2 == 0:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        return nums

# @lc code=end
