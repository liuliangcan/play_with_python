# Problem: D. Balanced Ternary String
# Contest: Codeforces - Codeforces Round 531 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1102/D
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
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb
from types import GeneratorType

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1102/D

输入 n(3≤n≤3e5 且 n=3k) 和长为 n 的字符串 s，只包含 012。
你需要修改 s 中的字符，使得 012 的数量都等于 n/3。
修改次数应当尽量少。
输出修改后的字典序最小的字符串。
输入
3
121
输出 021

输入
6
000000
输出 001122

输入
6
211200
输出 211200

输入
6
120110
输出 120120
"""


#   140    ms
def solve():
    n, = RI()
    k = n // 3
    s, = RS()
    cnt = [0] * 3
    for v in s:
        cnt[int(v)] += 1
    s = list(map(int, s))
    if cnt[0] < k:
        for i, v in enumerate(s):
            if cnt[0] == k:
                break
            if cnt[v] > k:
                cnt[v] -= 1
                cnt[0] += 1
                s[i] = 0
    if cnt[2] < k:
        for i in range(n - 1, -1, -1):
            if cnt[2] == k:
                break
            v = s[i]
            if cnt[v] > k:
                cnt[v] -= 1
                cnt[2] += 1
                s[i] = 2
    if cnt[1] < k:
        pos = [[] for _ in range(3)]
        for i, v in enumerate(s):
            pos[v].append(i)
        t = pos[0][k:] + pos[2][::-1][k:]
        for i in t:
            s[i] = 1
    print(''.join(map(str, s)))


#   140    ms
def solve2():
    n, = RI()
    k = n // 3
    s, = RS()
    cnt = [0] * 3
    for v in s:
        cnt[int(v)] += 1
    s = list(map(int, s))
    for i, v in enumerate(s):
        if cnt[v] > k:
            for j in range(v):
                if cnt[j] < k:
                    cnt[j] += 1
                    cnt[v] -= 1
                    s[i] = j
                    break
    for i in range(n - 1, -1, -1):
        v = s[i]
        if cnt[v] > k:
            for j in range(2, v, -1):
                if cnt[j] < k:
                    cnt[j] += 1
                    cnt[v] -= 1
                    s[i] = j
                    break

    print(''.join(map(str, s)))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
