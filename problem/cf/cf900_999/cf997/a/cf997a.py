# Problem: A. Convert to Ones
# Contest: Codeforces - Codeforces Round 493 (Div. 1)
# URL: https://codeforces.com/problemset/problem/997/A
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/997/A

输入 n(1≤n≤3e5) x(0≤x≤1e9) y(0≤y≤1e9) 和长为 n 的 01 字符串 s。

你可以执行任意次操作，每次选择其中一种操作执行。
1. 花费 x，reverse s 的一个子串，例如 1110 -> 0111。
2. 花费 y，flip s 的一个子串，例如 1110 -> 0001。

目标：使 s 中只有 1。
输出最少花费。
输入
5 1 10
01000
输出
11

输入
5 10 1
01000
输出
2

输入
7 2 3
1111111
输出
0
"""
"""https://codeforces.com/contest/997/submission/205172377

如果没有 0，输出 0。
如果 x < y，那么可以把所有 0 通过多次 reverse 操作聚在一起，然后再操作一次 flip。
reverse 的操作次数就是 0 组的个数减一。例如 001101000 中有三个 0 组，需要两次 reverse。
如果 x >= y，那么把每个 0 组 flip 掉即可。"""


#       ms
def solve():
    n, x, y = RI()
    s, = RS()
    if '0' not in s:
        return print(0)
    f = [0] * n
    if s[0] == '0':
        f[0] = 1
    for i in range(1, n):
        if s[i] == '0':
            f[i] = f[i - 1] + 1
    zero = f.count(1)

    if x < y:
        ans = (zero - 1) * x + y
    else:
        ans = zero * y
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
