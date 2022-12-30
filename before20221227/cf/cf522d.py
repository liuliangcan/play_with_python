import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: sys.stdin.readline().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/522/D

输入 n(2≤n≤2e5) 和 m(1≤m≤2e5)；然后输入一个长为 n 的数组 a(-1e9≤a[i]≤1e9)，数组下标从 1 开始；然后输入 m 个询问，每个询问表示一个数组 a 内的闭区间 [L,R] (1≤L≤R≤n)。

对每个询问，输出区间内的相同元素下标之间的最小差值。如果区间内不存在相同元素，输出 -1。

输入
5 3
1 1 2 3 2
1 5
2 4
3 5
输出
1
-1
2

输入
6 5
1 2 1 3 2 3
4 6
1 3
2 5
2 4
1 6
输出
2
2
3
-1
2
"""


class ITreeNode:
    __slots__ = ['val', 'l', 'r']

    def __init__(self, l=None, r=None, v=0):
        self.val, self.l, self.r = v, l, r


class IntervalTree:
    def __init__(self):
        self.root = ITreeNode()

    def update_from_son(self, node):
        node.val = min(node.l.val if node.l else inf, node.r.val if node.r else inf)
        return node

    def update_point(self, node, l, r, index, val):
        if index < l or r < index:
            return None
        if not node:
            node = ITreeNode(v=inf)
        if l == r:
            node.val = val
            return node
        mid = (l + r) // 2
        if index <= mid:
            node.l = self.update_point(node.l, l, mid, index, val)
        else:
            node.r = self.update_point(node.r, mid + 1, r, index, val)

        return self.update_from_son(node)

    def query(self, node, l, r, x, y):
        if not node or y < l or r < x:
            return inf
        if x <= l and r <= y:
            return node.val
        mid = (l + r) // 2
        s = inf
        if x <= mid:
            s = min(s, self.query(node.l, l, mid, x, y))
        if mid < y:
            s = min(s, self.query(node.r, mid + 1, r, x, y))
        return s


class BinIndexTreeMax:
    def __init__(self, size):
        self.size = size
        self.a = [-inf for _ in range(size + 5)]
        self.h = self.a[:]
        self.mx = -inf

    def update(self, x, v):
        if v > self.mx:
            self.mx = v
        a = self.a
        h = self.h
        a[x] = v
        while x <= self.size:
            if h[x] < v:
                h[x] = v
            else:
                break
            x += self.lowbit(x)

    def query(self, l, r):
        a = self.a
        h = self.h
        ans = a[r]
        while l != r:
            r -= 1
            while r - self.lowbit(r) > l:
                if ans < h[r]:
                    ans = h[r]
                    if ans == self.mx:
                        break
                r -= self.lowbit(r)
            # ans = min(ans, self.a[r])
            if ans > a[r]:
                ans = a[r]
            if ans == self.mx:
                break
        return ans

    def lowbit(self, x):
        return x & -x


class BinIndexTreeMin:
    def __init__(self, size):
        self.size = size
        self.a = [inf for _ in range(size + 5)]
        self.h = self.a[:]
        self.mn = inf

    def update(self, x, v):
        if v < self.mn:
            self.mn = v
        a = self.a
        h = self.h
        a[x] = v
        while x <= self.size:
            if h[x] > v:
                h[x] = v
            else:
                break
            x += self.lowbit(x)

    def query(self, l, r):
        a = self.a
        h = self.h
        ans = a[r]
        while l != r:
            r -= 1
            while r - self.lowbit(r) > l:
                if ans > h[r]:
                    ans = h[r]
                    if ans == self.mn:
                        break
                r -= self.lowbit(r)
            # ans = min(ans, self.a[r])
            if ans > a[r]:
                ans = a[r]
            if ans == self.mn:
                break
        return ans

    def lowbit(self, x):
        return x & -x


# 	2932  ms
def solve(n, m, a, q):
    a = [0] + a
    q = sorted([(l, r, i) for i, (l, r) in enumerate(q)], key=lambda x: x[1])
    # tree = IntervalTree()
    tree = BinIndexTreeMin(n + 5)
    pre = {}
    j = 1
    ans = [-1] * m
    for l, r, i in q:
        while j <= r:
            v = a[j]
            if v in pre:
                idx = pre[v]
                d = j - idx
                tree.update(idx, d)

            pre[v] = j
            j += 1
        cur = tree.query(l, r)
        # print(tree.a, tree.h, l, r, cur)
        if cur < inf:
            ans[i] = cur

    # print(ans)
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    n, m = RI()
    a = RILST()
    q = []
    for _ in range(m):
        q.append(RILST())

    solve(n, m, a, q)