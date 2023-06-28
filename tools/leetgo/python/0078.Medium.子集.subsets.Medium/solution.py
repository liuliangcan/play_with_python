# Created by Bob at 2023/06/28 11:34
# https://leetcode.cn/problems/subsets/

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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return list(chain(*[combinations(nums,i) for i in range(len(nums)+1)]))
        n = len(nums)
        mask = (1 << n) - 1
        s = mask
        ans = []
        while True:
            cur = []
            for j in range(s.bit_length()):
                if s >> j & 1:
                    cur.append(nums[j])
            ans.append(cur)
            s = (s - 1) & mask
            if s == mask: break
        return ans

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().subsets(nums)
    print("output:", serialize(ans))
