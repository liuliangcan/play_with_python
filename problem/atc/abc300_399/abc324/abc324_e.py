# Problem: E - Joint Two Strings
# Contest: AtCoder - Japan Registry Services (JPRS) Programming Contest 2023 (AtCoder Beginner Contest 324)
# URL: https://atcoder.jp/contests/abc324/tasks/abc324_e
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
if not sys.version.startswith('3.5.3'):  # ACW没有comb
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
PROBLEM = """
"""


def f(s,t):
    j = 0
    n = len(t)
    for c in s:
        if j < n and t[j] == c:
            j += 1
    return j
#       ms
def solve():
    n, t = RS()
    n = int(n)
    tn = len(t)
    tt = t[::-1]
    pre,suf = [],[]
    ans = 0
    for _ in range(n):
        s, = RS()
        x, y = f(s,t),f(s[::-1],tt)
        # print(x,y,tn)
        pre.append(x)
        suf.append(y)
        # ans += pre.bisect_right(tn-y) +suf.bisect_right(tn-x)
    pre.sort()
    # print(pre,suf)
    for v in suf:
        # print(v,bisect_right(pre,tn-v), n)
        ans += n - bisect_left(pre,tn-v)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
