# Created by Bob at 2023/02/12 10:30
# https://leetcode.cn/problems/count-the-number-of-fair-pairs/
# https://leetcode.cn/contest/weekly-contest-332/problems/count-the-number-of-fair-pairs/


"""
6355. 统计公平数对的数目 (Medium)

给你一个下标从 **0** 开始、长度为 `n` 的整数数组 `nums` ，和两个整数 `lower` 和
`upper` ，返回 **公平数对的数目** 。
如果 `(i, j)` 数对满足以下情况，则认为它是一个 **公平数对** ：
- `0 <= i < j < n`，且
- `lower <= nums[i] + nums[j] <= upper`
**示例 1：**
```
输入：nums = [0,1,7,4,4,5], lower = 3, upper = 6
输出：6
解释：共计 6 个公平数对：(0,3)、(0,4)、(0,5)、(1,3)、(1,4) 和 (1,5) 。
```
**示例 2：**
```
输入：nums = [1,7,9,2,5], lower = 11, upper = 11
输出：1
解释：只有单个公平数对：(2,3) 。
```
**提示：**
- `1 <= nums.length <= 10⁵`
- `nums.length == n`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= lower <= upper <= 10⁹`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n = len(s)
        qs = set([x^y for x,y in queries])
        ans = {}
        for r in range(n):
            for d in range(31):
                l = r-d
                if l >= 0:
                    x = int(s[l:r+1],2)
                    if x in qs:
                        if x not in ans:
                            ans[x] = [l,r]
                        else:
                            a,b = ans[x]
                            if b-a>r-l:
                                ans[x] = [l,r]
        return [ ans.get(x^y,[-1,-1]) for x,y in queries]
# @lc code=end

