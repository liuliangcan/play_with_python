# Problem: F. 3SUM
# Contest: Codeforces - Codeforces Round 799 (Div. 4)
# URL: https://codeforces.com/problemset/problem/1692/F
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1692/F

输入 T(≤1e3) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(3≤n≤2e5) 和长为 n 的数组 a(1≤a[i]≤1e9)。

判断是否存在 3 个下标不同的数 a[i], a[j], a[k]，
使得 a[i] + a[j] + a[k] 的个位数是 3。
输出 YES 或 NO。
输入
6
4
20 22 19 84
4
1 11 1 2022
4
1100 1100 1100 1111
5
12 34 56 78 90
4
1 9 8 4
6
16 38 94 25 18 99
输出
YES
YES
NO
NO
YES
YES
"""

good = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            if (i + j + k) % 10 == 3:
                c = [0] * 10
                c[i] += 1
                c[j] += 1
                c[k] += 1
                good.append([(v, c[v]) for v in {i, j, k}])


#  155     ms
def solve():
    n, = RI()
    a = RILST()
    cnt = [0] * 10
    for v in a:
        cnt[v % 10] += 1
    for p in good:
        for x, c in p:
            if c > cnt[x]:
                break
        else:
            return print('YES')
    # for i in range(10):  # 171ms
    #     for j in range(10):
    #         for k in range(10):
    #             if (i + j + k) % 10 == 3:
    #                 c = [0] * 10
    #                 c[i] += 1
    #                 c[j] += 1
    #                 c[k] += 1
    #                 if c[i] <= cnt[i] and c[j] <= cnt[j] and c[k] <= cnt[k]:
    #                     return print('YES')
    print('NO')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
