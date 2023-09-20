# Problem: 小美的区间异或和
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65051/D
# Memory Limit: 524288 MB
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
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """贡献法
拆位，每位分别计算，计数1的个数。
遍历到第i个数，如果是1，需要和前边的0发生配对，那么子段右端可以选i~n-1，即n-i个选择。
右边要计算0的个数就很emm,考虑在第i位遇到的0:
它在后续使用使，左端点选0~i位都是可以的，所以其实要计算i+1次，所以每次cnt0+=i+1
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    ans = 0
    for j in range(30):
        x = y = 0
        for i, v in enumerate(a):
            if v >> j & 1:
                ans += ((x * (n - i)) << j) % MOD
                y += i + 1
            else:
                ans += ((y * (n - i)) << j) % MOD
                x += i + 1
            ans %= MOD
    print(ans % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
