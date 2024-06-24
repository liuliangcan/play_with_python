# Problem: G - Sum of Tree Distance
# Contest: AtCoder - UNIQUE VISION Programming Contest 2024 Summer (AtCoder Beginner Contest 359)
# URL: https://atcoder.jp/contests/abc359/tasks/abc359_g
# Memory Limit: 1024 MB
# Time Limit: 4000 ms

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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""


#       ms
def solve():
    n, = RI()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)
    a = [0] + RILST()
    cnt, deep = [Counter() for _ in range(n + 1)], [Counter() for _ in range(n + 1)]

    st = [(1, 0, True, 0)]  # root,fa,入栈标记,节点深度
    ans = 0
    while st:
        u, fa, in_, depth = st.pop()
        if in_:
            st.append((u, fa, False, depth))  # 注册自己的出栈动作
            for v in g[u]:
                if v != fa:
                    st.append((v, u, True, depth + 1))  #
        else:
            cnt[u][a[u]] += 1
            deep[u][a[u]] += depth
            for v in g[u]:
                if v != fa:
                    if len(cnt[u]) < len(cnt[v]):
                        cnt[u], cnt[v] = cnt[v], cnt[u]
                        deep[u], deep[v] = deep[v], deep[u]
                    for x, y in deep[v].items():
                        ans += cnt[u][x] * (y - cnt[v][x] * depth) + cnt[v][x] * (deep[u][x] - cnt[u][x] * depth)
                        cnt[u][x] += cnt[v][x]
                        deep[u][x] += y

    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
