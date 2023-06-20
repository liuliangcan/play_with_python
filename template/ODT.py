"""珂朵莉树模板"""
import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')


RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7

"""https://codeforces.com/problemset/problem/292/E

输入 n(≤1e5) 和 m (≤1e5)，两个长度都为 n 的数组 a 和 b（元素范围在 [-1e9,1e9] 内，下标从 1 开始）。
然后输入 m 个操作：
操作 1 形如 1 x y k，表示把 a 的区间 [x,x+k-1] 的元素拷贝到 b 的区间 [y,y+k-1] 上（输入保证下标不越界）。
操作 2 形如 2 x，输出 b[x]。
输入
5 10
1 2 0 -1 3
3 1 5 -2 0
2 5
1 3 3 3
2 5
2 4
2 1
1 2 1 4
2 1
2 4
1 4 2 1
2 2
输出
0
3
-1
3
2
3
-1
"""

MAX_LEVEL = 20  # 建议设置成lg(n),n是数据长度，20满足1e6,32满足1e10。由于跳表复杂度lgn，所以通常n<2e5,20就够
P_FACTOR = 0.25


def random_level() -> int:
    lv = 1
    while lv < MAX_LEVEL and random.random() < P_FACTOR:
        lv += 1
    return lv


class SkiplistNode:
    __slots__ = 'val', 'forward', 'nb_len'

    def __init__(self, val: int, max_level=MAX_LEVEL):
        self.val = val
        self.forward = [None] * max_level
        self.nb_len = [1] * max_level

    def __str__(self):
        return str(f'{self.val},{self.forward},{self.nb_len}')

    def __repr__(self):
        return str(f'{self.val},,{self.nb_len}')


class Skiplist:
    def __init__(self, nums=None):
        self.head = SkiplistNode(-1)
        self.level = 0
        self._len = 0

        if nums:
            for i in nums:
                self.add(i)

    def __len__(self):
        return self._len

    def find(self, target: int) -> bool:  # 判断target是否存在
        cur = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 target 的元素
            while cur.forward[i] and cur.forward[i].val < target:
                cur = cur.forward[i]
        cur = cur.forward[0]
        # 检测当前元素的值是否等于 target
        return cur is not None and cur.val == target

    def index(self, target: int) -> int:  # 在数据中找到target第一次出现的位置，找不到就返回-1
        cur = self.head
        idx = 0
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 target 的元素
            while cur.forward[i] and cur.forward[i].val < target:
                idx += cur.nb_len[i]
                cur = cur.forward[i]
        # idx -= 1
        cur = cur.forward[0]
        # 检测当前元素的值是否等于 target
        if cur is None or cur.val != target:
            return -1
        return idx

    def bisect_left(self, target) -> int:  # 返回第一个插入位置
        curr = self.head
        idx = 0
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 target 的元素
            while curr.forward[i] and curr.forward[i].val < target:
                idx += curr.nb_len[i]
                curr = curr.forward[i]
        return idx

    def bisect_right(self, target) -> int:  # 返回最后一个插入位置（本方法未经严格测试
        curr = self.head
        idx = 0
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 target 的元素
            while curr.forward[i] and curr.forward[i].val <= target:
                idx += curr.nb_len[i]
                curr = curr.forward[i]
        return idx

    def bisect_left_kvp(self, target):  # 返回下标，当前下标的值，前一个下标的值
        curr = self.head
        idx = 0
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 target 的元素
            while curr.forward[i] and curr.forward[i].val < target:
                idx += curr.nb_len[i]
                curr = curr.forward[i]
        return idx, curr.forward[0].val if idx < self._len else None, curr.val

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(self._len)
            if step == 1 and start < stop:
                ans = []
                cur = self.head
                idx = 0
                for i in range(self.level - 1, -1, -1):
                    # 当本层位置+前向长度小于目标位置时，在同层右移
                    while cur.forward[i] and idx + cur.nb_len[i] <= start:
                        idx += cur.nb_len[i]
                        cur = cur.forward[i]
                p = start
                while p < stop and cur.forward[0]:
                    ans.append(cur.forward[0].val)
                    cur = cur.forward[0]
                    p += 1
                return ans
            if start < stop:
                return self.__getitem__[slice(start, stop, 1)][index]

            if stop < start:
                return self.__getitem__[slice(start + 1, stop + 1, -step)][::-1]

        else:
            if index >= self._len or index + self._len < 0:
                raise Exception(f'index out of range: {index}')
            if index < 0:
                index += self._len
            cur = self.head
            idx = 0
            for i in range(self.level - 1, -1, -1):
                # 当本层位置+前向长度小于目标位置时，在同层右移
                while cur.forward[i] and idx + cur.nb_len[i] <= index:
                    idx += cur.nb_len[i]
                    cur = cur.forward[i]

            return cur.forward[0].val

    def __delitem__(self, index):
        if index >= self._len or index + self._len < 0:
            raise Exception(f'index out of range {index}')
        if index < 0:
            index += self._len
        update = [None] * MAX_LEVEL
        curr = self.head
        idx = 0
        for i in range(self.level - 1, -1, -1):
            # 当同层位置+前向长度小于目标位置时，在同层右移
            while curr.forward[i] and idx + curr.nb_len[i] <= index:
                idx += curr.nb_len[i]
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        self._len -= 1
        for i in range(self.level):
            if update[i].forward[i] != curr:
                update[i].nb_len[i] -= 1
            else:
                # 对第 i 层的状态进行更新，将 forward 指向被删除节点的下一跳
                update[i].nb_len[i] += curr.nb_len[i] - 1
                update[i].forward[i] = curr.forward[i]
        # 更新当前的 level
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1

    def add(self, num) -> None:
        self._len += 1
        update = [self.head] * MAX_LEVEL
        cur_idx = [0] * MAX_LEVEL
        curr = self.head

        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 num 的元素
            if i < self.level - 1 and not cur_idx[i]:
                cur_idx[i] = cur_idx[i + 1]
            while curr.forward[i] and curr.forward[i].val < num:
                # cur_idx[i] += curr.forward[i].nb_len[i]
                cur_idx[i] += curr.nb_len[i]
                curr = curr.forward[i]
            update[i] = curr
        idx = cur_idx[0] + 1
        # print(cur_idx,idx)
        lv = random_level()
        self.level = max(self.level, lv)
        new_node = SkiplistNode(num, lv)
        for i in range(lv):
            # 对第 i 层的状态进行更新，将当前元素的 forward 指向新的节点
            old = update[i].nb_len[i] + 1
            update[i].nb_len[i] = idx - cur_idx[i]
            new_node.nb_len[i] = old - update[i].nb_len[i]
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node
        for i in range(lv, self.level):
            update[i].nb_len[i] += 1

    def discard(self, num: int) -> bool:
        update = [None] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # 找到第 i 层小于且最接近 num 的元素
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr is None or curr.val != num:  # 值不存在
            return False
        self._len -= 1
        for i in range(self.level):
            if update[i].forward[i] != curr:
                update[i].nb_len[i] -= 1
                # break
            else:
                # 对第 i 层的状态进行更新，将 forward 指向被删除节点的下一跳
                update[i].nb_len[i] += curr.nb_len[i] - 1
                update[i].forward[i] = curr.forward[i]
        # 更新当前的 level
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True

    def __str__(self):
        cur = self.head
        ans = []
        while cur.forward[0]:
            ans.append(cur.forward[0].val)
            cur = cur.forward[0]
        return str(ans)

    def __repr__(self):
        return self.__str__()


class ODTNode:
    __slots__ = ['l', 'r', 'v']

    def __init__(self, l, r, v):
        self.l, self.r, self.v = l, r, v

    def __lt__(self, other):
        return self.l < other.l

    def jiebao(self):
        return self.l, self.r, self.v

    def __str__(self):
        return str(self.jiebao())

    def __repr__(self):
        return str(self.jiebao())


class ODT:
    def __init__(self, l=0, r=10 ** 9, v=0):
        # 珂朵莉树，声明闭区间[l,r]上所有的值都是v
        # l可以从0开始，r可以不建议大于1e18，因为py会变成大数运算
        # 注意v赋初值
        # 以后都用手撕的跳表做了
        self.tree = Skiplist([ODTNode(l, r, v)])

    def __str__(self):
        return str(self.tree)

    def split(self, pos):
        """ 在pos位置切分，返回左边界l为pos的线段下标 lgn  """
        tree = self.tree
        p, v1, v2 = tree.bisect_left_kvp(ODTNode(pos, 0, 0))
        if p != len(tree) and v1.l == pos:
            return p
        l, r, v = v2.jiebao()
        v2.r = pos - 1
        # tree.pop(p)
        # tree.add(ODTNode(l,pos-1,v))
        tree.add(ODTNode(pos, r, v))
        return p

    def assign(self, l, r, v):
        """        把[l,r]区域全变成val    lgn    """
        tree = self.tree
        begin = self.split(l)
        end = self.split(r + 1)
        for _ in range(begin, end):
            del tree[begin]
        tree.add(ODTNode(l, r, v))

    def query_point(self, pos):
        """ 单点查询pos位置的值 """
        tree = self.tree
        p, v, v1 = tree.bisect_left_kvp(ODTNode(pos, 0, 0))
        if p != len(tree) and v.l == pos:
            return v.v
        return v1.v


#  	1714 ms
def solve(n, m, a, b, qs):
    INF = inf
    st = ODT(0, 10 ** 10, INF)
    ans = []
    for q in qs:
        if q[0] == 1:
            x, y, k = q[1] - 1, q[2] - 1, q[3]
            st.assign(y, y + k - 1, x - y)
        elif q[0] == 2:
            i = q[1] - 1
            d = st.query_point(i)
            if d < INF:
                ans.append(a[i + d])
            else:
                ans.append((b[i]))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    import gc; # 注意gc不写会TLE

    gc.disable()
    n, m = RI()
    a = RILST()
    b = RILST()
    q = []
    for _ in range(m):
        q.append(RILST())
    solve(n, m, a, b, q)

