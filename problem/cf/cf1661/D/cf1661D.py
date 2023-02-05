# Problem: D. Progressions Covering
# Contest: Codeforces - Educational Codeforces Round 126 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1661/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1661/D

输入 n k(k≤n≤3e5) 和长为 n 的数组 b(1≤b[i]≤1e12)。

初始你有一个长为 n 的数组 a，元素都为 0。
每次操作你要选一个长度恰好等于 k 的连续子数组，从左到右，第1个数加1，第2个数加2，……第k个数加k。
要使每个 a[i] >= b[i]，至少需要操作多少次？
输入
3 3
5 4 6
输出
5

输入
6 3
1 2 3 2 2 3
输出
3

输入
6 3
1 2 4 1 2 3
输出
3

输入
7 3
50 17 81 25 42 39 96
输出
92
"""
"""https://codeforces.com/problemset/submission/1661/190145738

提示 1：倒着思考，这样可以贪心处理每个下标要操作多少次。

提示 2：用差分数组来处理这个等差数列，维护差分的差分。"""
"""
 a[l,r] += v 
= d[l]+=v,d[r+1]-=v

a[l,l+k-1] += 1..k
= d[l,l+k-1] += 1
= d2[l]+=1,d[l+k] -= 1
"""

#   187    ms
def solve():
    n, k = RI()
    b = RILST()
    ans = a = d = 0
    d2 = [0] * n  # 二阶差分
    for i in range(n - 1, -1, -1):
        d += d2[i]  # 一阶差分
        a += d  # a[i]的值
        if a < b[i]:
            k2 = min(i + 1, k)
            times = (b[i] - a + k2 - 1) // k2
            ans += times
            a += times * k2
            if i:
                # 因为维护的是反过来的差分 所以区间加的相当于是k..1,加了times次-1，所以i-1位置是减，后边位置是加；
                # 而k..1其实相当于k..0，这个差值是长一位的所以前边位置要多-1
                d2[i - 1] -= times
                if i > k2:
                    d2[i - k2 - 1] += times
    print(ans)


if __name__ == '__main__':
    solve()
