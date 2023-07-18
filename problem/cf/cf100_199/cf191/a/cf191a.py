# Problem: A. Dynasty Puzzles
# Contest: Codeforces - Codeforces Round 121 (Div. 1)
# URL: https://codeforces.com/problemset/problem/191/A
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/191/A

输入 n(1≤n≤5e5) 和长为 n 的字符串数组 a，只包含小写字母，每个 a[i] 的长度至多为 10。

你需要选择 a 的一个子序列 b，满足 b[i] 的最后一个字母等于 b[i+1] 的第一个字母，且 b[0] 的第一个字母等于 b[-1] 的最后一个字母。这里 b[-1] 表示最后一项。
输出 b 中字符串长度之和的最大值。

注：子序列不要求连续。
输入
3
abc
ca
cba
输出 6

输入
4
vvp
vvp
dam
vvp
输出 0

输入
3
ab
c
def
输出 1
"""


#  998     ms
def solve():
    n, = RI()
    f = [[-inf] * 26 for _ in range(26)]  # f[i][j][k]表示前i个串，j开头k结尾的最大长度
    for _ in range(n):
        s, = RS()
        x, y = ord(s[0]) - ord('a'), ord(s[-1]) - ord('a')
        # print(x, y)
        for j in range(26):
            f[j][y] = max(f[j][y], f[j][x] + len(s))
        f[x][y] = max(f[x][y], len(s))
    # print(f)
    print(max(0, max(f[i][i] for i in range(26))))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
