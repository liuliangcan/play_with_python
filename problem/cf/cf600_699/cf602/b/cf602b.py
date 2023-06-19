# Problem: B. Approximating a Constant Range
# Contest: Codeforces - Codeforces Round 333 (Div. 2)
# URL: https://codeforces.com/problemset/problem/602/B
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/602/B

输入 n(2≤n≤1e5) 和长为 n 的数组 a(1≤a[i]≤1e5 且 abs(a[i]-a[i-1])≤1)。
输出 a 的最长连续子数组的长度，满足数组中的最大值减最小值不超过 1。
输入
5
1 2 3 3 2
输出 4

输入
11
5 4 5 5 6 7 8 8 8 7 6
输出 5
"""


#     139  ms
def solve1():
    n, = RI()
    a = RILST()
    mx, mn = -inf, inf
    ans = 2
    cnt = [0] * (max(a) + 1)
    q = deque()
    for v in a:
        q.append(v)
        cnt[v] += 1
        mx, mn = max(mx, v), min(mn, v)
        while mn + 1 < mx:
            cnt[q.popleft()] -= 1
            while not cnt[mx]:
                mx -= 1
            while not cnt[mn]:
                mn += 1
        ans = max(ans, len(q))
    print(ans)


#     109  ms
def solve():
    n, = RI()
    a = RILST()
    mx, mn = -inf, inf
    ans = 2
    cnt = [0] * 100001
    l = 0
    for r, v in enumerate(a):
        cnt[v] += 1
        mx, mn = max(mx, v), min(mn, v)
        while mn + 1 < mx:
            cnt[a[l]] -= 1
            l += 1
            while not cnt[mx]:
                mx -= 1
            while not cnt[mn]:
                mn += 1
        ans = max(ans, r - l + 1)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
