# Created by Bob at 2023/05/25 10:21
# https://leetcode.cn/problems/longest-cycle-in-a-graph/

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
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        time = [0] * n
        clock = 1
        ans = -1
        for i, t in enumerate(time):
            if t: continue
            start_time = clock
            while i != -1:
                if time[i]:
                    if time[i] >= start_time:
                        ans = max(ans, clock - time[i])
                    break
                time[i] = clock
                clock += 1
                i = edges[i]
        return ans


# @lc code=end

if __name__ == "__main__":
    edges: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestCycle(edges)
    print("output:", serialize(ans))
