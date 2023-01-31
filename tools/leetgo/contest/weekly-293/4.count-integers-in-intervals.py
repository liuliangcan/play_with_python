# Created by Bob at 2023/01/31 19:38
# https://leetcode.cn/problems/count-integers-in-intervals/
# https://leetcode.cn/contest/weekly-contest-293/problems/count-integers-in-intervals/


"""
2276. 统计区间中的整数数目 (Hard)

给你区间的 **空** 集，请你设计并实现满足要求的数据结构：
- **新增：** 添加一个区间到这个区间集合中。
- **统计：** 计算出现在 **至少一个** 区间中的整数个数。
实现 `CountIntervals` 类：
- `CountIntervals()` 使用区间的空集初始化对象
- `void add(int left, int right)` 添加区间 `[left, right]`
到区间集合之中。
- `int count()` 返回出现在 **至少一个** 区间中的整数个数。
**注意：** 区间 `[left, right]` 表示满足 `left <= x <= right` 的所有整数
`x` 。
**示例 1：**
```
输入
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
输出
[null, null, null, 6, null, 8]
解释
CountIntervals countIntervals = new CountIntervals(); //
用一个区间空集初始化对象
countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
countIntervals.count();    // 返回 6
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 7、8、9、10 出现在区间 [7, 10] 中
countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
countIntervals.count();    // 返回 8
                           // 整数 2 和 3 出现在区间 [2, 3] 中
                           // 整数 5 和 6 出现在区间 [5, 8] 中
                           // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7,
10] 中
                           // 整数 9 和 10 出现在区间 [7, 10] 中
```
**提示：**
- `1 <= left <= right <= 10⁹`
- 最多调用  `add` 和 `count` 方法 **总计** `10⁵` 次
- 调用 `count` 方法至少一次
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


class ODTNode:
    __slots__ = ['l', 'r', 'v']

    def __init__(self, l, r, v):
        self.l, self.r, self.v = l, r, v

    def __lt__(self, other):
        return self.l < other.l

    def jiebao(self):
        return self.l, self.r, self.v


class ODT:
    def __init__(self, l, r, v):
        from sortedcontainers import SortedList
        self.tree = SortedList([ODTNode(l, r, v)])

    def split(self, pos):
        """ 在pos位置切分，返回左边界l为pos的线段下标
        """
        tree = self.tree
        p = tree.bisect_left(ODTNode(pos, 0, 0))
        if p != len(tree) and tree[p].l == pos:
            return p
        p -= 1
        l, r, v = tree[p].jiebao()
        tree[p].r = pos - 1
        # tree.pop(p)
        # tree.add(ODTNode(l,pos-1,v))
        tree.add(ODTNode(pos, r, v))
        return p + 1

    def assign(self, l, r, v):
        """
        把[l,r]区域全变成val
        """
        tree = self.tree
        begin = self.split(l)
        end = self.split(r + 1)
        # del tree[begin:end]
        ans = 0
        for i in range(begin, end):
            x, y, z = tree.pop(begin).jiebao()
            # print(l,r,x)
            if z:
                ans += y - x + 1
        tree.add(ODTNode(l, r, v))
        return ans



class CountIntervals:

    def __init__(self):
        self.tree = ODT(1, 10 ** 9, 0)
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        self.cnt -= self.tree.assign(left, right, 1)
        # print(self.tree.tree)
        self.cnt += right - left + 1

    def count(self) -> int:
        return self.cnt

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

# @lc code=end
