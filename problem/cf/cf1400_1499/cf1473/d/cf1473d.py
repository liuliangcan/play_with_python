# Problem: D. Program
# Contest: Codeforces - Educational Codeforces Round 102 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1473/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1473/D

输入 t(≤1e3) 表示 t 组数据。所有数据的 n 之和 ≤2e5，m 之和 ≤2e5。
每组数据输入 n(≤2e5) m(≤2e5) 和长为 n 的字符串 s，仅包含 '+' 和 '-'，分别表示 +1 和 -1，下标从 1 开始。
然后输入 m 个询问，每个询问输入 L 和 R，表示区间 [L,R] (1≤L≤R≤n)。
把从 s[L] 到 s[R] 的这段子串去掉后，s 的剩余部分记作 t。
对于数字 x=0，逐个执行 t 中的字符，输出你能得到多少个不同的数字。
例如 t="+--"，那么 x 分别为 0,1,0,-1，一共有 3 个不同的数字，输出 3。
又例如 t=""，那么只有 0，输出 1。
每个询问互相独立。
"""
"""输入
2
8 4
-+--+--+
1 8
2 8
2 5
1 1
4 10
+-++
1 1
1 2
2 2
1 3
2 3
3 3
1 4
2 4
3 4
4 4
输出
1
2
4
4
3
3
4
2
3
2
1
2
2
2
"""
"""前缀和+前后缀极值
- 由于+-变化都是1，因此数据范围是连续的，只需要知道最大最小值即可。
- 计算出整个字符串的前缀和，那么l之前的最大/最小值可以用2个前缀极值数组维护。
- 后缀的最大最小值可以用后缀极值数组维护，但变化是从左往右的，没关系，让两个极值减去中间删去的那段即可。相当于从l-1开始变化的。
"""

#   311    ms
def solve():
    n, m = RI()
    s, = RS()
    a = [0]  # 前缀和
    for c in s:
        if c == '+':
            a.append(a[-1] + 1)
        else:
            a.append(a[-1] - 1)
    rmx, rmn = [a[-1]] * (n + 1), [a[-1]] * (n + 1)  # 后缀最大/最小值
    for i in range(n - 1, -1, -1):
        rmx[i] = max(a[i], rmx[i + 1])
        rmn[i] = min(a[i], rmn[i + 1])
    lmx, lmn = [a[0]] * (n + 1), [a[0]] * (n + 1)  # 前缀最大/最小值
    for i in range(1, n + 1):
        lmx[i] = max(a[i], lmx[i - 1])
        lmn[i] = min(a[i], lmn[i - 1])
    for _ in range(m):
        l, r = RI()
        s = a[r] - a[l - 1]
        lx = lmn[l - 1]
        ly = lmx[l - 1]
        rx = ry = 0
        if r < n:
            rx = rmn[r + 1] - s
            ry = rmx[r + 1] - s
        print(max(ly, ry) - min(rx, lx) + 1)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
