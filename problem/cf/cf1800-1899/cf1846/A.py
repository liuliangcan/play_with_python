# Problem: A. Rudolph and Cut the Rope
# Contest: Codeforces - Codeforces Round 883 (Div. 3)
# URL: https://codeforces.com/contest/1846/problem/A
# Memory Limit: 256 MB
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

if sys.version >= '3.8':  # ACW没有comb
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
PROBLEM = """输入标准输入
输出标准输出
墙上有 n 个钉子，第 i 个钉子离地面高度为 ai 米，一根长度为 bi 米的绳子的一端绑在它上面。所有的钉子都悬挂在不同的高度上。一块糖果同时绑在所有的绳子上，糖果绑在没有绑在钉子上的绳子的末端。

要拿到糖果，你需要将它放到地面上。为了做到这一点，Rudolph 可以一次剪断一些绳子。帮助 Rudolph 找到必须剪断的绳子的最小数量，以取得糖果。

下图展示了第一个测试的示例：
"""


#       ms
def solve():
    n, = RI()
    ans = 0
    for _ in range(n):
        a, b = RI()
        if a > b:
            ans += 1
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
