# Created by Bob at 2023/02/26 10:30
# https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid/
# https://leetcode.cn/contest/weekly-contest-334/problems/minimum-time-to-visit-a-cell-in-a-grid/

"""
6366. 在网格图中访问一个格子的最少时间 (Hard)

给你一个 `m x n` 的矩阵 `grid` ，每个元素都为 **非负** 整数，其中
`grid[row][col]` 表示可以访问格子 `(row, col)` 的 **最早**
时间。也就是说当你访问格子 `(row, col)` 时，最少已经经过的时间为 `grid[row][col]` 。

你从 **最左上角** 出发，出发时刻为 `0` ，你必须一直移动到上下左右相邻四个格子中的 **任意**
一个格子（即不能停留在格子上）。每次移动都需要花费 1 单位时间。

请你返回 **最早** 到达右下角格子的时间，如果你无法到达右下角的格子，请你返回 `-1` 。

**示例 1：**

![](https://assets.leetcode.com/uploads/2023/02/14/yetgriddrawio-8.png)

```
输入：grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
输出：7
解释：一条可行的路径为：
- 时刻 t = 0 ，我们在格子 (0,0) 。
- 时刻 t = 1 ，我们移动到格子 (0,1) ，可以移动的原因是 grid[0][1] <= 1 。
- 时刻 t = 2 ，我们移动到格子 (1,1) ，可以移动的原因是 grid[1][1] <= 2 。
- 时刻 t = 3 ，我们移动到格子 (1,2) ，可以移动的原因是 grid[1][2] <= 3 。
- 时刻 t = 4 ，我们移动到格子 (1,1) ，可以移动的原因是 grid[1][1] <= 4 。
- 时刻 t = 5 ，我们移动到格子 (1,2) ，可以移动的原因是 grid[1][2] <= 5 。
- 时刻 t = 6 ，我们移动到格子 (1,3) ，可以移动的原因是 grid[1][3] <= 6 。
- 时刻 t = 7 ，我们移动到格子 (2,3) ，可以移动的原因是 grid[2][3] <= 7 。
最终到达时刻为 7 。这是最早可以到达的时间。

```

**示例 2：**

![](https://assets.leetcode.com/uploads/2023/02/14/yetgriddrawio-9.png)

```
输入：grid = [[0,2,4],[3,2,1],[1,0,4]]
输出：-1
解释：没法从左上角按题目规定走到右下角。

```

**提示：**

- `m == grid.length`
- `n == grid[i].length`
- `2 <= m, n <= 1000`
- `4 <= m * n <= 10⁵`
- `0 <= grid[i][j] <= 10⁵`
- `grid[0][0] == 0`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        vis = [[10 ** 6] * n for _ in range(m)]
        vis[0][0] = 0

        q = [(0, 0, 0)]
        while q:
            d, x, y = heappop(q)

            for a, b in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= a < m and 0 <= b < n and vis[a][b] > vis[x][y] + 1:
                    w = grid[a][b]
                    if w <= vis[x][y] + 1:
                        vis[a][b] = vis[x][y] + 1
                        heappush(q, (vis[a][b], a, b))

                    elif (a + b) % 2 == 0:
                        vis[a][b] = w if w % 2 == 0 else w + 1
                        heappush(q, (vis[a][b], a, b))
                    else:
                        vis[a][b] = w if w % 2 == 1 else w + 1
                        heappush(q, (vis[a][b], a, b))
                    if a == m - 1 and b == n - 1:
                        return vis[a][b]

        return vis[m - 1][n - 1]

# @lc code=end
