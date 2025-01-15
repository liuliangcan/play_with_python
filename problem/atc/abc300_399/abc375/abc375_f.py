# Problem: F - Road Blocked
# Contest: AtCoder - Panasonic Programming Contest 2024（AtCoder Beginner Contest 375）
# URL: https://atcoder.jp/contests/abc375/tasks/abc375_f
# Memory Limit: 1024 MB
# Time Limit: 2500 ms

import sys

from types import GeneratorType
import bisect
import io, os
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from contextlib import redirect_stdout
from itertools import accumulate, combinations, permutations
# combinations(a,k)a序列选k个 组合迭代器
# permutations(a,k)a序列选k个 排列迭代器
from array import *
from functools import lru_cache, reduce
from heapq import heapify, heappop, heappush
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from random import randint, choice, shuffle, randrange
# randint(a,b)从[a,b]范围随机选择一个数
# choice(seq)seq可以是一个列表,元组或字符串,从seq中随机选取一个元素
# shuffle(x)将一个可变的序列x中的元素打乱
from string import ascii_lowercase, ascii_uppercase, digits
# 小写字母，大写字母，十进制数字
from decimal import Decimal, getcontext

# Decimal(s) 实例化Decimal对象,一般使用字符串
# getcontext().prec=100 修改精度
# sys.setrecursionlimit(10**6) #调整栈空间
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc375/tasks/abc375_f

输入 n(2≤n≤300) m(0≤m≤n*(n-1)/2) q(1≤q≤2e5)，表示一个 n 点 m 边的无向图。保证图中无自环和重边。
然后输入 m 条边，每条边输入 x y w(1≤w≤1e9)，表示一条边权为 w 的无向边连接 x 和 y。节点编号从 1 开始。

然后输入 q 个询问，格式如下：
"1 i"：删掉输入的第 i(1≤i≤m) 条边。保证这条边没被删除。
"2 x y"：输出从 x 到 y 的最短距离。如果无法到达，输出 -1。

保证第一种询问不超过 300 个。
"""


#       ms
def solve():
    n, m, q = RI()
    es = []
    dis = [[inf] * n for _ in range(n)]
    for i in range(n):
        dis[i][i] = 0
    for _ in range(m):
        u, v, w = RI()
        u -= 1
        v -= 1
        es.append((u, v, w))
        dis[u][v] = dis[v][u] = w
    qs = []
    for _ in range(q):
        op = RILST()
        qs.append(op)
        if op[0] == 1:
            _, i = op
            u, v, _ = es[i - 1]
            dis[u][v] = dis[v][u] = inf
    for k in range(n):
        for u in range(n):
            for v in range(n):
                dis[u][v] = min(dis[u][v], dis[u][k] + dis[k][v])
    ans = []
    for q in qs[::-1]:
        t, *op = q
        if t == 1:
            u, v, w = es[op[0] - 1]
            # dis[u][v] = dis[v][u] = min(w, dis[v][u])  # 这句没用
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][u] + w + dis[v][j], dis[i][v] + w + dis[u][j])
        else:
            u, v = op
            ans.append(dis[u - 1][v - 1] if dis[u - 1][v - 1] < inf else -1)
    print(*ans[::-1], sep='\n')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
