# Problem: 智商药
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/5049/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
from bisect import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""


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
            self.c[i] %= MOD
            i += i & -i

    # def set_point(self, i, v):  # 单点修改，下标从1开始 需要先计算差值，然后调用add
    #     self.add_point(i, v - self.a[i])
    #     self.a[i] = v

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return (self.sum_prefix(r) - self.sum_prefix(l - 1)) % MOD

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            s %= MOD
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

    def kth(self, s):
        """返回<=s的最小下标"""
        pos = 0
        for j in range(18, -1, -1):
            if pos + (1 << j) <= self.size and self.c[pos + (1 << j)] <= s:
                pos += (1 << j)
                s -= self.c[pos]
        return pos

    def lowbit(self, x):
        return x & -x


#       ms
def solve():
    n, m = RI()
    a = []
    for _ in range(m):
        a.append(RILST())

    a.sort(key=lambda x: x[1])
    b = [y for _, y in a]
    f = BinIndexTree(m)
    ans = 0
    for i, (l, r) in enumerate(a, start=1):
        x = bisect_left(b, l) + 1
        y = bisect_right(b, r - 1) - 1 + 1
        if x <= y:
            f.add_point(i, f.sum_interval(x, y))
        if l == 0:
            f.add_point(i, 1)

        if r == n:
            ans = (ans + f.sum_interval(i, i)) % MOD
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
