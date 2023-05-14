# Created by Bob at 2023/05/14 12:05
# https://leetcode.cn/problems/distant-barcodes/

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
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        n = len(barcodes)
        ans = [0] * n
        cnt = sorted([(v, k) for k, v in cnt.items()])
        m = len(range(0, n, 2))
        p = []
        while len(p) < m:
            v, k = cnt.pop()
            p.extend([k] * v)
            if len(p) > m:
                cnt.append((len(p) - m, k))
                p = p[:m]
        ans[0:n:2] = p
        v = 0
        for i in range(1, n, 2):
            if v == 0:
                v, k = cnt.pop()
            ans[i] = k
            v -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    barcodes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().rearrangeBarcodes(barcodes)
    print("output:", serialize(ans))
