# Problem: B. Peculiar Movie Preferences
# Contest: Codeforces - Codeforces Round 767 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1628/B
# Memory Limit: 512 MB
# Time Limit: 2000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1628/B

输入 t(≤100) 表示 t 组数据。所有数据的 n 之和 ≤1e5。
每组数据输入 n(≤1e5) 和长为 n 的字符串数组 a，每个 a[i] 长度都不超过 3，由小写字母组成。

能否从 a 中找到一个非空子序列 b，使得按顺序连接 b 中的字符串，得到的是一个回文串。
输出 YES 或 NO。

注：子序列不要求连续。

"""
"""输入
6
5
zx
ab
cc
zx
ba
2
ab
bad
4
co
def
orc
es
3
a
b
c
3
ab
cd
cba
2
ab
ab
输出
YES
NO
NO
YES
YES
NO"""


#    124   ms
def solve1():
    n, = RI()
    a = []
    for _ in range(n):
        s, = RS()
        a.append(s)

    p22 = set()  # 长度为2的字符串
    p32 = set()  # 长度为3的字符串前两个字符
    p33 = set()  # 长度为3的字符串

    for s in a:
        if s[0] == s[-1]:
            return print('YES')
        if len(s) == 2:
            t = s[::-1]
            if t in p22 or t in p32:
                return print('YES')
            p22.add(s)
        elif len(s) == 3:
            t = s[::-1]
            if t in p33:
                return print('YES')
            if t[:2] in p22:
                return print('YES')
            p33.add(s)
            p32.add(s[:2])
    print('NO')


#    140   ms
def solve():
    n, = RI()
    a = []
    for _ in range(n):
        s, = RS()
        a.append(s)

    p2233 = set()  # 长度为2/3的字符串
    p32 = set()  # 长度为3的字符串前两个字符

    for s in a:
        if s[0] == s[-1]:
            return print('YES')
        if len(s) == 2:
            t = s[::-1]
            if t in p2233 or t in p32:
                return print('YES')
            p2233.add(s)
        elif len(s) == 3:
            t = s[::-1]
            if t in p2233:
                return print('YES')
            if t[:2] in p2233:
                return print('YES')
            p2233.add(s)
            p32.add(s[:2])
    print('NO')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
