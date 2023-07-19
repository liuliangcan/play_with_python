# Created by Bob at 2023/07/19 15:31
# https://leetcode.cn/problems/boats-to-save-people/

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
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0
        while l < r:
            while l < r and people[l] + people[r] > limit:
                # print(l,r)
                ans += 1
                r -= 1
            if l == r:
                break
            ans += 1
            l += 1
            r -= 1
        return ans + (l == r)


# @lc code=end

if __name__ == "__main__":
    people: List[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().numRescueBoats(people, limit)
    print("output:", serialize(ans))
