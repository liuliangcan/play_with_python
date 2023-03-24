# Problem: D. Martial Arts Tournament
# Contest: Codeforces - Educational Codeforces Round 121 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1626/problem/D
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
PROBLEM = """https://codeforces.com/contest/1626/problem/D

输入 t(≤1e4) 表示 t 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(≤2e5) 和长为 n 的数组 a(1≤a[i]≤n)。

你需要选择两个整数 x y (x<y)，把 a 中小于 x 的数分为一组，大于等于 y 的分为一组，其余的分为一组，一共三组。
对每一组，如果组的大小不是 2 的幂次，则增加到最近的 2 的幂次，花费为增量。比如 5 补齐到 8，花费为 8-5=3。如果已经是 2 的幂次，则花费为 0。
计算花费之和的最小值。
输入
4
4
3 1 2 1
1
1
6
2 2 2 1 1 1
8
6 3 6 3 6 3 6 6
输出 
0
2
3
2
"""
"""https://codeforces.com/contest/1626/submission/198620816

提示 1：如果只有两个组，要如何快速枚举？

提示 2：假设第一个组的大小可以是 3 5 6 9 10，那么只需要枚举 3 6 10 这些离 2^k 最近的数。
反证法：假设选的不是离 2^k 最近的数（比如不选 6 选 5），第一个组的花费会变大，另外一个组的花费要么同等变小，要么越过了 2^k 变得更大。所以只需要贪心枚举离 2^k 最近的数。

提示 3：统计 cnt，求 cnt 的前缀和，然后枚举第三个组的大小，转换成两个组的问题。然后枚举并在前缀和上二分查找 2^k，作为第一个组的大小。"""


def f(x):
    if x == 0: return 1
    if x & (x - 1) == 0:
        return 0
    t = 1 << x.bit_length()
    return t - x


#   576    ms
def solve1():
    n, = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    pre = list(accumulate(cnt))

    suf = 0
    ans = f(0) * 2 + f(pre[-1])  # 全分到1组

    for y in range(n, -1, -1):  # 枚举第三组的长度
        suf += cnt[y]
        if cnt[y]:  # 只有长度变化才需要重新计算
            ans = min(ans, f(suf) + f(pre[-1] - suf) + f(0))  # 分两组
            x = 1
            while True:
                p = bisect_right(pre, x, hi=y) - 1  # 找最后一个小于等于x的位置
                if pre[p] + suf >= pre[-1]: break
                ans = min(ans, f(pre[p]) + f(suf) + f(pre[-1] - pre[p] - suf))
                x <<= 1
    print(ans)


#   639 去重排序逆序枚举第三组    ms
def solve2():
    n, = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    pre = list(accumulate(cnt))
    a = sorted(set(a), reverse=True)  #
    suf = 0
    ans = f(0) * 2 + f(pre[-1])  # 全分到1组

    for y in a:  # 枚举第三组的长度
        suf += cnt[y]
        if cnt[y]:  # 只有长度变化才需要重新计算
            ans = min(ans, f(suf) + f(pre[-1] - suf) + f(0))  # 分两组
            x = 1
            lo = 0  # 左端点其实可以继承，但实测不如从0开始快
            while True:
                p = bisect_right(pre, x, lo=lo, hi=y) - 1  # 找最后一个小于等于x的位置
                if pre[p] + suf >= pre[-1]: break  # 超过右端点了
                ans = min(ans, f(pre[p]) + f(suf) + f(pre[-1] - pre[p] - suf))
                x <<= 1
                lo = p
    print(ans)


#   358 列出关键元素  ms
def solve3():
    n, = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    s = 0
    mx = {}
    mn = {}
    for v in cnt:
        s += v
        l = s.bit_length()
        if l not in mx or mx[l] < s:
            mx[l] = s
        if l not in mn or mn[l] > s:
            mn[l] = s
    vs = sorted(set(mx.values()) | set(mn.values()))
    suf = 0
    ans = f(0) * 2 + f(s)  # 全分到1组

    for y in range(n, -1, -1):  # 枚举第三组的长度
        suf += cnt[y]
        if cnt[y]:  # 只有长度变化才需要重新计算
            ans = min(ans, f(suf) + f(s - suf) + f(0))  # 分两组
            for x in vs:  # 枚举第一组的长度
                if x + suf >= s: break
                ans = min(ans, f(x) + f(suf) + f(s - x - suf))
                x <<= 1
    print(ans)


#   311 列出关键元素  ms
def solve():
    n, = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    for v in a:
        cnt[v] += 1
    s = 0
    mx = {}
    for v in cnt:
        s += v
        l = s.bit_length()
        if s & (s - 1) == 0:
            mx[l - 1] = s
        elif l not in mx or mx[l] < s:
            mx[l] = s
    vs = sorted(mx.values())
    suf = 0
    ans = f(0) * 2 + f(s)  # 全分到1组

    for y in range(n, -1, -1):  # 枚举第三组的长度
        suf += cnt[y]
        if cnt[y]:  # 只有长度变化才需要重新计算
            ans = min(ans, f(suf) + f(s - suf) + f(0))  # 分两组
            for x in vs:  # 枚举第一组的长度
                if x + suf >= s: break
                ans = min(ans, f(x) + f(suf) + f(s - x - suf))

    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
