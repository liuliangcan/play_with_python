# Problem: G. Hits Different
# Contest: Codeforces - Codeforces Round 871 (Div. 4)
# URL: https://codeforces.com/contest/1829/problem/G
# Memory Limit: 256 MB
# Time Limit: 2500 ms

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
PROBLEM = """输入t组数据，每组数据：
输入一个n，代表击中的编号。
一些罐头按金字塔图（去看图）摆放：
第一行1个，第二行2个..编号按这个顺序从1开始递增，每个罐头的价值是编号的平方
你抛掷一个小球，仅会击中一个编号，叠在这个罐头以上的罐头都会摔落，问摔落的总价值
"""
"""用dp预处理，然后查表。
首先按二维建图。
f[i][j]为第i行第j个罐头的摔落值。
发现每个罐头的摔落值等于自己加上前一排的右侧值和左侧那一竖排。
那么令g[i][j]等于每个罐头的竖排求和，则可以递推。
由于是按编号查询的，因此构造一个ans下标等于编号。
"""



NN = 2023
# a = [[0]*2023 for _ in range(NN)]
f = [[0] * 2023 for _ in range(NN)]
g = [[0] * 2023 for _ in range(NN)]
ans = [0]
x = 1
for i in range(NN):
    for j in range(i + 1):
        # a[i][j] = x*x
        f[i][j] = x * x
        g[i][j] = x * x
        if i:
            f[i][j] += f[i - 1][j]
            if j:
                f[i][j] += g[i - 1][j - 1]
                g[i][j] += g[i - 1][j - 1]
        x += 1
        ans.append(f[i][j])


#       ms
def solve():
    n, = RI()
    print(ans[n])


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
