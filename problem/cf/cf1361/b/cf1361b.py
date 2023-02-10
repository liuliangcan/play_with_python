# Problem: B. Johnny and Grandmaster
# Contest: Codeforces - Codeforces Round #647 (Div. 1) - Thanks, Algo Muse!
# URL: https://codeforces.com/problemset/problem/1361/B
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
PROBLEM = """https://codeforces.com/problemset/problem/1361/B

输入 t(≤1e5) 表示 t 组数据，每组数据输入 n(≤1e6) p(1≤p≤1e6) 和长为 n 的数组 k(0≤k[i]≤1e6)。所有数据的 n 之和不超过 1e6。

从这 n 个数中选出若干个数（可以为空）组成一组，剩余的数组成另一组。
每组计算 pow(p,k[i]) 之和。
输出这两个和的差值的最小值，对结果模 1e9+7。
输入
4
5 2
2 3 4 4 3
3 1
2 10 1000
4 5
0 1 1 100
1 8
89
输出
4
1
146981438
747093407
"""
"""排序 贪心，栈
p进制思想，为了便于思考，令p=10,排好序的k数组可能是[..,3,3,3,4]
4的贡献是1e4,显然需要10个3才能抵消。
从3的视角来看，累积到10个3能变成1个4。
因此栈中每当累积p个相同值k，就可以变成1个k+1。这个变化一定是连续的（考虑进制）。
由于排序了，因此可以用栈来从大到小模拟这个p进制进位的过程。
"""

#    1949  ms
def solve1():
    n, p = RI()
    a = RILST()
    if p == 1:
        return print(n & 1)
    a.sort()
    target_k = a.pop()
    st = []
    while a:
        k = a.pop()
        while st and st[-1] == [k, p - 1]:
            st.pop()
            k += 1
        if k == target_k:
            if not a:
                return print(0)
            target_k = a.pop()
        elif st and st[-1][0] == k:
            st[-1][1] += 1
        else:
            st.append([k, 1])
    ans = pow(p, target_k, MOD)
    for k, c in st:
        ans -= c * pow(p, k, MOD)
        ans %= MOD

    print(ans % MOD)

#    1887  ms
def solve():
    n, p = RI()
    a = RILST()
    if p == 1:
        return print(n & 1)
    a.sort()
    target_k = a[-1]
    st = []
    i = n - 2
    while i >= 0:
        k = a[i]
        while st and st[-1] == [k, p - 1]:
            st.pop()
            k += 1
        if k == target_k:
            if i == 0:
                return print(0)
            i -= 1
            target_k = a[i]
        elif st and st[-1][0] == k:
            st[-1][1] += 1
        else:
            st.append([k, 1])
        i -= 1
    ans = pow(p, target_k, MOD)
    for k, c in st:
        ans -= c * pow(p, k, MOD)
        ans %= MOD

    print(ans % MOD)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
