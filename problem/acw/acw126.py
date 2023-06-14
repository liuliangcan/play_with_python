# Problem: 数的进制转换
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/description/126/
# Memory Limit: 64 MB
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
PROBLEM = """
"""


#       ms
def solve():
    p, q, s = RS()
    p, q = int(p), int(q)
    n = len(s)
    a = [0] * n
    for i, v in enumerate(s):
        if v.isdigit():
            a[i] = int(v)
        elif 'A' <= v <= 'Z':
            a[i] = ord(v) - ord('A') + 10
        elif 'a' <= v <= 'z':
            a[i] = ord(v) - ord('a') + 36
    a = a[::-1]

    ans = []
    while n:
        x = 0
        for i in range(n - 1, -1, -1):
            a[i], x = divmod(x * p + a[i], q)

        while not a[n - 1] and n:
            n -= 1
        if 0 <= x <= 9:
            ans.append(str(x))
        elif 10 <= x <= 35:
            ans.append(chr(ord('A') + x - 10))
        elif 36 <= x <= 61:
            ans.append(chr(ord('a') + x - 36))
    print(p, s)
    print(q, ''.join(ans[::-1]))
    print()


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
