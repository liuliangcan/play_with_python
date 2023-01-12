# Problem: Checkout Assistant
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/CF19B
# Memory Limit: 250 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://www.luogu.com.cn/problem/CF19B
输入n(1≤n≤2000)代表n件商品,
然后输入n行t(0<=t<=2000),c(1<=c<=1e9)代表扫描时间和商品花费
当你花费c购买一件商品时，可以偷走尚未购买的其它t件商品。
求最少花多少钱可以买完n件商品。

输入
4
2 10
0 20
1 5
1 3
输出
8 
"""
"""01背包
对于每件已购买商品，他实际能提供t+1件贡献。
假设我们最终实际花钱买了k件商品，我们需要这k件商品总贡献>=n。
把贡献看做体积V，我们从商品里选择，看看超过n的体积下最少花费是多少。
体积上限应该是n+max(t),即超过n的部分不用再接着算了，但这个没超的还要
"""


#       ms
def solve():
    n, = RI()
    a = []
    v = 0
    for _ in range(n):
        a.append(RILST())
        if a[-1][0] > v:
            v = a[-1][0]
    v += n
    f = [0] + [inf] * v
    for t, c in a:
        for j in range(v, t, -1):
            f[j] = min(f[j], f[j - t - 1] + c)
    print(min(f[n:]))


if __name__ == '__main__':
    solve()
