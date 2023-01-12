# Problem: G. Old Floppy Drive
# Contest: Codeforces - Codeforces Round #702 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1490/G
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
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1490/G

输入 t(≤1e4) 表示 t 组数据，每组数据输入 n(≤2e5) m(≤2e5) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)，表示一个由数组 a 无限重复的序列 b。
然后输入 m 个询问，每个询问输入 x(1≤x≤1e9)。
对每个询问，输出 b 的前缀和中首次 ≥x 的下标（下标从 0 开始），如果不存在，输出 -1。
所有数据的 n 之和、m 之和均不超过 2e5。
输入
3
3 3
1 -3 4
1 5 2
2 2
-2 0
1 2
2 2
0 1
1 2
输出
0 6 2 
-1 -1 
1 3 
"""

"""
记录a的前缀和，注意，我们只需要>0(询问x>0) 且 >前一个数的值（类似单调队列）
    这是因为更小的值前边已经达到过了，没有意义。
记录s为sum(s)，若s<=0，则不能通过叠加多几轮a来达到x，只能通过一轮内二分找找看（即需要<=max）
若s>0，则尝试叠加几轮，显然叠加的轮数尽量少，即最后一步尽量迈的大，那么最后一轮我们选max，计算前边需要叠几轮，向上取整cnt。
再通过cnt判断前边叠加实际贡献了多少，再确定最后一轮至少要迈多大步，再二分找找。
"""


#   265    ms
def solve():
    t, = RI()
    for _ in range(t):
        n, m = RI()
        a = RILST()
        s = 0
        z, y = [0], [0]
        for i, v in enumerate(a):
            s += v
            if s > z[-1]:  # 类似单调队列，向右时只需要更大的数，小的数在前边已达到
                z.append(s)
                y.append(i)
        mx = z[-1]

        ans = []
        q = RILST()
        if s <= 0:
            for x in q:
                ans.append(-1 if x > mx else y[bisect_left(z, x)])
        else:
            for x in q:
                if x <= mx:
                    ans.append(y[bisect_left(z, x)])
                else:
                    cnt = (x - mx + s - 1) // s
                    p = bisect_left(z, x - cnt * s)
                    ans.append(cnt * n + y[p])
        print(*ans)


#   265     ms
def solve4():
    t, = RI()
    for _ in range(t):
        n, m = RI()
        a = RILST()
        s = 0
        z, y = [0], [0]
        for i, v in enumerate(a):
            s += v
            if s > z[-1]:  # 类似单调队列，向右时只需要更大的数，小的数在前边已达到
                z.append(s)
                y.append(i)
        mx = z[-1]

        ans = []
        q = RILST()
        for x in q:
            if x <= mx:
                ans.append(y[bisect_left(z, x)])
            elif s <= 0:
                ans.append(-1)
            else:
                cnt = (x - mx + s - 1) // s
                p = bisect_left(z, x - cnt * s)
                ans.append(cnt * n + y[p])

        print(*ans)


#   311     ms
def solve3():
    t, = RI()
    for _ in range(t):
        n, m = RI()
        a = RILST()
        pre = list(accumulate(a))
        s = pre[-1]  # 一轮能加多少
        sp = [(0, -1)]
        for i, v in enumerate(pre):
            if v > sp[-1][0]:  # 类似单调队列，向右时只需要更大的数，小的数在前边已达到
                sp.append((v, i))  # 达到每个值的最小下标
        mx = sp[-1][0]

        ans = []
        q = RILST()
        for x in q:
            if x <= mx:
                ans.append(sp[bisect_left(sp, (x, 0))][1])
            elif s <= 0:
                ans.append(-1)
            else:
                cnt = (x - mx + s - 1) // s
                p = bisect_left(sp, (x - cnt * s, 0))
                ans.append(cnt * n + sp[p][1])

        print(*ans)


#    639    ms list[tuple]
def solve2():
    t, = RI()
    for _ in range(t):
        n, m = RI()
        a = RILST()
        pre = list(accumulate(a))
        s = pre[-1]  # 一轮能加多少
        ps = {}
        for i, v in enumerate(pre):
            if v not in ps:
                ps[v] = i  # 达到每个值的最小下标
        sp = sorted([(k, v) for k, v in ps.items()])  # 排序后把每个值对应下标更新为后缀最大值：因为达到更大的数等同于超过了这个数
        mx = sp[-1][0]
        for i in range(len(sp) - 2, -1, -1):
            if sp[i][1] > sp[i + 1][1]:
                sp[i] = (sp[i][0], sp[i + 1][1])

        ans = []
        q = RILST()
        if s <= 0:  # 如果每轮不能增长，那只能看这个询问是否在前缀和里
            for x in q:
                ans.append(-1 if x > mx else sp[bisect_left(sp, (x, 0))][1])
        else:  # 如果可以通过叠加完整一轮增长，则尝试
            for x in q:
                if x <= mx:  # 如果小于最大值，则在第一轮里找第一个大于x的数对应的下标
                    ans.append(sp[bisect_left(sp, (x, 0))][1])
                else:  # 贪心：尝试用最大数作为最后一轮，这样前边轮数才少
                    l = x - mx  # 前边轮数需要累计的数
                    cnt = (l + s - 1) // s  # ceil求至少需要多少轮
                    l = cnt * s  # 这么多轮实际能累计的前边的数
                    r = x - l  # 那么最后一轮只需要这么多
                    p = bisect_left(sp, (r, 0))
                    ans.append(cnt * n + sp[p][1])  # 轮数*n+最后一轮的下标
        print(*ans)


#    858   ms list[list]
def solve1():
    t, = RI()
    for _ in range(t):
        n, m = RI()
        a = RILST()
        pre = list(accumulate(a))
        s = pre[-1]  # 一轮能加多少
        ps = {}
        for i, v in enumerate(pre):
            if v not in ps:
                ps[v] = i  # 达到每个值的最小下标
        sp = sorted([[k, v] for k, v in ps.items()])  # 排序后把每个值对应下标更新为后缀最大值：因为达到更大的数等同于超过了这个数
        mx = sp[-1][0]
        for i in range(len(sp) - 2, -1, -1):
            sp[i][1] = min(sp[i][1], sp[i + 1][1])
        ans = []
        q = RILST()
        if s <= 0:  # 如果每轮不能增长，那只能看这个询问是否在前缀和里
            for x in q:
                ans.append(-1 if x > mx else sp[bisect_left(sp, [x, 0])][1])
        else:  # 如果可以通过叠加完整一轮增长，则尝试
            for x in q:
                if x <= mx:  # 如果小于最大值，则在第一轮里找第一个大于x的数对应的下标
                    ans.append(sp[bisect_left(sp, [x, 0])][1])
                else:  # 贪心：尝试用最大数作为最后一轮，这样前边轮数才少
                    l = x - mx  # 前边轮数需要累计的数
                    cnt = (l + s - 1) // s  # ceil求至少需要多少轮
                    l = cnt * s  # 这么多轮实际能累计的前边的数
                    r = x - l  # 那么最后一轮只需要这么多
                    p = bisect_left(sp, [r, 0])
                    ans.append(cnt * n + sp[p][1])  # 轮数*n+最后一轮的下标
        print(*ans)


if __name__ == '__main__':
    solve()
