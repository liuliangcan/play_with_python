# Problem: C. Playlist
# Contest: Codeforces - Educational Codeforces Round 62 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1140/C
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
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1140/C

输入 n k(1≤k≤n≤3e5) 和 n 个物品，每个物品输入两个属性值 t[i] 和 b[i]，范围 [1,1e6]。
从这 n 个物品中选出至多 k 个物品，输出这 k 个物品的 sum(t) * min(b) 的最大值。

输入
4 3
4 7
15 1
3 6
6 8
输出 78

输入
5 3
12 31
112 4
100 100
13 55
55 50
输出 10000
"""


#   1201    ms
def solve():
    n, k = RI()
    a = []
    for _ in range(n):
        t, b = RI()
        a.append((b, t))
    a.sort(reverse=True)
    ans = s = 0
    h = []
    for b, t in a:
        if len(h) < k:
            heappush(h, t)
            s += t
        else:
            s += t - heappushpop(h, t)
        ans = max(ans, s*b)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
