# Problem: 小美的元素删除
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/64593/D
# Memory Limit: 524288 MB
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
PROBLEM = """读完题觉得最后保留的数列是一个顺序递增的倍数串，即后一个一定包含前边的因数，那么在1e9内，最长也就只能是全2，长度30。
然后硬写个二维dp，由于是求方案数，因此定义f[i][j]时，表示以i为结尾的方案数，一定要包含i。
那么是可以遍历更小的数，找因数来转移的，由于还要遍历每个长度，因此是三次方。
注意到长度一定<=30,否则就是0，所以可以剪掉这部分。优化成n^2 * 30。
注意到转移时长度只用到前边一个状态，因此状态反过来定义，就可以滚动了。
滚动时可以按背包逆序，只需要一个数组，但是注意这题是求方案数，记得清空
"""


#       ms
def solve():
    n, k = RI()
    a = RILST()
    if k == n:
        return print(1)
    p = n - k
    if p > 31:  # 不写这个就是n^3,注意到保留的长度最多是30,即2^30约1e9
        return print(0)
    p = min(p, 31)
    a.sort()
    f = [1] * n  # f[j][i] 以i为结尾，长为j的序列的方案数
    for k in range(p - 1):
        for i in range(n - 1, -1, -1):
            f[i] = 0  # 逆序更新，就可以用一个数组滚动，但是这题求方案数，注意记得清空f[i]
            for j in range(i):
                if a[i] % a[j] == 0:  # 从可行的地方转移来
                    f[i] += f[j]  # 从k-1长度的方案加上a[i],变成尾巴为a[i]长度为k的方案数
                    f[i] %= MOD

    print(sum(f) % MOD)


#       ms
def solve2():
    n, k = RI()
    a = RILST()
    if k == n:
        return print(1)
    p = n - k
    if p > 31:  # 不写这个就是n^3
        return print(0)
    p = min(p, 31)
    a.sort()
    f = [1] * n  # f[j][i] 以i为结尾，长为j的序列的方案数
    for k in range(p - 1):
        g = [0] * n
        for i, v in enumerate(a):
            for j in range(i):
                if v % a[j] == 0:  # 从可行的地方转移来
                    g[i] += f[j]  # 从k-1长度的方案加上a[i],变成尾巴为a[i]长度为k的方案数
                    g[i] %= MOD
        f = g

    print(sum(f) % MOD)


#       ms
def solve1():
    n, k = RI()
    a = RILST()
    if k == n:
        return print(1)
    p = n - k
    if p > 31:  # 不写这个就是n^3
        return print(0)
    p = min(p, 31)
    a.sort()
    f = [[0] * (p + 1) for _ in range(n)]  # f[i][j] 以i为结尾，长为j的序列的方案数
    for i in range(n):
        f[i][1] = 1
    for i, v in enumerate(a):
        for j in range(i):
            if v % a[j] == 0:  # 从可行的地方转移来
                for k in range(2, p + 1):
                    f[i][k] += f[j][k - 1]  # 从k-1长度的方案加上a[i],变成尾巴为a[i]长度为k的方案数
                    f[i][k] %= MOD
    ans = 0
    for i in range(n):
        ans += f[i][p]
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
