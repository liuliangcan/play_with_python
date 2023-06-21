# Created by Bob at 2023/06/21 15:00
# https://leetcode.cn/problems/maximum-nesting-depth-of-the-parentheses/

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
    def maxDepth(self, s: str) -> int:
        st = []
        ans = 0
        for c in s:
            if c == '(':
                st.append(c)
                ans = max(ans,len(st))
            elif c == ')':
                st.pop()
        return ans

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maxDepth(s)
    print("output:", serialize(ans))
