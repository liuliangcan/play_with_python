# Problem: 游游的树上边染红
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/66943/D
# Memory Limit: 524288 MB
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
# MOD = 998244353
PROBLEM = """
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


#       ms
def solve():
    n, = RI()
    g = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = RI()
        g[u].append((v, w))
        g[v].append((u, w))
    bs = [0] * (n + 1)  # 当前点没红
    rs = [0] * (n + 1)  # 当前点红

    @bootstrap
    def dfs(u, fa):
        red, blue = 0, 0
        for v, w in g[u]:
            if v == fa: continue
            yield dfs(v, u)
            bs[u] += max(bs[v], rs[v])  # 蓝色的话，子节点可以任意
            red = max(red, w+bs[v]-max(bs[v],rs[v]))  # 选一条边给红,那么它的贡献是子树选成蓝

        rs[u] = bs[u] + red
        yield

    dfs(1, 0)
    # print(rs)
    # print(bs)
    print(max(rs[1], bs[1]))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
