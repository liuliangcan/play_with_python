# Problem: C. Mr. Perfectly Fine
# Contest: Codeforces - Codeforces Round 871 (Div. 4)
# URL: https://codeforces.com/contest/1829/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/1829/problem/C
输入t组数据。每组数据：
输入n。
接下来n行输入m和一个长为2的01串，代表阅读这本书需要m分钟，01串上的1代表给这个技能。
输入最少要几分钟可以获得2个不同技能。
"""
"""由于只有01，一共4种情况，直接每种情况求最小即可"""

#       ms
def solve():
    n, = RI()
    c = defaultdict(lambda: inf)
    for _ in range(n):
        m, s = RS()
        m = int(m)
        c[s] = min(c[s], m)
    ans = min(c['11'], c['01'] + c['10'])
    if ans < inf:
        return print(ans)
    print(-1)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
