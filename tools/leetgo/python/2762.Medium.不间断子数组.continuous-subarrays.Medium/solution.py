# Created by Bob at 2023/07/04 16:31
# https://leetcode.cn/problems/continuous-subarrays/

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
    def continuousSubarrays(self, nums: List[int]) -> int:
        mx, mn = deque(), deque()
        ans = 0
        l = 0
        for r, v in enumerate(nums):
            while mn and v <= nums[mn[-1]]:
                mn.pop()
            mn.append(r)
            while mx and v >= nums[mx[-1]]:
                mx.pop()
            mx.append(r)
            while nums[mx[0]] - nums[mn[0]] > 2:
                l += 1
                if mn[0] < l:
                    mn.popleft()
                if mx[0] < l:
                    mx.popleft()
            ans += r - l + 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().continuousSubarrays(nums)
    print("output:", serialize(ans))
