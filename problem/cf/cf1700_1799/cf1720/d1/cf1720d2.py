# Problem: D2. Xor-Subsequence (hard version)
# Contest: Codeforces - Codeforces Round 815 (Div. 2)
# URL: https://codeforces.com/contest/1720/problem/D2
# Memory Limit: 512 MB
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
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/1720/problem/D2

输入 T(≤1e5) 表示 T 组数据。所有数据的 n 之和 ≤3e5。
每组数据输入 n(2≤n≤3e5) 和长为 n 的数组 a(0≤a[i]≤1e9)，下标从 0 开始。

构造一个严格单调递增的，元素范围在 [0,n-1] 的下标数组 id。
要求 id 中的所有相邻元素 i 和 j，都满足 a[i] XOR j < a[j] XOR i。
例如 a=[5,2,4,3,1]，构造 id=[1,2,4]，满足 a[1] XOR 2 < a[2] XOR 1 以及 a[2] XOR 4 < a[4] XOR 2。

输出 id 的最大长度。
输入
3
2
1 2
5
5 2 4 3 1
10
3 8 8 2 9 1 6 2 8 3
输出
2
3
6
"""

"""https://codeforces.com/contest/1720/submission/204199800

看到 a[i] XOR j < a[j] XOR i 这个式子，就很想把 i 移到左边，j 移到右边，这样就好处理了。
但这是小于，不是等于，没法移项！
要是能想办法改成等于就好了。

既然是位运算，那么从比特位入手，想一想这个 < 是怎么产生的。
假设 a[i] XOR j 和 a[j] XOR i 的高 k 个比特位都相等，从高到低第 k+1 个比特位不同，那么一定是 a[i] XOR j 这一位是 0，a[j] XOR i 这一位是 1，这样才能是小于的关系。

a[i] XOR j 和 a[j] XOR i 的高 k 个比特位都相等，意味着只看这些比特位，a[i] XOR j = a[j] XOR i。
是等号！太棒了，这样就可以把 i 移到左边，j 移到右边了，用哈希表统计 a[i] XOR i，统计什么呢？
但还要比较第 k+1 个比特位，必须满足：
1. a[i] XOR j = 0，那要么 a[i] = j = 0，要么 a[i] = j = 1。
2. a[j] XOR i = 1，那要么 a[j] = 0，i = 1，要么 a[j] = 1，i = 0。
假设当前遍历到 a[j]，由于 j 和 a[j] 是已知的，我们需要找的 a[i] 和 j 在这个比特位是相等的，i 和 a[j] 在这个比特位是相反的。

一通分析后，定义 f[k][x][0/1][0/1] 记录 a[i] XOR i 的高 k 个比特位的值为 x，i 的从高到低第 k+1 的比特值 0/1，a[i] 的从高到低第 k+1 的比特值 0/1，此时的下标数组 id 长度的最大值。
枚举 k，按上述规则求 id 长度的最大值，加一后更新到对应的位置上。"""
"""直接用01trie更直观，每到一个节点查看当前节点下的转移来源即可，之前的高位(父路径)自动相同。这里trie代替了灵神题解中的那个map
注意，trie不能用{}来建，会TLE。
也不能trie = [[0]*2 for _ in range(size)] 会MLE，
要把size和2换一下，小维度在外边才可以过。因为py的内存处理实在傻逼。
另外灵神的写法放到py也是一样TLE，原因同上。
"""


#   tle3    ms
def solve1():
    n, = RI()
    a = RILST()
    f = [defaultdict(lambda: [[0] * 2 for _ in range(2)]) for _ in range(30)]
    ans = 0
    for i, v in enumerate(a):
        mx = 0
        for k in range(30):
            mx = max(mx, f[k][(v ^ i) >> (k + 1)][v >> k & 1 ^ 1][i >> k & 1])
        mx += 1
        ans = max(ans, mx)
        for k in range(30):
            p = f[k][(v ^ i) >> (k + 1)]
            p[i >> k & 1][v >> k & 1] = max(p[i >> k & 1][v >> k & 1], mx)
            # f[k][(v ^ i) >> (k + 1)] = p
    print(ans)


# TLE3
def solve2():
    n, = RI()
    a = RILST()
    # f = [defaultdict(lambda: [[0] * 2 for _ in range(2)]) for _ in range(30)]
    f = [[[{} for _ in range(30)] for _ in range(2)] for _ in range(2)]
    ans = 0
    for i, v in enumerate(a):
        mx = 0
        for k in range(30):
            z = f[v >> k & 1 ^ 1][i >> k & 1][k].get((v ^ i) >> (k + 1), 0)
            if z > mx:
                mx = z
        mx += 1
        ans = max(ans, mx)
        for k in range(30):
            z = f[i >> k & 1][v >> k & 1][k].get((v ^ i) >> (k + 1), 0)
            if mx > z:
                f[i >> k & 1][v >> k & 1][k][(v ^ i) >> (k + 1)] = mx

    print(ans)


# tle3
def solve3():
    n, = RI()
    a = RILST()
    f = [0] * n
    trie = {}
    for i, v in enumerate(a):
        cur = trie
        vi = i ^ v
        for j in range(29, -1, -1):
            p = vi >> j & 1
            if p not in cur:
                cur[p] = {}
            z = cur.get((v >> j & 1 ^ 1) * 2 + (i >> j & 1) + 2, 0)
            if z > f[i]:
                f[i] = z
            cur = cur[p]
        f[i] += 1
        cur = trie
        for j in range(29, -1, -1):
            p = vi >> j & 1
            z = cur.get((i >> j & 1) * 2 + (v >> j & 1) + 2, 0)
            if z < f[i]:
                cur[(i >> j & 1) * 2 + (v >> j & 1) + 2] = f[i]
            cur = cur[p]
    print(max(f))


# tle
def solve4():
    n, = RI()
    a = RILST()
    f = [0] * n
    trie = [[], [], 0, 0, 0, 0]
    for i, v in enumerate(a):
        cur = trie
        vi = i ^ v
        for j in range(29, -1, -1):
            p = vi >> j & 1
            if not cur[p]:
                cur[p] = [[], [], 0, 0, 0, 0]
            # print(i, j)
            z = cur[(v >> j & 1 ^ 1) * 2 + (i >> j & 1) + 2]
            if z > f[i]:
                f[i] = z
            cur = cur[p]
        f[i] += 1
        cur = trie
        for j in range(29, -1, -1):
            p = vi >> j & 1

            z = cur[(i >> j & 1) * 2 + (v >> j & 1) + 2]
            if z < f[i]:
                cur[(i >> j & 1) * 2 + (v >> j & 1) + 2] = f[i]
            cur = cur[p]
    print(max(f))


# MLE
def solve5():
    n, = RI()
    a = RILST()
    f = [0] * n
    trie = [[0, 0] for _ in range(n * 20 + 1)]
    dp = [[0, 0, 0, 0] for _ in range(n * 20 + 1)]
    size = 1
    for i, v in enumerate(a):
        vi = i ^ v
        u = 0
        for j in range(29, -1, -1):
            p = vi >> j & 1
            f[i] = max(f[i], dp[u][(v >> j & 1 ^ 1) * 2 + (i >> j & 1)])
            u = trie[u][p]
            if u == 0:
                break

        f[i] += 1
        u = 0
        for j in range(29, -1, -1):
            p = vi >> j & 1
            if trie[u][p] == 0:
                trie[u][p] = size
                size += 1
            dp[u][(i >> j & 1) * 2 + (v >> j & 1)] = max(dp[u][(i >> j & 1) * 2 + (v >> j & 1)], f[i])

            u = trie[u][p]
    print(max(f))


# 1044ms 428.03 MB
def solve6():
    n, = RI()
    a = RILST()
    f = [0] * n
    trie = [[0] * (n * 30) for _ in range(2)]
    dp = [[0] * (n * 30) for _ in range(4)]
    size = 1
    for i, v in enumerate(a):
        vi = i ^ v
        u = 0
        for j in range(29, -1, -1):
            p = vi >> j & 1
            f[i] = max(f[i], dp[(v >> j & 1 ^ 1) * 2 + (i >> j & 1)][u])
            u = trie[p][u]
            if u == 0:
                break

        f[i] += 1
        u = 0
        for j in range(29, -1, -1):
            p = vi >> j & 1
            if trie[p][u] == 0:
                trie[p][u] = size
                size += 1
            dp[(i >> j & 1) * 2 + (v >> j & 1)][u] = max(dp[(i >> j & 1) * 2 + (v >> j & 1)][u], f[i])

            u = trie[p][u]
    print(max(f))


# 982 ms 425.29 MB
def solve():
    n, = RI()
    a = RILST()
    trie = [[0] * (n * 30) for _ in range(2)]
    dp = [[0] * (n * 30) for _ in range(4)]
    ans = size = 1

    for i, v in enumerate(a):
        vi = i ^ v
        f = 0
        u = 0
        for j in range(29, -1, -1):
            p = vi >> j & 1
            z = dp[((v >> j & 1 ^ 1) << 1) | (i >> j & 1)][u]
            if z > f:
                f = z
            u = trie[p][u]
            if not u:
                break

        f += 1
        if f > ans:
            ans = f
        u = 0
        for j in range(29, -1, -1):
            p = vi >> j & 1
            if not trie[p][u]:
                trie[p][u] = size
                size += 1

            z = dp[((i >> j & 1) << 1) | (v >> j & 1)][u]
            if z < f:
                dp[((i >> j & 1) << 1) | (v >> j & 1)][u] = f

            u = trie[p][u]
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
