# Problem: E. Almost Regular Bracket Sequence
# Contest: Codeforces - Codeforces Round #529 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1095/E
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1095/E

输入 n(≤1e6) 和长为 n 的括号字符串 s。

你必须执行如下操作恰好一次：
选择一个下标 i，如果 s[i] 是 ')'，则修改为 '('，反之亦然。

有多少个不同的 i，可以使 s 是一个平衡括号字符串？

思考：如果可以改两个 s[i] 呢？
输入
6
(((())
输出 3

输入
6
()()()
输出 0

输入
1
)
输出 0

输入
8
)))(((((
输出 0
"""


#    140  ms
def solve():
    n, = RI()
    s, = RS()
    if n & 1:
        return print(0)
    suf = [n * 2] * n + [0]
    for i in range(n - 1, -1, -1):
        if s[i] == ')':
            suf[i] = suf[i + 1] + 1
        else:
            suf[i] = suf[i + 1] - 1
            if suf[i] < 0:
                break

    p = ans = 0
    for i, c in enumerate(s):
        if c == '(':
            if 0 < p == suf[i + 1] + 1:
                ans += 1
            p += 1
        else:
            if 0 < suf[i + 1] == p + 1:
                ans += 1
            p -= 1
            if p < 0:
                break
    print(ans)


#     155  ms
def solve1():
    n, = RI()
    s, = RS()
    if n & 1:
        return print(0)
    pre = [0] + [n * 2] * n
    for i, c in enumerate(s):
        if c == '(':
            pre[i + 1] = pre[i] + 1
        else:
            pre[i + 1] = pre[i] - 1
            if pre[i + 1] < 0:
                break
    suf = [n * 2] * n + [0]
    for i in range(n - 1, -1, -1):
        if s[i] == ')':
            suf[i] = suf[i + 1] + 1
        else:
            suf[i] = suf[i + 1] - 1
            if suf[i] < 0:
                break

    ans = 0
    for i, c in enumerate(s):
        if c == '(':
            if 0 < pre[i] == suf[i + 1] + 1:
                ans += 1
        else:
            if 0 < suf[i + 1] == pre[i] + 1:
                ans += 1

    print(ans)


if __name__ == '__main__':
    solve()
