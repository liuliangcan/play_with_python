# Problem: B - Chessboard
# Contest: AtCoder - AtCoder Beginner Contest 296
# URL: https://atcoder.jp/contests/abc296/tasks/abc296_b
# Memory Limit: 1024 MB
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
PROBLEM = """https://atcoder.jp/contests/abc296/tasks/abc296_b
给你一个8*8的棋盘。由'.*'两种字符组成。
棋盘上只有一个*，找出*的坐标。
其中横坐标从下往上编码为1-8；纵坐标从左到右编码为a-h。
"""


#       ms
def solve():
    g = []
    for _ in range(8):
        s, = RS()
        g.append(s)
    for i in range(8):
        for j, c in enumerate(g[i]):
            if c == '*':
                a = chr(ord('a') + j)
                print(f"{a}{8 - i}")


if __name__ == '__main__':
    solve()
