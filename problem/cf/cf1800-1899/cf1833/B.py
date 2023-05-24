# Problem: B. Restore the Weather
# Contest: Codeforces - Codeforces Round 874 (Div. 3)
# URL: https://codeforces.com/contest/1833/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，实测这个快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """输入n、k和长为n的数组a、b。
a[i]代表第i天预测的气温。
b[i]代表第i天实际气温。但是b被打乱了。
已知每天的abs(预测值-实际值)<=k。
请还原出一个正确的b。数据保证有解
"""
"""贪心思考，优先匹配大的或者小的值即可。由于数据保证有解，k实际没用。
为了代码方便，从大的开始匹配，这样b就可以一直pop
"""


#       ms
def solve():
    n, k = RI()
    a = RILST()
    b = RILST()
    b.sort()
    ans = [0] * n
    for i in sorted(range(n), key=lambda x: -a[x]):
        ans[i] = b.pop()
    print(*ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
