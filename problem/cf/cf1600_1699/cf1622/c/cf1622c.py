# Problem: C. Set or Decrease
# Contest: Codeforces - Educational Codeforces Round 120 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1622/problem/C
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
PROBLEM = """https://codeforces.com/contest/1622/problem/C

输入 t(≤1e4) 表示 t 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(≤2e5) k(1≤k≤1e15) 和长为 n 的数组 a(1≤a[i]≤1e9)。

每次操作，选择一个 a[i]，要么把 a[i] 变成 a[i]-1，要么变成另外一个 a[j]。
要使 sum(a) <= k，至少需要操作多少次？

注意可以把 a[i] 减成负数。
输入
4
1 10
20
2 69
6 9
7 8
1 2 1 3 1 2 1
10 1
1 2 3 1 2 6 1 6 8 10
输出 
10
0
2
7
"""
"""贪心
变的话肯定大的数变成最小的，那么尝试先给给最小的-1，再找几个大的变.
假设现在最大的cnt个数求和是s，最小的l变x次,总共要减小超过d：
    x + s - (l-x)*cnt >= d 
    s - d >= l*cnt-x*(cnt+1)
    x >= (l*cnt-s+d)/(cnt+1)
"""


#    186   ms
def solve():
    n, k = RI()
    a = RILST()
    s = sum(a)
    if s <= k:
        return print(0)
    d = s - k  # 需要总共降d
    if n == 1:
        return print(s - k)
    a.sort()
    l = a[0]
    ans = s - k
    cnt = s = 0
    for v in a[:0:-1]:
        s += v
        cnt += 1
        if s - l * cnt >= d:
            ans = min(ans, cnt)
            break
        x = (l * cnt - s + d + cnt + 1 - 1) // (cnt + 1)
        ans = min(ans, x + cnt)
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
