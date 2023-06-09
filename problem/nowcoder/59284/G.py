# Problem: 跳石头，搭梯子
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/59284/G
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
PROBLEM = """
"""


class BinIndexTreeRURQ:
    """树状数组的RURQ模型"""

    def __init__(self, size_or_nums):  # 树状数组,区间加区间求和，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            self.c2 = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.c = [0 for _ in range(self.size + 5)]
            self.c2 = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_interval(i + 1, i + 1, v)

    def add_point(self, c, i, v):  # 单点增加,下标从1开始;不支持直接调用，这里增加的是差分数组的单点,同步修改c2
        while i <= self.size:
            c[i] += v
            i += -i & i

    def sum_prefix(self, c, i):  # 前缀求和，下标从1开始；不支持直接调用，这里求和的是差分数组的前缀和;传入c决定怎么计算，但是不要直接调用 无视吧
        s = 0
        while i >= 1:
            s += c[i]
            i -= -i & i
        return s

    def add_interval(self, l, r, v):  # 区间加，下标从1开始，把[l,r]闭区间都加v
        self.add_point(self.c, l, v)
        self.add_point(self.c, r + 1, -v)
        self.add_point(self.c2, l, (l - 1) * v)
        self.add_point(self.c2, r + 1, -v * r)

    def sum_interval(self, l, r):  # 区间求和，下标从1开始，返回闭区间[l,r]上的求和
        return self.sum_prefix(self.c, r) * r - self.sum_prefix(self.c2, r) - self.sum_prefix(self.c, l - 1) * (
                l - 1) + self.sum_prefix(self.c2, l - 1)

    def query_point(self, i):  # 单点询问值，下标从1开始，返回i位置的值
        return self.sum_prefix(self.c, i)

    def lowbit(self, x):
        return x & -x

"""
先用单调栈求出所有可以搭的桥
记录每个桥如果搭，贡献是多少，显然是 原花费-过桥的花费
把桥按贡献排序，从大到小取m个，但不能重叠
答案就是 原花费-桥的贡献
证明：请木木大佬补充
"""
#   1113ms
def solve():
    n, m = RI()
    a = RILST()
    ans = 0
    p = [0] * n  # 相邻差的前缀和
    for i in range(1, n):
        d = abs(a[i] - a[i - 1])
        ans += d
        p[i] = d + p[i - 1]
    # print(p)
    st = []
    lines = []
    for i, v in enumerate(a):
        while st and a[st[-1]] < v:
            j = st[-1]
            if j + 1 < i:
                lines.append((abs(v - a[j]) - (p[i] - p[j]), j, i))  # j~i可以搭梯子
            st.pop()
        if st and st[-1] + 1 < i:
            j = st[-1]
            if j + 1 < i:
                lines.append((abs(v - a[j]) - (p[i] - p[j]), j, i))  # j~i可以搭梯子
        st.append(i)
    lines.sort()
    tree = BinIndexTreeRURQ(n)
    for w, l, r in lines:
        if not m:
            break
        if tree.sum_interval(l + 1, r) == 0:
            ans += w
            m -= 1
        tree.add_interval(l + 1, r, 1)

    # print(lines)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
