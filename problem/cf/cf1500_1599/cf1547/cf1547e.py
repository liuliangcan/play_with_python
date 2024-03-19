# Problem: E. Air Conditioners
# Contest: Codeforces - Codeforces Round 731 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1547/E
# Memory Limit: 512 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/1547/E

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤3e5。
每组数据输入 n k (1≤k≤n≤3e5)，长为 k 的数组 a(1≤a[i]≤n)，长为 k 的数组 t(1≤t[i]≤1e9)。

数轴上有 k 个正在制冷的空调，第 i 个空调的位置是 a[i]，温度为 t[i]。
位置 j 的温度会受到空调 i 的影响，离空调越远，温度越高，具体温度为 t[i] + |a[i] - j|。
如果位置 j 被多个空调影响，取温度最小值。

输出 1~n 每个位置的温度。
输入
5

6 2
2 5
14 16

10 1
7
30

5 5
3 1 4 2 5
3 1 4 2 5

7 1
1
1000000000

6 3
6 1 3
5 5 5
输出
15 14 15 16 16 17
36 35 34 33 32 31 30 31 32 33
1 2 3 4 5
1000000000 1000000001 1000000002 1000000003 1000000004 1000000005 1000000006
5 6 5 6 6 5
"""


#       ms
def solve():
    RS()
    n, k = RI()
    a = RILST()
    t = RILST()
    ans = [inf] * n
    for i, v in zip(a, t):
        ans[i - 1] = v
    for i in range(1, n):
        ans[i] = min(ans[i], ans[i - 1] + 1)
    for i in range(n - 2, -1, -1):
        ans[i] = min(ans[i], ans[i + 1] + 1)
    print(*ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
