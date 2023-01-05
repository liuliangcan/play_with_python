# Problem: A2. Burenka and Traditions (hard version)
# Contest: Codeforces - Codeforces Round #814 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1718/A2
# Memory Limit: 256 MB
# Time Limit: 1000 ms
#
# Powered by CP Editor (https://cpeditor.org)

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1718/A2

输入 t(≤500) 表示 t 组数据，每组数据输入 n(≤1e5) 和长为 n 的数组 a (0≤a[i]<2^30)。
所有数据的 n 之和不超过 1e5。
每次操作你可以把 a 的下标从 L 到 R 的元素都异或一个数，花费为 ceil((R-L+1)/2)。
输出把 a 的所有元素都变成 0 的最小代价。
输入 
7
4
5 5 5 5
3
1 3 2
2
0 0
3
2 5 7
6
1 2 3 3 2 1
10
27 27 34 32 2 31 23 56 52 4
5
1822 1799 57 23 55
输出
2
2
0
2
4
7
4
https://codeforces.com/contest/1718/submission/187981040

提示 1：ceil((R-L+1)/2) 有什么性质？

提示 2：对一个长为 4 的子数组操作，相当于对两个长为 2 的子数组操作；对一个长为 3 的子数组操作，相当于对一个长为 2 和一个长为 1 的子数组操作。换句话说，可以只有长为 1 和 2 的操作。

提示 3：如果有一个子数组的异或和为 0，那么可以用若干长为 2 的子数组来操作，这样花费是 长度-1。

提示 4：答案是 n - 异或和为 0 的不相交子数组的个数。

代码实现时可以用前缀和+哈希表快速判断。
为了保证不相交，在遇到相同前缀和时，需要把哈希表重置为 {0}，前缀和重置为 0。
也可以重置为 {xor}，这样前缀和无需重置。
"""


#   202    ms
def solve():
    t, = RI()
    for _ in range(t):
        n, = RI()
        ans, xor = n, 0
        has = {0}
        for x in RI():
            xor ^= x
            if xor in has:
                ans -= 1
                has = {xor}
            else:
                has.add(xor)
        print(ans)


#   218   ms
def solve2():
    t, = RI()
    for _ in range(t):
        n, = RI()
        a = RILST()
        ans, xor = n, 0
        has = {0}
        for x in a:
            xor ^= x
            if xor in has:
                ans -= 1
                has = {xor}
            else:
                has.add(xor)
        print(ans)


#   tle   ms
def solve1():
    t, = RI()
    for _ in range(t):
        n, = RI()
        a = RILST()
        d = {0: 0}
        if a[0] != 0:
            d = {0: 1, a[0]: 0}

        for i in range(1, n):
            e = {}
            d0 = d[0]
            e[0] = e0 = d0 + (a[i] > 0)
            if a[i] not in e or e[a[i]] > d0:
                e[a[i]] = d0
            x = inf
            if a[i]:
                x = d0
            for k, v in d.items():
                if v >= e0: continue
                z = k ^ a[i]
                if z not in e or e[z] > v + 1:
                    e[z] = v + 1
                if z and v + 1 < x:  # 非0的最小值
                    x = v + 1

            d = {k: v for k, v in e.items() if v <= x or k == 0}
        # print(d)
        print(d[0])


if __name__ == '__main__':
    solve()
