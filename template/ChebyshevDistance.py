"""切比雪夫距离（Chebyshev distance）是向量空间中的一种度量，得名自俄罗斯数学家切比雪夫。两个点之间的距离定义为其各坐标数值差绝对值的最大值
把二维坐标系顺时针旋转45°，并扩大√2倍，(x,y)变成(x',y')=(y+x,y-x)
此时曼哈顿距离 |x1-x2|+|y1-y2| = max(|x'1-x'2|,|y'1-y'2|)。
因此可以把二维关系转变成讨论两次一维关系，省事很多

例题：
    曼哈顿距离转化成切比雪夫距离 https://leetcode.cn/problems/minimize-manhattan-distances/description/
"""

from sortedcontainers import SortedList


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        a, b = SortedList(), SortedList()
        for x, y in points:
            a.add(x + y)
            b.add(y - x)
        ans = inf
        for x, y in points:
            x, y = x + y, y - x
            a.remove(x)
            b.remove(y)

            ans = min(ans, max(a[-1] - a[0], b[-1] - b[0]))
            a.add(x)
            b.add(y)
        return ans
