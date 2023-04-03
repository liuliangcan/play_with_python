# Problem: E. Porcelain
# Contest: Codeforces - Codeforces Round 105 (Div. 2)
# URL: https://codeforces.com/problemset/problem/148/E
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/148/E

输入 n(≤100) m(≤1e4) 和 n 个双端队列（dq），对于每个 dq，先输入 k(≤100) 表示 dq 的大小，然后输入 dq 中的 k 个数，范围在 [1,100]。所有 k 之和 ≥m。

你需要从这 n 个 dq 中取出 m 个数，输出这 m 个数的和的最大值。
输入
2 3
3 3 7 2
3 4 1 5
输出 15

输入
1 3
4 4 3 1 2
输出 9
"""


class GroupedPackMaxMin:
    """分组背包求最大/最小值
    传入多组物品，每组中只能选一个，求极值。转化成01背包考虑，外层枚举体积j，内层尝试这个j选不同物品(注意和多重背包区分)。
    注意有时会和多重背包混淆：如题意描述成，第i种物品有c个，可以任选几个，但同种物品不区分。
    这种情况用多重背包计算就会出现重复方案，实际上考虑分组背包：这组中有c种物品，只能选0/1个。这c种物品分别是1个i，2个i。。c个i。
    """

    def __init__(self, vol, grouped_items=None, merge=max):
        self.grouped_items = grouped_items  # 形如[[(1,2),(2,3)],[(1,2),(2,3)],]，注意是多组数组，每组中只能选一个
        self.merge = merge
        self.vol = vol
        self.f = [0] * (vol + 1)  # f[j]代表体积不超过j时的最优值，

    def grouped_pack(self, items):  # 注意items不要传入迭代器，只能扫一遍被坑了
        f, merge = self.f, self.merge
        for j in range(self.vol, 0, -1):
            for v, w in items:
                if j >= v:
                    f[j] = merge(f[j], f[j - v] + w)

    def run(self):
        if self.grouped_items:
            for items in self.grouped_items:
                self.grouped_pack(items)
        return self.f


#   608    ms
def solve1():
    n, m = RI()
    gp = GroupedPackMaxMin(m)
    for _ in range(n):
        k, *q = RI()
        mx = [0] * (k + 1)
        mx[k] = sum(q)  # 这个队列选k个只能全选
        # 枚举中间一个连续段的和，剩下两段就是前后缀的和，花费k*k时间
        for l in range(k):
            p = 0
            for r in range(l, k):
                p += q[r]
                size = k - (r - l + 1)
                mx[size] = max(mx[size], mx[k] - p)

        gp.grouped_pack(list(enumerate(mx)))  # 注意不要传入迭代器，只能扫一遍

    print(gp.f[-1])


#   483    ms
def solve():
    n, m = RI()
    t = 0
    f = [0] + [-inf] * m
    for _ in range(n):
        k, *q = RI()
        mx = [0] * (k + 1)
        mx[k] = sum(q)  # 这个队列选k个只能全选
        # 枚举中间一个连续段的和，剩下两段就是前后缀的和
        for l in range(k):
            p = 0
            for r in range(l, k):
                p += q[r]
                size = k - (r - l + 1)
                mx[size] = max(mx[size], mx[k] - p)
        t = min(t + k, m)
        for j in range(t, 0, -1):
            for v, w in enumerate(mx):
                if j < v: break
                f[j] = max(f[j], f[j - v] + w)

    print(f[-1])


if __name__ == '__main__':
    solve()
