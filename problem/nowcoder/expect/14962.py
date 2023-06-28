# Problem: Alice和Bob赌糖果
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/problem/14962
# Memory Limit: 2 MB
# Time Limit: 14962000 ms

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
PROBLEM = """概率博弈
令fi为alice手头有i个，赢的概率。显然：
f(0)=0,f(n+m)=1
令p为每次游戏alice赢一颗的概率
f[i] = (1-p)f[i-1] + pf[i+1]  # 意思是有i颗的话，有1-p概率转移到f[i-1]，有p概率转移到f[i]
"""



#       ms
def solve():
    n, l, r = RI()
    m, x, y = RI()
    if m == 0:
        return 1
    if n == 0:
        return 0
    if r <= x:
        return 0
    if l >= y:
        return 1
    s = p = 0
    for i in range(l, r + 1):
        for j in range(x, y + 1):
            s += i != j
            p += i > j
    p /= s
    ans = 0
    k = [0] * (m + n)  # k[i]=p/(1-(1-p)*k[i-1])
    for i in range(1, n+m):
        k[i] = p / (1 - (1 - p) * k[i - 1])
    f = 1
    for i in range(m + n-1, n-1, -1):
        f = k[i] * f
    return f


if __name__ == '__main__':
    print(f'{solve():.5f}')
