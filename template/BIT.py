""" 树状数组可以用来解决区间问题。
国内喜欢叫它BIT(BinaryIndexed-Tree),国外喜欢叫FenwickTree

树状数组的核心是:i的父节点是i+lowbit(i)。
通过这个可以把区间信息汇总到它的父节点。即：所有信息都在二进制的每个1位上。
更新时只需要更新所有包含目标节点的父节点。
查询时把每个lowbit记录的信息相加，就是前缀和。两个前缀和相减就是区间和。

复杂度：
    - 由于更新和查询都是遍历每个二进制的1，复杂度均为O(logn)

应用包括但不限于:
- 单点更新-区间求和PURQ: 最常规应用  BinIndexTree
- 区间更新-单点求和: 是PURQ+差分的演变  BinIndexTreeRUPQ
- 区间更新-区间求和: 需要推一下公式  BinIndexTreeRURQ
- 单点更新-区间求极值: 线段树卡常才需要用，好像不支持回退。而且复杂度多个log。   BinIndexTreeMin/BinIndexTreeMax
- 二维树状数组: 不太常用  BinTree2DIUPQ
- 另外还可以实现ranktree(权值树状数组)，要求值域小或者可离散化，复杂度是O(lgn)：思想是维护01值然后用sum(i)前边代表i是第几小  https://leetcode.cn/problems/sliding-subarray-beauty/
- 判断两个部分是否相交（覆盖也不算），类似扫描线， https://atcoder.jp/contests/abc424/tasks/abc424_f
我的csdn:[[python刷题模板] 树状数组](https://blog.csdn.net/liuliangcan/article/details/124990108)

"""
from math import inf
from typing import List


class BinIndexTree:
    """    PURQ的最经典树状数组，每个基础操作的复杂度都是logn；如果需要查询每个位置的元素，可以打开self.a    """
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            # self.a = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            # self.a = [0 for _ in range(self.size + 5)]
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_point(i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始
        # self.a[i] += v
        while i <= self.size:
            self.c[i] += v
            i += i & -i

    # def set_point(self, i, v):  # 单点修改，下标从1开始 需要先计算差值，然后调用add
    #     self.add_point(i, v - self.a[i])
    #     self.a[i] = v

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            # i -= i&-i
            i &= i - 1
        return s

    def min_right(self, i):
        """寻找[i,size]闭区间上第一个正数(不为0的数),注意i是1-indexed。若没有返回size+1;复杂度O(lgnlgn)"""
        p = self.sum_prefix(i)
        if i == 1:
            if p > 0:
                return i
        else:
            if p > self.sum_prefix(i - 1):
                return i

        l, r = i, self.size + 1
        while l + 1 < r:
            mid = (l + r) >> 1
            if self.sum_prefix(mid) > p:
                r = mid
            else:
                l = mid
        return r

    def kth_upper(self, s):
        """返回>=s的最大下标，注意这个是upperbound-1"""
        pos = 0
        for j in range(18, -1, -1):
            if pos + (1 << j) <= self.size and self.c[pos + (1 << j)] <= s:
                pos += (1 << j)
                s -= self.c[pos]
        return pos
    def kth_lower(self, s):
        """返回>=s的最小下标，注意这个是upperbound-1"""
        pos = 0
        for j in range(18, -1, -1):
            if pos + (1 << j) <= self.size and self.c[pos + (1 << j)] < s:
                pos += (1 << j)
                s -= self.c[pos]
        return pos + 1
    def lowbit(self, x):
        return x & -x


class BinIndexTreeRUPQ:
    """树状数组的RUPQ模型，结合差分理解"""
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_interval(i + 1, i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始;不支持直接调用，这里增加的是差分数组的单点
        while i <= self.size:
            self.c[i] += v
            i += i&-i

    def sum_prefix(self, i):  # 前缀求和，下标从1开始；不支持直接调用，这里求和的是差分数组的前缀和
        s = 0
        while i >= 1:
            s += self.c[i]
            i &= i-1
        return s

    def add_interval(self, l, r, v):  # 区间加，下标从1开始，把[l,r]闭区间都加v
        self.add_point(l, v)
        self.add_point(r + 1, -v)

    def query_point(self, i):  # 单点询问值，下标从1开始，返回i位置的值
        return self.sum_prefix(i)

    def lowbit(self, x):
        return x & -x



class BinIndexTreeRURQ:
    """树状数组的RURQ模型"""
    def __init__(self, size_or_nums):  # 树状数组,区间加区间求和，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.d = [0 for _ in range(self.size + 5)]
            self.d2 = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.d = [0 for _ in range(self.size + 5)]
            self.d2 = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_interval(i + 1, i + 1, v)

    def _add_point(self, c, i, v):  # 单点增加,下标从1开始;不支持直接调用，这里增加的是差分数组的单点,同步修改c2
        while i <= self.size:
            c[i] += v
            i += -i&i

    def _sum_prefix(self, c, i):  # 前缀求和，下标从1开始；不支持直接调用，这里求和的是差分数组的前缀和;传入c决定怎么计算，但是不要直接调用 无视吧
        s = 0
        while i >= 1:
            s += c[i]
            i -= -i&i
        return s

    def add_interval(self, l, r, v):  # 区间加，下标从1开始，把[l,r]闭区间都加v
        self._add_point(self.d, l, v)
        self._add_point(self.d, r + 1, -v)
        self._add_point(self.d2, l, (l - 1) * v)
        self._add_point(self.d2, r + 1, -v * r)

    def sum_interval(self, l, r):  # 区间求和，下标从1开始，返回闭区间[l,r]上的求和
        return self._sum_prefix(self.d, r) * r - self._sum_prefix(self.d2, r) - self._sum_prefix(self.d, l - 1) * (
                l - 1) + self._sum_prefix(self.d2, l - 1)

    def query_point(self, i):  # 单点询问值，下标从1开始，返回i位置的值
        return self._sum_prefix(self.d, i)

    def lowbit(self, x):
        return x & -x


class BinIndexTreeMin:
    """树状数组求min的模型"""
    def __init__(self, size):
        self.size = size
        self.a = [inf for _ in range(size + 5)]
        self.h = self.a[:]
        self.mn = inf

    def update(self, x, v):
        if v < self.mn:
            self.mn = v
        a = self.a
        h = self.h
        a[x] = v
        while x <= self.size:
            if h[x] > v:
                h[x] = v
            else:
                break
            x += self.lowbit(x)

    def query(self, l, r):
        a = self.a
        h = self.h
        ans = a[r]
        while l != r:
            r -= 1
            while r - self.lowbit(r) > l:
                if ans > h[r]:
                    ans = h[r]
                    if ans == self.mn:
                        break
                r -= self.lowbit(r)
            # ans = min(ans, self.a[r])
            if ans > a[r]:
                ans = a[r]
            if ans == self.mn:
                break
        return ans

    def lowbit(self, x):
        return x & -x


class BinIndexTreeMax:
    """树状数组求max模型"""
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数组；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.h = [-inf for _ in range(self.size + 5)]
            self.a = [-inf for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.a = [-inf for _ in range(self.size + 5)]
            self.h = [-inf for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.set_point(i + 1, v)

    def set_point(self, x, v):  # 单点修改，下标从1开始 修改原数组和h数组
        self.a[x] = v
        while x <= self.size:
            # self.h[x] = max(self.h[x], self.a[lx])
            if self.h[x] < v:
                self.h[x] = v
            x += (x & -x)

    def query_interval_max(self, l, r):  # 区间询问最大值，下标从1开始
        ans = -inf
        while l <= r:
            # ans = max(self.a[r], ans)
            if ans < self.a[r]:
                ans = self.a[r]
            r -= 1
            while r - (r & -r) >= l:
                # ans = max(self.h[r], ans)
                if ans < self.h[r]:
                    ans = self.h[r]
                r -= (r & -r)
        return ans

    def lowbit(self, x):
        return x & -x


class BinTree2DIUPQ:
    """二维树状数组"""
    def __init__(self, m, n):
        self.n = n
        self.m = m
        self.tree = [[0] * (n + 1) for _ in range(m + 1)]

    def lowbit(self, x):
        return x & (-x)

    def _update_point(self, x, y, val):
        m, n, tree = self.m, self.n, self.tree
        while x <= m:
            y1 = y
            while y1 <= n:
                tree[x][y1] += val
                y1 += y1 & -y1
            x += x & -x

    def _sum_prefix(self, x, y):
        res = 0
        tree = self.tree
        while x > 0:
            y1 = y
            while y1 > 0:
                res += tree[x][y1]
                y1 &= y1 - 1
            x &= x - 1
        return res

    def add_interval(self, x1, y1, x2, y2, v):
        self._update_point(x1, y1, v)
        self._update_point(x2 + 1, y1, -v)
        self._update_point(x1, y2 + 1, -v)
        self._update_point(x2 + 1, y2 + 1, v)

    def query_point(self, x, y):
        return self._sum_prefix(x, y)


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        tree = BinTree2DIUPQ(n, n)
        for x1, y1, x2, y2 in queries:
            tree.add_interval(x1 + 1, y1 + 1, x2 + 1, y2 + 1, 1)
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[i][j] = tree.query_point(i + 1, j + 1)
        return res

# a = [1,2,30,2]
# t = BinIndexTree(a)
# print(t.kth(0))
# print(t.kth(1))
# print(t.kth(2))
# print(t.kth(3))
# print(t.kth(32))
# print(t.kth(33))
# print(t.kth(34))
# print(t.kth(35))
# print(t.kth(36))
# print(t.kth(37))
# print(t.kth(38))
# print(t.kth(39))