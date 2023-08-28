# Problem: D - Count Interval
# Contest: AtCoder - AtCoder Beginner Contest 233
# URL: https://atcoder.jp/contests/abc233/tasks/abc233_d
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
PROBLEM = """https://atcoder.jp/contests/abc233/tasks/abc233_d

输入 n(1≤n≤2e5) k(-1e15≤k≤1e15) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)。
输出元素和等于 k 的连续子数组个数。

如果你觉得本题太简单，请思考这个问题：
所有元素和等于 k 的连续子数组的长度之和。
输入
6 5
8 -3 5 7 0 -4
输出 3
"""
"""思考题的话，同时记录前缀和的下标和以及个数即可"""


#   181    ms
def solve():
    n, k = RI()
    p = ans = 0
    cnt = Counter([0])
    for v in RI():
        p += v
        ans += cnt[p - k]
        cnt[p] += 1
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
