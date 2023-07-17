# Problem: C. Basketball Exercise
# Contest: Codeforces - Codeforces Round 574 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1195/C
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
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1195/C

输入 n(1≤n≤1e5) 和一个 2 行 n 列的矩阵 a(1≤a[i][j]≤1e9)。
你需要从矩阵中选择一些数，要求任意两数不能左右相邻，也不能上下相邻。
输出所选数字之和的最大值。

思考：如果改成 m 列要怎么做？ https://ac.nowcoder.com/acm/contest/59157/O
输入
5
9 3 5 7 3
5 8 1 4 5
输出 29

输入
3
1 2 9
10 1 1
输出 19

输入
1
7
4
输出 7
"""

# 155ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    if n == 1:
        return print(max(a[0], b[0]))
    f = [[0, 0] for _ in range(n)]
    f[0] = [a[0], b[0]]
    f[1] = [b[0] + a[1], a[0] + b[1]]
    for i in range(2, n):
        f[i][0] = a[i] + max(f[i - 1][1], max(f[i - 2]))
        f[i][1] = b[i] + max(f[i - 1][0], max(f[i - 2]))
    print(max(f[-1]))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
