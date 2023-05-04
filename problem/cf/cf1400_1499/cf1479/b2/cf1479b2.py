# Problem: B2. Painting the Array II
# Contest: Codeforces - Codeforces Round 700 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1479/B2
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

MOD = 10**9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1479/B2

输入 n(1≤n≤1e5) 和长为 n 的数组 a(1≤a[i]≤n)。

从 a 中选择一个子序列 A，剩余元素作为另一个子序列 B。
定义 f(C) 表示对序列 C 不断去掉相邻相同元素，直到没有相邻相同元素为止，返回剩余元素的个数。
例如 f([1,1,2,1,1]) = f([1,2,1]) = 3。
输出 f(A) + f(B) 的最小值。

变形（这场的 B1：输出 f(A) + f(B) 的最大值。
"""

#       ms
def solve():
    n, = RI()
    a = RILST()
    pos = [[n] for _ in range(n+1)]
    for i in range(n-1,-1,-1):
        pos[a[i]].append(i)
    ans = s = t = 0
    for v in a:
        if t != v != s:
            ans += 1
            if pos[s][-1] > pos[t][-1]:
                s = v
            else:
                t = v
        pos[v].pop()
    print(ans)




if __name__ == '__main__':
    solve()
