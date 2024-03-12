# Problem: C. Two TVs
# Contest: Codeforces - Educational Codeforces Round 27
# URL: https://codeforces.com/problemset/problem/845/C
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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/845/C

输入 n(1≤n≤2e5) 和 n 个闭区间，每个闭区间 [L,R] 都满足 0≤L<R≤1e9。
能否将这 n 个闭区间分成两组，每组内的区间交集为空？允许一组是空的。
输出 YES 或 NO。
输入
3
1 2
2 3
4 5
输出 YES

输入
4
1 2
2 3
2 3
1 2
输出 NO
"""


#       ms
def solve():
    n, = RI()
    lr = []
    for _ in range(n):
        l, r = RI()
        lr.append((l, r))
    lr.sort()
    a = []
    y = -1
    for l, r in lr:
        if l <= y:
            a.append((l, r))
        else:
            y = r
    y = -1
    for l, r in a:
        if l <= y:
            return print('NO')
        else:
            y = r
    print('YES')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
