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
        n = len(nums)
        f = [0]*n
        f[0] = nums[0]
        for i in range(n):
            f[i] = max(f[i-1],0)+nums[i]
        ans = max(f)
        if ans > 0:
            mn = inf
            p,pmx = 0,0
            for v in nums:
                p += v
                mn = min(mn,p-pmx)
                pmx = max(pmx,p)
            ans = max(ans,sum(nums)-mn)
        return ans

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubarraySumCircular(nums)
    print("output:", serialize(ans))
