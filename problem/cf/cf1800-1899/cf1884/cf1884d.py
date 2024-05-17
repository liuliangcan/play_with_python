# Problem: D. Counting Rhyme
# Contest: Codeforces - Codeforces Round 904 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1884/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1884/D

输入 T(≤2e4) 表示 T 组数据。所有数据的 n 之和 ≤1e6。
每组数据输入 n(1≤n≤1e6) 和长为 n 的数组 a(1≤a[i]≤n)。

输出有多少对 (i,j)，满足 i<j 且不存在 a[k] (1≤k≤n) 既可以整除 a[i] 又可以整除 a[j]。
输入
6
4
2 4 4 4
4
2 3 4 4
9
6 8 9 4 6 8 9 4 9
9
7 7 4 4 9 9 6 2 9
18
10 18 18 15 14 4 5 6 8 9 10 12 15 16 18 17 13 11
21
12 19 19 18 18 12 2 18 19 12 12 3 12 12 12 18 19 16 18 19 12
输出
0
3
26
26
124
82
"""
"""整体思路
考虑有多少对 (a[i],a[j]) 的 GCD 恰好等于 k，将其记作 res[k]。
如果 a 中没有数能整除 k，我们就可以把 res[k] 加入答案。

如何计算 res[k]
统计 a 中每个元素的出现次数 cnt。
枚举 k 及其倍数（k,2k,3k,...），累加这些数的出现次数，记作 c。
这 c 个数中，任选两个数的 GCD，一定是 k 的倍数。所以 c*(c-1)/2 就是 GCD 等于 k,2k,3k,... 的数对的个数。
但我们要计算的是【恰好】等于 k 的数对个数，所以要减去 GCD 恰好等于 2k,3k,... 的数对个数，得
res[k] = c*(c-1)/2 - res[2k] - res[3k] - ...
这个过程可以用 O(nlogn) 的枚举完成。（调和级数）
注意要倒序枚举 k，因为转移来源是比 k 大的数。

如何计算 a 中是否有整除 k 的数（a 中是否有 k 的因子）
如果 cnt[i] > 0，那么对于 i,2i,3i,... 这些数来说，a 中都有这些数的因子。标记这些数。
这个过程也可以用 O(nlogn) 的枚举完成。

注意使用 64 位整数。
如果觉得代码有些慢，可以加个快读来提速。

代码
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    res = [0] * (n + 1)
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    for i in range(n, 0, -1):
        c = 0
        for j in range(i, n + 1, i):
            res[i] -= res[j]
            c += cnt[j]
        res[i] += c * (c - 1) // 2
    # print(res)
    for i, v in enumerate(cnt):
        if v:
            for j in range(i, n + 1, i):
                res[j] = 0
    # print(res)
    print(sum(res))


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
