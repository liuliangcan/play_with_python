# Problem: E - Dice Product 3
# Contest: AtCoder - UNIQUE VISION Programming Contest 2023 Spring(AtCoder Beginner Contest 300)
# URL: https://atcoder.jp/contests/abc300/tasks/abc300_e
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
PROBLEM = """https://atcoder.jp/contests/abc300/tasks/abc300_e

输入 n(1≤n≤1e18)。
你有一个整数 x，初始值为 1。
你有一个六面的骰子，可以等概率地掷出 1~6。

不断重复如下操作，直到 x>=n 为止：
掷骰子。把 x 乘上骰子显示的数字。

问：当你停止操作时，x 恰好等于 n 的概率是多少？
设概率为 a/b，输出 a * pow(b,mod-2) % mod，其中 mod=998244353。
输入 6
输出 239578645

输入 7
输出 0

输入 300
输出 183676961

输入 979552051200000000
输出 812376310
"""
"""定义 P(n) 表示得到 n 的概率。
则有 P(n) = (1/6) * (P(n) + P(n/2) + P(n/3) + P(n/4) + P(n/5) + P(n/6))。
整理得到 P(n) = (1/5) * (P(n/2) + P(n/3) + P(n/4) + P(n/5) + P(n/6))。
如果 n%i>0，则 P(n/i)=0。

由于 n 很大，需要用 map+记忆化搜索。从 n 出发递归到 1。
递归边界：P(1)=1。

注：除以 5 等价于乘以 pow(5,998244353-2)%998244353 = 598946612。

https://atcoder.jp/contests/abc300/submissions/44675024"""


#  406   ms
def solve():
    n, = RI()
    inv5 = pow(5, MOD - 2, MOD)

    @lru_cache(None)
    def f(n):
        if n == 1:
            return 1
        ans = 0
        for i in range(2, 7):
            if n % i == 0:
                ans += f(n // i)
        return ans * inv5 % MOD

    print(f(n))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
