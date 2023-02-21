# Problem: C. Longest Regular Bracket Sequence
# Contest: Codeforces - Codeforces Beta Round #5
# URL: https://codeforces.com/problemset/problem/5/C
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/5/C

输入括号字符串 s，长度不超过 1e6。

输出 s 的最长合法括号子串的长度和数量。
如果不存在，输出 0 1。
输入 )((())))(()())
输出 6 2

输入 ))(
输出 0 1
"""
"""令f[i]表示以i位置为结尾的最长合法子串。
显然s[i]=='('则f[i] = 0，否则分类讨论
若 s[i-1]=='(' 则只能这俩匹配，f[i] = f[i-2] + 2
若 f[i-1]>0则说明前边挨着一段合法串，i只能和合法串左边的'('匹配；同时，若匹配成功，新串左边挨着合法串，也要加上。
实现时，在s之前增加一个')'避免讨论边界0
"""


#   248    ms
def solve2():
    s, = RS()
    n = len(s)
    res = {}
    ans = 0

    def calc(s, l='('):
        nonlocal ans, res
        cnt = 0
        p = -1
        for i, c in enumerate(s):
            if c == l:
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    p = i
                    cnt = 0
                    continue
                if cnt == 0:
                    if i - p > ans:
                        ans = i - p
                        res = {p if l == '(' else n - i - 2}
                    elif i - p == ans:
                        res.add(p if l == '(' else n - i - 2)

    calc(s, '(')
    calc(s[::-1], ')')
    print(ans, len(res) if res else 1)


#    278  ms
def solve():
    s, = RS()
    ans, cnt = 0, 1
    st = [-1]
    for i, c in enumerate(s):
        if c == '(':
            st.append(i)
        elif len(st) > 1:
            st.pop()
            p = i - st[-1]
            if ans < p:
                ans = p
                cnt = 1
            elif ans == p > 0:
                cnt += 1
        else:
            st[0] = i
    print(ans, cnt)


#   248    ms
def solve1():
    s, = RS()
    n = len(s)
    s = ')' + s
    ans, cnt = 0, 1
    f = [0] * (n + 1)
    for i, c in enumerate(s[2:], start=2):
        if c == '(':
            continue
        if s[i - 1] == '(':  # 匹配相邻的前一个(
            f[i] = f[i - 2] + 2
        elif f[i - 1] and s[i - f[i - 1] - 1] == '(':  # 匹配合法串前边那  个(
            f[i] = f[i - 1] + 2 + f[i - f[i - 1] - 2]  # 还要加上新串左边那一串合法串
        if ans < f[i]:
            ans = f[i]
            cnt = 1
        elif ans == f[i] > 0:
            cnt += 1

    print(ans, cnt)


if __name__ == '__main__':
    solve()
