# Problem: D. Green and Black Tea
# Contest: Codeforces - Codeforces Round 386 (Div. 2)
# URL: https://codeforces.com/problemset/problem/746/D
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
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/746/D

输入 n k(1≤k≤n≤1e5) a b(0≤a,b≤n 且 a+b=n)。
构造一个长为 n 的字符串，包含 a 个 'G' 和 b 个 'B'，且不能有长度超过 k 的连续相同字母。
如果无法构造，输出 NO，否则输出任意一个符合要求的字符串。
输入 5 1 3 2
输出 GBGBG

输入 7 2 2 5
输出 BBGBGBB

输入 4 3 4 0
输出 NO
"""
"""分类讨论：
若a==b:GB交错即可，连续长度不会超过1.
令a>b:
    那么用b个B当隔板，隔出b+1个位置，每个位置放[1~k]个G即可。
实现时，初始化b*2+1个位置，每个位置填一个G/B。然后用剩余的G补充位置即可。
"""

#   93    ms
def solve():
    n, k, a, b = RI()
    G, B = 'G', 'B'

    if a == b:
        return print('GB' * a)
    elif a < b:
        a, b = b, a
        G, B = B, G
    if k * (b + 1) < a:
        return print('NO')
    ans = [G, B] * b + [G]
    a -= b + 1
    for i in range(0, len(ans), 2):
        p = min(k - 1, a)
        ans[i] += G * p
        a -= p
        if a == 0:
            break
    print(''.join(ans))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
