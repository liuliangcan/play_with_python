# Problem: Absolute Min Max
# Contest: CodeChef - LTIME84
# URL: https://www.codechef.com/problems/ABSNX?tab=statement
# Memory Limit: 256 MB
# Time Limit: 2500 ms

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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """给一个数组，问有多少个子数组a[l,r]满足a[l]和a[r]是子数组的最小/最大值（前后皆可）
那我们算左端是mn，右端是mx的种类；然后计算一个对称情况（把数组翻转走同逻辑）；这样会计算重复一种情况:mn==mx。可以后边减去一次（分组循环计算相邻相同段）。
如何计算呢？用两个单调栈。
枚举i为合法端的右端点，它作为最大值可以管辖到哪个下标，这可以用单调栈计算。
在i的管辖区域内，有多少个下标可以作为左端点呢？
即，有多少个点作为最小值向右能管辖到i或超过。发现这也是个单调栈可以解决的问题。
然后用BIT储存所有左端点，当单减栈出栈时，也从BIT中移除，即它已经不是合法左端点了（因为它管不到i才会被移除，之后栈里所有剩余左端点都是合法的。回想一下单调栈的出栈更新过程）
因此最终做法：
    两个单调栈mn(计算每个点作为mn向右能管到哪)和mx（计算每个点作为mx向左管到哪）
    一个BIT，储存当前所有合法的左端点，从mn中出来的时候同步从BIT中移除
    对每个i，作为右端点，计算当前BIT中管辖位置之后大小
"""


class BIT:
    def __init__(self, n):
        self.c = [0] * (n + 1)
        self.n = n

    def add(self, i, v):
        while i <= self.n:
            self.c[i] += v
            i += i & -i

    def get(self, i):
        s = 0
        while i:
            s += self.c[i]
            i -= i & -i
        return s

    def query(self, l, r):
        return self.get(r) - self.get(l - 1)


def solve():
    n, = RI()
    a = RILST()

    def f(a):
        bit = BIT(n + 1)
        mn, mx = [], []
        ans = 0
        for i, v in enumerate(a):
            while mn and a[mn[-1]] > v:
                bit.add(mn.pop() + 1, -1)
            mn.append(i)
            bit.add(i + 1, 1)
            while mx and a[mx[-1]] <= v:
                mx.pop()
            l = -1
            if mx:
                l = mx[-1]
            ans += bit.query(l + 2, i + 1)
            mx.append(i)

        return ans

    ans = f(a) + f(a[::-1])

    i = 0
    while i < n:
        i0 = i
        while i < n and a[i] == a[i0]:
            i += 1
        d = i - i0
        ans -= d * (d + 1) // 2
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
