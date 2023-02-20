# Created by Bob at 2023/02/19 10:30
# https://leetcode.cn/problems/minimum-operations-to-reduce-an-integer-to-0/
# https://leetcode.cn/contest/weekly-contest-333/problems/minimum-operations-to-reduce-an-integer-to-0/

"""
6365. 将整数减少到零需要的最少操作数 (Easy)

给你一个正整数 `n` ，你可以执行下述操作 **任意** 次：

- `n` 加上或减去 `2` 的某个 **幂**

返回使 `n` 等于 `0` 需要执行的 **最少** 操作数。

如果 `x == 2ⁱ` 且其中 `i >= 0` ，则数字 `x` 是 `2` 的幂。

**示例 1：**

```
输入：n = 39
输出：3
解释：我们可以执行下述操作：
- n 加上 2⁰ = 1 ，得到 n = 40 。
- n 减去 2³ = 8 ，得到 n = 32 。
- n 减去 2⁵ = 32 ，得到 n = 0 。
可以证明使 n 等于 0 需要执行的最少操作数是 3 。

```

**示例 2：**

```
输入：n = 54
输出：3
解释：我们可以执行下述操作：
- n 加上 2¹ = 2 ，得到 n = 56 。
- n 加上 2³ = 8 ，得到 n = 64 。
- n 减去 2⁶ = 64 ，得到 n = 0 。
使 n 等于 0 需要执行的最少操作数是 3 。

```

**提示：**

- `1 <= n <= 10⁵`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList
@cache
def dfs(x):
    if x.bit_count() == 1:
        return 1
    lb = x & -x
    return 1 + min(dfs(x+lb),dfs(x-lb))
class Solution:
    def minOperations(self, n: int) -> int:
        return dfs(n)

# @lc code=end
