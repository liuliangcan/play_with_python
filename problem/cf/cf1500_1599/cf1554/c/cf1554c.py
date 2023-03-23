# Problem: C. Mikasa
# Contest: Codeforces - Codeforces Round #735 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1554/C
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
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1554/C

输入 t(≤3e4) 表示 t 组数据，每组数据输入两个整数 n 和 m，均在 [0,1e9] 范围内。

定义数组 a = [n xor 0, n xor 1, n xor 2, ..., n xor m]。
输出不在 a 中的最小非负整数。
输入
5
3 5
4 6
3 2
69 696
123456 654321
输出
4
3
0
640
530866
"""
"""https://codeforces.com/contest/1554/submission/164112524

提示 1：把答案记作 mex，把所有 a[i] 和 mex 都异或上 n，
那么 n xor mex 不能在 [0,1,2,...,m] 中，也就是 n xor mex >= m+1。

提示 2：从高到低考虑 mex 的每一位。

提示 3：如果 n 这一位是 0，m+1 这一位是 1，那么 mex 这一位一定要是 1。
如果 n 这一位是 1，m+1 这一位是 0，那么 mex 这一位可以是 0，此时 n xor mex 是 1，已经大于 m+1 了，退出循环。其余情况 mex 可以是 0，但是不能退出循环。"""


#     171  ms
def solve():
    n, m = RI()
    m += 1
    mex = 0
    for i in range(29, -1, -1):
        x, y = (n >> i) & 1, (m >> i) & 1
        if x > 0 and y == 0:
            break
        if x == 0 and y == 1:
            mex |= 1 << i
    print(mex)


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


#    TLE   ms
def solve1():
    n, m = RI()

    def ok(x):
        for i in range(x, -1, -1):
            if (n ^ i) > m:
                return True
        return False

    return my_bisect_left(range((m + n) * 2), True, key=ok)


if __name__ == '__main__':
    t, = RI()
    ans = []
    for _ in range(t):
        ans.append(solve())
    print(*ans, sep='\n')
