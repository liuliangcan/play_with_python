# Problem: 割草机
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/problem/14417?&headNav=acm
# Memory Limit: 2 MB
# Time Limit: 14417000 ms

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
PROBLEM = """
"""

"""dp
手玩一下发现，路径是单向的，第一行一定是向右走，第二行向左走，第三行向左。。即偶数行向右奇数行向左（0-indexed)
同时如果最后几行/末行最后位置没有草，可以直接到最后一块草结束。这块草就是本行最左(奇数行)或最右(偶数行)的草
定义f[i][j]为走到第i行第j列时，需要的最小步数
首行f[0]是确定的即list(range(m))。即只能从本行前一步过来
考虑f[i][j]的转移，
1. 它可以从上一行下来，即f[i-1][j]+1
2. 它可以从前一步过来，即f[i][j-1/+1]+1，注意奇偶性。
什么时候从上一行下来呢，手玩发现，必须是j在本行第一个草前边，且是上一行最后一个草后边；同时如果这行或上一行没有草，则没有这个限制。
"""
#       ms
def solve():
    n, m = RI()
    g = []
    for _ in range(n):
        a, = RS()
        x, y = -1, -1
        for i, v in enumerate(a):
            if v == 'W':
                if x == - 1:
                    x = i
                y = i
        g.append((x, y))
    while g[-1][-1] == -1:
        g.pop()
    if not g:
        return print(0)
    f = list(range(m))
    for i in range(1, len(g)):
        f1 = [0] * m
        if i & 1:
            j = m - 1
            while j >= 0 and (j >= g[i][1] or g[i][1] == -1) and (j >= g[i - 1][1] or g[i - 1][1] == -1):
                f1[j] = f[j] + 1
                j -= 1
            while j >= 0:
                f1[j] = f1[j + 1] + 1
                j -= 1
        else:
            j = 0
            while j < m and (j <= g[i][0] or g[i][0] == -1) and (j <= g[i - 1][0] or g[i - 1][0] == -1):
                f1[j] = f[j] + 1
                j += 1
            while j < m:
                f1[j] = f1[j - 1] + 1
                j += 1
        f = f1

    print(f[g[-1][len(g) & 1]])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
