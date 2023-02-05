# Created by Bob at 2023/02/05 10:30
# https://leetcode.cn/problems/count-vowel-strings-in-ranges/
# https://leetcode.cn/contest/weekly-contest-331/problems/count-vowel-strings-in-ranges/


"""
6347. 统计范围内的元音字符串数 (Medium)

给你一个下标从 **0** 开始的字符串数组 `words` 以及一个二维整数数组 `queries` 。
每个查询 `queries[i] = [lᵢ, rᵢ]` 会要求我们统计在 `words` 中下标在 `lᵢ` 到
`rᵢ` 范围内（ **包含** 这两个值）并且以元音开头和结尾的字符串的数目。
返回一个整数数组，其中数组的第 `i` 个元素对应第 `i` 个查询的答案。
**注意：** 元音字母是 `'a'`、 `'e'`、 `'i'`、 `'o'` 和 `'u'` 。
**示例 1：**
```
输入：words = ["aba","bcb","ece","aa","e"], queries =
[[0,2],[1,4],[1,1]]
输出：[2,3,0]
解释：以元音开头和结尾的字符串是 "aba"、"ece"、"aa" 和 "e" 。
查询 [0,2] 结果为 2（字符串 "aba" 和 "ece"）。
查询 [1,4] 结果为 3（字符串 "ece"、"aa"、"e"）。
查询 [1,1] 结果为 0 。
返回结果 [2,3,0] 。
```
**示例 2：**
```
输入：words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
输出：[3,2,1]
解释：每个字符串都满足这一条件，所以返回 [3,2,1] 。
```
**提示：**
- `1 <= words.length <= 10⁵`
- `1 <= words[i].length <= 40`
- `words[i]` 仅由小写英文字母组成
- `sum(words[i].length) <= 3 * 10⁵`
- `1 <= queries.length <= 10⁵`
- `0 <= queries[j][0] <= queries[j][1] < words.length`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


class BinIndexTree:
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            self.a = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.a = [0 for _ in range(self.size + 5)]
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_point(i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始
        self.a[i] += v
        while i <= self.size:
            self.c[i] += v
            i += self.lowbit(i)

    def set_point(self, i, v):  # 单点修改，下标从1开始 需要先计算差值，然后调用add
        self.add_point(i, v - self.a[i])
        self.a[i] = v

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            i -= self.lowbit(i)
        return s

    def lowbit(self, x):
        return x & -x


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        tree = BinIndexTree(n)
        for i, v in enumerate(words):
            if v[0] in 'aeiou' and v[-1] in 'aeiou':
                tree.add_point(i+1,1)
        return [tree.sum_interval(l + 1, r + 1) for l, r in queries]

# @lc code=end
