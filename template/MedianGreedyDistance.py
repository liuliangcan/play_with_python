"""听灵神的，打一个货仓问题模板。
货仓问题：中位数贪心
如果是普通的，可以直接找(r+l)//2位置
例题：每次+-x,则先算余数，然后全部除x，转化成x是1：https://leetcode.cn/problems/minimum-operations-to-make-a-uni-value-grid/description/
"""
from itertools import accumulate


class MedianGreedyDistance:
    """计算升序数组里，所有值调整到同一个值的步数（距离）"""

    def __init__(self, a):
        self.pre = [0] + list(accumulate(a))
        self.a = a

    def sum_dis_to_i(self, l, r, i):
        """计算a[l,r]里所有数字到a[i]的距离和"""
        if i <= l:
            return self.pre[r + 1] - self.pre[l] - self.a[i] * (r - l + 1)
        elif i >= r:
            return self.a[i] * (r - l + 1) - self.pre[r + 1] + self.pre[l]
        else:
            # return self.a[i] * (i - l + 1) - self.pre[i + 1] + self.pre[l] + self.pre[r + 1] - self.pre[i] - self.a[i] * (r - i + 1)
            return self.a[i] * (i * 2 - l + 1 - r) - 2 * self.pre[i + 1] + self.pre[l] + self.pre[r + 1]

    def sum_dis_to_v(self, l, r, v):
        """计算a[l,r]里所有数字到v的距离和"""
        if v <= self.a[l]:
            return self.pre[r + 1] - self.pre[l] - v * (r - l + 1)
        elif v >= self.a[r]:
            return v * (r - l + 1) - self.pre[r + 1] + self.pre[l]
        else:
            i = bisect_left(self.a, v)
            return v * (i * 2 - l + 1 - r) - 2 * self.pre[i + 1] + self.pre[l] + self.pre[r + 1]
