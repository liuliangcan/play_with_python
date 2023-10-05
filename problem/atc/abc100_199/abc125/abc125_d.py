# Problem: D - Flipping Signs
# Contest: AtCoder - AtCoder Beginner Contest 125
# URL: https://atcoder.jp/contests/abc125/tasks/abc125_d
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
PROBLEM = """https://atcoder.jp/contests/abc125/tasks/abc125_d

输入 n(2≤n≤1e5) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)。
你可以执行如下操作任意多次：
选择 a 中两个相邻数字，把它们俩都乘上 -1。
输出 sum(a) 的最大值。

思考：如果只能选择 a[i] 和 a[i+2] 呢？（间隔一个数）
思考：如果至多操作 k 次呢？
输入
3
-10 5 -4
输出 19

输入
5
10 -4 -8 -11 3
输出 30

输入
11
-1000000000 1000000000 -1000000000 1000000000 -1000000000 0 1000000000 -1000000000 1000000000 -1000000000 1000000000
输出 10000000000
"""
"""操作不会改变负数个数的奇偶性。
如果有偶数个负数（或者存在 0），那么所有数都可以变成非负数。
如果有奇数个负数，并且没有 0，那么最后会剩下一个负数，我们可以让绝对值最小的那个数是负数。

https://atcoder.jp/contests/abc125/submissions/46144732

如果至多操作 k 次，可以用 DP 思考。"""


#   117    ms
def solve():
    n, = RI()
    a = RILST()
    neg = 0
    for v in a:
        if v < 0:
            neg ^= 1
    a = [abs(v) for v in a]

    print(sum(a) - neg * min(a) * 2)


#   129    ms
def solve1():
    n, = RI()
    a = RILST()
    neg = 0
    for v in a:
        if v < 0:
            neg ^= 1
    a = sorted([abs(v) for v in a])
    if neg:
        return print(sum(a[1:]) - a[0])
    print(sum(a))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
