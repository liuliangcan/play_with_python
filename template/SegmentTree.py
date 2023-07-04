"""线段树"""

class IntervalTreeRURQSum:
    """区间加，区间求和"""
    def __init__(self, size):
        self.size = size
        self.interval_tree = [0 for _ in range(size * 4)]
        self.lazys = [0 for _ in range(size * 4)]

    def give_lay_to_son(self, p, l, r):
        interval_tree = self.interval_tree
        lazys = self.lazys
        if lazys[p] == 0:
            return
        mid = (l + r) // 2
        interval_tree[p * 2] += lazys[p] * (mid - l + 1)
        interval_tree[p * 2 + 1] += lazys[p] * (r - mid)
        lazys[p * 2] += lazys[p]
        lazys[p * 2 + 1] += lazys[p]
        lazys[p] = 0

    def add_interval(self, p, l, r, x, y, val):
        """
        把[x,y]区域全+=val
        """
        if y < l or r < x:
            return
        interval_tree = self.interval_tree
        lazys = self.lazys
        if x <= l and r <= y:
            interval_tree[p] += val * (r - l + 1)
            lazys[p] += val
            return
        self.give_lay_to_son(p, l, r)
        mid = (l + r) // 2

        if x <= mid:
            self.add_interval(p * 2, l, mid, x, y, val)
        if mid < y:
            self.add_interval(p * 2 + 1, mid + 1, r, x, y, val)
        interval_tree[p] = interval_tree[p * 2] + interval_tree[p * 2 + 1]

    def sum_interval(self, p, l, r, x, y):
        """
        查找x,y区间的最大值        """

        if y < l or r < x:
            return 0
        if x <= l and r <= y:
            return self.interval_tree[p]
        self.give_lay_to_son(p, l, r)
        mid = (l + r) // 2
        s = 0
        if x <= mid:
            s += self.sum_interval(p * 2, l, mid, x, y)
        if mid < y:
            s += self.sum_interval(p * 2 + 1, mid + 1, r, x, y)
        return s
