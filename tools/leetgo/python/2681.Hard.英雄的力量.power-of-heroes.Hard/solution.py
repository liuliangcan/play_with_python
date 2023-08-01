# Created by Bob at 2023/08/01 10:26
# https://leetcode.cn/problems/power-of-heroes/

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
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        p = ans = 0
        nums.sort()
        for v in nums:
            ans = (ans + v * v * (p + v)) % MOD
            p = (p * 2 + v) % MOD
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumOfPower(nums)
    print("output:", serialize(ans))
