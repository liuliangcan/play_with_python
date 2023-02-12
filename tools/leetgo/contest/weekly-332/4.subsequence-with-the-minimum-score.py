# Created by Bob at 2023/02/12 10:30
# https://leetcode.cn/problems/subsequence-with-the-minimum-score/
# https://leetcode.cn/contest/weekly-contest-332/problems/subsequence-with-the-minimum-score/


"""
6357. 最少得分子序列 (Hard)

给你两个字符串 `s` 和 `t` 。
你可以从字符串 `t` 中删除任意数目的字符。
如果没有从字符串 `t` 中删除字符，那么得分为 `0` ，否则：
- 令 `left` 为删除字符中的最小下标。
- 令 `right` 为删除字符中的最大下标。
字符串的得分为 `right - left + 1` 。
请你返回使 `t` 成为 `s` 子序列的最小得分。
一个字符串的 **子序列**
是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。（比方说 `"ace"` 是
`"abcde"` 的子序列，但是 `"aec"` 不是）。
**示例 1：**
```
输入：s = "abacaba", t = "bzaa"
输出：1
解释：这个例子中，我们删除下标 1 处的字符 "z" （下标从 0 开始）。
字符串 t 变为 "baa" ，它是字符串 "abacaba" 的子序列，得分为 1 - 1 + 1 = 1 。
1 是能得到的最小得分。
```
**示例 2：**
```
输入：s = "cde", t = "xyz"
输出：3
解释：这个例子中，我们将下标为 0， 1 和 2 处的字符 "x" ，"y" 和 "z" 删除（下标从 0 开始）。
字符串变成 "" ，它是字符串 "cde" 的子序列，得分为 2 - 0 + 1 = 3 。
3 是能得到的最小得分。
```
**提示：**
- `1 <= s.length, t.length <= 10⁵`
- `s` 和 `t` 都只包含小写英文字母。
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        pre = [m] * n
        j = 0
        for i, c in enumerate(t):
            while j < m and s[j] != c:
                j += 1
            if j == m:
                break
            pre[i] = j
            j += 1
        suf = [-1] * n
        j = m - 1
        for i in range(n - 1, -1, -1):
            while j >= 0 and s[j] != t[i]:
                j -= 1
            if j < 0:
                break
            suf[i] = j
            j -= 1
        if pre[0] == n and suf[-1] == -1:
            return n
        print(pre)
        print(suf)
        ans = n - bisect_left(pre, m)
        ans = min(ans, bisect_right(suf, -1))
        j = 0
        for i, v in enumerate(suf):
            while j < i and pre[j] < v:
                j += 1
            if j and v > pre[j - 1]:
                ans = min(ans, i - j)

        return ans

# @lc code=end

