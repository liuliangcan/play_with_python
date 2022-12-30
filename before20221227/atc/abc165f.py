import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *
from types import GeneratorType

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 998244353
"""https://atcoder.jp/contests/abc165/tasks/abc165_f

输入 n (2≤n≤2e5) 和长为 n 的数组 a (1≤a[i]≤1e9)，表示每个节点的点权。
然后输入一棵树的 n-1 条边（节点编号从 1 开始）。
输出 n 个数，第 i 个数为从节点 1 到节点 i 的路径上点权的 LIS 长度。

注：LIS 指最长上升子序列。
输入
10
1 2 5 3 4 6 7 3 2 4
1 2
2 3
3 4
4 5
3 6
6 7
1 8
8 9
9 10
输出
1
2
3
3
4
4
5
2
2
3
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
#    736 装饰	 ms
def solve1(n, a, es):
    g = [[] for _ in range(n)]
    for u, v in es:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    dp = []
    ans = [1] * n
    @bootstrap
    def dfs(u, fa):
        x = a[u]  # 当前点的点权
        if not dp or x > dp[-1]:  # LIS前缀路径信息在dp里
            dp.append(x)
            p = -1  # 记录dp改变，用于还原：-1代表append，其它代表修改的下标
        else:
            p = bisect_left(dp, x)
            x, dp[p] = dp[p], x  # x没用了，借用来记录dp这个位置本来的值，用于还原
        ans[u] = len(dp)  # 当前路径LIS

        for v in g[u]:
            if v != fa:
                yield dfs(v, u)
        # 回溯还原dp状态
        if p == -1:
            dp.pop()
        else:
            dp[p] = x
        yield
    dfs(0, -1)

    print('\n'.join(map(str, ans)))

# 1092 不装饰，开递归深度
def solve(n, a, es):
    g = [[] for _ in range(n)]
    for u, v in es:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    dp = []
    ans = [1] * n
    def dfs(u, fa):
        x = a[u]  # 当前点的点权
        if not dp or x > dp[-1]:  # LIS前缀路径信息在dp里
            dp.append(x)
            p = -1  # 记录dp改变，用于还原：-1代表append，其它代表修改的下标
        else:
            p = bisect_left(dp, x)
            x, dp[p] = dp[p], x  # x没用了，借用来记录dp这个位置本来的值，用于还原
        ans[u] = len(dp)  # 当前路径LIS

        for v in g[u]:
            if v != fa:
                dfs(v, u)
        # 回溯还原dp状态
        if p == -1:
            dp.pop()
        else:
            dp[p] = x
    sys.setrecursionlimit(n+10)
    dfs(0, -1)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    n, = RI()
    a = RILST()
    es = []
    for _ in range(n - 1):
        es.append(RILST())

    solve(n, a, es)
