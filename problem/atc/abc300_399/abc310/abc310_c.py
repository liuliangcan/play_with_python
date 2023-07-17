# Problem: C - Reversible
# Contest: AtCoder - freee Programming Contest 2023（AtCoder Beginner Contest 310）
# URL: https://atcoder.jp/contests/abc310/tasks/abc310_c
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
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """有N根棍子，上面粘着几个球。每个球上都写着一个小写英文字母。

对于每个i=1,2,…,N，粘在第i根棍子上的球上的字母由字符串Si表示。具体来说，第i根棍子上粘着的球的数量是字符串Si的长度∣Si∣，而Si是从棍子一端开始的球上的字母序列。

当从一根棍子的一端开始的球上的字母序列等于另一根棍子的一端开始的球上的字母序列时，两根棍子被认为是相同的。更具体地说，对于介于1和N之间的整数i和j，当且仅当Si等于Sj或者其反转时，第i根球和第j根球被认为是相同的。

打印出N根棍子中不同的棍子数量。

约束条件
N是一个整数。
2≤N≤2×10^5
Si是由小写英文字母组成的字符串。
∣Si∣≥1
∑∣Si∣≤2×10^5
"""


#       ms
def solve():
    n, = RI()
    a = set()
    for _ in range(n):
        s, = RS()
        a.add(''.join(min(s,s[::-1])))
    print(len(a))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
