# Problem: 字符串匹配
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/5151/
# Memory Limit: 256 MB
# Time Limit: 1000 ms
import string
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
PROBLEM = """
"""


#       ms
def solve():
    s, = RS()
    t, = RS()
    a, b = Counter(s), Counter(t)
    x = y = 0
    for c in string.ascii_letters:
        p = min(a[c], b[c])
        x += p
        a[c] -= p
        b[c] -= p
    for c in string.ascii_lowercase:
        y += min(a[c], b[c.upper()])
    for c in string.ascii_uppercase:
        y += min(a[c], b[c.lower()])
    print(x, y)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
