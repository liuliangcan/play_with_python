import io
import os
import sys
from collections import *
from functools import reduce, lru_cache
from itertools import *
from math import gcd, inf

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = sys.stdin.buffer.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())
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


# MX = 200000*200001
def solve1(n, a):
    pre = [0] + list(accumulate(a))

    def calc(i, j):
        return pre[j + 1] - pre[i]

    cur = defaultdict(list)
    ans = 0
    for i, v in enumerate(a):
        nxt = defaultdict(list)
        for k, bs in cur.items():
            p = k * v
            if p > pre[-1]:
                continue
            j = my_bisect_left(pre, -p, lo=0, hi=i - 1, key=lambda x: -calc(x, i))
            if j < i and calc(j, i) == p:
                ans += 1
            for b in bs:
                nxt[p].append(b)
        ans += 1
        nxt[v].append(i)
        cur = nxt

    print(ans)


def solve(n, a):
    pre = [0] + list(accumulate(a))

    def calc(i, j):
        return pre[j + 1] - pre[i]

    cur = set()
    ans = 0
    for i, v in enumerate(a):
        nxt = set()
        for k in cur:
            p = k * v
            if p > pre[-1]:
                continue
            j = my_bisect_left(pre, -p, lo=0, hi=i - 1, key=lambda x: -calc(x, i))
            if j < i and calc(j, i) == p:
                ans += 1
            nxt.add(k)
        ans += 1
        nxt.add(v)
        cur = nxt

    print(ans)


def solve2(n, a):
    pre = [0] + list(accumulate(a))

    def calc(i, j):
        return pre[j + 1] - pre[i]

    cur = {}
    ans = 0
    for i, v in enumerate(a):
        nxt = {}
        for k, (mn, mx) in cur.items():
            p = k * v
            if p > pre[-1]:
                continue
            j = my_bisect_left(pre, -p, lo=mn, hi=mx, key=lambda x: -calc(x, i))
            if j < i and calc(j, i) == p:
                ans += 1
            if k in nxt:
                mn1, mx1 = nxt[k]
                nxt[k] = (min(mn, mn1), max(mx, mx1))
            else:
                nxt[k] = (mx, mx)
        ans += 1
        if v in nxt:
            mn, mx = nxt[v]
            nxt[v] = (min(mn, i), max(mx, i))
        else:
            nxt[v] = (i, i)
        cur = nxt

    print(ans)


if __name__ == '__main__':
    n, = RI()
    a = RILST()
    solve(n, a)
