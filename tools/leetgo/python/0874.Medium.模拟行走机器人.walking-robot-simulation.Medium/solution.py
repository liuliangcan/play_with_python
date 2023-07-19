# Created by Bob at 2023/07/19 14:40
# https://leetcode.cn/problems/walking-robot-simulation/

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
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, col = defaultdict(list), defaultdict(list)
        for x, y in obstacles:
            row[x].append(y)
            col[y].append(x)
        for x in row.values():
            x.sort()
        for x in col.values():
            x.sort()
        x = y = 0
        ans = d = 0
        for c in commands:
            if c < 0:
                d = (d + c * 2 + 3) % 4
            else:
                dx, dy = DIRS[d]
                # print(d,dx,dy)
                a, b = x + dx * c, y + dy * c
                if d & 1:
                    li = col[y]
                    if d == 1:
                        p = bisect_right(li, x)
                        if p == len(li) or li[p] > a:
                            x = a
                        else:
                            x = li[p] - 1
                    else:
                        p = bisect_left(li, x)
                        if p == 0 or li[p - 1] < a:
                            x = a
                        else:
                            x = li[p - 1] + 1
                else:
                    li = row[x]
                    # print(c,d,x,y,a,b,li)
                    if d == 0:
                        p = bisect_right(li, y)
                        if p == len(li) or li[p] > b:
                            y = b
                        else:
                            y = li[p] - 1
                    else:
                        p = bisect_left(li, y)
                        if p == 0 or li[p - 1] < b:
                            y = b
                        else:
                            y = li[p - 1] + 1
                    # print(x,y)
                ans = max(ans, x * x + y * y)
        return ans


# @lc code=end

if __name__ == "__main__":
    commands: List[int] = deserialize("List[int]", read_line())
    obstacles: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().robotSim(commands, obstacles)
    print("output:", serialize(ans))
