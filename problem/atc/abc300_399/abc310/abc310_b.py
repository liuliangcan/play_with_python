# Problem: B - Strictly Superior
# Contest: AtCoder - freee Programming Contest 2023（AtCoder Beginner Contest 310）
# URL: https://atcoder.jp/contests/abc310/tasks/abc310_b
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
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """tCoder商店有N个产品。第i个产品（1≤i≤N）的价格是Pi。第i个产品（1≤i≤N）有Ci个功能。第i个产品（1≤i≤N）的第j个功能（1≤j≤Ci）表示为一个介于1和M之间的整数Fi,j。

高桥想知道是否有一个产品严格优于另一个产品。如果存在i和j（1≤i，j≤N），使得第i个和第j个产品满足以下所有条件，则输出Yes；否则输出No。

Pi≥Pj。 第j个产品具有第i个产品的所有功能。 Pi>Pj，或者第j个产品具有第i个产品缺少的一个或多个功能。
"""


#       ms
def solve():
    n, m = RI()
    g = []
    for _ in range(n):
        p, c, *f = RI()
        g.append((p, set(f)))
    # g.sort(reverse=True)
    for i in range(n):
        a = g[i][1]
        pi = g[i][0]
        for j in range( n):
            if i == j: continue
            b = g[j][1]
            pj = g[j][0]
            # if i == 4 and j == 3:
            #     print(pi,pj,a,b)
            if pi >= pj:
                if len(b) == len(b | a):
                    # print(a,b)
                    if pi > pj or b - a:
                        return print('Yes')
    print('No')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
