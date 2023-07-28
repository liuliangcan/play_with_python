# Created by Bob at 2023/07/28 11:43
# https://leetcode.cn/problems/parallel-courses-iii/

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
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # g = [[] for _ in range(n)]
        # indeg = [0] * n
        # for u, v in relations:
        #     g[u - 1].append(v - 1)
        #     indeg[v - 1] += 1
        # f = time[:]
        # q = deque([i for i, v in enumerate(indeg) if v == 0])
        # while q:
        #     u = q.popleft()
        #     for v in g[u]:
        #         f[v] = max(f[v], f[u] + time[v])
        #         indeg[v] -= 1
        #         if indeg[v] == 0:
        #             q.append(v)
        # return max(f)
        dependence = [[] for _ in range(n)]
        for u, v in relations:
            dependence[v - 1].append(u - 1)

        @cache
        def f(v):
            return max((f(u) for u in dependence[v]), default=0) + time[v]

        return max(f(i) for i in range(n))


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    relations: List[List[int]] = deserialize("List[List[int]]", read_line())
    time: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumTime(n, relations, time)
    print("output:", serialize(ans))
