# Problem: E. Masha-forgetful
# Contest: Codeforces - Codeforces Round 764 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1624/E
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
PROBLEM = """https://codeforces.com/problemset/problem/1624/E

输入 t(≤1e4) 表示 t 组数据。所有数据的 n*m 之和 ≤1e6。
每组数据输入 n(≤1e3) m(≤1e3) 和长为 n 的字符串数组 a。
然后再输入一个字符串 s。
所有字符串长度均为 m，仅包含 '0'~'9'。

你需要将 s 划分成若干个长度至少为 2 的子串，且每个子串都是某个 a[i] 的子串（不同子串对应的 a[i] 可以不同）。
如果无法划分，输出 -1；否则输出划分出的子串个数 k，然后输出 k 行，每行三个数字 l r i，表示这个子串等于 a[i] 的子串 [l,r]。注意 l r i 的下标均从 1 开始。注意输出的 k 行要与划分的顺序相同。
如果有多种划分方案，输出任意一种。
"""
"""输入
5

4 8
12340219
20215601
56782022
12300678
12345678

2 3
134
126
123

1 4
1210
1221

4 3
251
064
859
957
054

4 7
7968636
9486033
4614224
5454197
9482268
输出 
3
1 4 1
5 6 2
3 4 3
-1
2
1 2 1
2 3 1
-1
3
1 3 2
5 6 3
3 4 1"""


#    670   ms
def solve():
    RS()
    n, m = RI()
    two, three = {}, {}
    for i in range(1, n + 1):
        s, = RS()
        if m == 1:
            continue
        two[s[:2]] = (1, 2, i)
        for j in range(3, m + 1):
            two[s[j - 2:j]] = (j - 1, j, i)
            three[s[j - 3:j]] = (j - 2, j, i)
    s, = RS()
    if m == 1:
        return print(-1)
    f = [1] + [0] * m
    if s[:2] in two:
        f[2] = 1
    for j in range(3, m + 1):
        if s[j - 2:j] in two and f[j - 2]:
            f[j] = 1
        elif s[j - 3:j] in three and f[j - 3]:
            f[j] = 1
    if not f[-1]:
        return print(-1)

    ans = []
    j = m
    while j > 0:
        if s[j - 2:j] in two and f[j - 2]:
            ans.append(two[s[j - 2:j]])
            j -= 2
        else:
            ans.append(three[s[j - 3:j]])
            j -= 3
    print(len(ans))
    for x in ans[::-1]:
        print(*x)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
