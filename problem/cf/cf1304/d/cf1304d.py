# Problem: D. Shortest and Longest LIS
# Contest: Codeforces - Codeforces Round 620 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1304/D
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
PROBLEM = """http://codeforces.com/problemset/problem/1304/D

输入 t(≤1e4) 表示 t 组数据。所有数据的 n 之和 ≤2e5。

每组数据输入 n(2≤n≤2e5) 和长为 n-1 的字符串 s，仅包含 '<' 和 '>'。

s[i]='<' 表示 a[i]<a[i+1]，
s[i]='>' 表示 a[i]>a[i+1]。

请构造两个 1~n 的排列，符合字符串 s，且第一个数组的 LIS 最短，第二个数组的 LIS 最长。
如果有多种构造方案，输出任意一种。

思考题：在这题的基础上，构造长度恰好为 k 的 LIS。

相似题目：https://leetcode.cn/problems/construct-smallest-number-from-di-string/

"""
"""https://codeforces.com/contest/1304/submission/71173824
https://codeforces.com/contest/1304/submission/197174298

for _ in range(int(input())):
    n, s = input().split()
    n = int(n)
    a = [list(range(n, 0, -1)), list(range(1, n + 1))]
    i = 0
    while i < n - 1:
        h = i
        while i < n - 1 and s[i] == s[h]: i += 1
        b = a[s[h] == '>']
        b[h:i + 1] = b[h:i + 1][::-1]
    print(*a[0])
    print(*a[1])

最短：拆分成若干上升段，那么把最大的数字分配给最左边的上升段，剩余的最大数字分配给第二个上升段，依此类推。

最长：拆分成若干下降段，那么把最小的数字分配给最左边的下降段，剩余的最小数字分配给第二个下降段，依此类推。"""


#       ms
def solve():
    n, s = RS()
    n = int(n)
    a = [list(range(n, 0, -1)), list(range(1, n + 1))]
    r = 0
    while r < n - 1:
        l = r
        while r < n - 1 and s[r] == s[l]:
            r += 1
        b = a[s[l] == '>']
        b[l:r + 1] = b[l:r + 1][::-1]
    print(*a[0])
    print(*a[1])


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
