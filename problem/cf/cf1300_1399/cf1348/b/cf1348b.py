# Problem: B. Phoenix and Beauty
# Contest: Codeforces - Codeforces Round 638 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1348/B
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
PROBLEM = """https://codeforces.com/problemset/problem/1348/B

输入 t(≤50) 表示 t 组数据。
每组数据输入 n k(1≤k≤n≤100) 和长为 n 的数组 a(1≤a[i]≤n)。

你可以在 a 中插入任意多个整数（包括开头和末尾），这些数必须在区间 [1,n] 内。
设插入之后的数组为 b，要求 b 中每个长为 k 的子数组的元素和必须都相同，且 b 的长度不能超过 1e4。

如果无法做到，输出 -1。否则输出数组 b 的长度，以及数组 b。
如果有多个答案，输出任意一个均可。
输入
4
4 2
1 2 2 1
4 3
1 2 2 1
3 2
1 2 3
4 4
4 3 4 2
输出 
5
1 2 1 2 1
4
1 2 2 1
-1
7
4 3 2 1 4 3 2
"""
"""https://codeforces.com/contest/1348/submission/127732185

相关题目：上周六双周赛第三题

突破口在 1e4，构造一个长为 k 的循环节，这个循环节要包含 a 中所有数字。把循环节重复 n 次得到 b，这样可以保证 a 是 b 的一个子序列，且长度至多 n*k 不会超过 1e4。
例如 a=[2,2,3,3]，k=3，构造循环节 [2,3,1]（a 去重，如果不足 k 个，补上 1），重复 4 次得到 [2,3,1,2,3,1,2,3,1,2,3,1]。
如果 a 去重后，元素个数大于 k，则输出 -1。"""


#       ms
def solve():
    n, k = RI()
    a = RILST()
    s = set(a)
    if len(s) > k:
        return print(-1)
    ans = list(s) + [1] * (k - len(s))

    print(n * k)
    for _ in range(n):
        print(*ans, end=' ')
    print()


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
