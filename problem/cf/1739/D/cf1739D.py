# Problem: D. Reset K Edges
# Contest: Codeforces - Educational Codeforces Round 136 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1739/D
# Memory Limit: 256 MB
# Time Limit: 4000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """http://codeforces.com/problemset/problem/1739/D

输入 t(≤1e4) 表示 t 组数据，每组数据输入 n k(0≤k<n≤2e5)，有一颗 n 个节点的树，输入 n-1 个数 p[2],p[3],...,p[n]，p[i] 表示点 i 的父节点为 p[i]。
所有数据的 n 之和不超过 2e5。
你可以做如下操作至多 k 次：
断开 p[i] 和 i 之间的边，然后在 1 和 i 之间连边。
输出操作后，这颗树的最小高度。
高度的定义为 1 到最远叶子节点的路径的边数。
输入
5
5 1
1 1 2 2
5 2
1 1 2 2
6 0
1 2 3 4 5
6 1
1 2 3 4 5
4 3
1 1 1
输出
2
1
5
3
1
"""


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


#     467   ms
def solve():
    t, = RI()
    for _ in range(t):
        n, k = RI()
        g = [[] for _ in range(n)]
        f = RILST()
        for i, u in enumerate(f, start=1):
            g[u - 1].append(i)  # 明确根，存有向图
        q = deque([0])
        order = []  # 自低向上求树高的顺序：层序逆序
        while q:
            u = q.popleft()
            order.append(u)
            for v in g[u]:
                q.append(v)
        order = order[::-1]
        f = [0] + [x - 1 for x in f]  # f[i]代表i的父节点是f[i]

        def ok(x):
            left = k  # 还能剪几次
            hs = [0] * n  # 初始化高度都是0
            for v in order:
                if hs[v] == x - 1 and f[v]:
                    left -= 1
                else:
                    hs[f[v]] = max(hs[f[v]], hs[v] + 1)

            return left >= 0  # 还余修剪步数说明方案可行

        # ok(x)代表如果最终答案树高是x，是否有可行方案，显然树越高越可行，可以二分
        print(my_bisect_left(range(n), True, lo=1, key=ok))


#     3306    ms
def solve1():
    t, = RI()
    for _ in range(t):
        n, k = RI()
        g = [[] for _ in range(n)]
        f = RILST()
        for i, u in enumerate(f, start=1):
            g[u - 1].append(i)  # 明确根，存有向图

        f = [0] + [x - 1 for x in f]  # f[i]代表i的父节点是f[i]

        def ok(x):
            left = k  # 还能剪几次
            # 自顶向下是错的，wa2
            # @bootstrap
            # def dfs(u, depth=0):
            #     nonlocal left
            #     if left >= 0:
            #         for v in g[u]:
            #             if depth == x:
            #                 left -= 1
            #                 yield dfs(v, 1)
            #             else:
            #                 yield dfs(v, depth + 1)
            #     yield
            hs = [-1] * n  # 初始化高度都是-1，这样如果剪掉了，对父节点也没有影响。

            # 自低向上:遇到x-1高度的子树，就剪掉，连到根上。
            @bootstrap
            def dfs(u):  # dfs(u)计算以u为根的子树高度
                nonlocal left
                if left >= 0:  # 剪枝，left已经小于0了就不用继续了
                    h = 0
                    for v in g[u]:
                        yield dfs(v)
                        # h = max(h,hs[v]+1)
                        if h < hs[v] + 1:
                            h = hs[v] + 1
                    if h == x - 1 and f[u]:
                        # hs[u] = -1  # 剪掉,为了避免对父节点高度产生影响，设置为-1
                        left -= 1
                    else:
                        hs[u] = h
                yield

            dfs(0)
            return left >= 0  # 还余修剪步数说明方案可行

        # ok(x)代表如果最终答案树高是x，是否有可行方案，显然树越高越可行，可以二分
        print(my_bisect_left(range(n), True, lo=1, key=ok))


if __name__ == '__main__':
    solve()
