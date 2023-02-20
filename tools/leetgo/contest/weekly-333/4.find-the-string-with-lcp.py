# Created by Bob at 2023/02/19 10:30
# https://leetcode.cn/problems/find-the-string-with-lcp/
# https://leetcode.cn/contest/weekly-contest-333/problems/find-the-string-with-lcp/

"""
6363. 找出对应 LCP 矩阵的字符串 (Hard)

对任一由 `n` 个小写英文字母组成的字符串 `word` ，我们可以定义一个 `n x n` 的矩阵，并满足：

- `lcp[i][j]` 等于子字符串 `word[i,...,n-1]` 和 `word[j,...,n-1]`
之间的最长公共前缀的长度。

给你一个 `n x n` 的矩阵 `lcp` 。返回与 `lcp` 对应的、按字典序最小的字符串 `word`
。如果不存在这样的字符串，则返回空字符串。

对于长度相同的两个字符串 `a` 和 `b` ，如果在 `a` 和 `b` 不同的第一个位置，字符串 `a`
的字母在字母表中出现的顺序先于 `b` 中的对应字母，则认为字符串 `a` 按字典序比字符串 `b` 小。例如，
`"aabd"` 在字典上小于 `"aaca"` ，因为二者不同的第一位置是第三个字母，而 `'b'` 先于 `'c'`
出现。

**示例 1：**

```
输入：lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
输出："abab"
解释：lcp 对应由两个交替字母组成的任意 4 字母字符串，字典序最小的是 "abab" 。

```

**示例 2：**

```
输入：lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
输出："aaaa"
解释：lcp 对应只有一个不同字母的任意 4 字母字符串，字典序最小的是 "aaaa" 。

```

**示例 3：**

```
输入：lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
输出：""
解释：lcp[3][3] 无法等于 3 ，因为 word[3,...,3] 仅由单个字母组成；因此，不存在答案。

```

**提示：**

- `1 <= n == ` `lcp.length == ` `lcp[i].length` `<= 1000`
- `0 <= lcp[i][j] <= n`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [''] * n
        i = 0
        for c in ascii_lowercase:  # 优先用小的字母
            while i < n and s[i]:  # 找到还没填的位置
                i += 1
            if i == n:break
            s[i] = c  # 直接填
            for j in range(i+1,n):  # 和这个位置相同的位置都要填它
                if lcp[i][j]:
                    s[j] = c
        if '' in  s:  # 如果字母都用完了还没填完就失败
            return ''
        # 在原数组上验证
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i] == s[j]:
                    if i == n-1 or j == n-1:
                        if lcp[i][j] != 1:
                            return ''
                    else:
                        if lcp[i][j] != lcp[i+1][j+1] + 1:
                            return ''
                else:
                    if lcp[i][j]:
                        return ''
        return ''.join(s)

# @lc code=end
