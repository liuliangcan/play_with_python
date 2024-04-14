# Problem: 小红的排列构造
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/80259/C
# Memory Limit: 524288 MB
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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""



#       ms
def solve():
    n, = RI()
    a = RILST()
    cnt = Counter(sorted(a))
    if max(cnt.values())>=3:
        return print(-1)
    a1,a2 = [0]*n,[0]*n
    s1,s2 = set(),set()
    for i, v in enumerate(a):
        if v in s1:
            s2.add(v)
            a2[i] = v
        else:
            s1.add(v)
            a1[i] = v
    s1 = set(range(1,n+1)) - s1
    for i, v in enumerate(a1):
        if not v:
            a1[i] = s1.pop()
    s2 = set(range(1,n+1)) - s2
    for i, v in enumerate(a2):
        if not v:
            a2[i] = s2.pop()
    print(*a1)
    print(*a2)



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
