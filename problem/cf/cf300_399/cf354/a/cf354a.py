# Problem: A. Vasya and Robot
# Contest: Codeforces - Codeforces Round 206 (Div. 1)
# URL: https://codeforces.com/problemset/problem/354/A
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
PROBLEM = """https://codeforces.com/problemset/problem/354/A

输入 n(1≤n≤1e5) l r(1≤l,r≤100) ql qr(1≤l,r≤1e4) 和长为 n 的双端队列 q(1≤q[i]≤100)。
每次操作弹出 q 的队首或者队尾，代价分别为 l*a[i] 和 r*a[i]。
如果上一次和当前都是弹出队首，则代价额外加上 ql。
如果上一次和当前都是弹出队尾，则代价额外加上 qr。
输出清空 q 的最小代价。
输入
3 4 4 19 1
42 3 99
输出 576

输入
4 7 2 3 9
1 2 3 4
输出 34
"""
"""https://codeforces.com/contest/354/submission/210296537

前后缀分解。

枚举弹出队首 i 次，那么弹出队尾 n-i 次。
如果 i 比较小，那么操作应该是首尾首尾 ... 尾尾尾尾。
如果 i 比较大，那么操作应该是尾首尾首 ... 首首首首。"""


#     108  ms
def solve():
    n, l, r, ql, qr = RI()
    a = RILST()
    s = sum(a) * r
    ans = s + (n - 1) * qr
    p = 0
    for i, v in enumerate(a, start=1):
        p += l * v
        s -= r * v
        if i > n - i:
            x = i - n + i - 1
            ans = min(ans, p + s + x * ql)
        else:
            x = n - i - i - 1
            if x >= 1:
                ans = min(ans, p + s + x * qr)
            else:
                ans = min(ans, p + s)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
