import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from types import GeneratorType

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

# RI = lambda: map(int, sys.stdin.buffer.readline().split())
# RS = lambda: sys.stdin.readline().strip().split()
# RILST = lambda: list(RI())

# input = sys.stdin.buffer.readline
# RI = lambda: map(int, input().split())
# RS = lambda: map(bytes.decode, input().strip().split())
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/274/B

输入 n(≤1e5)，表示一棵有 n 个节点的树。
然后输入 n-1 条边：这条边所连接的两点的编号（从 1 开始）。
最后输入 n 个数，表示每个节点的值 a[i](-1e9≤a[i]≤1e9)。

每次操作，你可以选择一个包含节点 1 的连通块，把所有点的值都 +1 或都 -1。
输出把树上所有节点的值都变为 0 的最少操作次数。
输入
3
1 2
1 3
1 -1 1
输出
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


#  爆栈  RE	 ms
def solve1(n, e, a):
    g = [[] for _ in range(n)]
    for u, v in e:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    def dfs(u, fa):
        # 返回当前子树全0需要的-1次数、+1次数，
        # 每种操作取最大的，因为如果两个孩子v1,v2需要次数分别是a,b(a<b),显然在操作v2时可以选a次带上v1
        m = p = 0
        for v in g[u]:
            if v == fa:
                continue
            minus, plus = dfs(v, u)
            m = max(m, minus)
            p = max(p, plus)
        v = a[u] + p - m
        if v > 0:
            return m + v, p
        return m, p - v

    print(sum(dfs(0, -1)))


# 1184 ms ;py dfs爆栈，使用装饰器+yield强行递归，外部建立辅助dp数组记录返回值--终于明白树形DP为什么是DP
def solve2(n, e, a):
    g = [[] for _ in range(n)]
    for u, v in e:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    f = [[0, 0] for _ in range(n)]  # 每个子树减的次数，加的次数

    @bootstrap
    def dfs(u, fa):
        for v in g[u]:
            if v == fa:
                continue
            yield dfs(v, u)
            f[u][0] = max(f[u][0], f[v][0])
            f[u][1] = max(f[u][1], f[v][1])
        v = a[u] + f[u][1] - f[u][0]
        if v > 0:
            f[u][0] += v
        else:
            f[u][1] -= v
        yield

    dfs(0, -1)
    print(sum(f[0]))


# 1060 ms
def solve(n, e, a):
    g = [[] for _ in range(n)]
    for u, v in e:
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    @bootstrap
    def dfs(u, fa):
        m = p = 0
        for v in g[u]:
            if v == fa:
                continue
            minus, plus = yield dfs(v, u)
            m = max(m, minus)
            p = max(p, plus)
        v = a[u] + p - m
        if v > 0:
            yield m + v, p
        else:
            yield m, p - v

    print(sum(dfs(0, -1)))


if __name__ == '__main__':
    n, = RI()
    e = []
    for _ in range(n - 1):
        e.append(RILST())
    a = RILST()

    solve(n, e, a)
