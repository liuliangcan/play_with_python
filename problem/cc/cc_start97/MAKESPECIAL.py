# Problem: Make It Special
# Contest: CodeChef - START97
# URL: https://www.codechef.com/problems/MAKESPECIAL
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """给n代表一个1~n的排列。
把这个排列里所有数异或上同一个数x，如果排列能变成[y,y+n-1]的连续集合，则认为x是个好数。
给出n和q个询问，每次询问[l,r]区间内有多少个好数
"""
"""打表猜结论：发现 设n二进制有p位，那么x的后p位必须全是0或者全是1.
全0：相当于1~n每个数加了x
全1：相当于1~n每个数取反加x高位
"""


#       ms
def solve():
    n, q = RI()
    p = len(bin(n)) - 2
    mask = (1 << p) - 1  # 用来截取后p位
    for _ in range(q):
        l, r = RI()
        if len(bin(r)) - 1 < p:  # 右边界长度都不够，根本无法让后几位全是0或者1
            print(0)
            continue
        x, y = r >> p, l >> p  # 计算不同高位数量
        a, b = r & mask, l & mask  # 分别截取低位

        if x == y:  # 高位相同，只能看低位是否包含全0、全1
            ans = 0
            if a >= mask:  # 包含全1
                ans += 1
            if b <= 0:  # 包含全0
                ans += 1
            print(ans)
        else:
            ans = (x - y - 1) * 2  # 有这么多高位可以任取到全0全1
            if b == 0:  # 低位如果全0则可以同时取到全0全1
                ans += 2
            else:  # 否则一定可以取到全1
                ans += 1
            if a == mask:  # 同理
                ans += 2
            else:
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
