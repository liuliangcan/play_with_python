# Problem: D. Bookshelves
# Contest: Codeforces - Avito Code Challenge 2018
# URL: https://codeforces.com/problemset/problem/981/D
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/981/D

输入 n k(1≤k≤n≤50) 和长为 n 的数组 a(0<a[i]<2^50)。
把 a 划分成恰好 k 个非空连续子数组。
把第 i 个子数组记作 b[i]。
最大化 sum(b[0]) AND sum(b[1]) AND ... AND sum(b[k-1])。
这里 AND 表示按位与。

输入
10 4
9 14 28 1 7 13 15 29 2 31
输出 24

输入
7 3
3 14 15 92 65 35 89
输出 64
"""
"""经典位运算最大化贪心。
拆位，从高到低尝试每一位能否赋1，然后check验证。如果可以就加入ans，并带到下一位的验证里。
注意每次是拿当前ans验证，而不是只验证本1位。
验证的思路就是经典的划分型dp，令f(i,k)为从i开始向后能否划分k组，使每组的和都可以覆盖ans里的1
"""
"""涉及到二进制的题目，其中一种思路是拆位。

设最高位为 m。
第 m 位能不能是 1？如果能，那么答案至少是 1<<m。
怎么判断？标准的划分型 DP，定义 f[i][r] 表示 a[0] 到 a[r-1] 能否分成 i 段，且每一段的第 m 位都是 1。

设 target = 1<<m，有
f[i][r] |= f[i-1][l] && ((sum[r] - sum[l]) & target) == target
其中 sum[0] = 0, sum[i] = a[0] + ... + a[i-1]

初始值 f[0][0] = true，如果最后 f[k][n] = true 则说明第 m 位可以是 1。

然后继续判断，第 m-1 位能不能是 1？第 m-2 位能不能是 1？……
注意如果第 m 位是 1，那么在判断其余位的时候，要带着第 m 位是 1 一块判断。

https://codeforces.com/contest/981/submission/213277313"""
#    202   ms
def solve():
    n, k = RI()
    a = RILST()
    ans = 0  #
    for hi in range(55, -1, -1):
        mask = ans | (1 << hi)

        @lru_cache(None)
        def f(i, k):  # 从第i个数开始向后分k组能否满足条件：每组的和都包含mask每位1
            if i == n:
                return k == 0
            if k < 0:  # 分负组
                return False
            if n - i < k:  # 剩下不到k个数
                return False
            s = 0
            for j in range(i, n):
                s += a[j]
                if s & mask == mask:
                    if f(j + 1, k - 1):
                        return True

            return False

        if f(0, k):
            ans = mask
        # f.cache_clear()
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
