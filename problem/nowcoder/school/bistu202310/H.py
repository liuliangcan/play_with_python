# Problem: 小苯的异或疑惑（easy）
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65319/H
# Memory Limit: 524288 MB
# Time Limit: 4000 ms

import sys
import random
from operator import xor
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
PROBLEM = """
方法1. 拆位计数，由于只看奇偶性且只有加减法，直接用异或代替
方法2. 如果n是奇数，那么每个数会用偶数次，返回0；如果n是偶数，那么美个数会用奇数次，全部异或起来即可。
---
验题发现数据错误：最后5组case n=199999,实际a给了200000个数，不特判就会wa。
"""


#       ms
def solve1():
    n, = RI()
    a = RILST()
    if n & 1:
        return print(0)

    print(reduce(xor, a))


#       ms
def solve():
    n, = RI()
    a = RILST()
    if n != len(a):
        print(n,a[:5])
    ans = 0
    zero = one = 0
    for v in a:
        for j in range(31):
            if v >> j & 1:
                one ^= 1 << j
                ans ^= zero & (1 << j)
            else:
                zero ^= 1 << j
                ans ^= one & (1 << j)
    print(ans)


#       ms
def ff(n, a):
    #       ms
    def f():
        if n & 1:
            return (0)

        return (reduce(xor, a))

    #       ms
    def g():
        ans = 0
        zero = one = 0
        for v in a:
            for j in range(31):
                if v >> j & 1:
                    one ^= 1 << j
                    ans ^= zero & (1 << j)
                else:
                    zero ^= 1 << j
                    ans ^= one & (1 << j)
        return (ans)

    ans1 = f()
    ans2 = g()
    assert ans1 == ans2
    # print(ans1)


#       ms
def solve3():
    n, = RI()
    a = RILST()
    ans = [0] * 31
    zero, one = [0] * 31, [0] * 31
    for v in a:
        for j in range(31):
            if v >> j & 1:
                one[j] += 1
                ans[j] += zero[j]
            else:
                zero[j] += 1
                ans[j] += one[j]
    r = 0
    for v in ans[::-1]:
        r = (r << 1) | (v & 1)
    print(r)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

    # for _ in range(1000):
    #     n = random.randint(1,2*10**5+1)
    #     a = []
    #     for _ in range(n):
    #         a.append(random.randint(0, 10 ** 9 + 1))
    #     ff(n, a)
