# Problem: D. Absolute Sorting
# Contest: Codeforces - Codeforces Round 839 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1772/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1772/D

输入 T(≤2e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(2≤n≤2e5) 和长为 n 的数组 a(1≤a[i]≤1e8)。
选择一个整数 x(0≤x≤1e9)，生成一个序列 b，满足 b[i]=abs(a[i]-x) 且 b[i]≤b[i+1]。
如果不存在这样的 x，输出 -1，否则输出任意一个符合要求的 x。
输入
8
5
5 3 3 3 5
4
5 3 4 5
8
1 2 3 4 5 6 7 8
6
10 5 4 3 2 1
3
3 3 1
3
42 43 42
2
100000000 99999999
6
29613295 52036613 75100585 78027446 81409090 73215
输出
4
-1
0
42
2
-1
100000000
40741153
"""
"""只需保证相邻两项满足 abs(a[i]-x)≤abs(a[i+1]-x)，那么整个 b[i] 就是递增的（充分必要条件）。

分类讨论：
如果 a[i]=a[i+1]，x 取什么数都满足上面的不等式，所以无视这种情况。
如果 a[i]<a[i+1]，解得 x≤(a[i]+a[i+1])/2。（画出 abs(a[i]-x) 和 abs(a[i+1]-x) 的图像即可得到）
如果 a[i]>a[i+1]，解得 x≥(a[i]+a[i+1])/2。注意这里的除法没有下取整，代码中要写成 (a[i]+a[i+1]+1)/2。

用 l 维护 x 的最小值，r 维护 x 的最大值。
如果最后 l>r 就输出 -1，否则输出 [l,r] 内的任意整数，例如 l。注意 a[i] 的范围可以保证 x 在 [0,1e9] 内。

https://codeforces.com/problemset/submission/1772/214608589"""

#     187  ms
def solve():
    n, = RI()
    a = RILST()
    l, r = 0, 10 ** 9
    for i in range(n - 1):
        x, y = a[i], a[i + 1]
        if x == y:
            continue
        if x < y:
            r = min(r, (x + y) // 2)
        else:
            l = max(l, (x + y + 1) // 2)
        if l > r:
            return print(-1)
    print(l)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
