# Problem: C. Restore the Array
# Contest: Codeforces - Codeforces Round 863 (Div. 3)
# URL: https://codeforces.com/contest/1811/problem/C
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
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/1811/problem/C
输入t(<=1e4)表示t组数据，每组数据：
输入n(<=2e5)和长为n-1的数组b(bi<=1e9)。
构造一个长为n的数组a，使对于所有i<n-1,max(a[i],a[i+1])=b[i]
你可以输出任意一个合法答案。
"""
"""贪心构造
最左边的位置显然是最不受影响的，让a[0]=b[0]，那么a[1]就可以是0~b[0]之间任意数，我们希望它空出来不要影响后一个数b[1]，因此填0最佳。
对于b[i]如果前边的a[i]已经填了一个b[i]则他可以不填，取前边的数；如果前边没填数据，且b[i]比前边那个数小，则可以填到a[i]上；否则为了不影响前边只能填到后边的位置。
"""


#       ms
def solve():
    n, = RI()
    b = RILST()
    a = [0] * n
    a[0] = b[0]
    for i in range(1, n - 1):
        if b[i] <= b[i - 1] and a[i] == 0:
            a[i] = b[i]
        elif a[i] == b[i]:
            pass
        else:
            a[i + 1] = b[i]
    print(*a)
    # c = []
    # for i in range(n-1):
    #     c.append(max(a[i],a[i+1]))
    # print(b == c)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
