from heapq import *


class ExamRoom:

    def __init__(self, n: int):
        from sortedcontainers import SortedList
        self.pos = SortedList()
        self.h = []
        self.n = n

    def seat(self) -> int:
        pos = self.pos
        h = self.h
        n = self.n
        if not pos:
            pos.add(0)
            # print(h)
            # print(pos)
            return 0
        if len(pos) == 1:
            p = pos[0]
            a, d = 0, p
            l, r = 0, p
            if n - 1 - p > d:
                a = n - 1
                l, r = p, n - 1
            pos.add(a)
            heappush(h, (-((r - l) // 2), l, r))
            # print(h)
            # print(pos)
            return a

        def ok(d, l, r):
            if l not in pos:
                return False
            p = pos.bisect_right(l)
            if p == len(pos) or pos[p] != r:
                return False
            return True

        a, d = 0, 0
        if pos[0] != 0 and pos[0] > d:
            a = 0
            d = pos[0]
        if pos[-1] != n - 1 and n - 1 - pos[-1] > d:
            d = n - 1 - pos[-1]
            a = n - 1

        while h and (-h[0][0] > d or (-h[0][0] == d and h[0][1] < a)):
            d, l, r = heappop(h)
            if not ok(d, l, r):
                continue
            a = (l + r) // 2
            break
        if a == 0:
            l, r = 0, pos[0]
            heappush(h, (-((r - l) // 2), l, r))
        elif a == n - 1:
            l, r = a, n - 1
            heappush(h, (-((r - l) // 2), l, r))
        else:
            x, y = l, r
            l, r = x, a
            heappush(h, (-((r - l) // 2), l, r))
            l, r = a, y
            heappush(h, (-((r - l) // 2), l, r))
        pos.add(a)
        # print(h)
        # print(pos)
        return a

    def leave(self, p: int) -> None:
        pos = self.pos
        if p == pos[0] or p == pos[-1]:
            pos.remove(p)
            return
        h = self.h
        a = pos.bisect_left(p)
        l, r = pos[a - 1], pos[a + 1]
        pos.remove(p)
        heappush(h, (-((r - l) // 2), l, r))
        # print(self.pos)

"""懒删除堆+SortedList
有序集合pos存储已占用的座位号
大顶堆里维护可用区间，保证 (r - l) // 2 最大的在堆顶(l小的也在前边)，这样遇到的第一个合法区间就可以用。
如何判断合法区间[l,r]：
    lr必须都在pos且比l大的第一个数一定是r（即中间不能有其他值，且必须存在r）
另外，要特殊尝试0和n-1位置能不能放，因为讨论区间时，不包括他们。
seat:
    特殊处理len(pos)<2的情况，即没有区间：
        0: 直接坐在0
        1: 一定是坐0或1，检查一下，且增加一个区间。
    其它情况必至少存在一个区间(2个以上pos)
        先尝试坐0或n-1计算这时的最大距离，
        然后以这个距离为基准去堆里找第一个合法区间，不合法的干掉即可。
        注意 如果距离相同，区间里的坐标可能小于n-1,因此依然需要尝试。
"""
    """
["ExamRoom","seat","seat","seat","seat","leave","seat"]
[[10],[],[],[],[],[4],[]]
[null,0,9,4,2,null,1]
[null,0,9,4,2,null,5]

[]
SortedList([0])
[(-4, 0, 9)]
SortedList([0, 9])
[(-2, 0, 4), (-2, 4, 9)]
SortedList([0, 4, 9])
[(-2, 4, 9), (-1, 0, 2), (-1, 2, 4)]
SortedList([0, 2, 4, 9])
SortedList([0, 2, 9])
[(-1, 2, 4), (0, 0, 1), (0, 1, 2)]
SortedList([0, 1, 2, 9])


    """
