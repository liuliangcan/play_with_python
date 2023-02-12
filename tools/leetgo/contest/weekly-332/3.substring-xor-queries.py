# Created by Bob at 2023/02/12 10:30
# https://leetcode.cn/problems/substring-xor-queries/
# https://leetcode.cn/contest/weekly-contest-332/problems/substring-xor-queries/


"""
6356. 子字符串异或查询 (Medium)

给你一个 **二进制字符串** `s` 和一个整数数组 `queries` ，其中 `queries[i] =
[firstᵢ, secondᵢ]` 。
对于第 `i` 个查询，找到 `s` 的 **最短子字符串** ，它对应的 **十进制** 值 `val` 与
`firstᵢ` **按位异或** 得到 `secondᵢ` ，换言之， `val ^ firstᵢ ==
secondᵢ` 。
第 `i` 个查询的答案是子字符串 `[leftᵢ, rightᵢ]` 的两个端点（下标从 **0**
开始），如果不存在这样的子字符串，则答案为 `[-1, -1]` 。如果有多个答案，请你选择 `leftᵢ`
最小的一个。
请你返回一个数组 `ans` ，其中 `ans[i] = [leftᵢ, rightᵢ]` 是第 `i` 个查询的答案。
**子字符串** 是一个字符串中一段连续非空的字符序列。
**示例 1：**
```
输入：s = "101101", queries = [[0,5],[1,2]]
输出：[[0,2],[2,3]]
解释：第一个查询，端点为 [0,2] 的子字符串为 "101" ，对应十进制数字 5 ，且 5 ^ 0 = 5
，所以第一个查询的答案为 [0,2]。第二个查询中，端点为 [2,3] 的子字符串为 "11" ，对应十进制数字 3
，且 3 ^ 1 = 2 。所以第二个查询的答案为 [2,3] 。
```
**示例 2：**
```
输入：s = "0101", queries = [[12,8]]
输出：[[-1,-1]]
解释：这个例子中，没有符合查询的答案，所以返回 [-1,-1] 。
```
**示例 3：**
```
输入：s = "1", queries = [[4,5]]
输出：[[0,0]]
解释：这个例子中，端点为 [0,0] 的子字符串对应的十进制值为 1 ，且 1 ^ 4 = 5 。所以答案为 [0,0]
。
```
**提示：**
- `1 <= s.length <= 10⁴`
- `s[i]` 要么是 `'0'` ，要么是 `'1'` 。
- `1 <= queries.length <= 10⁵`
- `0 <= firstᵢ, secondᵢ <= 10⁹`
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

