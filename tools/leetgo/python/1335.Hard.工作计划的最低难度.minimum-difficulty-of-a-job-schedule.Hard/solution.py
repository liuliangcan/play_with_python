# Created by Bob at 2023/05/16 13:05
# https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/

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
    def minDifficulty1(self, job: List[int], d: int) -> int:
        # 732ms
        n = len(job)
        if n < d:
            return -1
        f = [inf] * (n + 1)
        f[0] = 0
        for i in range(1, d + 1):
            for j in range(n - 1, -1, -1):
                mx = 0
                f[j + 1] = inf
                for k in range(j, i - 2, -1):
                    mx = max(mx, job[k])
                    f[j + 1] = min(f[j + 1], f[k] + mx)

        return f[-1]

    def minDifficulty(self, job: List[int], d: int) -> int:
        n = len(job)
        if n < d:
            return -1
        f = list(accumulate(job, max))  # 第1日的情况先算出来

        for i in range(1, d):
            g = f  # 滚动
            f = [inf] * n
            st = []  # 存(left[j]，被j消掉的区间的mn(g)（即min(g[left[j],j-1]  )
            for j in range(i, n):
                mn = g[j - 1]  # 只用job[j],则从g[j-1]转移
                while st and job[st[-1][0]] <= job[j]:
                    mn = min(mn, st.pop()[1])  # st[-1]要被j消掉，那么把这个mn继承到j上
                f[j] = job[j] + mn  # 从mn(min(g[left[j],j-1])转移
                if st:
                    f[j] = min(f[j], f[st[-1][0]])  # 从left[j]转移
                st.append((j, mn))

        return f[-1]


# @lc code=end

if __name__ == "__main__":
    jobDifficulty: List[int] = deserialize("List[int]", read_line())
    d: int = deserialize("int", read_line())
    ans = Solution().minDifficulty(jobDifficulty, d)
    print("output:", serialize(ans))
