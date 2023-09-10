# Problem: B - Measure
# Contest: AtCoder - AtCoder Beginner Contest 319
# URL: https://atcoder.jp/contests/abc319/tasks/abc319_b
# Memory Limit: 1024 MB
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
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """给定一个正整数N。打印一个长度为(N+1)的字符串，定义如下。

对于每个i=0,1,2,…,N，

如果存在一个在1和9之间的N的因子j，并且i是N/j的倍数，则si是对应最小的j的数字(si将是1,2,...,9中的一个)；
如果不存在这样的j，则si为-。
"""



#       ms
def solve():
    n, = RI()
    ans = []
    for i in range(n+1):
        for j in range(1,10):
            if n%j == 0 and i%(n//j) == 0:
                ans.append(str(j))
                break
        else:
            ans.append('-')
    print(''.join(ans))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
