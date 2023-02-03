# Problem: C - ARC Wrecker 2
# Contest: AtCoder - AtCoder Regular Contest 119
# URL: https://atcoder.jp/contests/arc119/tasks/arc119_c
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
PROBLEM = """https://atcoder.jp/contests/arc119/tasks/arc119_c

输入 n(2≤n≤3e5) 和长为 n 的数组 a(1≤a[i]≤1e9)。

每次操作，你可以选择两个相邻的数字，把它们都加一，或者都减一。
对于 a 的一个连续子数组 b，如果可以通过执行任意多次操作，使 b 的所有元素为 0，则称 b 为好子数组。
输出 a 的好子数组的数量。
输入
5
5 8 8 6 6
输出
3
"""
"""遇到这种一次会改变多个数的题目，往往入手点在「不变量」上，也就是操作不会改变什么。

交错和是不变的。

那么题目就变成有多少个区间的交错和等于 0。

这是个经典问题，做法与「和为 0 的子数组个数」是一样的，用前缀和 + 哈希表解决。"""


#    317    ms
def solve():
    n, = RI()
    a = RILST()
    cnt = Counter()
    cnt[0] = 1
    s = ans = 0
    for i, v in enumerate(a):
        s += v * ((i & 1) * 2 - 1)  # 奇数1 偶数-1
        ans += cnt[s]
        cnt[s] += 1
    print(ans)


if __name__ == '__main__':
    solve()
