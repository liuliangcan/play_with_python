# Problem: E. Two Teams
# Contest: Codeforces - Codeforces Round 552 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1154/E
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
PROBLEM = """https://codeforces.com/problemset/problem/1154/E

输入 n k(1≤k≤n≤2e5) 和一个 1~n 的排列 p。
每次操作，选择 p 中最大的数字，然后删除 p 及其左右各 k 个未被删除的元素。
对于每个 p[i]，如果它是第 1,3,5,… 次操作被删除的，输出 1；如果它是第 2,4,6,… 次操作被删除的，输出 2。
输入
5 2
2 4 5 3 1
输出 11111

输入
5 1
2 1 3 5 4
输出 22111
解释 第一次操作删除 [3,5,4]，第二次操作删除 [2,1]

输入
7 1
7 2 1 3 5 4 6
输出 1121122

输入
5 1
2 4 5 3 1
输出 21112
"""
"""三个并查集模拟
- 又是连续集合的删除，考虑用并查集模拟。
- 由于p是个排列，求移除一些数后的最大值可以直接用一个并查集维护，每次删除一个数v就union(v,v-1)，这样最大值就是find(n)。DSU(n+1)
    - 若不是排列，可以用有序集合每次取end；或者先离散化，依然并查集。
- 令起两个并查集用来向后/向前删除，注意向前删除0需要连接到-1，但并查集没有-1，因此整体右移，下标从1开始计数比较方便。因此DSU(n+1)。
    - 基于同样的原因，向后删除n需要连接到n+1,因此DSU(n+2)。
- 注意代码里的s其实可以不删除，mx发现是0的时候跳出即可。
---
- 原来数组删除可以用双链表模拟，~~淦~~。
"""
"""https://codeforces.com/contest/1154/submission/201766208

由于数据范围是 1~n，可以用一个 pos 数组记录每个数的下标，然后用双向链表模拟。
从 n 开始倒着找这个数的位置，比如叫 i，如果它没有被删除，就在双向链表上删除 i 及其前后各 k 各节点。

双向链表可以用数组实现，维护 prev 和 next。
"""


class DSU:

    def __init__(self, n):
        self.fathers = list(range(n))

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
        self.fathers[x] = y
        return True


class LNode:
    __slots__ = 'pre', 'nxt', 'val'

    def __init__(self, val, pre=None, nxt=None):
        self.val, self.pre, self.nxt = val, pre, nxt
    def __str__(self):
        return f'LNode({self.val})'


class LinkedList:
    """双向链表，可以用来模拟一些删除数组中的元素的情况"""

    def __init__(self):
        self.head = LNode(0)
        self.tail = LNode(0, pre=self.head)
        self.head.nxt = self.tail
        self.size = 0

    def __len__(self):
        return self.size

    def append(self, v):
        """在链表尾添加元素  O(1)"""
        pre = self.tail.pre
        cur = LNode(v, nxt=self.tail, pre=pre)
        self.tail.pre = pre.nxt = cur
        self.size += 1
        return cur

    def appendleft(self, v):
        """在链表头添加元素 O(1)"""
        nxt = self.head.nxt
        cur = LNode(v, pre=self.head, nxt=nxt)
        self.head.nxt = nxt.pre = cur
        self.size += 1
        return cur

    def delete_node(self, node):
        """删除一个节点 O(1)"""
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre
        self.size -= 1
        return node

    def insert_after(self, node, v):
        """在指定节点node后边添加一个节点，赋值v,O(1)"""
        nxt = node.nxt
        new = LNode(v, pre=node, nxt=nxt)
        node.nxt = nxt.pre = new
        self.size += 1
        return new

    def insert_before(self, node, v):
        """在指定节点node前边添加一个节点，赋值v,O(1)"""
        pre = node.pre
        new = LNode(v, pre=pre, nxt=node)
        node.pre = pre.nxt = new
        self.size += 1
        return new

    def front(self):
        """获取第一个节点 O(1)"""
        return self.head.nxt

    def last(self):
        """获取最后一个节点 O(1)"""
        return self.tail.pre

    def __getitem__(self, idx):
        """按下标索引节点最坏O(n),首尾结点O(1),取决于离两端的距离"""
        if idx >= self.size or -idx > self.size:
            raise Exception(f'下标越界:{idx} of {self.size}')
        if idx < 0:
            idx = self.size + idx
        if idx < (self.size >> 1):
            cur = self.head
            for _ in range(idx + 1):
                cur = cur.nxt
            return cur
        else:
            cur = self.tail
            for _ in range(self.size - idx):
                cur = cur.pre
            return cur

    def clear(self):
        """清空链表 O(1)"""
        self.head.nxt = self.tail
        self.tail.pre = self.head
        self.size = 0

    def __repr__(self):
        ans = []
        cur = self.head.nxt
        while cur != self.tail:
            ans.append(cur.val)
            cur = cur.nxt
        return str(ans)


#    342   ms
def solve():
    n, k = RI()
    p = RILST()
    idx = [0] * n
    lst = LinkedList()
    mx = [None] * n
    for i, v in enumerate(p):
        idx[v - 1] = i
        lst.append(v - 1)
        # mx[v - 1] = lst.last()
        mx[v - 1] = lst[-1]
    # print(lst)
    # print(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5])
    # print(lst[-1],lst[-5],lst[-2],lst[-3],lst[-4],lst[-5])
    # print(mx)
    ans = [0] * n
    cnt = 0
    m = n - 1
    while True:
        while m >= 0 and not mx[m]:  # 找现存最大值
            m -= 1
        if m < 0: break  # 没有最大值
        i = mx[m]
        for _ in range(k):  # 向右删k个
            i = i.nxt
            if i is lst.tail:
                break
            v = lst.delete_node(i).val
            mx[v] = None
            ans[idx[v]] = cnt + 1
        i = mx[m]
        for _ in range(k):  # 向左删k个
            i = i.pre
            if i is lst.head:
                break
            v = lst.delete_node(i).val
            mx[v] = None
            ans[idx[v]] = cnt + 1
        lst.delete_node(mx[m])
        mx[m] = None
        ans[idx[m]] = cnt + 1
        # print(m,ans)
        # print(lst)
        cnt ^= 1

    print(*ans, sep='')


#  638     ms
def solve1():
    n, k = RI()
    p = RILST()
    s = {v: i for i, v in enumerate(p, start=1)}  # 记录每个数的下标
    mx, pre, suf = DSU(n + 1), DSU(n + 1), DSU(n + 2)  # 三个并查集用来记录相邻的数
    ans = [0] * n
    cnt = 0
    while s:
        m = mx.find_fa(n)
        mx.union(m, m - 1)
        i = s[m]
        ans[i - 1] = cnt + 1
        s.pop(m)
        mx.union(m, m - 1)
        suf.union(i, i + 1)
        pre.union(i, i - 1)
        j = i
        for _ in range(k):
            j = suf.find_fa(j)
            if j > n:
                break
            ans[j - 1] = cnt + 1
            s.pop(p[j - 1])
            mx.union(p[j - 1], p[j - 1] - 1)
            suf.union(j, j + 1)
            pre.union(j, j - 1)
        j = i
        for _ in range(k):
            j = pre.find_fa(j)
            if j == 0:
                break
            ans[j - 1] = cnt + 1
            s.pop(p[j - 1])
            mx.union(p[j - 1], p[j - 1] - 1)
            suf.union(j, j + 1)
            pre.union(j, j - 1)
        cnt ^= 1
    print(*ans, sep='')

#    514   ms
def solve2():
    n, k = RI()
    p = [1] + RILST()

    pos = {v: i for i, v in enumerate(p)}
    mx, pre, suf = n, list(range(n + 1)), list(range(n + 2))

    def find(fa, x):
        t = x
        while x != fa[x]:
            x = fa[x]
        while t != x:
            t, fa[t] = fa[t], x
        return x

    def union(fa, x, y):
        x, y = find(fa, x), find(fa, y)
        fa[x] = y
        return y

    cnt = 0
    ans = [0] * (n + 1)
    while mx:
        while mx and mx not in pos:
            mx -= 1
        if mx == 0: break
        ps = pos[mx]

        def delete(i):
            pos.pop(p[i])
            ans[i] = cnt + 1
            return union(pre, i, i - 1), union(suf, i, i + 1)

        delete(ps)
        i = find(suf, ps)
        for _ in range(k):
            if i == n + 1:
                break
            i = delete(i)[1]
        i = find(pre, ps)
        for _ in range(k):
            if i == 0:
                break
            i = delete(i)[0]
        cnt ^= 1
    print(*ans[1:], sep='')
if __name__ == '__main__':
    solve()
