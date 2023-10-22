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

if not sys.version.startswith('3.5.3'):  # ACW没有comb
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
# MOD = 998244353
PROBLEM = """https://www.lanqiao.cn/problems/5130/learning/?contest_id=144
由于一个健身计划要2^k天，那么它可以贡献2^(k+1),2^(k+2)..2^(k+x)天，并获取对应倍数的收益，那么所有这种天都可以取最大。
然后把每个天而二进制分解就行。
"""


#       ms
def solve():
    n, m, q = RI()
    t = RILST()
    t = [0] + t + [n + 1]
    ps = []
    for i in range(1, len(t)):
        x = t[i] - t[i - 1] - 1
        if x:
            ps.append(x)

    g = [0] * 21
    for _ in range(m):
        k, s = RI()
        for i in range(k, 21):
            g[i] = max(g[i], s)
            s *= 2
    ans = 0
    for p in ps:
        for i in range(20):
            if p >> i & 1:
                ans += g[i]
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
