# Created by Bob at 2023/06/27 11:47
# https://leetcode.cn/problems/maximum-subarray-sum-with-one-deletion/

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
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        f, g = arr[:], arr[:]

        for i in range(1, n):
            if f[i - 1] > 0:
                f[i] += f[i - 1]
        for i in range(n - 2, -1, -1):
            if g[i + 1] > 0:
                g[i] += g[i + 1]
        ans = max(f)
        for i in range(1, n - 1):
            ans = max(ans, f[i - 1] + g[i + 1])
        return ans

    # @lc code=end


if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSum(arr)
    print("output:", serialize(ans))
