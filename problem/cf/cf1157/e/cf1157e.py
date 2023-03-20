# Problem: E. Minimum Array
# Contest: Codeforces - Codeforces Round 555 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1157/E
# Memory Limit: 256 MB
# Time Limit: 2000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1157/E

输入 n(≤2e5) 和两个长为 n 的数组 a b，元素范围在 [0,n-1]。

你可以重排数组 b。
还有一个长为 n 的数组 c，其中 c[i] = (a[i] + b[i]) % n。
输出字典序最小的 c。
输入
4
0 1 2 1
3 2 1 1
输出
1 0 0 2 

输入
7
2 5 1 5 3 4 3
2 4 3 5 6 5 1
输出
0 0 0 1 0 2 4 
"""
"""https://codeforces.com/contest/1157/submission/198294259

对于 a[i]，需要去找 (n-a[i])%n，如果不存在就找更大的，如果找到 n-1 都没有，就从 0 开始找。

这样做是暴力的，有多种优化方法：

- 类似 multiset 这样的平衡树，只维护存在的
- 并查集，如果 x 不存在，则把 x 和 x+1 合并，这样可以快速找到下一个存在的。
"""

class BinIndexTree:
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
            i += i & -i

    # def set_point(self, i, v):  # 单点修改，下标从1开始 需要先计算差值，然后调用add
    #     self.add_point(i, v - self.a[i])
    #     self.a[i] = v

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            # i -= i&-i
            i &= i - 1
        return s

    def min_right(self, i):
        """寻找[i,size]闭区间上第一个正数(不为0的数),注意i是1-indexed。若没有返回size+1"""
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

    def lowbit(self, x):
        return x & -x


#    546   ms
def solve1():
    n, = RI()
    a = RILST()
    b = RILST()
    tree = BinIndexTree(n * 2)
    for v in b:
        tree.add_point(v + 1, 1)
        tree.add_point(v + 1 + n, 1)
    c = []
    for v in a:
        p = tree.min_right(n - v + 1) - 1
        c.append((p + v) % n)
        tree.add_point(p % n + 1, -1)
        tree.add_point(p % n + 1 + n, -1)
    print(*c)


class DSU:
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.setCount = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            self.edge_size[y] += 1
            return False
        # if self.size[x] > self.size[y]:  # 注意如果要定向合并x->y，需要干掉这个；实际上上边改成find_fa后，按轶合并没必要了，所以可以常关
        #     x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.setCount -= 1
        return True


#    311   ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    dsu = DSU(n * 2 + 1)
    cnt = [0] * (2 * n + 1)
    for v in b:
        cnt[v] += 1
        cnt[v + n] += 1

    def find(x):
        while cnt[x] <= 0:
            dsu.union(x, x + 1)
            x = dsu.find_fa(x)
        cnt[x % n] -= 1
        cnt[x % n + n] -= 1
        return x % n

    print(*[(find(n - v) + v) % n for v in a])


if __name__ == '__main__':
    solve()
