# Problem: D. Directed Roads
# Contest: Codeforces - Codeforces Round 369 (Div. 2)
# URL: https://codeforces.com/problemset/problem/711/D
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
from functools import lru_cache, reduce
from types import GeneratorType
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

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/711/D

输入 n(2≤n≤2e5) 和长为 n 的数组 a(1≤a[i]≤n,a[i]≠i)，表示一个 n 点 n 边的无向图（节点编号从 1 开始），点 i 和 a[i] 相连。

你需要给每条边定向（无向变有向），这一共有 2^n 种方案。
其中有多少种方案，可以使图中没有环？
模 1e9+7。
输入
3
2 3 1
输出 6

输入
4
2 1 1 1
输出 8

输入
5
2 4 2 5 3
输出 28
"""
"""https://codeforces.com/contest/711/submission/207047798

前置题目：
2550. 猴子碰撞的方法数
2360. 图中的最长环

遍历每个环，这个环的贡献为 2^环长 - 2。
不在环上的边可以随意取，贡献为 2^边数。
这些贡献相乘即为答案。"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    for i in range(n):
        a[i] -= 1
    ans = 1
    clock = 1
    circle = 0
    time = [0] * n
    for u, t in enumerate(time):
        if t: continue
        start_time = clock
        while u >= 0:
            if time[u]:
                if time[u] >= start_time:
                    p = clock - time[u]
                    circle += p
                    ans = ans * (pow(2, p, MOD) - 2) % MOD
                break
            time[u] = clock
            clock += 1
            u = a[u]
    print(ans * pow(2, n - circle, MOD) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
