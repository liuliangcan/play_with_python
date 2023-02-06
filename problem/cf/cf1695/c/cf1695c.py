# Problem: C. Zero Path
# Contest: Codeforces - Codeforces Round #801 (Div. 2) and EPIC Institute of Technology Round
# URL: https://codeforces.com/problemset/problem/1695/C
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
PROBLEM = """https://codeforces.com/problemset/problem/1695/C

输入 t(≤1e4) 表示 t 组数据，每组数据输入 n(≤1e3) m(≤1e3) 和一个 n 行 m 列的矩阵，元素值只有 -1 和 1。所有数据的 n*m 之和不超过 1e6。

你从矩阵左上出发，走到右下，每步只能向下或者向右。
路径上的元素和能否为 0？输出 YES 或 NO。
输入
5
1 1
1
1 2
1 -1
1 4
1 -1 1 -1
3 4
1 -1 -1 -1
-1 1 1 -1
1 1 1 -1
3 4
1 -1 1 1
-1 1 -1 1
1 -1 1 1
输出
NO
YES
YES
YES
NO
"""
"""https://codeforces.com/contest/1695/submission/192354976

提示 1：交换路径中的相邻两步，比如向右向下变成向下向右，路径和会发生什么变化？

路径和会 +0/+2/-2。

因此，如果 n+m 是偶数，路径和必然为奇数，无法变成 0。此时可以直接输出 NO。

如果 n+m 是奇数，路径和必然为偶数，然后要怎么判断？

提示 2：求出最小路径和以及最大路径和，如果一个 <=0，一个 >=0，根据提示 1，可以通过交换，变成 0。

怎么求？这是个经典 DP，见 https://leetcode.cn/problems/minimum-path-sum/

是不是有点双周赛求轮廓的味道了？"""
"""
今天的题想到了求上下界 但不知道怎么证明上下界包含0就YES  灵神这个思考方法感觉很骚
直观上由于只有+-1 感觉和的可能性应该是连续的 所以想到上下界
但是自己脑测了一下 发现不连续 比如[[1,1],[-1,1]]
看了灵神的题解 应该是分奇偶连续。
"""

#   186    ms
def solve():
    n, m = RI()
    mx = [0] + [-inf] * m
    mn = [0] + [inf] * m
    for _ in range(n):
        a = RILST()
        for j in range(m):
            mx[j + 1] = max(mx[j], mx[j + 1]) + a[j]
            mn[j + 1] = min(mn[j], mn[j + 1]) + a[j]
        mx[0] = -inf
        mn[0] = inf

    if (n + m) & 1 and mn[-1] <= 0 <= mx[-1]:
        return print('YES')
    print('NO')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
