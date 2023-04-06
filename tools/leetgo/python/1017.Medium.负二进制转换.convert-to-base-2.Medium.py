# Created by Bob at 2023/04/06 14:51
# https://leetcode.cn/problems/convert-to-base-2/

"""
1017. 负二进制转换 (Medium)
给你一个整数 `n` ，以二进制字符串的形式返回该整数的 **负二进制（ `base -2`）** 表示。

**注意，** 除非字符串就是 `"0"`，否则返回的字符串中不能含有前导零。

**示例 1：**

```
输入：n = 2
输出："110"
解释：(-2)² + (-2)¹ = 2

```

**示例 2：**

```
输入：n = 3
输出："111"
解释：(-2)² + (-2)¹ + (-2)⁰ = 3

```

**示例 3：**

```
输入：n = 4
输出："100"
解释：(-2)² = 4

```

**提示：**

- `0 <= n <= 10⁹`
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
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        s = bin(n)[2:]
        ans = [int(x) for x in s][::-1] + [0, 0]
        for i, v in enumerate(ans):
            if v == 2:
                ans[i] = 0
                ans[i + 1] += 1
            elif v == 1 and i & 1:
                ans[i + 1] += 1
        while not ans[-1]:
            ans.pop()
        ans = ans[::-1]
        return ''.join(map(str, ans))

# @lc code=end
