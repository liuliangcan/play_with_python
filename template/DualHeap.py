"""对顶堆，实时计算当前集合前k小的元素和。每个操作均摊时间复杂度O(lgn)，总体O(nlgn)。
用途:
1. 维护前k小
2. 维护中位数（非定长数组，中位数的位置k是变化的)
用两个堆存储集合，一个计数器实现延迟删除：注意prune操作紧跟在每个出堆动作后，保证两个堆顶元素永远有效(它们可能相等)。
另一种更方便的实现是：两个有序集合sl1+sl2。保证sl1[-1]<-sl2[0]即可，但效率上慢一些。
也可以用一个名次树sl实现，需要支持查询名次。
维护前k小：https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/description/
维护前一半：https://leetcode.cn/problems/5TxKeK/description/
"""
from collections import Counter, defaultdict
from heapq import *


class DualHeap:
    """对顶堆，实时计算当前集合前k小的元素和(如果k设0,则保持平衡，0<=small-large<=1)。每个操作均摊时间复杂度O(lgn)，总体O(nlgn)。682ms"""

    def __init__(self, k=0):
        self.k = k  # 如果k=0，表示保持两个堆一样大(0<=small-large<=1),此时-small[0]就是中位数
        self.small = []  # 大顶堆存较小的k个数，注意py默认小顶堆，因此需要取反
        self.large = []  # 小顶堆存较大的剩余数
        self.delay_rm = defaultdict(int)  # 延时删除标记
        self.sum_kth = 0  # 前k小数字的和
        self.small_size = 0
        self.large_size = 0

    def prune(self, h):
        """修剪h，使h堆顶的已标记删除元素全部弹出"""
        delay_rm = self.delay_rm
        p = -1 if h is self.small else 1
        while h:
            v = h[0] * p
            if v in delay_rm:
                delay_rm[v] -= 1
                if not delay_rm[v]:
                    del delay_rm[v]
                heappop(h)
            else:
                break

    def make_balance(self):
        """调整small和large的大小，使small中达到k个（或清空large）"""
        k = self.k or (self.small_size + self.large_size + 1) // 2  # 如果self.k是0，表示前后要balance
        if self.small_size > k:
            heappush(self.large, -self.small[0])
            self.sum_kth += heappop(self.small)  # 其实是-=负数
            self.large_size += 1
            self.small_size -= 1
            self.prune(self.small)
        elif self.small_size < k and self.large:
            heappush(self.small, -self.large[0])
            self.sum_kth += heappop(self.large)
            self.small_size += 1
            self.large_size -= 1
            self.prune(self.large)

    def add(self, v):
        """添加值v，判断需要加到哪个堆"""
        small = self.small
        if not small or v <= -small[0]:
            heappush(small, -v)
            self.sum_kth += v
            self.small_size += 1
        else:
            heappush(self.large, v)
            self.large_size += 1
        self.make_balance()

    def remove(self, v):
        """移除v，延时删除，但可以实时判断是否贡献了前k和"""
        small, large = self.small, self.large
        self.delay_rm[v] += 1
        if large and v >= large[0]:
            self.large_size -= 1
            if v == large[0]:
                self.prune(large)
        else:
            self.small_size -= 1
            self.sum_kth -= v
            if v == -small[0]:
                self.prune(small)
        self.make_balance()


from sortedcontainers import SortedList


class TwoSL:
    """两个有序集合"""

    def __init__(self, k):
        self.k = k
        self.small = SortedList()
        self.large = SortedList()
        self.sum_kth = 0

    def make_balance(self):
        if len(self.small) > self.k:
            v = self.small.pop()
            self.large.add(v)
            self.sum_kth -= v
        elif len(self.small) < self.k and self.large:
            v = self.large.pop(0)
            self.small.add(v)
            self.sum_kth += v

    def add(self, v):
        if not self.small or v <= self.small[-1]:
            self.small.add(v)
            self.sum_kth += v
        else:
            self.large.add(v)
        self.make_balance()

    def remove(self, v):
        if self.large and v >= self.large[0]:
            self.large.remove(v)
        else:
            self.small.remove(v)
            self.sum_kth -= v
            self.make_balance()


class OneSL:
    """一个有序集合"""

    def __init__(self, k):
        self.k = k
        self.sl = SortedList()
        self.sum_kth = 0

    def add(self, v):
        if len(self.sl) < self.k:  # 如果长度不到k直接添加
            self.sum_kth += v
        else:  # 看看是否会把原k-1位置的顶出去
            v1 = self.sl[self.k - 1]
            if v < v1:
                self.sum_kth += v - v1
        self.sl.add(v)

    def remove(self, v):
        if len(self.sl) <= self.k:
            self.sum_kth -= v
        else:  # 看看删除后k位置是否前移
            v1 = self.sl[self.k]
            if v < v1:
                self.sum_kth += v1 - v
        self.sl.remove(v)


# class Solution:
#     def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
#         ans = inf
#         l = 1
#         dh = OneSL(k - 1)
#         for i in range(1, len(nums)):
#             dh.add(nums[i])
#             while i - l + 1 > dist + 1:
#                 dh.remove(nums[l])
#                 l += 1
#             if i - l + 1 == dist + 1:
#                 ans = min(ans, nums[0] + dh.sum_kth)
#
#         return ans
