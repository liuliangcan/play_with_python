# Problem: E. Nearest Opposite Parity
# Contest: Codeforces - Codeforces Round #605 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1272/E
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1272/E

输入 n(≤2e5) 和长为 n 的数组 a(1≤a[i]≤n)，下标从 1 开始。

从位置 i，你可以移动到位置 i-a[i] 或者 i+a[i]，移动后的位置必须在 [1,n] 内。
定义 d(i) 表示从位置 i 出发，移动到某个位置 j 的最小移动次数，要求 a[i] 和 a[j] 的奇偶性不同。如果不存在这样的 j，则 d(i) 为 -1。
输出 d(1),d(2),...,d(n)。
输入
10
4 5 7 6 7 5 4 4 6 4
输出
1 1 1 2 -1 1 1 3 1 1 
"""
"""反向建图，从终点出发看看能到哪些数字
枚举所有奇数偶数作为终点，它们距离自己是0
"""

#    405  ms
def solve():
    n, = RI()
    a = RILST()
    g = [[] for _ in range(n + 1)]
    even = [-1] * (n + 1)  # 到达偶数的最小距离
    odd = [-1] * (n + 1)  # 到达奇数的最小距离
    q0, q1 = deque(), deque()
    for i, x in enumerate(a, start=1):
        for v in i + x, i - x:
            if 1 <= v <= n:
                g[v].append(i)
        if x & 1:
            q1.append(i)
            odd[i] = 0
        else:
            q0.append(i)
            even[i] = 0

    def bfs(q, dist):
        while q:
            u = q.popleft()
            for v in g[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)

    bfs(q0, even)
    bfs(q1, odd)
    dd = [odd, even]  # 注意反过来
    print(*[dd[v & 1][i] for i, v in enumerate(a, start=1)])


if __name__ == '__main__':
    solve()
