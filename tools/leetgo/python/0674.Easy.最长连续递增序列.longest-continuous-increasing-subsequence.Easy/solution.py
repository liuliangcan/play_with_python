# Created by Bob at 2023/06/21 15:18
# https://leetcode.cn/problems/longest-continuous-increasing-subsequence/

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
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1]*n
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                f[i] += f[i-1]
        return max(f)

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findLengthOfLCIS(nums)
    print("output:", serialize(ans))
