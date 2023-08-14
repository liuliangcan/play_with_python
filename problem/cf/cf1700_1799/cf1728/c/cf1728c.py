# Problem: C. Digital Logarithm
# Contest: Codeforces - Educational Codeforces Round 135 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1728/C
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
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1728/C

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(1≤n≤2e5) 和两个长为 n 的数组 a b (1≤a[i],b[i]<1e9)。

每次操作，把其中一个数组的一个元素替换成这个数的十进制长度。比如 123 替换成 3。
若干次操作后，将 a 和 b 排序，要求所有 a[i]=b[i]。
输出最小操作次数。
输入
4
1
1
1000
4
1 2 3 4
3 1 4 2
3
2 9 3
1 100 9
10
75019 709259 5 611271314 9024533 81871864 9 3 6 4865
9503 2 371245467 6 7 37376159 8 364036498 52295554 169
输出
2
0
2
18
"""


#     280  ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    small, big = [0] * 10, Counter()
    for x, y in zip(a, b):
        if x < 10:
            small[x] += 1
        else:
            big[x] += 1
        if y < 10:
            small[y] -= 1
        else:
            big[y] -= 1
    ans = 0
    for k, v in big.items():
        ans += abs(v)
        small[len(str(k))] += v
    print(ans + sum(map(abs, small[2:])))


#     327  ms
def solve1():
    n, = RI()
    a = RILST()
    b = RILST()
    small, big = [0] * 10, Counter()
    for v in a:
        if v < 10:
            small[v] += 1
        else:
            big[v] += 1
    for v in b:
        if v < 10:
            small[v] -= 1
        else:
            big[v] -= 1
    # print(small, big)
    ans = 0
    for k, v in big.items():
        ans += abs(v)
        small[len(str(k))] += v
    # print(ans,small[2:],sum(map(abs, small[2:])))
    print(ans + sum(map(abs, small[2:])))


# 608ms
def solve1():
    n, = RI()
    a = Counter(RILST())
    b = Counter(RILST())

    def f(a, down):
        c = Counter()
        p = 0
        for k, v in a.items():
            if k >= down:
                k = len(str(k))
                p += v
            c[k] += v
        return c, p

    c = Counter({k: min(v, b[k]) for k, v in a.items() if k >= 10})  # 超过10的共同部分减去，不用处理
    a -= c
    b -= c
    ans = 0
    a, p = f(a, 10)
    ans += p
    b, p = f(b, 10)
    ans += p

    c = Counter({k: min(v, b[k]) for k, v in a.items() if k >= 2})  # 超过2的共同部分减去，不用处理
    a -= c
    b -= c
    ans += f(a, 2)[1] + f(b, 2)[1]

    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
