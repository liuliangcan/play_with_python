# Problem: A. Points on Line
# Contest: Codeforces - Codeforces Round 153 (Div. 1)
# URL: https://codeforces.com/problemset/problem/251/A
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
PROBLEM = """https://codeforces.com/problemset/problem/251/A

输入 n(1≤n≤1e5) d(1≤d≤1e9) 和长为 n 的严格递增数组 a(-1e9≤a[i]≤1e9)。
输出有多少个三元组 (i,j,k) 满足 i<j<k 且 a[k]-a[i]<=d。
输入
4 3
1 2 3 4
输出 4

输入
4 2
-3 -2 -1 0
输出 2

输入
5 19
1 10 20 30 50
输出 1
"""
"""双指针能秒
看错题：忽略‘严格递增’这个条件，那么变成了典双BIT题
考虑枚举k时，所有符合要求的i，那么i+1~k-1都可以作为j。j的数量是k-i-1,即其中下标的数量。
那么对下标k上的v来说，所有左边的>=v-d的数位置都可以作i，那么k的贡献是:
    sum{(k-i-1)|a[i]>=a[k]-d}
    = k*cnt(i)-sum(i)-cnt(i)
用值域BIT统计他们的下标sum(i)和数量cnt(i)，即可
"""

#    468   ms
def solve():
    n, d = RI()
    a = RILST()
    ci, cnt = [0] * (n + 1), [0] * (n + 1)

    def add(i, v, c):
        while i <= n:
            c[i] += v
            i += i & -i

    def get(i, c):
        s = 0
        while i:
            s += c[i]
            i -= i & -i
        return s

    ans = 0
    for i, v in enumerate(a):
        v1, v2 = bisect_left(a, v - d) + 1, bisect_left(a, v) + 1
        c = get(v2, cnt) - get(v1 - 1, cnt)
        s = get(v2, ci) - get(v1 - 1, ci)

        ans += i * c - s - c
        add(v2, 1, cnt)
        add(v2, i, ci)

    print(ans)


#    310    ms
def solve1():
    n, d = RI()
    a = RILST()
    q = deque()
    ans = 0
    for v in a:
        q.append(v)
        while q[-1] - q[0] > d:
            q.popleft()
        ans += (len(q) - 2) * (len(q) - 1) // 2
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
