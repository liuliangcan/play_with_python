import sys
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc106/tasks/abc106_d

输入 n(≤500) m(≤2e5) q(≤1e5)。
然后输入 m 个在 [1,n] 内的闭区间，即每行输入两个数表示闭区间 [L,R]。
然后输入 q 个询问，每个询问也是输入两个数表示闭区间 [p,q]。
对每个询问，输出在 [p,q] 内的完整闭区间的个数。
输入
2 3 1
1 1
1 2
2 2
1 2
输出
3
解释 输入的三个闭区间都在 [1,2] 内

输入
10 3 2
1 5
2 8
7 10
1 7
3 10
输出
1
1
https://atcoder.jp/contests/abc106/submissions/36691336

定义 f[l][r] 表示在 [l,r] 内的完整闭区间个数。

容斥一下可得
f[l][r] = f[l+1][r] + f[l][r-1] - f[l+1][r-1] + a[l][r]
这里 a[l][r] 是 m 个闭区间中的 [l,r] 的个数。

这样就可以 O(1) 地回答每个询问了。
"""
"""方法2
对询问离线，右端点排序。
对输入也按右端点排序，然后双指针处理询问。
记输入的左右端点是l,r;询问的左右端点是x,y
对输入r小于询问y的输入l加入集合。则集合内r一定包含在询问的y内(r<=y)，只需判断左端点也包含即可(l>=x)。
因此需要用个有序集合，且能快速计数>=x的数量。
显然SortedList可以胜任；
由于lr的数据范围是500，因此可以树状数组。如果含负数或者特别大，可以先离散化。
"""


#  335 ms
def solve3(n, m, q, lr, qs):
    a = [[0] * (n + 2) for _ in range(n + 2)]
    for l, r in lr:
        a[l][r] += 1
    f = [[0] * (n + 2) for _ in range(n + 2)]
    for l in range(n, 0, -1):
        for r in range(l, n + 1):
            f[l][r] = f[l + 1][r] + f[l][r - 1] - f[l + 1][r - 1] + a[l][r]
    ans = [0] * q
    for i, (l, r) in enumerate(qs):
        ans[i] = f[l][r]
    # print('\n'.join(map(str, ans)))
    print(*ans, sep='\n')


class BinIndexTree:
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.a = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_point(i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始
        while i <= self.size:
            self.c[i] += v
            i += i & -i

    def set_point(self, i, v):  # 单点修改，下标从1开始 需要先计算差值，然后调用add
        self.add_point(i, v - self.a[i])

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            i = i & (i - 1)
        return s

    def lowbit(self, x):
        return x & -x


#   SortedList   ms
def solve1(n, m, q, lr, qs):
    lr.sort(key=lambda x: x[1])
    j = 0
    from sortedcontainers import SortedList
    h = SortedList()
    ans = [0] * q
    for i, (x, y) in sorted(zip(range(q), qs), key=lambda v: v[1][1]):
        while j < m and lr[j][1] <= y:
            h.add(lr[j][0])
            j += 1
        ans[i] = len(h) - h.bisect_left(x)
    print('\n'.join(map(str, ans)))


#   708      ms
def solve(n, m, q, lr, qs):
    lr.sort(key=lambda x: x[1])
    mx = 500
    j = 0
    tree = BinIndexTree(mx)

    ans = [0] * q
    for i, (x, y) in sorted(zip(range(q), qs), key=lambda v: v[1][1]):
        while j < m and lr[j][1] <= y:
            tree.add_point(lr[j][0], 1)
            j += 1
        ans[i] = tree.sum_interval(x, mx)
    print('\n'.join(map(str, ans)))


def main(rs=None, ri=None):
    global RS, RI
    if rs:
        RS, RI = rs, ri
    n, m, q = RI()
    lr = []
    for _ in range(m):
        lr.append(RILST())
    qs = []
    for _ in range(q):
        qs.append(RILST())

    solve(n, m, q, lr, qs)


if __name__ == '__main__':
    if os.path.exists('test.test'):
        # testcase 2个字段分别是input和output；仅当 spider_switch=False时，这里才生效，否则会在线爬
        test_cases = (
            (
                """
    4 2
    2 3
    3 5
    """,
                """
    11
    """
            ),
            (
                """
    6 1
    3 4
    """,
                """
    -1
    """
            ),
        )
        from atc.AtcLocalTest import AtcLocalTest

        AtcLocalTest(main, url=PROBLEM.strip().split('\n')[0].strip(), test_cases=test_cases, spider_switch=True).run()
    else:
        main()
