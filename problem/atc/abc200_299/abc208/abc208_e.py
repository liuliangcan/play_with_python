# Problem: E - Digit Products
# Contest: AtCoder - AtCoder Beginner Contest 208
# URL: https://atcoder.jp/contests/abc208/tasks/abc208_e
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
PROBLEM = """https://atcoder.jp/contests/abc208/tasks/abc208_e

输入 n(1≤n≤1e18) 和 k(1≤k≤1e9)。
问：有多少个不超过 n 的正整数，其数位乘积不超过 k？
输入 13 2
输出 5
解释 1,2,10,11,12 共 5 个

输入 100 80
输出 99

输入 1000000000000000000 1000000000
输出 841103275147365677
"""
"""数位DP
可能会担心乘积的状态数太多，但其实不会有很多，因为mul一定是数位的乘积，那么因子只会有2 3 5 7。
互相组合，一个宽泛的界就是18^4。
注意，不能根据m<=k剪枝，因为后边可以填0
"""


#       ms
def solve():
    n, k = RI()
    s = str(n)

    @lru_cache(None)
    def f(i, m, is_limit, is_num):
        if i == len(s):
            return int(is_num and m <= k)
        ans = 0
        if not is_num:
            ans += f(i + 1, m, False, False)
        up = int(s[i]) if is_limit else 9
        down = 0 if is_num else 1
        for j in range(down, up + 1):
            ans += f(i + 1, m * j, is_limit and j == up, True)
        return ans

    print(f(0, 1, True, False))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
