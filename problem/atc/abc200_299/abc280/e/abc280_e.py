# Problem: E - Critical Hit
# Contest: AtCoder - Denso Create Programming Contest 2022 Winter(AtCoder Beginner Contest 280)
# URL: https://atcoder.jp/contests/abc280/tasks/abc280_e
# Memory Limit: 1024 MB
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
# MOD = 10**9 + 7
MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc280/tasks/abc280_e

输入 n(1≤n≤2e5) p(0≤p≤100)
怪物的血量为 n。
每次攻击，有 p/100 的概率会对怪物造成 2 点伤害，有 1-p/100 的概率会造成 1 点伤害。
让怪物血量 <= 0，攻击次数的期望是多少？
假设期望等于分数 a/b，你需要输出 a * pow(b, mod-2) % mod，其中 mod=998244353。
输入 3 10
输出 229596204

输入 5 100
输出 3

输入 280 59
输出 567484387
"""
"""期望 DP 入门题。

用 f[i] 表示血量为 i 时的攻击次数的期望。
那么 f[i] = p/100 * (f[i-2]+1) + (1-p/100) * (f[i-1]+1)
初始值 f[0]=0, f[1]=1。
答案为 f[n]。

https://atcoder.jp/contests/abc280/submissions/44230154"""


#       ms
def solve():
    n, p = RI()
    if p == 0:
        return print(n)
    elif p == 100:
        return print((n + 1) // 2)
    x, y = 0, 1
    p = p * pow(100, MOD - 2, MOD)  # p=p/100=p*inv100
    for i in range(2, n + 1):
        x, y = y, (x * p + y * (1 - p) + 1) % MOD  # 从i-2和i-1转移而来，并且次数要+1

    print(y)


#    182   ms
def solve1():
    n, p = RI()
    if p == 0:
        return print(n)
    elif p == 100:
        return print((n + 1) // 2)
    f = [0] * (n + 1)  # f[i] 代表怪物有i血时，攻击次数的期望
    f[1] = 1
    p = p * pow(100, MOD - 2, MOD)  # p=p/100=p*inv100
    for i in range(2, n + 1):
        f[i] = (f[i - 2] * p + f[i - 1] * (1 - p) + 1) % MOD  # 从i-2和i-1转移而来，并且次数要+1

    print(f[-1])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
