# Problem: B. Pasha Maximizes
# Contest: Codeforces - Codeforces Round 249 (Div. 2)
# URL: https://codeforces.com/problemset/problem/435/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/435/B

输入 a(1≤a≤1e18) 和 k(0≤k≤100)。
你需要操作至多 k 次。
每次操作，交换 a 的两个相邻数位。
输出 a 的最大值。
输入 1990 1
输出 9190

输入 300 0
输出 300

输入 1034 2
输出 3104

输入 9090000078001234 6
输出 9907000008001234
"""
"""https://codeforces.com/contest/435/submission/209289302

由于 k 较小，直接模拟。
每次循环尽量把大的换到前面。
具体来说，第 i 次循环，贪心找从第 i 个位置往后 min(k+1,n) 个数位的最大值，然后不断交换到第 i 个位置上。
直接模拟邻项交换，每次交换把 k 减一。这样写是最稳的。"""


#       ms
def solve():
    a, k = RI()
    a = list(map(int, str(a)))

    n = len(a)
    for i in range(n):
        if k == 0: break
        mxj = i
        for j in range(i + 1, min(i + k + 1, n)):
            if a[j] > a[mxj]:
                mxj = j
        if a[mxj] == a[i]: continue
        a[i], a[i + 1:mxj + 1] = a[mxj], a[i:mxj]
        k -= mxj - i
        # print(k,mxj,i)
    print(''.join(map(str, a)))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
