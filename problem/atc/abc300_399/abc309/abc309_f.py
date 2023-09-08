# Problem: F - Box in Box
# Contest: AtCoder - Denso Create Programming Contest 2023 (AtCoder Beginner Contest 309)
# URL: https://atcoder.jp/contests/abc309/tasks/abc309_f
# Memory Limit: 1024 MB
# Time Limit: 2500 ms

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
# MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc309/tasks/abc309_f

输入 n(2≤n≤2e5) 和 n 个盒子的长宽高，每行输入三个数，范围 [1,1e9]。
你可以随意旋转盒子，也可以保持不变。
问：是否存在一个盒子可以被另一个盒子装下，也就是一个盒子的长宽高都分别严格小于另一个盒子的长宽高。
输出 "Yes" 或 "No"。

相似题目：
1691. 堆叠长方体的最大高度
输入
3
19 8 22
10 24 12
15 25 11
输出 Yes

输入
3
19 8 22
10 25 12
15 24 11
输出 No

输入
2
1 1 2
1 2 2
输出 No
"""
"""请先阅读：
【图解】算法优化+详细证明 

接着上面的题解说。对于每个盒子，把长宽高从小到大排序（排序后分别记作 a[i][0], a[i][1], a[i][2]），然后按照 a[i][0] 从小到大排序所有盒子。

接下来只需要考虑是否有 a[i][1] < a[j][1] 且 a[i][2] < a[j][2]，这可以用树状数组解决（数据范围太大可以用离散化或者哈希表实现）。
把 (a[i][1], a[i][2]) 看成是二维平面的坐标点，我们可以维护 x=a[i][1] 这条线左侧的所有坐标点的纵坐标的最小值，即前缀最小值 preMin(a[i][1]-1)。
只要满足 preMin(a[i][1]-1) < a[i][2] 就可以输出 Yes。
具体细节见代码，注意为了满足严格小于，对于相同的 a[i][0] 需要先查询完再一并更新。

https://atcoder.jp/contests/abc309/submissions/45242148
"""


#   816    ms
def solve():
    n, = RI()
    box = []
    hs = []
    for _ in range(n):
        p = sorted(RI())
        hs.append(p[1])
        box.append(p)
    box.sort()
    hs = [0] + sorted(set(hs))
    size = len(hs)
    cc = [inf] * (size + 1)  # BIT前缀min

    def upd(i, v):
        while i <= size:
            if cc[i] <= v:
                break
            cc[i] = v
            i += i & -i

    def pre_min(i):
        s = inf
        while i:
            s = min(s, cc[i])
            i -= i & -i
        return s

    for i in range(n):
        box[i][1] = bisect_left(hs, box[i][1])
    i = 0
    while i < n:
        st = i
        while i < n and box[i][0] == box[st][0]:
            if pre_min(box[i][1] - 1) < box[i][2]:
                return print('Yes')
            i += 1
        while st < i:
            upd(box[st][1], box[st][2])
            st += 1
    print('No')


#   734    ms
def solve3():
    n, = RI()
    box = []
    hs = []
    for _ in range(n):
        p = sorted(RI())
        hs.append(p[1])
        box.append(p)
    box.sort()
    hs = [0] + sorted(set(hs))
    size = len(hs)
    cc = [inf] * (size + 1)  # BIT前缀min

    def upd(i, v):
        while i <= size:
            if cc[i] <= v:
                break
            cc[i] = v
            i += i & -i

    def pre_min(i):
        s = inf
        while i:
            s = min(s, cc[i])
            i -= i & -i
        return s

    q = []  # delay
    for x, y, z in box:
        if q and x > q[0][0]:
            for _, b, c in q:
                mn = pre_min(b - 1)
                if mn < c:
                    return print('Yes')
            for _, b, c in q:
                upd(b, c)
            q = [(x, bisect_left(hs, y), z)]
        else:
            q.append((x, bisect_left(hs, y), z))

    for _, b, c in q:
        mn = pre_min(b - 1)
        if mn < c:
            return print('Yes')
    print('No')


#   768    ms
def solve2():
    n, = RI()
    box = []
    hs = []
    for _ in range(n):
        p = sorted(RI())
        hs.append(p[1])
        box.append(p)
    box.sort()
    hs = sorted(set(hs))
    size = len(hs)
    cc = [inf] * (size + 1)  # BIT前缀min

    def add(i, v):
        while i <= size:
            cc[i] = min(cc[i], v)
            i += i & -i

    def get(i):
        s = inf
        while i:
            s = min(s, cc[i])
            i -= i & -i
        return s

    q = []  # delay
    for x, y, z in box:
        if q and x > q[0][0]:
            for _, b, c in q:
                mn = get(b - 1)
                if mn < c:
                    return print('Yes')
            for _, b, c in q:
                add(b, c)
            q = [(x, bisect_left(hs, y) + 1, z)]
        else:
            q.append((x, bisect_left(hs, y) + 1, z))

    for _, b, c in q:
        mn = get(b - 1)
        if mn < c:
            return print('Yes')
    print('No')


#   875    ms
def solve1():
    n, = RI()
    box = []
    hs = []
    for _ in range(n):
        p = sorted(RI())
        hs.append(p[1])
        box.append(p)
    box.sort()
    hs = sorted(set(hs))
    size = len(hs)
    cc = [inf] * (size + 1)  # BIT前缀min

    def add(i, v):
        while i <= size:
            cc[i] = min(cc[i], v)
            i += i & -i

    def get(i):
        s = inf
        while i:
            s = min(s, cc[i])
            i -= i & -i
        return s

    q = []  # delay
    for x, y, z in box:
        if q and x > q[0][0]:
            for _, b, c in q:
                b = bisect_left(hs, b) + 1
                mn = get(b - 1)
                if mn < c:
                    return print('Yes')
            for _, b, c in q:
                b = bisect_left(hs, b) + 1
                add(b, c)
            q = [(x, y, z)]
        else:
            q.append((x, y, z))

    for _, b, c in q:
        b = bisect_left(hs, b) + 1
        mn = get(b - 1)
        if mn < c:
            return print('Yes')
    print('No')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
