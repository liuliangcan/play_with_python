# Created by Bob at 2023/06/21 15:05
# https://leetcode.cn/problems/permutation-ii-lcci/

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
    def permutation(self, S: str) -> List[str]:
        s = sorted(S)
        n = len(s)
        ans = []
        path = []
        used = [False] * n

        def dfs():
            if len(path) == n:
                ans.append(''.join(path))
            for i, c in enumerate(s):
                if i and s[i] == s[i - 1] and used[i-1]:
                    continue
                if used[i]:
                    continue
                used[i] = True
                path.append(c)
                dfs()
                path.pop()
                used[i] = False
        dfs()
        return ans


# @lc code=end

if __name__ == "__main__":
    S: str = deserialize("str", read_line())
    ans = Solution().permutation(S)
    print("output:", serialize(ans))
