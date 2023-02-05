# Created by Bob at 2023/02/05 10:30
# https://leetcode.cn/problems/rearranging-fruits/
# https://leetcode.cn/contest/weekly-contest-331/problems/rearranging-fruits/


"""
6345. 重排水果 (Hard)

你有两个果篮，每个果篮中有 `n` 个水果。给你两个下标从 **0** 开始的整数数组 `basket1` 和
`basket2` ，用以表示两个果篮中每个水果的成本。
你希望两个果篮相等。为此，可以根据需要多次执行下述操作：
- 选中两个下标 `i` 和 `j` ，并交换 `basket1` 中的第 `i` 个水果和 `basket2` 中的第
`j` 个水果。
- 交换的成本是 `min(basket1ᵢ,basket2ⱼ)` 。
根据果篮中水果的成本进行排序，如果排序后结果完全相同，则认为两个果篮相等。
返回使两个果篮相等的最小交换成本，如果无法使两个果篮相等，则返回 `-1`。
**示例 1：**
```
输入：basket1 = [4,2,2,2], basket2 = [1,4,1,2]
输出：1
解释：交换 basket1 中下标为 1 的水果和 basket2 中下标为 0 的水果，交换的成本为 1
。此时，basket1 = [4,1,2,2] 且 basket2 = [2,4,1,2]
。重排两个数组，发现二者相等。
```
**示例 2：**
```
输入：basket1 = [2,3,4,1], basket2 = [3,2,5,1]
输出：-1
解释：可以证明无法使两个果篮相等。
```
**提示：**
- `basket1.length == bakste2.length`
- `1 <= basket1.length <= 10⁵`
- `1 <= basket1ᵢ,basket2ᵢ <= 10⁹`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # print(sorted(basket1))
        # print(sorted(basket2))
        n = len(basket1)
        cnt = Counter(basket1 + basket2)
        if any(x & 1 for x in cnt.values()):
            return -1
        c1 = Counter(basket1)
        c2 = Counter(basket2)
        a = []
        for k, v in c1.items():
            d = v - c2[k]
            if d > 0:
                if d & 1:
                    return -1
                a.append((k, d // 2))
        b = []
        for k, v in c2.items():
            d = v - c1[k]
            if d > 0:
                if d & 1:
                    return -1
                b.append([k, d // 2])
        mn = min(cnt.keys())
        a.sort()
        b.sort()
        # print(a,b)
        j = len(b) - 1
        ans = 0
        for x, y in a:
            while y:
                if j < 0:
                    return -1
                d = min(b[j][1], y)
                y -= d
                b[j][1] -= d
                p = min(x, b[j][0], mn * 2)
                ans += p * d
                if not b[j][1] and j >= 0:
                    j -= 1
        if b and b[0][1] > 0:
            return -1
        return ans

# @lc code=end
