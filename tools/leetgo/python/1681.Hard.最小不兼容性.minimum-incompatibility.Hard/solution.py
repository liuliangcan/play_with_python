# Created by Bob at 2023/06/28 10:40
# https://leetcode.cn/problems/minimum-incompatibility/

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

# 枚举子集dp/combinations
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = Counter(nums)
        if max(cnt.values()) > k:
            return -1
        m = n // k
        if m == 1:
            return 0
        p = {}
        for i in range(1 << n):
            if i.bit_count() == m:
                s = set()
                for j in range(i.bit_length()):
                    if i >> j & 1:
                        if nums[j] in s:
                            break
                        s.add(nums[j])
                else:
                    p[i] = max(s) - min(s)

        @cache
        def dfs(mask):
            if not mask:
                return 0
            ans = inf
            for j, v in p.items():
                if (j & mask) == j:
                    ans = min(ans, p[j] + dfs(mask ^ j))
            # j = mask
            # while j:
            #     if j in p:
            #         ans = min(ans, p[j] + dfs(mask ^ j))
            #     j = (j - 1) & mask
            return ans

        return dfs((1 << n) - 1)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumIncompatibility(nums, k)
    print("output:", serialize(ans))
