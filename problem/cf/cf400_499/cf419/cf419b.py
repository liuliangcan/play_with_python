# Problem: B. Karen and Coffee
# Contest: Codeforces - Codeforces Round 419 (Div. 2)
# URL: https://codeforces.com/problemset/problem/816/B
# Memory Limit: 512 MB
# Time Limit: 2500 ms

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

if not sys.version.startswith('3.5.3'):  # ACW没有comb
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
PROBLEM = """https://codeforces.com/problemset/problem/816/B

输入 n k(1≤k≤n≤2e5) q(1≤q≤2e5)。
然后输入 n 个 recipe，每个 recipe 输入两个数 L R(1≤L≤R≤2e5)，表示冲一杯咖啡的推荐温度范围为 [L,R]。
定义一个整数温度 t 是「可接受的」，如果 t 包含在至少 k 个 recipe 的推荐温度范围内。
然后输入 q 个询问，每个询问输入两个数 a b(1≤a≤b≤2e5)，输出 [a,b] 内有多少个温度是可接受的，每行一个答案。

进阶：如果 k 是每个询问输入的数呢？@liupengsay

输入
3 2 4
91 94
92 97
97 99
92 94
93 97
95 96
90 100
输出
3
3
0
4

输入
2 1 1
1 1
200000 200000
90 100
输出 0
"""
"""差分即可
思考题：离线询问，按k从大到小，用树状数组维护求和。
"""

#   326    ms
def solve():
    n, k, q = RI()
    d = [0] * (2 * 10 ** 5 + 2)
    for _ in range(n):
        l, r = RI()
        d[l] += 1
        d[r + 1] -= 1
    a = 0
    p = [0] * len(d)
    for i, v in enumerate(d[1:], start=1):
        a += v
        p[i] = p[i - 1] + (a >= k)
    for _ in range(q):
        a, b = RI()
        print(p[b] - p[a - 1])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
