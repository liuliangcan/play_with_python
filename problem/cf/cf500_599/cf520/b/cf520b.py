# Problem: B. Two Buttons
# Contest: Codeforces - Codeforces Round 295 (Div. 2)
# URL: https://codeforces.com/problemset/problem/520/B
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
PROBLEM = """https://codeforces.com/problemset/problem/520/B

输入两个不同的整数 n m，范围都在 [1,1e4]。

每次操作，可以 n*=2，或者 n-=1。
至少操作多少次可以得到 m？
输入 4 6
输出 2

输入 10 1
输出 9
"""


#       ms
def solve():
    n, m = RI()
    if n >= m:
        return print(n - m)

    q = [n]
    vis = {n}
    step = 0
    while q:
        nq = []
        for u in q:
            if u == m:
                return print(step)
            v = u * 2
            if v not in vis and v <= 20000:
                vis.add(v)
                nq.append(v)
            v = u - 1
            if v not in vis and v > 0:
                vis.add(v)
                nq.append(v)
        q = nq
        step += 1


if __name__ == '__main__':
    solve()
