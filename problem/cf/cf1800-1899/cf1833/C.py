# Problem: C. Vlad Building Beautiful Array
# Contest: Codeforces - Codeforces Round 874 (Div. 3)
# URL: https://codeforces.com/contest/1833/problem/C
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，实测这个快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """输入n和n个正整数a[i]。
构造一个长为n的数组b。
其中b[i]要么等于a[i]，要么等于a[i]-a[j]。其中j随便选1~n。
要求b中所有数据奇偶性相同。
"""
"""分别尝试奇数或者偶数即可。
这题灵神还挖掘了更多性质，其实代码可以很短，只讨论最小的奇数即可。
但比赛中没必要深挖，直接写即可"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    even, odd = [], []
    for v in a:
        if v & 1:
            odd.append(v)
        else:
            even.append(v)
    if not even or not odd:
        return print("YES")
    even.sort()
    odd.sort()

    def try_1():
        for i, v in enumerate(a):
            if v & 1:
                continue
            if odd[0] >= v:
                return False
        return True

    def try_2():
        for i, v in enumerate(a):
            if not v & 1:
                continue
            if odd[0] >= v:
                return False
        return True

    if try_1() or try_2():
        return print("YES")
    print("NO")


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
