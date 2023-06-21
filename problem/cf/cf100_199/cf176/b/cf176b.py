# Problem: B. Word Cut
# Contest: Codeforces - Croc Champ 2012 - Round 2
# URL: https://codeforces.com/problemset/problem/176/B
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
PROBLEM = """https://codeforces.com/problemset/problem/176/B

输入两个长度相等的字符串 s 和 t，长度在 [2,1000] 内，只包含小写字母。
然后输入 k(0≤k≤1e5) 表示操作次数。

你需要恰好执行 k 次操作。
每次操作你可以把 s 分割成两个非空字符串 s1 和 s2，然后替换 s = s2 + s1。
把 s 变成 t 有多少种方案？模 1e9+7。
输入
ab
ab
2
输出 1

输入
ababab
ababab
1
输出 2

输入
ab
ba
2
输出 0
"""
"""https://codeforces.com/contest/176/submission/210387377

手玩一下发现操作与「把 s 循环右移（左移）」是一样的。
假设有 c 种不同的循环右移可以让 s=t。那么有 n-c 种不同的循环右移让 s≠t。
定义 f[i] 表示操作 i 次后 s=t，g[i] 表示表示操作 i 次后 s≠t。
那么
f[i] = f[i-1] * (c-1) + g[i-1] * c
g[i] = f[i-1] * (n-c) + g[i-1] * (n-c-1)
初始值 f[0]=(s==t), g[0]=f[0]^1"""


#   186    ms
def solve():
    s, = RS()
    t, = RS()
    k, = RI()
    n = len(s)
    f = int(s == t)
    g = f ^ 1
    s += s
    c = 0
    for i in range(n):
        if t == s[i:i + n]:
            c += 1
    # if not c:
    #     return print(0)
    # print(c)

    for _ in range(k):
        f, g = (f * (c - 1) + g * c) % MOD, (f * (n - c) + g * (n - c - 1)) % MOD

    print(f)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
