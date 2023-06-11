# Problem: 区间异或
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/5040/
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

MOD = 10 ** 9 + 7
PROBLEM = """
"""


class IntervalTree:
    def __init__(self, size, nums):
        self.size = size
        self.interval_tree = [0 for _ in range(size * 4)]
        self.lazys = [0 for _ in range(size * 4)]

        self.nums = nums
        self.build_tree(1, 1, size)

    def give_lay_to_son(self, p, l, r):
        interval_tree = self.interval_tree
        lazys = self.lazys
        if lazys[p] == 0:
            return
        mid = (l + r) // 2
        interval_tree[p * 2] = mid - l + 1 - interval_tree[p * 2]
        interval_tree[p * 2 + 1] = r - mid - 1 + 1 - interval_tree[p * 2 + 1]
        lazys[p * 2] ^= lazys[p]
        lazys[p * 2 + 1] ^= lazys[p]
        lazys[p] = 0

    def update(self, p, l, r, x, y, val):
        """
        把[x,y]区域全异或val
        """
        if y < l or r < x:
            return
        interval_tree = self.interval_tree
        lazys = self.lazys
        if x <= l and r <= y:
            interval_tree[p] = (r-l+1)-interval_tree[p]
            lazys[p] ^= val
            return
        self.give_lay_to_son(p, l, r)
        mid = (l + r) // 2
        if x <= mid:
            self.update(p * 2, l, mid, x, y, val)
        if mid < y:
            self.update(p * 2 + 1, mid + 1, r, x, y, val)
        interval_tree[p] = interval_tree[p * 2] + interval_tree[p * 2 + 1]

    def query(self, p, l, r, x, y):
        """
        查找x,y区间的和        """

        if y < l or r < x:
            return 0
        if x <= l and r <= y:
            return self.interval_tree[p]
        self.give_lay_to_son(p, l, r)
        mid = (l + r) // 2
        s = 0
        if x <= mid:
            s += self.query(p * 2, l, mid, x, y)
        if mid < y:
            s += self.query(p * 2 + 1, mid + 1, r, x, y)
        return s

    def build_tree(self, p, l, r):
        interval_tree = self.interval_tree
        nums = self.nums
        if l == r:
            interval_tree[p] = nums[l - 1]
            return
        mid = (l + r) // 2
        self.build_tree(p * 2, l, mid)
        self.build_tree(p * 2 + 1, mid + 1, r)
        interval_tree[p] = interval_tree[p * 2] + interval_tree[p * 2 + 1]


#       ms
def solve():
    n, = RI()
    a = RILST()
    tree = [IntervalTree(n, [v >> i & 1 for v in a]) for i in range(20)]
    m, = RI()
    for _ in range(m):
        t, *q = RI()
        if t == 1:
            l, r = q
            print(sum(tree[i].query(1, 1, n, l, r) << i for i in range(20)))
        else:
            l, r, x = q
            for i in range(20):
                p = x >> i & 1
                if p:
                    tree[i].update(1, 1, n, l, r, 1)


if __name__ == '__main__':
    n, = RI()
    a = RILST()
    tree = [IntervalTree(n, [v >> i & 1 for v in a]) for i in range(20)]
    m, = RI()
    for _ in range(m):
        t, *q = RI()
        if t == 1:
            l, r = q
            print(sum(tree[i].query(1, 1, n, l, r) << i for i in range(20)))
        else:
            l, r, x = q
            for i in range(20):
                p = x >> i & 1
                if p:
                    tree[i].update(1, 1, n, l, r, 1)
