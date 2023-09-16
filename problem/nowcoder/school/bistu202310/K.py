# Problem: 轻舟已过万重山
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65319/K
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """计算几何 不会不会 
"""


def substraction(a, b):
    # 向量a-向量b
    return a[0] - b[0], a[1] - b[1]


def cross(a, b):
    # 向量叉乘
    return a[0] * b[1] - a[1] * b[0]


def get_area(a, b, c):
    # 向量ab转为向量ac过程中扫过的面积;
    # 返回负代表ac在ab的左边，即逆时针旋转(向左)
    # 返回0代表共线;
    # 返回正代表ac在ab的右边，即顺时针旋转(向右)
    return cross(substraction(b, a), substraction(c, a))


def AnrewHull(points, keep_point_on_edges=False):
    n = len(points)
    if n < 4:
        return points
    points.sort()
    hull = [0]
    used = [False] * n

    def when_pop(a, b, c):  # 如果要保留边上的点，则>才弹栈
        return (get_area(a, b, c) > 0) if keep_point_on_edges else (get_area(a, b, c) >= 0)

    def make_hull(i, limit):
        while len(hull) > limit and when_pop(points[hull[-2]], points[hull[-1]], points[i]):
            used[hull.pop()] = False
        used[i] = True
        hull.append(i)

    for i in range(1, n):
        make_hull(i, 1)
    m = len(hull)
    for i in range(n - 2, -1, -1):
        if not used[i]:
            make_hull(i, m)
    # hull.pop()
    return [points[i] for i in hull[:-1]]


def calc_triangle_area(a, b, c=(0, 0)):
    # 给三个点，求这三个点组成的三角形面积
    return abs(a[0] * b[1] + b[0] * c[1] + c[0] * a[1] - a[0] * c[1] - b[0] * a[1] - c[0] * b[1]) / 2


#     wa  ms
def solve():
    n, = RI()
    a = []
    for _ in range(n):
        a.append(RILST())
    p = AnrewHull(sorted(a))

    if len(p) < 2:
        return print(0)
    ans = calc_triangle_area(p[0], p[-1])
    j, k, n = 0, 1, len(p)
    while calc_triangle_area(p[j], p[k]) < calc_triangle_area(p[j], p[(k + 1) % n]):
        k = (k + 1) % n
    kk = (k + 1) % n
    while j != kk:
        ans = max(ans, calc_triangle_area(p[j], p[k]))
        while calc_triangle_area(p[j], p[k]) < calc_triangle_area(p[j], p[(k + 1) % n]):
            k = (k + 1) % n
        j = (j + 1) % n
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
