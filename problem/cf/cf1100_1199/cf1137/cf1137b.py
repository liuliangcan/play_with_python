# Problem: B. Camp Schedule
# Contest: Codeforces - Codeforces Round 545 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1137/B
# Memory Limit: 512 MB
# Time Limit: 1000 ms

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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1137/B

输入两个长度均 ≤5e5 的字符串 s 和字符串 t，只包含 '0' 和 '1'。

重排 s 中的字符，使得 s 中有尽量多的子串等于 t。

输出重排后的 s。
如果有多个答案，输出任意一个。

思考题：如果有多个答案，输出其中字典序最小的。@lympanda
输入
101101
110
输出
110110

输入
10010110
100011
输出
01100011

输入
10
11100
输出
01
"""


class ZFunction:

    def __init__(self, s):
        n = len(s)
        self.z = z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r and z[i - l] < r - i + 1:
                z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1


#    RE in cf   ms
def solve1():
    s, = RS()
    t, = RS()
    scnt = Counter(s)
    tcnt = Counter(t)
    if tcnt['0'] > scnt['0'] or tcnt['1'] > scnt['1']:
        return print(''.join(sorted(s)))
    z = ZFunction(t).z
    ans = [t]
    scnt -= tcnt
    cnt = Counter()
    n = len(t)
    for i, c in enumerate(t):
        if z[i] == n - i:
            while cnt <= scnt:
                ans.append(t[-i:])
                scnt -= cnt
        cnt[t[n - i - 1]] += 1

    while tcnt <= scnt:
        ans.append(t)
        scnt -= tcnt
    ans = '0' * scnt['0'] + ''.join(ans) + '1' * scnt['1']

    print(ans)


#    295   ms
def solve():
    s, = RS()
    t, = RS()
    scnt = Counter(s)
    tcnt = Counter(t)
    if tcnt['0'] > scnt['0'] or tcnt['1'] > scnt['1']:
        return print(''.join(sorted(s)))
    z = ZFunction(t).z
    ans = [t]
    scnt -= tcnt
    cnt = Counter()
    n = len(t)
    for i, c in enumerate(t):
        if z[i] == n - i:
            while cnt['0'] <= scnt['0'] and cnt['1'] <= scnt['1']:
                ans.append(t[-i:])
                scnt -= cnt
        cnt[t[n - i - 1]] += 1

    while tcnt['0'] <= scnt['0'] and tcnt['1'] <= scnt['1']:
        ans.append(t)
        scnt -= tcnt
    ans = '0' * scnt['0'] + ''.join(ans) + '1' * scnt['1']

    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
