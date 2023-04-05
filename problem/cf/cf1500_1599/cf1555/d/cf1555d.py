# Problem: D. Say No to Palindromes
# Contest: Codeforces - Educational Codeforces Round 112 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1555/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1555/D

输入 n(≤2e5) m(≤2e5) 和长为 n 的字符串 s，仅包含小写字母 'a' 'b' 'c'，下标从 1 开始。
然后输入 m 个询问，每个询问输入 L R(1≤L≤R≤n)。
对每个询问，要使 s[L] 到 s[R] 中没有长度大于等于 2 的回文子串，至少需要修改多少个字符？注意你只能使用 'a' 'b' 'c' 来修改。
每个询问是独立的，即修改操作不影响其他询问。
输入
5 4
baacb
1 3
1 5
4 5
2 3
输出
1
2
0
1
"""
"""
https://codeforces.com/contest/1555/submission/130420793

手玩一下发现只能由 abc 的某个排列重复多次，才能没有长度大于等于 2 的回文子串。

所以预处理 abc 的 6 种排列对应的修改次数的前缀和，就可以 O(1) 回答每个询问了。
"""


#     405  ms
def solve1():
    n, m = RI()
    s, = RS()
    sel = [
        'abc',
        'acb',
        'bac',
        'bca',
        'cab',
        'cba',
    ]
    pre = [[0] for _ in range(6)]
    for t, p in zip(sel, pre):
        for i, c in enumerate(s):
            p.append(p[-1] + int(c != t[i % 3]))
    for _ in range(m):
        l, r = RI()
        print(min(p[r] - p[l - 1] for p in pre))


#    389   ms
def solve():
    n, m = RI()
    s, = RS()
    sel = [
        'abc',
        'acb',
        'bac',
        'bca',
        'cab',
        'cba',
    ]
    pre = [[0] for _ in range(6)]
    for t, p in zip(sel, pre):
        for i, c in enumerate(s):
            p.append(p[-1] + int(c != t[i % 3]))
    ans = []
    for _ in range(m):
        l, r = RI()
        ans.append(min(p[r] - p[l - 1] for p in pre))
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
