# Problem: D. Non-Secret Cypher
# Contest: Codeforces - Codeforces Round 120 (Div. 2)
# URL: https://codeforces.com/problemset/problem/190/D
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/190/D

输入 n k(1≤k≤n≤4e5) 和长为 n 的数组 a(1≤a[i]≤1e9)。
统计有多少个连续子数组 b，满足 b 中有至少 k 个数都相同。
输入
4 2
1 2 1 2
输出 3

输入
5 3
1 2 1 1 3
输出 2

输入
3 1
1 1 1
输出 6
"""
"""同向双指针滑就换了
枚举右端点，看看有多少个满足条件的左端点。
cnt维护最大左端点到i之间的数字计数，有任意cnt>=k则缩窗。
那么窗内都是不满足的，窗外都是满足的，即：窗左的所有点都可以当左端点。
正难则反更简单：找到所有段，满足所有cnt<k，用总数减去即可。
"""


#    530   ms
def solve2():
    n, k = RI()
    a = RILST()
    ans = 0
    cnt = Counter()
    l = 0
    for i, v in enumerate(a):
        cnt[v] += 1
        while cnt[v] >= k:
            cnt[a[l]] -= 1
            l += 1
        ans += l
    print(ans)


#  590  ms
def solve():
    n, k = RI()
    a = RILST()
    ans = n * (n + 1) // 2
    cnt = Counter()
    l = 0
    for i, v in enumerate(a):
        cnt[v] += 1
        while cnt[v] >= k:
            cnt[a[l]] -= 1
            l += 1
        ans -= i - l + 1
    print(ans)


#    1058   ms
def solve1():
    n, k = RI()
    a = RILST()
    h = sorted(set(a))
    ans = 0
    cnt = [0] * len(h)
    l = 0
    for v in a:
        p = bisect_left(h, v)
        cnt[p] += 1
        while cnt[p] >= k:
            cnt[bisect_left(h, a[l])] -= 1
            l += 1
        ans += l
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
