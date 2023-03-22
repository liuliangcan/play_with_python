# Problem: B. Ugly Pairs
# Contest: Codeforces - Educational Codeforces Round 64 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1156/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """http://codeforces.com/problemset/problem/1156/B

输入 t(≤100) 表示 t 组数据。每组数据输入一个长度不超过 100 的字符串 s，只包含小写字母。

你需要重排 s 中的字母（或者保持 s 不变），使得 abs(s[i]-s[i+1]) != 1，即任意相邻字母在字母表中不相邻。
输出任意一个符合要求的结果，如果不存在，输出 No answer。
"""
"""https://codeforces.com/contest/1156/submission/197311349

提示 1：想想 s 中没有重复字母要怎么做。

提示 2：s 排序后，按照 ASCII 码的奇偶性分组，设为 x 和 y。

提示 3：看看 x+y 或者 y+x 行不行，如果这样都不行就无解。比如 acb，bac 等。"""


#    93   ms
def solve():
    s, = RS()
    a = sorted(s)
    x, y = [], []
    for c in a:
        if ord(c) & 1:
            x.append(c)
        else:
            y.append(c)
    if not x:
        print(''.join(y))
    elif not y:
        print(''.join(x))
    elif 1 != abs(ord(x[-1]) - ord(y[0])):
        print(''.join(x + y))
    elif 1 != abs(ord(y[-1]) - ord(x[0])):
        print(''.join(y + x))
    else:
        print('No answer')


#    93   ms
def solve1():
    s, = RS()
    cnt = Counter(s)
    a = sorted(cnt.keys())

    def ok(p):
        ans = []
        for c in p:
            if ans and abs(ord(ans[-1]) - ord(c)) == 1:
                return ''
            ans.extend([c] * cnt[c])
        return ''.join(ans)

    print(ok(a[::2] + a[1::2]) or ok(a[1::2] + a[::2]) or 'No answer')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
