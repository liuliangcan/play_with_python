# Problem: C. Helping the Nature
# Contest: Codeforces - Codeforces Round 802 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1700/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf
if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1700/C

输入 T(≤2e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(1≤n≤2e5) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)。

每次操作，你可以执行如下三种中的一种：
1. 把一个前缀的 a[i]-=1
2. 把一个后缀的 a[i]-=1
3. 把所有 a[i]+=1

把所有 a[i] 都变成 0，至少要操作多少次？
输入
4
3
-2 -2 -2
3
10 4 7
4
4 -4 4 -4
5
1 -2 3 -4 5
输出
2
13
36
33
"""
"""https://codeforces.com/problemset/submission/1700/209616776

用差分思考，计算 a 的差分数组 d。

操作 1 变成给 d[0]-=1，d[i]+=1。
操作 2 变成给 d[i]-=1。
操作 3 变成给 d[0]+=1。

根据这些操作，把所有 d[i] 变成 0。

相似题目：见 2023.2.8 的茶"""


#    124   ms
def solve():
    n, = RI()
    a = RILST()
    d0 = a[0]
    neg = pos = 0
    for i in range(1,n):
        d = a[i] - a[i-1]
        if d < 0:
            neg += d
        else:
            pos += d
    ans = -neg
    d0 += neg
    if d0 > 0:
        ans += d0 + pos
    else:
        ans += pos - d0
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
