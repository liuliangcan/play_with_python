# Created by Bob at 2023/08/03 10:43
# https://leetcode.cn/problems/remove-comments/

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
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        p = False
        st = []
        for line in source:
            i, n = 0, len(line)
            while i < n:
                if p:
                    if line[i:i+2] == '*/':
                        p = False
                        i += 1
                else:
                    x = line[i:i+2]
                    if x == '//':
                        break
                    elif x == '/*':
                        p = True
                        i += 2
                        continue
                    st.append(line[i])
                i += 1

            if not p and st:
                ans.append(''.join(st))
                st = []
        return ans

# @lc code=end

if __name__ == "__main__":
    source: List[str] = deserialize("List[str]", read_line())
    ans = Solution().removeComments(source)
    print("output:", serialize(ans))
