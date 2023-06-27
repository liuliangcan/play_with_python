# Problem: C. Three displays
# Contest: Codeforces - Codeforces Round 485 (Div. 2)
# URL: https://codeforces.com/problemset/problem/987/C
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
from bisect import bisect_left

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/987/C

输入 n(3≤n≤3000) 和长度均为 n 的数组 a(1≤a[i]≤1e9) 和数组 b(1≤b[i]≤1e8)。
输出在满足 i<j<k 且 a[i]<a[j]<a[k] 的前提下，b[i]+b[j]+b[k] 的最小值。
如果不存在这样的 (i,j,k)，输出 -1。

进阶：O(nlogn)。
进阶：改成 a 的长为 4 的递增子序列（本题长为 3）。改成 5？改成 m？
输入
5
2 4 5 4 10
40 30 20 10 40
输出 90

输入
3
100 101 100
2 4 5
输出 -1

输入
10
1 2 3 4 5 6 7 8 9 10
10 13 11 14 15 12 13 13 18 13
输出 33
"""

inf = 10 ** 9


#    187   ms
def solve1():
    n, = RI()
    a = RILST()
    b = RILST()
    f, g = [inf] * n, [inf] * n
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                f[i] = min(f[i], b[j] + b[i])
    for i in range(2, n):
        for j in range(i):
            if a[j] < a[i]:
                g[i] = min(g[i], f[j] + b[i])
    ans = min(g)
    if ans == inf:
        return print(-1)
    print(ans)


#    124   ms
def solve2():
    n, = RI()
    a = RILST()
    b = RILST()
    f, g = [inf] * n, [inf] * n
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i] and f[i] > b[j] + b[i]:
                f[i] = b[j] + b[i]
    for i in range(2, n):
        for j in range(i):
            if a[j] < a[i] and g[i] > f[j] + b[i]:
                g[i] = f[j] + b[i]
    ans = min(g)
    if ans == inf:
        return print(-1)
    print(ans)


class ZKW:
    # n = 1
    # size = 1
    # log = 2
    # d = [0]
    # op = None
    # e = 10 ** 15
    """自低向上非递归写法线段树，0_indexed
    tmx = ZKW(pre, max, -2 ** 61)
    """
    __slots__ = ('n', 'op', 'e', 'log', 'size', 'd')

    def __init__(self, V, OP, E):
        """
        V: 原数组
        OP: 操作:max,min,sum
        E: 每个元素默认值
        """
        self.n = len(V)
        self.op = OP
        self.e = E
        self.log = (self.n - 1).bit_length()
        self.size = 1 << self.log
        self.d = [E for i in range(2 * self.size)]
        for i in range(self.n):
            self.d[self.size + i] = V[i]
        for i in range(self.size - 1, 0, -1):
            self.update(i)

    def set(self, p, x):
        # assert 0 <= p and p < self.n
        update = self.update
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1):
            update(p >> i)

    def get(self, p):
        # assert 0 <= p and p < self.n
        return self.d[p + self.size]

    def query(self, l, r):  # [l,r)左闭右开
        # assert 0 <= l and l <= r and r <= self.n
        sml, smr, op, d = self.e, self.e, self.op, self.d

        l += self.size
        r += self.size

        while l < r:
            if l & 1:
                sml = op(sml, d[l])
                l += 1
            if r & 1:
                smr = op(d[r - 1], smr)
                r -= 1
            l >>= 1
            r >>= 1
        return self.op(sml, smr)

    def all_query(self):
        return self.d[1]

    def max_right(self, l, f):
        """返回l右侧第一个不满足f的位置"""
        # assert 0 <= l and l <= self.n
        # assert f(self.e)
        if l == self.n:
            return self.n
        l += self.size

        sm, op, d, size = self.e, self.op, self.d, self.size
        while True:
            while l % 2 == 0:
                l >>= 1
            if not (f(op(sm, d[l]))):
                while l < size:
                    l = 2 * l
                    if f(op(sm, d[l])):
                        sm = op(sm, d[l])
                        l += 1
                return l - size
            sm = op(sm, d[l])
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, f):
        """返回r左侧连续满足f的最远位置的位置"""
        # assert 0 <= r and r < self.n
        # assert f(self.e)
        if r == 0:
            return 0
        r += self.size
        sm, op, d, size = self.e, self.op, self.d, self.size

        while True:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not (f(op(d[r], sm))):
                while r < size:
                    r = (2 * r + 1)
                    if f(op(d[r], sm)):
                        sm = op(d[r], sm)
                        r -= 1
                return r + 1 - size
            sm = op(d[r], sm)
            if (r & -r) == r:
                break
        return 0

    def update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def __str__(self):
        return str([self.get(i) for i in range(self.n)])


#    140   ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    h = sorted(set(a))
    f1 = ZKW([inf] * len(h), min, inf)
    f2 = ZKW([inf] * len(h), min, inf)
    ans = inf
    for k, v in zip(a, b):
        x = bisect_left(h, k)
        ans = min(ans, f2.query(0, x) + v)
        f2.set(x, min(f2.get(x), f1.query(0, x) + v))
        f1.set(x, min(f1.get(x), v))

    if ans == inf:
        return print(-1)
    print(ans)


if __name__ == '__main__':
    solve()
