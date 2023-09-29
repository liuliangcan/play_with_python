# Problem: D - aab aba baa
# Contest: AtCoder - AISing Programming Contest 2021（AtCoder Beginner Contest 202）
# URL: https://atcoder.jp/contests/abc202/tasks/abc202_d
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
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc202/tasks/abc202_d

输入 A B(1≤A,B≤30) K。
在所有由恰好 A 个 'a' 和恰好 B 个 'b' 组成的字符串中，输出字典序第 K 小的字符串。
例如 K=1 表示字典序最小的字符串。
K 的范围保证有解。
输入 2 2 4
输出 baab

输入 30 30 118264581564861424
输出 bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaa
"""


#       ms
def solve():
    a, b, k = RI()
    ans = [''] * (a + b)
    for i in range(a + b):
        p = comb(a + b - 1, b)  # 如果当前选a，有几种方案
        if p < k:  # 如果方案数不够用，只能选b
            b -= 1
            ans[i] = 'b'
            k -= p
        else:
            a -= 1
            ans[i] = 'a'
    print(*ans, sep='')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
