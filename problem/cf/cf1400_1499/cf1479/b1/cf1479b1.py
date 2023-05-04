# Problem: B1. Painting the Array I
# Contest: Codeforces - Codeforces Round 700 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1479/B1
# Memory Limit: 512 MB
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
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1479/B1

输入 n(1≤n≤1e5) 和长为 n 的数组 a(1≤a[i]≤n)。

从 a 中选择一个子序列 A，剩余元素作为另一个子序列 B。
定义 f(C) 表示对序列 C 不断去掉相邻相同元素，直到没有相邻相同元素为止，返回剩余元素的个数。
例如 f([1,1,2,1,1]) = f([1,2,1]) = 3。
输出 f(A) + f(B) 的最大值。

变形（这场的 B2）：输出 f(A) + f(B) 的最小值。
输入
7
1 1 2 2 3 3 3
输出 6

输入
7
1 2 3 4 5 6 7
输出 7
"""

"""https://codeforces.com/problemset/submission/1479/204384720

想象成往两个数组 s 和 t 的末尾不断添加元素。

为方便计算，初始时 s 和 t 中都添加一个 0。

如果 a[i] 与 s、t 的末尾元素都相同，那么加到哪个数组末尾都是一样的。
如果 a[i] 与 t 的末尾元素相同，那么加到 s 末尾。
如果 a[i] 与 s 的末尾元素相同，那么加到 t 末尾。
如果 a[i] 与 s、t 的末尾元素都不相同，例如 s 末尾为 1，t 末尾为 2，a[i]=3，此时应考察下一个 1 以及下一个 2 的位置，
哪个位置更近，就加到哪个数组末尾（如果没有下一个元素就视作 n+1）。例如下一个 1 的位置更近，那么应当把 a[i] 加到 s 末尾，
相当于把这两个 1 隔开；至于 t，后面还有机会把 t 末尾的 2 和下一个 2 隔开。更严谨的证明见右边链接。
https://codeforces.com/blog/entry/87598"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


#   171  二分  ms
def solve1():
    n, = RI()
    a = RILST()
    pos = [[] for _ in range(n + 1)]
    for i, v in enumerate(a):
        pos[v].append(i)
    ans = s = t = 0

    for i, v in enumerate(a):
        if v == s:
            if t != v:
                ans += 1
            t = v
        elif v == t:
            if s != v:
                ans += 1
            s = v
        else:
            ans += 1
            p1 = bisect_left(pos[s], i)
            pos1 = n if p1 == len(pos[s]) else pos[s][p1]
            p2 = bisect_left(pos[t], i)
            pos2 = n if p2 == len(pos[t]) else pos[t][p2]
            if pos1 <= pos2:
                s = v
            else:
                t = v

    print(ans)


#   311 deque   ms
def solve2():
    n, = RI()
    a = RILST()
    pos = [deque() for _ in range(n + 1)]
    for i, v in enumerate(a):
        pos[v].append(i)
    for v in pos:
        v.append(n)
    ans = s = t = 0

    for i, v in enumerate(a):
        if v == s:
            if t != v:
                ans += 1
            t = v
        elif v == t:
            if s != v:
                ans += 1
            s = v
        else:
            ans += 1
            pos1 = pos[s][0]
            pos2 = pos[t][0]
            if pos1 <= pos2:
                s = v
            else:
                t = v
        pos[v].popleft()

    print(ans)


#  623 del [0]   ms
def solve3():
    n, = RI()
    a = RILST()
    pos = [[] for _ in range(n + 1)]
    for i, v in enumerate(a):
        pos[v].append(i)
    for v in pos:
        v.append(n)

    ans = s = t = 0

    for i, v in enumerate(a):
        if v == s:
            if t != v:
                ans += 1
            t = v
        elif v == t:
            if s != v:
                ans += 1
            s = v
        else:
            ans += 1
            pos1 = pos[s][0]
            pos2 = pos[t][0]
            if pos1 <= pos2:
                s = v
            else:
                t = v
        del pos[v][0]

    print(ans)


#  155 reverse ms
def solve4():
    n, = RI()
    a = RILST()
    pos = [[n] for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        pos[a[i]].append(i)

    ans = s = t = 0

    for i, v in enumerate(a):
        if v == s:
            if t != v:
                ans += 1
            t = v
        elif v == t:
            if s != v:
                ans += 1
            s = v
        else:
            ans += 1
            pos1 = pos[s][-1]
            pos2 = pos[t][-1]
            if pos1 <= pos2:
                s = v
            else:
                t = v
        pos[v].pop()

    print(ans)

#  109 只考虑a[i+1]  ms
def solve():
    n, = RI()
    a = RILST()

    ans = s = t = 0

    for i, v in enumerate(a):
        if v == s:
            if t != v:
                ans += 1
            t = v
        elif v == t:
            if s != v:
                ans += 1
            s = v
        else:
            ans += 1
            if i < n - 1 and a[i+1] == s:
                s = v
            else:
                t = v

    print(ans)


if __name__ == '__main__':
    solve()
