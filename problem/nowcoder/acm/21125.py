# Problem: 践踏
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/problem/21125?&headNav=acm
# Memory Limit: 2 MB
# Time Limit: 21125000 ms

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
PROBLEM = """链接：https://ac.nowcoder.com/acm/problem/21125?&headNav=acm
来源：牛客网

首先给定一个定值k，支持如下操作（在数轴上）
1. 加入一条线段[l,r]
2. 删除一条已经存在的线段
3. 给定x，问有多少个区间包含x+kt，其中t是一个整数变量，即t ∈ Z
比如说当x=2,k=3的时候，区间[7,10]是应该算入答案的，因为x+2k=8，且7 ≤ 8 ≤ 10
如果n=0，那么你只需要输出一行"fafa"然后结束程序即可（注意不输出双引号）
"""


class BIT:
    def __init__(self, n):
        self.c = [0] * (n + 1)
        self.n = n

    def add(self, i, v):
        while i <= self.n:
            self.c[i] += v
            i += -i & i

    def query(self, i):
        s = 0
        while i:
            s += self.c[i]
            i -= -i & i
        return s


#       ms
def solve():
    n, k = RI()
    if n == k == 0:
        return print('fafa')

    def solve0():
        ops = []
        h = []
        for _ in range(n):
            ops.append(RILST())
            h.extend(ops[-1][1:])
        h = sorted(set(h))
        size = len(h)
        bit = BIT(size + 1)
        for t, *op in ops:
            if t < 3:
                v = 1 if t == 1 else -1
                l, r = op
                l, r = bisect_left(h, l) + 1, bisect_left(h, r) + 1
                bit.add(l, v)
                bit.add(r + 1, -v)
            else:
                print(bit.query(bisect_left(h, op[0]) + 1))

    def solvek():
        bit = BIT(k + 1)
        for _ in range(n):
            t, *op = RI()
            if t < 3:
                l, r = op
                v = 1 if t == 1 else -1
                if r - l + 1 >= k:
                    bit.add(1, v)
                    bit.add(k + 1, -v)
                else:
                    l = l % k + 1
                    r = r % k + 1
                    if l <= r:
                        bit.add(l, v)
                        bit.add(r + 1, -v)
                    else:
                        bit.add(l, v)
                        bit.add(k + 1, -v)
                        bit.add(1, v)
                        bit.add(r + 1, -v)
            else:
                print(bit.query(op[0] % k + 1))

    if k:
        solvek()
    else:
        solve0()


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
