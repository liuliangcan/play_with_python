# Created by Bob at 2023/05/12 14:39
# https://leetcode.cn/problems/reverse-subarray-to-maximize-array-value/

from typing import *
from leetgo_py import *
from bisect import *
from collections import *
from heapq import *
from itertools import *
from math import inf
from functools import cache

# @lc code=begin
from sortedcontainers import SortedList


class Solution:
    def maxValueAfterReverse(self, a: List[int]) -> int:
        n = len(a)
        mx, mn = -inf, inf
        ans = d = 0
        for x, y in pairwise(a):
            z = abs(x - y)
            ans += z
            d = max(d, abs(y - a[0]) - z, abs(x - a[-1]) - z)
            mx = max(mx, min(x, y))
            mn = min(mn, max(x, y))
        return ans + max(d, 2 * (mx - mn))


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxValueAfterReverse(nums)
    print("output:", serialize(ans))
