# Created by Bob at 2023/03/29 14:36
# https://leetcode.cn/problems/ZbAuEH/

"""
LCP 57. 打地鼠 (Hard)
欢迎各位勇者来到力扣城，本次试炼主题为「打地鼠」。
!\[middle\_img\_v2\_d5d09656-0616-4a80-845e-ece461c5ba9g.png\](https://pic.leetcode-cn.com/1650273183-nZIijm-middle\_img\_v2\_d5d09656-0616-4a80-845e-ece461c5ba9g.png){:height="200px"}
勇者面前有一个大小为 \`3\*3\` 的打地鼠游戏机，地鼠将随机出现在各个位置，\`moles\[i\] =
\[t,x,y\]\` 表示在第 \`t\` 秒会有地鼠出现在 \`(x,y)\` 位置上，并于第 \`t+1\`
秒该地鼠消失。

勇者有一把可敲打地鼠的锤子，初始时刻（即第 \`0\` 秒）锤子位于正中间的格子
\`(1,1)\`，锤子的使用规则如下：
\- 锤子每经过 \`1\` 秒可以往上、下、左、右中的一个方向移动一格，也可以不移动
\- 锤子只可敲击所在格子的地鼠，\\*\\*敲击不耗时\\*\\*

请返回勇者\\*\\*最多\\*\\*能够敲击多少只地鼠。

\\*\\*注意：\\*\\*
\- 输入用例保证在相同时间相同位置最多仅有一只地鼠

\*\*示例 1：\*\*
>输入： \`moles = \[\[1,1,0\],\[2,0,1\],\[4,2,2\]\]\`
>
>输出： \`2\`
>
>解释：
>第 0 秒，锤子位于 (1,1)
>第 1 秒，锤子移动至 (1,0) 并敲击地鼠
>第 2 秒，锤子移动至 (2,0)
>第 3 秒，锤子移动至 (2,1)
>第 4 秒，锤子移动至 (2,2) 并敲击地鼠
>因此勇者最多可敲击 2 只地鼠

\*\*示例 2：\*\*
>输入：\`moles =
\[\[2,0,2\],\[5,2,0\],\[4,1,0\],\[1,2,1\],\[3,0,2\]\]\`
>
>输出：\`3\`
>
>解释：
>第 0 秒，锤子位于 (1,1)
>第 1 秒，锤子移动至 (2,1) 并敲击地鼠
>第 2 秒，锤子移动至 (1,1)
>第 3 秒，锤子移动至 (1,0)
>第 4 秒，锤子在 (1,0) 不移动并敲击地鼠
>第 5 秒，锤子移动至 (2,0) 并敲击地鼠
>因此勇者最多可敲击 3 只地鼠

\*\*示例 3：\*\*
>输入：\`moles = \[\[0,1,0\],\[0,0,1\]\]\`
>
>输出：\`0\`
>
>解释：
>第 0 秒，锤子初始位于 (1,1)，此时并不能敲击 (1,0)、(0,1) 位置处的地鼠

\\*\\*提示：\\*\\*
\+ \`1 <= moles.length <= 10^5\`
\+ \`moles\[i\].length == 3\`
\+ \`0 <= moles\[i\]\[0\] <= 10^9\`
\+ \`0 <= moles\[i\]\[1\], moles\[i\]\[2\] < 3\`
"""

from bisect import *
from collections import *
from heapq import *
from math import inf
from typing import List

# @lc code=begin
from sortedcontainers import SortedList

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
        n = len(moles)
        mos = sorted(set(t for t, _, _ in moles) | {0})
        m = len(mos)
        a = set((t, x, y) for t, x, y in moles)

        f = [[-10 ** 9] * 3 for _ in range(3)]
        if (0, 1, 1) in a:
            f[1][1] = 1
        else:
            f[1][1] = 0

        for k in range(1, m):
            t = mos[k]
            d = t - mos[k - 1]
            g = [[-10 ** 9] * 3 for _ in range(3)]
            mx = max(max(r) for r in f)
            for i in range(3):
                for j in range(3):
                    p = int((t, i, j) in a)
                    if d >= 4:  # 这个优化能让tle变ac就离谱  10s->4s
                        g[i][j] = mx + p
                    else:
                        for x in range(3):
                            for y in range(3):
                                dis = abs(x - i) + abs(y - j)
                                if dis <= d and g[i][j] < f[x][y] + p:
                                    g[i][j] = f[x][y] + p
            f = g
        return max([max(r) for r in f])

# class Solution(object):
#     def getMaximumNumber(self, moles):
#         """
#         :type moles: List[List[int]]
#         :rtype: int
#         """
#
#         n = len(moles)
#         moles.sort()
#         f = [0] * n
#         j = mx = 0
#         for i, (t, x, y) in enumerate(moles):
#             while t - moles[j][0] >= 4:  # 如果距离当前步长超过4,那么九宫格所有位置可以互相到达
#                 mx = max(mx, f[j])
#                 j += 1
#             if j:
#                 f[i] = mx + 1
#             elif abs(x - 1) + abs(y - 1) <= t:
#                 f[i] = 1
#             for k in range(i - 1, j - 1, -1):
#                 if f[k] and abs(x - moles[k][1]) + abs(y - moles[k][2]) <= t - moles[k][0]:
#                     f[i] = max(f[i], f[k] + 1)
#
#         return max(f)
# @lc code=end
