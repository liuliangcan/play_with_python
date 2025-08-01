import itertools
from bisect import bisect_left, insort, bisect_right
from sortedcontainers import SortedList

    # n = 10 ** 5
    # nums1 = [1] * (n // 2)
    # nums1.extend([0] * (n // 2))
    # nums2 = [10 ** 9] * n
    # queries = [[1, 0, n - 1] for _ in range(n)]
    # queries[1::2] = [[2, 10 ** 6, 0] for _ in range(n // 2)]
    # queries[-1] = [3, 0, 0]
    # print(nums1)
    # print(nums2)
    # print(queries)
    # with open('text.txt', 'w') as f:
    #     f.write(str(nums1) + '\n')
    #     f.write(str(nums2) + '\n')
    #     f.write(str(queries) + '\n')
    # p = [[range(2, 17), range(17, 32), range(32, 47), range(47, 62), range(62, 77)],
    #      [range(77, 88), range(88, 99), range(99, 110), range(110, 121), range(121, 132)],
    #      [range(132, 141), range(141, 150), range(150, 159), range(159, 168), range(168, 177)],
    #      [range(177, 184), range(184, 191), range(191, 198), range(198, 205), range(205, 212)],
    #      [range(212, 217), range(217, 222), range(222, 227), range(227, 232), range(232, 237)],
    #      [range(237, 240), range(240, 243), range(243, 246), range(246, 249), range(249, 252)],
    #      [range(252, 255), range(255, 258), range(258, 261), range(261, 264), range(264, 267)],
    #      [range(267, 269), range(269, 271), range(271, 273), range(273, 275), range(275, 277)],
    #      [range(277, 279), range(279, 281), range(281, 283), range(283, 285), range(285, 287)],
    #      [range(287, 289), range(289, 291), range(291, 293), range(293, 295), range(295, 297)]]
    # for parts in zip(*p):
    #     print(parts)
    #
    # class SortedList:
    #     """简易SortedList名次树，只支持add不支持remove"""
    #
    #     def __init__(self, a=None):
    #         self.small = []
    #         self.big = [] if not a else a
    #
    #     def add(self, v):
    #         # 2000 1294ms
    #         # 1000 1216ms
    #         # 1500 1185ms
    #         # 1250 1232ms
    #         if len(self.small) > 5:
    #             self.big += self.small
    #             self.big.sort()
    #             self.small.clear()
    #         insort(self.small, v)
    #
    #     def __len__(self):
    #         return len(self.small) + len(self.big)
    #
    #     def bisect_left(self, v):
    #         return bisect_left(self.small, v) + bisect_left(self.big, v)
    #
    #     def bisect_right(self, v):
    #         return bisect_right(self.small, v) + bisect_right(self.big, v)
    #
    #     def __contains__(self, v):
    #         p = bisect_left(self.small, v)
    #         if p < len(self.small) and self.small[p] == v:
    #             return True
    #         p = bisect_left(self.big, v)
    #         return p < len(self.big) and self.big[p] == v
    #
    #     def __repr__(self):
    #         return str(sorted(self.small + self.big))
    #
    #     # def __getitem__(self, index):
    #     #     if index < 0:
    #     #         index = len(self.small) + len(self.big) - index
    #     #     assert 0 <= index < len(self.small) + len(self.big)
    #     #
    #     #     def findKthSortedArrays(num1, l1: int, num2, l2: int, k: int) -> int:
    #     #         r1 = len(num1)
    #     #         r2 = len(num2)
    #     #         if r1 <= l1:
    #     #             return num2[l2 + k - 1]
    #     #         if r2 <= l2:
    #     #             return num1[l1 + k - 1]
    #     #         if k == 1:
    #     #             return min(num1[l1], num2[l2])
    #     #         if r1 - l1 > r2 - l2:
    #     #             r1, r2 = r2, r1
    #     #             l1, l2 = l2, l1
    #     #             num1, num2 = num2, num1
    #     #
    #     #         m1 = min(k // 2, r1 - l1)
    #     #         m2 = k - m1
    #     #         if num1[l1 + m1 - 1] == num2[l2 + m2 - 1]:
    #     #             return num1[l1 + m1 - 1]
    #     #         elif num1[l1 + m1 - 1] < num2[l2 + m2 - 1]:
    #     #             return findKthSortedArrays(num1, l1 + m1, num2, l2, k - m1)
    #     #         else:
    #     #             return findKthSortedArrays(num1, l1, num2, l2 + m2, k - m2)
    #     #
    #     #     return findKthSortedArrays(self.small, 0, self.big, 0, index + 1)
    #
    #     def __getitem__(self, index):
    #         if index < 0:
    #             index = len(self.small) + len(self.big) - index
    #         assert 0 <= index < len(self.small) + len(self.big)
    #
    #         def findKthSortedArrays(nums1, nums2, k: int) -> int:
    #             index1, index2 = 0, 0
    #             m, n = len(nums1), len(nums2)
    #             while True:
    #                 # 特殊情况
    #                 if index1 == m:
    #                     return nums2[index2 + k - 1]
    #                 if index2 == n:
    #                     return nums1[index1 + k - 1]
    #                 if k == 1:
    #                     return min(nums1[index1], nums2[index2])
    #
    #                 # 正常情况
    #                 newIndex1 = min(index1 + k // 2 - 1, m - 1)
    #                 newIndex2 = min(index2 + k // 2 - 1, n - 1)
    #                 pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
    #                 if pivot1 <= pivot2:
    #                     k -= newIndex1 - index1 + 1
    #                     index1 = newIndex1 + 1
    #                 else:
    #                     k -= newIndex2 - index2 + 1
    #                     index2 = newIndex2 + 1
    #
    #         return findKthSortedArrays(self.small, self.big, index + 1)
    #
    # # p = SortedList()
    # # p.add(10)
    # # p.add(10)
    # # p.add(1)
    # # p.add(8)
    # # p.add(7)
    # # p.add(10)
    # # p.add(2)
    # # p.add(10)
    # # p.add(6)
    # # p.add(10)
    # # print(p)
    # # print(p.bisect_left(10))
    # # print(p.bisect_right(10))
    # # for i in range(len(p)):
    # #     print(p[i])
    # # print(text)


# def bitcnt(n):
#     c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
#     c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
#     c = (c & 0x0F0F0F0F0F0F0F0F) + ((c >> 4) & 0x0F0F0F0F0F0F0F0F)
#     c = (c & 0x00FF00FF00FF00FF) + ((c >> 8) & 0x00FF00FF00FF00FF)
#     c = (c & 0x0000FFFF0000FFFF) + ((c >> 16) & 0x0000FFFF0000FFFF)
#     c = (c & 0x00000000FFFFFFFF) + ((c >> 32) & 0x00000000FFFFFFFF)
#     return c


def bc(x):
    cnt = 0
    while x:
        x &= x - 1
        cnt += 1
    return cnt


def z(x):
    print(bc(x), bitcnt(x))


# z(10)
# z(100)
# z(123130)
# z(5431140)
# s = "Only the 11 CAPItalic"
# print(*[chr(ord('Z') - ord(c) + ord('A')) if c.isupper() else c for c in s], sep='')
# print(*[chr(155 - ord(c)) if c.isupper() else c for c in s], sep='')
# print(*[chr(155 - ord(c)) if 'A' <= c <= 'Z' else c for c in s], sep='')
# print(*map(lambda c:chr(155-ord(c))if c.isupper()else c,s),sep='')
# print(ord('Z') + ord('A'))
# 3905.44

a = [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1]


def max_steady_1(a):
    p = -1
    ans = 0
    for i, v in enumerate(a):
        if v == 0:
            p = i
        else:
            ans = max(ans, i - p)
    return ans


def max_steady_1_(a):
    n = len(a)
    f = a[:]
    for i in range(1, n):
        if a[i]:
            f[i] += f[i - 1]
    return max(f)


print(max_steady_1_(a))

from  sortedcontainers import SortedList



a = SortedList(range(10))
a.add(5)
a.add(10000000000)
del a[2]

del a[2:3]
print(a)


"""https://codeforces.com/contest/1851/submission/263850286
1.深呼吸，不要紧张，慢慢读题，读明白题，题目往往比你想的简单。
2.暴力枚举:枚举什么，是否可以使用一些技巧加快枚举速度（预处理、前缀和、数据结构、数论分块）。
3.贪心:需要排序或使用数据结构（pq）吗，这么贪心一定最优吗。
4.二分：满足单调性吗，怎么二分，如何确定二分函数返回值是什么。
5.位运算：按位贪心，还是与位运算本身的性质有关。
6.数学题：和最大公因数、质因子、取模是否有关。
7.dp：怎么设计状态，状态转移方程是什么，初态是什么，使用循环还是记搜转移。
8.搜索：dfs 还是 bfs ，搜索的时候状态是什么，需要记忆化吗。
9.树上问题：是树形dp、树上贪心、或者是在树上搜索。
10.图论：依靠什么样的关系建图，是求环统计结果还是最短路。
11.组合数学：有几种值，每种值如何被组成，容斥关系是什么。
12.交互题：log(n)次如何二分，2*n 次如何通过 n 次求出一些值，再根据剩余次数求答案。
13.如果以上几种都不是，多半是有一个 point 你没有注意到，记住正难则反。
"""

with open('1.txt','w+') as f:
    f.write(str([1]*(5*10**4)))