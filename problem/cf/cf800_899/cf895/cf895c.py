# Problem: C. Square Subsets
# Contest: Codeforces - Codeforces Round 448 (Div. 2)
# URL: https://codeforces.com/problemset/problem/895/C
# Memory Limit: 256 MB
# Time Limit: 4000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/895/C

输入 n(1≤n≤1e5) 和长为 n 的数组 a(1≤a[i]≤70)。
输出有多少个非空子序列，其元素乘积是完全平方数。模 1e9+7。

注：子序列不一定连续。
注：只要有元素下标不一样，就算做不同的子序列。
输入
4
1 1 1 1
输出 15

输入
4
2 2 2 2
输出 7

输入
5
1 2 4 5 8
输出 7
"""
"""有两种方法，状压 DP / 线性基。这里介绍状压 DP 的做法。

统计每个元素的出现次数，记到 cnt 数组中。

70 以内有 19 个质数，考虑状压 DP。
定义 f[x][s] 表示考虑从 1 到 x 中选择子序列的方案数，满足子序列乘积的质因子分解中出现奇数次的质因子的集合是 s。

设 x 出现了 c=cnt[x] 次。
如果选择偶数个 x（这样的方案有 pow(2,c-1) 个），那么 s 不变，有
f[x][s] += f[x-1][s] * pow(2,c-1)
如果选择奇数个 x（这样的方案有 pow(2,c-1) 个），那么 s 变成 s XOR mask，其中 mask 是 x 的质因子分解中出现奇数次的质因子的集合，有
f[x][s XOR mask] += f[x-1][s] * pow(2,c-1)
注：转移方程是用刷表法思考的。

初始值 f[0][0] = 1。
答案为 f[70][0]。

代码实现时，可以用滚动数组优化空间。

代码"""

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]


#       ms
def solve():
    n, = RI()
    a = RILST()
    v2p = [0] * 70
    for i, v in enumerate(PRIMES):
        v2p[v] = i
    pw2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pw2[i] = pw2[i - 1] * 2 % MOD
    masks = [0] * 71
    for i in range(1, 71):
        v = i
        s = 0
        x = 2
        while x * x <= v:
            cnt = 0
            while v % x == 0:
                v //= x
                cnt ^= 1
            if cnt:
                s |= 1 << v2p[x]
            x += 1
        if v != 1:
            s |= 1 << v2p[v]
        masks[i] = s
    cnt = Counter()
    for v in a:
        cnt[masks[v]] += 1

    mask = 1 << 19
    f = [0] * mask
    f[0] = pw2[cnt[0]]
    for k, v in cnt.items():
        if k == 0: continue
        e = pw2[v - 1]
        g = [0] * mask
        for i, v in enumerate(f):
            if v:
                g[i] += e * v % MOD
                g[i ^ k] += e * v % MOD
        f = g
    print((f[0] - 1) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
