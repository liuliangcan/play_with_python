# Problem: D. Watch the Videos
# Contest: Codeforces - 2022-2023 ICPC, NERC, Southern and Volga Russian Regional Contest (Online Mirror, ICPC Rules, Preferably Teams)
# URL: https://codeforces.com/problemset/problem/1765/D
# Memory Limit: 512 MB
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
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1765/D

输入 n(1≤n≤2e5) m(1≤m≤1e9) 和长为 n 的数组 a(1≤a[i]≤m)。
硬盘可用空间为 m。
有 n 个视频，下载第 i 个需要 a[i] 分钟，占用 a[i] 的硬盘空间。
同一时间只能下载一个视频，一旦视频开始下载，就会立刻占用 a[i] 的硬盘空间。
视频下完才能看。每个视频都恰好花 1 分钟看完，看完后可以立刻删除视频，释放空间。
你可以在看视频的同时下载另一个视频（如果硬盘空间足够的话）。
你需要下载并看完这 n 个视频。
问：到看完最后一个视频，最少要用多少分钟？
输入
5 6
1 2 3 4 5
输出 16

输入
5 5
1 2 3 4 5
输出 17

输入
4 3
1 3 2 3
输出 12
"""
"""请先做这题：
881. 救生艇

最多要花 n + sum(a) 分钟。在这基础上，考虑如何安排可以在看视频的同时下载。
受到救生艇这题的启发，排序+双指针，如果 a[l]+a[r]<=m，那么先下载 a[r]，看 a[r] 的同时下载 a[l]，那么看 a[l] 的同时，又可以下载另外一个视频（因为 a[l] 加上一个<=a[r] 的必然 <= m）。
所以只要 a[l]+a[r]<=m，那么就可以节省 2 分钟，除非 a[l] 是最后一个视频，那么最后一分钟只能看，此时只能节省 1 分钟。

https://codeforces.com/contest/1765/submission/214219665"""


#  171     ms
def solve():
    n, m = RI()
    a = RILST()
    a.sort()
    ans = sum(a) + n
    if n == 1 or a[0] + a[1] > m:
        return print(ans)

    r = bisect_right(a, m - a[0]) - 1
    l = 0
    while l < r:
        while l < r and a[l] + a[r] > m:
            r -= 1
        if l < r:
            if l + 1 < r:
                ans -= 2
            else:
                ans -= 1
            l += 1
            r -= 1
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
