# Created by Bob at 2023/06/21 15:17
# https://leetcode.cn/problems/combinations/

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
    def combine(self, n: int, k: int) -> List[List[int]]:
        t = range(1, n + 1)
        return list(combinations(t, k))


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().combine(n, k)
    print("output:", serialize(ans))
