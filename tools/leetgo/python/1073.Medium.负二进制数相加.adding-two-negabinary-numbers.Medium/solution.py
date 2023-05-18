# Created by Bob at 2023/05/18 14:33
# https://leetcode.cn/problems/adding-two-negabinary-numbers/

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
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a = arr1[::-1]
        b = arr2[::-1]
        if len(a) > len(b):
            a, b = b, a
        a += [0] * (len(b) - len(a))
        a += [0] * 2
        b += [0] * 2
        n = len(a)
        ans = [0] * n
        for i, (x, y) in enumerate(zip(a, b)):
            ans[i] += x + y
            while ans[i] >= 2:
                ans[i] -= 2
                if ans[i + 1]:
                    ans[i + 1] -= 1
                else:
                    ans[i + 1] += 1
                    ans[i + 2] += 1

        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()

        return ans[::-1]


# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().addNegabinary(arr1, arr2)
    print("output:", serialize(ans))
