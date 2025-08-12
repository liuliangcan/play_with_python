# Problem: F. 无产阶级万岁
# Contest: Codeforces - 2023 Hunan Provincal Multi-University Training (Xiangtan University)
# URL: https://codeforces.com/gym/104414/problem/F
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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
PROBLEM = """
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


#    373    ms
def solve():
    n, = RI()
    a = RILST()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    fas = [-1] * n
    order = []
    q = [0]
    while q:
        nq = []
        for u in q:
            order.append(u)
            for v in g[u]:
                if v == fas[u]: continue
                fas[v] = u
                nq.append(v)
        q = nq

    def ok(x):
        mn, mx = a[:], a[:]
        cnt = 0
        for u in order[::-1]:
            if mn[u]: continue
            mn[u], mx[u] = inf, -inf
            for v in g[u]:
                if v == fas[u]: continue
                mn[u] = min(mn[u], mn[v])
                mx[u] = max(mx[u], mx[v])
            if mn[u] + x < mx[u]:
                cnt += 1
                if cnt > 1:
                    return False
                mn[u] = inf
                mx[u] = -inf

        return True

    print(lower_bound(0, 10 ** 6, ok))


#    374    ms
def solve2():
    n, = RI()
    a = RILST()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    fas = [-1] * n
    order = []
    q = [0]
    while q:
        nq = []
        for u in q:
            order.append(u)
            for v in g[u]:
                if v == fas[u]: continue
                fas[v] = u
                nq.append(v)
        q = nq

    def ok(x):
        mn, mx = a[:], a[:]
        cnt = 0
        for u in order[::-1]:
            if mn[u]: continue
            lo, hi = inf, -inf
            for v in g[u]:
                if v == fas[u]: continue
                lo = min(lo, mn[v])
                hi = max(hi, mx[v])
            if lo + x < hi:
                cnt += 1
                mn[u] = inf
                mx[u] = -inf
            else:
                mn[u] = lo
                mx[u] = hi

        return cnt <= 1

    print(lower_bound(0, 10 ** 6, ok))


#    2776    ms
def solve1():
    n, = RI()
    a = RILST()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    def ok(x):
        mn, mx = a[:], a[:]
        cnt = 0

        @bootstrap
        def dfs(u, fa):
            if not mn[u]:
                lo = inf
                hi = -inf
                for v in g[u]:
                    if v == fa: continue
                    yield dfs(v, u)
                    lo = min(lo, mn[v])
                    hi = max(hi, mx[v])
                if hi - lo > x:
                    nonlocal cnt
                    cnt += 1
                    mn[u] = inf
                    mx[u] = -inf
                else:
                    mn[u] = lo
                    mx[u] = hi
            yield

        dfs(0, -1)
        return cnt <= 1

    print(lower_bound(0, 10 ** 6, ok))


#     wa nm的 input第三行说的是无向边，这是人话？ ms
def solve1():
    n, = RI()
    a = RILST()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)

    def ok(x):
        mn, mx = a[:], a[:]
        # mn, mx = [inf]*n,[-inf]*n
        cnt = 0

        @bootstrap
        def dfs(u):
            if not mn[u]:
                lo = inf
                hi = -inf
                for v in g[u]:
                    yield dfs(v)
                    lo = min(lo, mn[v])
                    hi = max(hi, mx[v])
                if hi - lo > x:
                    nonlocal cnt
                    cnt += 1
                    mn[u] = inf
                    mx[u] = -inf
                else:
                    mn[u] = lo
                    mx[u] = hi
            yield

        dfs(0)
        return cnt <= 1

    print(lower_bound(0, 10 ** 6, ok))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
