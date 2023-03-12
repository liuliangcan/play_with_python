# Created by Bob at 2023/03/12 10:30
# https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/
# https://leetcode.cn/contest/weekly-contest-336/problems/minimum-time-to-complete-all-tasks/

"""
6318. 完成所有任务的最少时间 (Hard)

你有一台电脑，它可以 **同时** 运行无数个任务。给你一个二维整数数组 `tasks` ，其中 `tasks[i] =
[startᵢ, endᵢ, durationᵢ]` 表示第 `i` 个任务需要在 **闭区间** 时间段
`[startᵢ, endᵢ]` 内运行 `durationᵢ` 个整数时间点（但不需要连续）。

当电脑需要运行任务时，你可以打开电脑，如果空闲时，你可以将电脑关闭。

请你返回完成所有任务的情况下，电脑最少需要运行多少秒。

**示例 1：**

```
输入：tasks = [[2,3,1],[4,5,1],[1,5,2]]
输出：2
解释：
- 第一个任务在闭区间 [2, 2] 运行。
- 第二个任务在闭区间 [5, 5] 运行。
- 第三个任务在闭区间 [2, 2] 和 [5, 5] 运行。
电脑总共运行 2 个整数时间点。

```

**示例 2：**

```
输入：tasks = [[1,3,2],[2,5,3],[5,6,2]]
输出：4
解释：
- 第一个任务在闭区间 [2, 3] 运行
- 第二个任务在闭区间 [2, 3] 和 [5, 5] 运行。
- 第三个任务在闭区间 [5, 6] 运行。
电脑总共运行 4 个整数时间点。

```

**提示：**

- `1 <= tasks.length <= 2000`
- `tasks[i].length == 3`
- `1 <= startᵢ, endᵢ <= 2000`
- `1 <= durationᵢ <= endᵢ - startᵢ + 1 `
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList
class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:x[1])
        work = [0] * 2001
        for s,e,d in tasks:
            d -= sum(work[s:e+1])
            if d > 0:
                for i in range(e,s-1,-1):
                    if not work[i]:
                        work[i] = 1
                        d -= 1
                        if not d:
                            break
        return sum(work)

# @lc code=end
