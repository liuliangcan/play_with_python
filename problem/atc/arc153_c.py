# Problem: C - ± Increasing Sequence
# Contest: AtCoder - AtCoder Regular Contest 153
# URL: https://atcoder.jp/contests/arc153/tasks/arc153_c
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
PROBLEM = """https://atcoder.jp/contests/arc153/tasks/arc153_c

输入 n(1≤n≤2e5) 和长为 n 的数组 a，只包含 -1 和 1。

你需要构造一个严格递增数组 b，元素范围在 [-1e12,1e12]，且 sum(a[i]*b[i]) = 0
如果无法构造，输出 No；否则输出 Yes 和数组 b。
输入
5
-1 1 -1 -1 1
输出
Yes
-3 -1 4 5 7

输入
1
-1
输出
Yes
0

输入
2
1 -1
输出
No
"""
"""https://atcoder.jp/contests/arc153/submissions/38517162

提示 1：b 的首尾元素受到的约束最小，是最灵活的。

提示 2：如果 a 的首尾元素相同，那么无论中间算出的是多少，都可以通过调整 b 的首尾元素让 sum=0。

提示 3：如果 a 的首尾元素不同，基于提示 2，找 a 的一个前缀和，它与 a 的末尾元素的正负号相同；找 a 的一个后缀和，它与 a[0] 的正负号相同。这样的前缀和/后缀和就能作为一个「整体」，达到和提示 2 一样的效果。
如果不存在，则无法构造。"""

#   194   ms
def solve():
    n, = RI()
    a = RILST()
    if n == 1:
        print('Yes')
        return print(0)
    # 把a分为三段：左段，中段，右端点。其中sum(左段) = a[-1]
    # 左右两段必是分别正负，目标让左右抵消；为了忽略中段影响，让中段足够小，左右在数量级上足够大即可:1e11。
    # 可以证明只要找到左段(仅多一个正/负)，那么左段和的数量级不会超过正负2e11,加上中间段1e10也没问题。
    # 中间段从0开始累加，和不会超过1e10(更紧致的界是(1e5+1)*1e5//2)，因此左段用-1e11数量级，右端点可以覆盖它+中间段
    p = s = 0
    x = -10 ** 11  # 左段起点
    b = []
    for i in range(n - 1):  # 找一个==a[-1]的前缀
        s += a[i]
        p += x * a[i]  # 累计
        b.append(x)
        x += 1
        if s == a[-1] and x < 0:  # 找到左段，开始计算中段
            x = 0
    if b[-1] < -p * a[-1] <= 10 ** 12:
        b.append(-p * a[-1])
        print('Yes')
        return print(*b)

    # 分三段:a[0],中，右。其中a[0] = sum(右)
    p = s = 0
    x = 10 ** 11
    b = []
    for i in range(n - 1, 0, -1):  # 找一个==a[0]的后缀
        s += a[i]
        p += x * a[i]  # 累计
        b.append(x)
        x -= 1
        if s == a[0] and x > 0:
            x = 0
    if -10 ** 12 <= -p * a[0] < b[-1]:
        b.append(-p * a[0])
        print('Yes')
        return print(*b[::-1])
    print('No')


if __name__ == '__main__':
    solve()
