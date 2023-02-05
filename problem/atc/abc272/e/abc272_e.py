# Problem: E - Add and Mex
# Contest: AtCoder - AtCoder Beginner Contest 272
# URL: https://atcoder.jp/contests/abc272/tasks/abc272_e
# Memory Limit: 1024 MB
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
PROBLEM = """https://atcoder.jp/contests/abc272/tasks/abc272_e

输入 n(≤2e5) m(≤2e5) 和长为 n 的整数数组 a (-1e9≤a[i]≤1e9)，下标从 1 开始。
执行如下操作 m 次：
对 1~n 的每个 i，把 a[i] += i。
每次操作后，输出 mex(a)，即不在 a 中的最小非负整数。

输入
3 3
-1 -1 -6
输出
2
2
0

输入
5 6
-2 -2 -5 -7 -15
输出
1
3
2
0
0

https://atcoder.jp/contests/abc272/submissions/37376965

提示 1：由于 a 中只有 n 个数，因此在 [0,n-1] 范围之外的 a[i] 是没有意义的。

提示 2：对于每个 i，有多少次操作，使得操作后 a[i] 仍然在 [0,n-1] 范围内？

提示 3：根据调和级数，总共有 O(nlogn) 次这样的操作。

提示 4：对每个 a[i]，把满足提示 2 的操作次数以及操作后的结果存下来，按照操作次数分组归类。

提示 5：每个操作次数所对应的结果记录到一个哈希表中，暴力枚举计算 mex（提示 3）。
代码实现时可以用时间戳来优化。
2022年12月19日
"""
"""这题我测了很多次 比较分类时  直接用set 或是 用list储存,计算答案时再去重
发现用set得不偿失，因为数组里一大半数据都操作不了几次就溢出了，比如后一半数 每次加一个>=n//2的数，只能操作一次。
这样大部分set只存几个数，考虑到set每次都add的常数太大，得不偿失；
但计算时用set竟然是可行的，只比时间戳方案慢了一丢丢
"""


#     374 ms
def solve():
    n, m = RI()
    a = RILST()
    c = [[] for _ in range(m + 1)]

    for i, v in enumerate(a, start=1):
        start = 1  # 由于至少操作1次，从1开始
        if v < 0:  # 如果从负的开始，直接跳到正的，因为<0的没用，上取整算步数
            start = (-v + i - 1) // i
        for j in range(start, m + 1):
            p = v + i * j
            if p < n:
                c[j].append(p)
            else:
                break

    ans = []
    for i in range(1, m + 1):
        t = set(c[i])

        for mex in range(n + 1):
            if mex not in t:
                ans.append(mex)
                break

    print(*ans, sep='\n')

#    cf547  ms
def solve5():
    n, m = RI()
    a = RILST()
    c = [set() for _ in range(m + 1)]

    for i, v in enumerate(a, start=1):
        start = 1  # 由于至少操作1次，从1开始
        if v < 0:  # 如果从负的开始，直接跳到正的，因为<0的没用，上取整算步数
            start = (-v + i - 1) // i
        for j in range(start, m + 1):
            p = v + i * j
            if p < n:
                c[j].add(p)
            else:
                break

    ans = []
    for i in range(1, m + 1):
        s = c[i]
        for mex in range(n + 1):
            if mex not in s:
                ans.append(mex)
                break

    print(*ans, sep='\n')


#   348      ms
def solve4():
    n, m = RI()
    a = RILST()
    c = [[] for _ in range(m + 1)]

    for i, v in enumerate(a, start=1):
        start = 1  # 由于至少操作1次，从1开始
        if v < 0:  # 如果从负的开始，直接跳到正的，因为<0的没用，上取整算步数
            start = (-v + i - 1) // i
        for j in range(start, m + 1):
            p = v + i * j
            if p < n:
                c[j].append(p)
            else:
                break

    ans = []
    t = [0] * (n + 1)
    for i in range(1, m + 1):
        for v in c[i]:
            t[v] = i

        for mex in range(n + 1):
            if t[mex] != i:
                ans.append(mex)
                break

    print(*ans, sep='\n')


#   578     ms
def solve3():
    n, m = RI()
    a = RILST()
    c = defaultdict(set)

    for i, v in enumerate(a, start=1):
        start = 1  # 由于至少操作1次，从1开始
        if v < 0:  # 如果从负的开始，直接跳到正的，因为<0的没用，上取整算步数
            start = (-v + i - 1) // i
        for j in range(start, m + 1):
            p = v + i * j
            if p < n:
                c[j].add(p)
            else:
                break

    ans = []
    for i in range(1, m + 1):
        s = c[i]
        for mex in range(n + 1):
            if mex not in s:
                ans.append(mex)
                break

    print(*ans, sep='\n')


#    566   ms
def solve2():
    n, m = RI()
    a = RILST()
    c = defaultdict(set)

    for i, v in enumerate(a, start=1):
        start = 1  # 由于至少操作1次，从1开始
        if v < 0:  # 如果从负的开始，直接跳到正的，因为<0的没用，上取整算步数
            start = (-v + i - 1) // i
        for j in range(start, m + 1):
            p = v + i * j
            if p < n:
                c[j].add(p)
            else:
                break

    ans = []
    for i in range(1, m + 1):
        def f(s):
            for i in range(n + 1):
                if i not in s:
                    return i

        ans.append(f(c[i]))
    print(*ans, sep='\n')


#   638    ms
def solve1():
    n, m = RI()
    a = RILST()
    c = defaultdict(set)

    for i, v in enumerate(a, start=1):
        start = 1  # 由于至少操作1次，从1开始
        if v < 0:  # 如果从负的开始，直接跳到正的，因为<0的没用，上取整算步数
            start = (-v + i - 1) // i
        for j in range(start, m + 1):
            p = v + i * j
            if p < n:
                c[j].add(p)
            else:
                break

    ans = []
    for i in range(1, m + 1):
        mex = 0
        s = c[i]
        while mex in s:
            mex += 1
        ans.append(mex)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
