# Problem: E. Kirei Attacks the Estate
# Contest: Codeforces - Codeforces Round 1027 (Div. 3)
# URL: https://codeforces.com/problemset/problem/2114/E
# Memory Limit: 256 MB
# Time Limit: 2000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/2114/E

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(2≤n≤2e5) 和长为 n 的数组 a(1≤a[i]≤1e9)。
然后输入一棵 n 个节点的无向树的 n-1 条边。节点编号从 1 开始。

树根为 1。节点点权记录在数组 a 中。
对于节点 v=1,2,3,...,n，输出从 v 往上的最大交替子段和，即 a[v] - a[parent[v]] + a[parent[parent[v]]] - ... 的最大值。
输入
2
5
4 5 2 6 7
1 2
3 2
4 3
5 1
6
1000000000 500500500 900900900 9 404 800800800
3 4
5 1
2 5
1 6
6 4
输出
4 5 2 9 7
1000000000 1500500096 1701701691 199199209 404 800800800
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    ans = [0] * n
    q = [(0, -1, 0, 0)]
    while q:
        u, fa, pos, neg = q.pop()
        ans[u] = max(a[u], a[u] + neg)

        for v in g[u]:
            if v == fa: continue
            q.append((v, u, max(0, neg) + a[u], max(pos, 0) - a[u]))
    print(*ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
