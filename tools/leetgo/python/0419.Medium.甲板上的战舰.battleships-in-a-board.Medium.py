# Created by Bob at 2023/04/20 18:25
# https://leetcode.cn/problems/battleships-in-a-board/

"""
419. 甲板上的战舰 (Medium)
给你一个大小为 `m x n` 的矩阵 `board` 表示甲板，其中，每个单元格可以是一艘战舰 `'X'`
或者是一个空位 `'.'` ，返回在甲板 `board` 上放置的 **战舰** 的数量。

**战舰** 只能水平或者垂直放置在 `board` 上。换句话说，战舰只能按 `1 x k`（ `1` 行， `k`
列）或 `k x 1`（ `k` 行， `1` 列）的形状建造，其中 `k`
可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/04/10/battelship-grid.jpg)

```
输入：board =
[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
输出：2

```

**示例 2：**

```
输入：board = [["."]]
输出：0

```

**提示：**

- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` 是 `'.'` 或 `'X'`

**进阶：** 你可以实现一次扫描算法，并只使用 `O(1)` 额外空间，并且不修改 `board`
的值来解决这个问题吗？
"""

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
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        ans = 0

        def dfs(x, y):
            board[x][y] = '.'
            for a, b in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= a < m and 0 <= b < n and board[a][b] == 'X':
                    dfs(a, b)

        for i, j in product(range(m), range(n)):
            if board[i][j] == 'X':
                dfs(i, j)
                ans += 1
        return ans

# @lc code=end
