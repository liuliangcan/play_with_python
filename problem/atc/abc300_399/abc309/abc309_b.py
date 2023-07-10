# Problem: B - Rotate
# Contest: AtCoder - Denso Create Programming Contest 2023 (AtCoder Beginner Contest 309)
# URL: https://atcoder.jp/contests/abc309/tasks/abc309_b
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
PROBLEM = """问题陈述
给定一个有 
N
行和 
N
列的网格。整数 
A 
i,j
​
 写在从上到下的第 
i
行和从左到右的第 
j
列的方格上。在这里，保证 
A 
i,j
​
 要么是 
0
要么是 
1
。

将外部方格上的整数顺时针移动一个方格，并打印结果网格。

这里，外部方格是至少在第 
1
行、第 
N
行、第 
1
列和第 
N
列中的一个方格。

约束条件
2
≤
N
≤
100
0
≤
A 
i,j
​
 ≤1(1≤i,j≤N)
所有输入值都是整数。
"""



#       ms
def solve():
    n, = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append(list(s))
    p = g[0][:]
    for i in range(1,n-1):
        p.append(g[i][-1])
    p.extend(g[-1][::-1])
    for i in range(n-2,0,-1):
        p.append(g[i][0])
    p = p[-1:] + p[:-1]
    # print(len(p),p)
    g[0] = p[:n]
    p = p[n:]
    for i in range(1,n-1):
        g[i][-1] = p[i-1]
    p = p[n-2:]
    g[-1] = p[:n][::-1]
    p = p[n:][::-1]
    # print(p)
    for i in range(n-2,0,-1):
        g[i][0] = p.pop()
    for row in g:
        print(''.join(row))



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
