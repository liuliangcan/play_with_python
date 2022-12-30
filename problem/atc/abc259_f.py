# Problem: F - Select Edges
# Contest: AtCoder - AtCoder Beginner Contest 259
# URL: https://atcoder.jp/contests/abc259/tasks/abc259_f
# Memory Limit: 1024 MB
# Time Limit: 3000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

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
PROBLEM = """https://atcoder.jp/contests/abc259/tasks/abc259_f

输入 n(≤3e5)，长为 n 的数组 d，和一颗带权树的 n-1 条边，边权 [-1e9,1e9]。
d[i] 不会超过点 i 的度数。
移除一些边，使得点 i 的度数不超过 d[i]。
输出剩余边的边权之和的最大值。
输入
7
1 2 1 0 2 1 1
1 2 8
2 3 9
2 4 10
2 5 -3
5 6 8
5 7 3
输出 28
"""
"""https://atcoder.jp/contests/abc259/submissions/37624720

写一个树形 DP。

类似打家劫舍 III，子树返回两个数：子树连了至多 d 条边，子树连了至多 d-1 条边（预留一条边给父节点）。
这两个数分别记作 full 和 notFull。

把 full 累加起来，这是一条边都不连的情况。
然后思考：在这个基础上，与哪些子树连边的收益最大？

把边权记作 weight，优先选择 weight + notFull - full 更大的子树，与之连边，这样收益最大。注意这个数有可能是负数，这种情况是不能连边的。
邻项交换法贪心，设需要选择连或不连得两项属性分别为w1,n1,f1 , w2,n2,f2
若连2不连1更加，则有：
    w1+n1+f2<w2+n2+f1
=>  w1+n1-f1<w2+n2-f2
因此优先选择w+n-f更大的树进行连边
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


#   ms
if __name__ == '__main__':
    n, = RI()
    d = RILST()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = RI()
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
    f = [[0, 0] for _ in range(n)]  # f[u]=[x,y] 代表u用子树 [最多连d个(连满)，最多连d-1个(不连满)]的情况，


    # 1262    ms
    @bootstrap
    def dfs(u, fa):
        cs = []  # 可以连的子树
        pride = 0  # 一个子树不连能有多少
        for v, w in g[u]:
            if v != fa:
                yield dfs(v, u)
                full, not_full = f[v]
                pride += full
                if d[u]:
                    diff = w + not_full - full  # 如果要连这个子树要补的差值
                    if diff > 0:
                        cs.append(diff)
        if not d[u]:
            f[u] = [pride, -inf]
        else:
            cs.sort(reverse=True)
            p = pride + sum(cs[:d[u] - 1])
            f[u] = [p, p]
            if len(cs) >= d[u]:
                f[u][0] += cs[d[u] - 1]
            # 实测这段优化意义不大，可能sort占得不多吧
            # if d[u] > len(cs):
            #     p = pride + sum(cs)
            #     f[u] = [p, p]
            # else:
            #     cs.sort(reverse=True)
            #     p = pride + sum(cs[:d[u] - 1])
            #     f[u] = [p, p]
            #     if len(cs) >= d[u]:
            #         f[u][0] += cs[d[u] - 1]
        yield


    # # 1309  ms
    # @bootstrap
    # def dfs(u, fa):
    #     h = []  # 可以连的子树
    #     pride = 0  # 一个子树不连能有多少
    #     for v, w in g[u]:
    #         if v != fa:
    #             yield dfs(v, u)
    #             full, not_full = f[v]
    #             pride += full
    #             diff = w + not_full - full  # 如果要连这个子树要补的差值
    #             if diff > 0:
    #                 if len(h) < d[u]:
    #                     heappush(h, diff)
    #                 else:
    #                     heappushpop(h, diff)
    #
    #     if not d[u]:
    #         f[u] = [pride, -inf]
    #     else:
    #         p = pride + sum(h)
    #         f[u] = [p, p]
    #         if len(h) == d[u]:
    #             f[u][1] -= h[0]
    #     yield

    dfs(0, -1)
    print(f[0][0])
