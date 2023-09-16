# Problem: B - Longest Palindrome
# Contest: AtCoder - Toyota Programming Contest 2023#5（AtCoder Beginner Contest 320）
# URL: https://atcoder.jp/contests/abc320/tasks/abc320_b
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
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """给定一个字符串S。找出S中连续子字符串中最长的回文字符串的长度。请注意，S中总是存在一个连续子字符串是回文字符串。
约束条件：S是一个长度在2到100之间（包括2和100）的字符串，由大写英文字母组成。
"""


#       ms
def solve():
    s, = RS()
    n = len(s)
    ans = 1
    for i in range(n):
        for j in range(i, n):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                ans = max(ans, j - i + 1)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
