# Problem: E - Apple Baskets on Circle
# Contest: AtCoder - TOYOTA MOTOR CORPORATION Programming Contest 2022(AtCoder Beginner Contest 270)
# URL: https://atcoder.jp/contests/abc270/tasks/abc270_e
# Memory Limit: 1024 MB
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
PROBLEM = """https://atcoder.jp/contests/abc270/tasks/abc270_e

输入 n(≤1e5) k(≤1e12) 和长为 n 的数组 a(0≤a[i]≤1e12, sum(a)≥k)

有 n 堆苹果顺时针围成一圈，第 i 堆有 a[i] 个苹果。
你从第一堆苹果开始吃，每堆吃了一个苹果后，就顺时针走到下一个还有苹果的堆，重复该过程，直到吃了 k 个苹果。
输出此时每堆剩余苹果数。

你能想出两种不同的做法吗？
输入
3 3
1 3 0
输出
0 1 0 
"""


def my_bisect_left(a, x, lo=None, hi=None, key=None):
    """
    由于3.10才能用key参数，因此自己实现一个。
    :param a: 需要二分的数据
    :param x: 查找的值
    :param lo: 左边界
    :param hi: 右边界(闭区间)
    :param key: 数组a中的值会依次执行key方法，
    :return: 第一个大于等于x的下标位置
    """
    if not lo:
        lo = 0
    if not hi:
        hi = len(a) - 1
    else:
        hi = min(hi, len(a) - 1)
    size = hi - lo + 1

    if not key:
        key = lambda _x: _x
    while size:
        half = size >> 1
        mid = lo + half
        if key(a[mid]) < x:
            lo = mid + 1
            size = size - half - 1
        else:
            size = half
    return lo


#   366     ms  排序前缀和+二分nlogn + logklogn
def solve1():
    n, k = RI()
    a = RILST()
    b = sorted(a)
    p = [0]  # 前缀和
    for x in b:
        p.append(p[-1] + x)

    def ok(x):
        pos = bisect_left(b, x)  # 找到x位置
        if p[pos] + (n - pos) * x > k:  # 计算x圈吃了多少个
            return True
        return False

    cnt = my_bisect_left(range(0, max(a) + 1), True, key=ok) - 1  # 二分能完整吃多少圈
    pos = bisect_left(b, cnt)
    k -= p[pos] + (n - pos) * cnt
    for i, v in enumerate(a):  # 最后一圈手动模拟
        v = v - cnt if v - cnt > 0 else 0
        if v and k:
            k -= 1
            v -= 1
        a[i] = v
    print(*a)


#    235   ms  # 排序+贪心
def solve2():
    n, k = RI()
    a = RILST()
    b = sorted(a)
    cnt = 0  # 完整吃的圈数

    for i, v in enumerate(b):  # 贪心的模拟一次吃v圈
        if k > (v - cnt) * (n - i):  # 如果这个数能吃完，计算增量
            k -= (v - cnt) * (n - i)
            cnt = v
        else:
            cnt += k // (n - i)  # 这个数不能完整的吃完，设只能吃v，则后续一定也吃v，向下取整
            k %= (n - i)  # 剩余不能吃掉完整一圈
            break

    for i, v in enumerate(a):
        v = v - cnt if v - cnt > 0 else 0
        if v and k:
            k -= 1
            v -= 1
        a[i] = v
    print(*a)


#   307     ms  直接模拟+二分 nlgk
def solve3():
    n, k = RI()
    a = RILST()

    def ok(x):
        s = 0
        for v in a:
            s += x if x <= v else v
            if s > k:
                return True

        return False

    cnt = my_bisect_left(range(0, max(a) + 1), True, key=ok) - 1  # 二分能完整吃多少圈

    for v in a:
        k -= cnt if cnt <= v else v
    for i, v in enumerate(a):  # 最后一圈手动模拟
        v = v - cnt if v - cnt > 0 else 0
        if v and k:
            k -= 1
            v -= 1
        a[i] = v
    print(*a)


#    175  ms  # 排序+贪心，使劲优化
def solve():
    n, k = RI()
    a = RILST()
    b = sorted(a)
    cnt = 0  # 完整吃的圈数

    for v in b:  # 贪心的模拟一次吃v圈
        d = v - cnt
        if d:
            if k > d * n:  # 如果这个数能吃完，计算增量
                k -= d * n
                cnt = v
            else:
                cnt += k // n  # 这个数不能完整的吃完，设只能吃v，则后续一定也吃v，向下取整
                k %= n  # 剩余不能吃掉完整一圈
                break
        n -= 1

    for i, v in enumerate(a):
        v = v - cnt if v - cnt > 0 else 0
        if v and k:
            k -= 1
            v -= 1
        a[i] = v
    print(*a)


if __name__ == '__main__':
    solve()
