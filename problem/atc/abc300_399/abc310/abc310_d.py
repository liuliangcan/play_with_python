# Problem: D - Peaceful Teams
# Contest: AtCoder - freee Programming Contest 2023（AtCoder Beginner Contest 310）
# URL: https://atcoder.jp/contests/abc310/tasks/abc310_d
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
PROBLEM = """有N个运动员。

其中，有M个不兼容的配对。第i个不兼容的配对（1≤i≤M）是第Ai个和第Bi个运动员。

你需要将这些运动员分成T个队伍。每个运动员必须属于且只能属于一个队伍，每个队伍必须有一个或多个运动员。另外，对于每个1≤i≤M，第Ai个和第Bi个运动员不能属于同一个队伍。

找出满足这些条件的方法数。在这里，当一个分组中有两个运动员属于同一个队伍而另一个分组中属于不同队伍时，这两个分组被认为是不同的。

约束条件
1≤T≤N≤10
0≤M≤2N(N−1)
1≤Ai<Bi≤N (1≤i≤M)
(Ai,Bi) ≠ (Aj,Bj) (1≤i<j≤M)
所有输入值都是整数。
"""


#       ms
def solve():
    n, t, m = RI()
    bad = set()
    for _ in range(m):
        bad.add(tuple(sorted(RILST())))

    def check(mask):
        s = []
        for i in range(n):
            if mask >> i & 1:
                for j in s:
                    if (j + 1, i + 1) in bad:
                        return False
                s.append(i)
        return True

    @lru_cache(None)
    def f(mask, t):
        if not mask:
            return int(t == 0)
        lb = mask & -mask
        s = mask
        ans = 0
        while s:
            if s & lb and check(s):
                ans += f(mask ^ s, t - 1)
            s = (s - 1) & mask
        return ans

    print(f((1 << n) - 1, t))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
