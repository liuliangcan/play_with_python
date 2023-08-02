# Created by Bob at 2023/08/02 15:38
# https://leetcode.cn/problems/trapping-rain-water-ii/

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
    def trapRainWater(self, g: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        if m <= 2 or n <= 2:
            return 0
        ans = 0
        q = []
        for i in range(1, m - 1):
            q.append((g[i][0], i, 0))
            q.append((g[i][n - 1], i, n - 1))
            g[i][0] = g[i][n - 1] = -1
        for j in range(n):
            q.append((g[0][j], 0, j))
            q.append((g[m - 1][j], m - 1, j))
            g[0][j] = g[m - 1][j] = - 1

        heapify(q)
        while q:
            h, x, y = heappop(q)
            for a, b in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= a < m and 0 <= b < n and g[a][b] != -1:
                    k = max(h, g[a][b])
                    ans += k - g[a][b]
                    heappush(q, (k, a, b))
                    g[a][b] = -1
        return ans


# @lc code=end

if __name__ == "__main__":
    heightMap: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().trapRainWater(heightMap)
    print("output:", serialize(ans))
