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
