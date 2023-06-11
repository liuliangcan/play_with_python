# Problem: E - Art Gallery on Graph
# Contest: AtCoder - KYOCERA Programming Contest 2023（AtCoder Beginner Contest 305）
# URL: https://atcoder.jp/contests/abc305/tasks/abc305_e
# Memory Limit: 1024 MB
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


#   tle    ms
def solve1():
    n, m, k = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    vis = [0] * n
    q = []
    ans = set()
    for _ in range(k):
        p, h = RI()
        vis[p - 1] = h
        ans.add(p - 1)
        q.append((-h, p - 1))
    while q:
        h, u = heappop(q)
        h = -h
        if h < vis[u]: continue
        h -= 1
        for v in g[u]:
            ans.add(v)
            if h <= vis[v]: continue

            vis[v] = h
            if h:
                q.append((-h, v))

    ans = sorted(ans)
    print(len(ans))
    print(*[i + 1 for i in ans])
#       ms
def solve():
    n, m, k = RI()
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    vis = [0] * n
    q = []
    ans = set()
    for _ in range(k):
        p, h = RI()
        vis[p - 1] = h
        ans.add(p - 1)
        q.append((-h, p - 1))
    q.sort()
    while q:
        h, u = heappop(q)
        h = -h
        if h < vis[u]: continue
        h -= 1
        for v in g[u]:
            ans.add(v)
            if h <= vis[v]: continue

            vis[v] = h
            if h:
                heappush(q,(-h,v))

    ans = sorted(ans)
    print(len(ans))
    print(*[i + 1 for i in ans])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
