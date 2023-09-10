# Problem: E - Bus Stops
# Contest: AtCoder - AtCoder Beginner Contest 319
# URL: https://atcoder.jp/contests/abc319/tasks/abc319_e
# Memory Limit: 1024 MB
# Time Limit: 3000 ms

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
from math import sqrt, gcd, inf, lcm

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
PROBLEM = """高桥最初在自己的房子里，准备去访问青木的房子。

两个房子之间有 N 个公交车站，编号从 1 到 N，高桥可以按以下方式在它们之间移动：

他可以在 X 单位时间内从自己的房子走到公交车站 1。
对于每个 i=1,2,…,N−1，公交车站 i 每隔 Pi 的倍数时间会有一辆公交车出发，乘坐这辆公交车，他可以在 Ti 单位时间内到达公交车站 (i+1)。这里的限制条件保证了 1≤Pi≤8。
高桥可以在 Y 单位时间内从公交车站 N 走到青木的房子。
对于每个 i=1,2,…,Q，处理以下查询：

找到高桥在时间 qi 离开自己的房子时最早可以到达青木的房子的时间。

注意，如果他恰好在公交车的发车时间到达一个公交车站，他可以乘坐那辆公交车。
"""
"""每层的状态计算ll=lcm(1~8)=840个，分别转移
"""


#    482   ms
def solve():
    n, x, y = RI()
    pt = []
    ll = 1
    for _ in range(n - 1):
        pt.append(RILST())
        ll = lcm(ll, pt[-1][0])
    f = [0] * ll  # f[i][j]到0时间模ll为j时，从0到达i的时间
    for p, t in pt:
        for j in range(ll):
            f[j] = f[j] + t + (p - f[j] - j) % p  # 到达上一步的实际是时间是f[j]+j，那么要等待(p - f[j] - j) % p

    q, = RI()
    for _ in range(q):
        qi, = RI()
        print(qi + x + f[(qi + x) % ll] + y)  # 到达0的时间是qi+x


#   1178    ms
def solve1():
    n, x, y = RI()
    pt = []
    ll = 1
    for _ in range(n - 1):
        pt.append(RILST())
        ll = lcm(ll, pt[-1][0])
    f = [[0] * ll for _ in range(n)]  # f[i][j]到0时间模ll为j时，从0到达i的时间
    for i, (p, t) in enumerate(pt, start=1):
        for j in range(ll):
            f[i][j] = f[i - 1][j] + t + (p - f[i - 1][j] - j) % p
    q, = RI()
    for _ in range(q):
        qi, = RI()
        print(qi + x + f[-1][(qi + x) % ll] + y)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
