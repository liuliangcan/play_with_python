"""迭代写法的zwk线段树，注意是1-indexed，注意query的时候是闭区间[l,r]"""


class SegTree:
    __slots__ = ('n', 'N', 'seg')

    def __init__(self, n):
        self.n = n
        N = 1
        while N < n:
            N <<= 1
        self.N = N
        self.seg = [0] * (2 * N)

    def build(self, arr):  # 这个arr是1-indexed
        for i in range(1, self.n + 1):
            self.seg[self.N + i - 1] = arr[i]
        for i in range(self.N - 1, 0, -1):
            a = self.seg[i << 1]
            b = self.seg[i << 1 | 1]
            self.seg[i] = a if a >= b else b

    def update(self, pos, val):
        i = self.N + pos - 1
        self.seg[i] = val
        i >>= 1
        while i:
            a = self.seg[i << 1]
            b = self.seg[i << 1 | 1]
            self.seg[i] = a if a >= b else b
            i >>= 1

    def query(self, l, r):
        l += self.N - 1
        r += self.N - 1
        res = 0
        while l <= r:
            if l & 1:
                if self.seg[l] > res:
                    res = self.seg[l]
                l += 1
            if not (r & 1):
                if self.seg[r] > res:
                    res = self.seg[r]
                r -= 1
            l >>= 1
            r >>= 1
        return res


""" 
"""