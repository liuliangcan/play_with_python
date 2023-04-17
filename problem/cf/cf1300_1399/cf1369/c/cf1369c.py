# Problem: C. RationalLee
# Contest: Codeforces - Codeforces Round 652 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1369/C
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
PROBLEM = """https://codeforces.com/problemset/problem/1369/C

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n k(1≤k≤n≤2e5) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)，长为 k 的数组 w(1≤w[i]≤n 且 sum(w)=n)。

把这 n 个数放到 k 个盒子中，使得第 i 个盒子恰好有 w[i] 个数。
定义一个盒子的价值为该盒子中的最大数与最小数之和。特别地，如果一个盒子只有一个数 x，那么这个盒子的价值为 2x。
累加所有盒子的价值，输出它的最大值。
输入
3
4 2
1 13 7 17
1 3
6 2
10 10 10 10 11 11
3 3
4 4
1000000000 1000000000 1000000000 1000000000
1 1 1 1
输出
48
42
8000000000
"""
"""https://codeforces.com/contest/1369/submission/201955758

提示 1：前 k 大的数一定可以作为最大值。且尽量把大的数放在 w[i] = 1 的组中，这样可以计入答案两次。
如果某个前 k 大的数 x 没有作为最大值（其中一个组的最大值是不在前 k 大中的 y），那么把 x 和 y 交换，
如果 x 是某个组的最小值，那么交换后 y 必然也是最小值，此时答案不变。
如果 x 不是某个组的最小值（这个组的最小值是 z）：
       如果 y 交换后变成了最小值，那么答案变大了 x-z。
       如果 y 交换后也不是最小值，那么答案变大了 x-y。
无论如何，这样交换都不会使答案变小，因此前 k 大的数一定可以作为最大值。

提示 2：然后来说最小值。a 的最小值必然要分到某个组中，为了「跳过」尽量多的较小的数，优先把 a 中较小的数分到 w 较大的组中。所以 a 从小到大遍历，w 从大到小遍历。"""


#    420   ms
def solve():
    n, k = RI()
    a = RILST()
    w = RILST()
    a.sort()
    w.sort()
    ans = sum(a[-k:])
    j = 0
    for i in range(k - 1, -1, -1):
        if w[i] > 1:
            ans += a[j]
            j += w[i] - 1
        else:
            ans += a[-i-1]
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
