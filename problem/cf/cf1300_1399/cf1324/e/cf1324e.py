# Problem: E. Sleeping Schedule
# Contest: Codeforces - Codeforces Round #627 (Div. 3)
# URL: https://codeforces.com/contest/1324/problem/E
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/1324/problem/E

输入 n(≤2000) h L R (0≤L≤R<h≤2000) 和长为 n 的数组 a(1≤a[i]<h)。

对于每个 a[i]，你可以把它减一，或者保持不变（换句话说，每个 a[i] 至多 -1 一次）。
定义前缀和 s[0]=a[0], s[i]=s[i-1]+a[i]。
如果 s[i]%h 落在闭区间 [L,R] 内，则分数加一。
最大化分数。

输入
7 24 21 23
16 17 14 20 20 11 22
输出 3
"""
"""https://codeforces.com/contest/1324/submission/193356533
https://codeforces.com/contest/1324/submission/193357512
https://codeforces.com/contest/1324/submission/193357666

我在 https://www.bilibili.com/video/BV1Xj411K7oF/ 中讲了，先把记忆化搜索写出来，再转成递推是最容易的。

那么定义 dfs(i,s)，i 表示当前在 a[i]，s 表示前面累计的和，返回最大分数。
那么 dfs(i,s) = max(dfs(i+1,(s+a[i])%h),dfs(i+1,(s+a[i]-1)%h)) + (l<=s<=r)
具体细节见代码（包含记忆化搜索、递推、空间优化）。"""


#    280   ms
def solve1():
    n, h, l, r = RI()
    a = RILST()
    f = [[0] * h for _ in range(n + 1)]
    for s in range(l, r + 1):
        f[n][s] = 1
    for i in range(n - 1, -1, -1):
        for s in range(h):
            f[i][s] = max(f[i + 1][(s + a[i]) % h], f[i + 1][(s + a[i] - 1) % h])
            if i > 0 and l <= s <= r:
                f[i][s] += 1
    print(f[0][0])


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


#   1465    ms
def solve2():
    n, h, l, r = RI()
    a = RILST()
    dp = [[-1] * h for _ in range(n + 1)]

    @bootstrap
    def dfs(i, s):
        if dp[i][s] == -1:
            if i == n:
                if l <= s <= r:
                    dp[i][s] = 1
                else:
                    dp[i][s] = 0
            else:
                yield dfs(i + 1, (s + a[i]) % h)
                yield dfs(i + 1, (s + a[i] - 1) % h)
                ans = max(dp[i + 1][(s + a[i]) % h], dp[i + 1][(s + a[i] - 1) % h])
                if i > 0 and l <= s <= r:
                    ans += 1
                dp[i][s] = ans
        yield

    dfs(0, 0)
    print(dp[0][0])


#    233   ms
def solve3():
    n, h, l, r = RI()
    a = RILST()
    f = [0] * h
    for s in range(l, r + 1):
        f[s] = 1
    for i in range(n - 1, -1, -1):
        g = [0] * h
        for s in range(h):
            g[s] = max(f[(s + a[i]) % h], f[(s + a[i] - 1) % h])
            if i > 0 and l <= s <= r:
                g[s] += 1
        f = g
    print(f[0])


#   233    ms
def solve():
    n, h, l, r = RI()
    a = RILST()
    dp = [[0] * h for _ in range(2)]
    f, g = dp
    for s in range(l, r + 1):
        f[s] = 1
    for i in range(n - 1, -1, -1):
        for s in range(h):
            g[s] = max(f[(s + a[i]) % h], f[(s + a[i] - 1) % h])
            if i > 0 and l <= s <= r:
                g[s] += 1
        f, g = g, f
    print(f[0])


if __name__ == '__main__':
    solve()
