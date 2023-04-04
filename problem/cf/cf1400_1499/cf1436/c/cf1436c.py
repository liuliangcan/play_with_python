# Problem: C. Binary Search
# Contest: Codeforces - Codeforces Round 678 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1436/C
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
from math import sqrt, gcd, inf, perm

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1436/C

输入 n x(1≤x≤n≤1e3) pos(0≤pos≤n-1)。

输出满足以下条件的数组 a 的个数：
1. a 是一个 1~n 的排列，且 a[pos] = x（下标从 0 开始）
2. 调用 BinarySearch(a, x) 的结果是 true。
答案模 1e9+7。
输入 4 1 2
输出 6

输入 123 42 24
输出 824071958
"""


"""https://codeforces.com/contest/1436/submission/96620271

要能二分查找到正确的 x，只需要每一步的 a[middle] 和 x 的大小关系是正确的。
因此统计二分中会遇到几次 middle < pos 的和几次 middle > pos 的。
middle < pos 的情况，a[middle] 一定要 <x
middle > pos 的情况，a[middle] 一定要 >x
这相当于统计 a 中有几个位置上的数一定比 x 小，有几个位置上的数一定比 x 大（注意 a 是一个排列）

设有 L 个比 x 小的数，有 g 个比 x 大的数，那么：
需要从 x-1 个数中选出 L 个数，填到这 L 个二分中的位置上，且可以随意排列，即 A(x-1,L) 种方案
需要从 n-x 个数中选出 g 个数，填到这 g 个二分中的位置上，且可以随意排列，即 A(n-x,g) 种方案
其余的 n-1-L-g 个数任意排列，即 (n-1-L-g)! 种方案
这三个方案数相乘，即为答案（乘法原理）"""

"""
132
"""
#  93     ms
def solve():
    n, x, pos = RI()
    less = 0
    big = 0
    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if mid < pos:
            less += 1
            l = mid + 1
        elif mid > pos:
            big += 1
            r = mid
        else:
            l = mid + 1
    # print(big,less)
    ans = perm(x - 1, less) % MOD * perm(n - x, big) % MOD * perm(n - less - big - 1) % MOD
    print(ans)


if __name__ == '__main__':
    solve()
