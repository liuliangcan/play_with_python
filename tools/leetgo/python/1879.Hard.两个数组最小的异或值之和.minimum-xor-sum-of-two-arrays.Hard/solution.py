# Created by Bob at 2023/07/14 10:35
# https://leetcode.cn/problems/minimum-xor-sum-of-two-arrays/

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
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        mask = 1 << n
        f = [inf] * mask
        f[0] = 0
        for i in range(1, mask):
            size = i.bit_count()
            p = nums1[size - 1]
            for j in range(n):
                if i >> j & 1:
                    f[i] = min(f[i], f[i ^ (1 << j)] + (p ^ nums2[j]))
        return f[-1]


# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumXORSum(nums1, nums2)
    print("output:", serialize(ans))
