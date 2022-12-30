import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10**9+7
"""https://atcoder.jp/contests/abc168/tasks/abc168_e

输入 n(≤2e5) 和 n 个点 (xi, yi)，范围 [-1e18,1e18]。
你需要从这 n 个点中选出一个非空子集，满足子集中任意两点都有 xi*xj+yi*yj ≠ 0。
子集的大小可以为 1。
输出有多少种不同的选法，模 1e9+7。

注意：可能有重复的点。
输入
3
1 2
-1 1
2 -1
输出 5

输入
10
3 2
3 2
-1 1
2 -1
-3 -9
-8 12
7 7
8 1
8 2
8 4
输出 479
https://atcoder.jp/contests/abc168/submissions/36333766

把点看成向量，公式看成向量不能垂直。

根据对称性，可以把在 x 轴下方或 y 轴负半轴的向量，按原点对称。

然后分别统计在坐标原点的、在第一象限或 x 正半轴的（集合 P）、在第二象限或 y 正半轴的（集合 Q)，
其中 P 和 Q 是有可能垂直的，而 P Q 内部的向量是不会垂直的。

P 中的每个向量和其在 Q 中垂直的向量是不能同时选的，把这些找出来，当成一组，计算方案数。
具体见代码。

根据乘法原理。每组的方案数可以相乘。

最后统计 Q 中剩余向量的方案数；以及零向量的方案数，由于零向量只能选一个，所以方案数是 cnt0；别忘了去掉一个都不选的方案。
"""


#   407  	 ms
def solve(n, m, s, x):
    cnt = Counter(x)
    ss = 0
    p = 1
    for i, v in enumerate(s):
        ss += p * v
        for y in x:
            z = ss - y * p
            cnt[z] += 1
        p *= -1
    print(cnt.most_common(1)[0][1])


if __name__ == '__main__':
    n, m = RI()
    s = RILST()
    x = RILST()

    solve(n, m, s, x)
