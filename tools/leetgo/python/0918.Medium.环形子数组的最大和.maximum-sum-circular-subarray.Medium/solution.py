# Created by Bob at 2023/07/20 12:02
# https://leetcode.cn/problems/maximum-sum-circular-subarray/

from typing import *
from leetgo_py import *
from bisect import *
from collections import *
from heapq import *
from typing import List
from itertools import *
from math import inf
from functools import cache

# @lc code=begin
from sortedcontainers import SortedList


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        p = 0
        mx = mn = 0
        ans = max(nums)
        if ans <= 0:
            return ans
        s = sum(nums)
        for v in nums:
            p += v
            ans = max(ans, p - mn, s - p + mx)  # 最大子段、s-最小子段(不可尝试移除整个数组,这种最优解只会是max(nums)<=0,特判)
            mn = min(mn, p)
            mx = max(mx, p)
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubarraySumCircular(nums)
    print("output:", serialize(ans))
