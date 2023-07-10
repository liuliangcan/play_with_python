# Problem: B. Rudolph and Tic-Tac-Toe
# Contest: Codeforces - Codeforces Round 883 (Div. 3)
# URL: https://codeforces.com/contest/1846/problem/B
# Memory Limit: 256 MB
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
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """Rudolph发明了一个三人玩的井字棋游戏。它有经典的规则，除了第三个玩家使用加号。Rudolph有一个3×3的棋盘，这是游戏结束后的结果。每个棋盘格子可以是叉叉、圆圈、加号或者空。游戏的赢家是能够在水平、垂直或对角线上连成3个相同符号的玩家。

Rudolph想要知道游戏的结果。结果要么是其中一个玩家胜利，要么是平局。保证不会出现多个玩家同时胜利的情况。

输入
第一行是一个整数t（1≤t≤104）——测试用例的数量。

每个测试用例由三行组成，每行有三个字符。字符可以是四种之一："X"代表叉叉，"O"代表圆圈，"+"代表加号，"."代表空格。

输出
对于每个测试用例，如果叉叉赢，输出字符串"X"；如果圆圈赢，输出字符串"O"；如果加号赢，输出字符串"+"；如果平局，输出字符串"DRAW"。
"""


#       ms
def solve():
    g = []
    for _ in range(3):
        s, = RS()
        g.append(s)
    def check(p):
        x = set(p)
        if len(x)==1:
            r = x.pop()
            if r != '.':return r
        return False
    def ok():
        for s in g:
            r = check(s)
            if r:return r
        for s in zip(*g):
            r = check(s)
            if r:return r
        r = check([g[0][0],g[1][1],g[2][2]])
        if r:return r
        r = check([g[0][2],g[1][1],g[2][0]])
        if r:return r
        return 'DRAW'
    print(ok())



if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
