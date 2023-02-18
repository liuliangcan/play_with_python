# Problem: 构造新矩阵
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4866/
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


#    5148   ms
def solve():
    RS()
    m, n = RI()
    g = []
    for _ in range(m):
        g.append(RILST())

    # 首先判断若每列都有满足>=x的数，则起码可以选不超过n行出来，满足条件。
    # 这是只要存在一行有用2个>=x得数，就可以少选一行即n-1行。
    # 否则就不行
    def ok(x):
        if all(max(col) >= x for col in zip(*g)) and any(sum(v >= x for v in row) >= 2 for row in g):
            return False
        return True

    print(my_bisect_left(range(10 ** 10), True, key=ok) - 1)


#     4887  ms
def solve1():
    RS()
    m, n = RI()
    g = []
    for _ in range(m):
        g.append(RILST())

    # 相当于给m个[1,0,1,0]布条重叠放，其中1是不透明的。
    # 问最少几根布条叠在一起可以全部不透明。
    # 或者说给m个n位的二进制数，问最少几个数或到一起可以全1。
    # 贪心考虑，优先选1最多的那个数。
    # 选了的1，从剩余数字每个中删掉，对剩余数字依然有1的数字，重新按照1数量排序。
    # 直到选完了或者数字没有了。这时如果没选完就失败。
    # 用set来储存每个数字1的位置，按len排序。每次排序复杂度log(m)
    # 这里的复杂度看似很高，但其实每位上的1最多从每个数中删去1次，复杂度是m*n的。
    def ok(x):
        p = []
        for row in g:
            s = {i for i, v in enumerate(row) if v >= x}
            if s:
                p.append(s)
        if not p:
            return True
        p.sort(key=len)
        c = 0
        t = set(range(n))
        while t and p:
            c += 1
            if c > n - 1:
                return True
            s = p.pop()
            if not s:
                break
            t -= s
            q = []
            for v in p:
                v -= s
                if v:
                    q.append(v)
            p = q
            p.sort(key=len)
        if t:
            return True
        return False

    print(my_bisect_left(range(10 ** 10), True, key=ok) - 1)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
