# Problem: C - AB Substrings
# Contest: AtCoder - diverta 2019 Programming Contest
# URL: https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c
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
PROBLEM = """https://atcoder.jp/contests/diverta2019/tasks/diverta2019_c

输入 n(1≤n≤1e4) 和 n 个字符串，每个字符串只包含大写字母，长度在 [2,10] 中。
将这些字符串按照某种顺序相连，得到字符串 s。
问：s 中最多可以有多少个连续子串是 "AB"？

进阶：子串长度为 3
https://codeforces.com/gym/102431/problem/H
输入
3
ABCA
XBAZ
BAD
输出
2
"""
"""首先把每个字符串中的 AB 个数加到答案中。

接着，如果只考虑以 A 结尾的字符串（个数记作 a），或者以 B 开头的字符串（个数记作 b），每一对拼起来可以得到一个 AB，那么答案额外加上 min(a,b)。
然后，考虑以 B 开头且以 A 结尾的字符串（个数记作 ba），这些字符串可以「插入」到上面拼起来的 AB 之间，那么答案额外加上 ba+min(a,b)。
除了一种特殊情况：ba > 0 且 a = 0 且 b = 0，此时答案只能加上 ba-1。

https://atcoder.jp/contests/diverta2019/submissions/45086403"""

#  110     ms
def solve():
    n, = RI()
    ans = a = b = ab = 0
    for _ in range(n):
        s, = RS()
        ans += s.count('AB')
        if s[0] == 'B' and s[-1] == 'A':
            ab += 1
        elif s[0] == 'B':
            b += 1
        elif s[-1] == 'A':
            a += 1
    if ab and a + b == 0:
        print(ans + ab - 1)
    else:
        print(ans + min(a, b) + ab)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
