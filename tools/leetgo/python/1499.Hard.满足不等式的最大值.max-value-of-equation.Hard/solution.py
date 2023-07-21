# Created by Bob at 2023/07/21 10:07
# https://leetcode.cn/problems/max-value-of-equation/

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
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:

        ans = -inf
        # (yi-xi) + (yj+xj)
        h = []
        for x, y in points:
            while h and h[0][1]+k < x:
                heappop(h)
            if h:
                ans = max(ans, -h[0][0]+x+y)
            heappush(h,(x-y,x))
        return ans


# @lc code=end

if __name__ == "__main__":
    points: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findMaxValueOfEquation(points, k)
    print("output:", serialize(ans))
