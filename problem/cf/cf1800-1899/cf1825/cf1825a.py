# Problem: A. LuoTianyi and the Palindrome String
# Contest: Codeforces - Codeforces Round 872 (Div. 2)
# URL: https://codeforces.com/contest/1825/problem/A
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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """输入t组数据，每组数据：
输入一个回文串s。
你需要找到最长的子序列，使这个子序列是非回文的，若找不到则返回-1
"""
"""要么-1，要么n-1
"""


#       ms
def solve():
    s, = RS()
    if len(set(s)) == 1:
        return print(-1)
    print(len(s) - 1)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
