# Problem: B. Little Dima and Equation
# Contest: Codeforces - Codeforces Round 262 (Div. 2)
# URL: https://codeforces.com/problemset/problem/460/B
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
PROBLEM = """https://codeforces.com/problemset/problem/460/B

输入 a(1≤a≤5) b(1≤b≤10000) c(-10000≤c≤10000)。
解方程：
x = b * pow(s(x),a) + c 且 0 < x < 1e9
其中 s(x) 是 x 的数位和。
第一行输出 x 的个数。
第二行按升序输出所有 x。
输入
3 2 8
输出
3
10 2008 13726

输入
1 2 -18
输出
0

输入
2 2 -1
输出
4
1 31 337 967
"""
"""https://codeforces.com/contest/460/submission/208147283

枚举 s(x)。

由于 0<x<1e9，所以 1<=s(x)<=81。
代入等式右边，算出 x，再验证 s(x) 是否等于所枚举的 s(x)。"""


#    93   ms
def solve():
    a, b, c = RI()
    ans = []
    for s in range(1, 82):
        x = b * pow(s, a) + c

        if 0 < x < 10 ** 9 and sum(map(int, str(x))) == s:
            ans.append(x)
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
