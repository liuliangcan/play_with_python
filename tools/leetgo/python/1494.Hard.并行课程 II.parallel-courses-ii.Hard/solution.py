# Created by Bob at 2023/06/16 16:47
# https://leetcode.cn/problems/parallel-courses-ii/

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
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        mask = 1 << n
        need = [0] * mask
        for u, v in relations:
            u -= 1
            v -= 1
            need[1 << v] |= 1 << u
        for i in range(1, mask):
            j = i
            while j:
                lb = j & -j
                need[i] |= need[lb]
                j ^= lb

        f = [inf] * mask
        f[0] = 0

        for i in range(1, mask):
            if need[i] & i != need[i]: continue  # i存在前置课程没学，这个状态就非法

            p = j = i ^ need[i]  # 当前状态去除前置，则是最后一学期可以学的课
            if j.bit_count() <= k:  # 如果这学期要学的少于k，则可以直接学
                f[i] = f[need[i]] + 1
                continue
            while j:
                if j.bit_count() == k:
                    f[i] = min(f[i], f[i ^ j] + 1)
                j = (j - 1) & p
        # print(f)
        # print(need)
        return f[-1]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    relations: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minNumberOfSemesters(n, relations, k)
    print("output:", serialize(ans))
