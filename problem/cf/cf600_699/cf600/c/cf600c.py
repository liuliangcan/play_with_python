# Problem: C. Make Palindrome
# Contest: Codeforces - Educational Codeforces Round 2
# URL: https://codeforces.com/problemset/problem/600/C
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
PROBLEM = """https://codeforces.com/problemset/problem/600/C

输入字符串 s，长度不超过 2e5，由小写字母组成。

你可以修改多个 s[i]，使得修改后的 s，通过重新排列，可以得到回文串。
设最少修改 x 次。输出修改 x 次且重排后字典序最小的回文串。
输入 aabc
输出 abba

输入 aabcd
输出 abcba
"""


#  93   ms
def solve1():
    s, = RS()
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] += 1
    l, r = 0, 25
    while l < r:
        while l < r and cnt[l] % 2 == 0:
            l += 1
        while l < r and cnt[r] % 2 == 0:
            r -= 1
        if l < r:
            cnt[l] += 1
            cnt[r] -= 1
            l += 1
            r -= 1
    mid = []
    if cnt[l] & 1:
        mid = [l]
    ans = []
    for i, v in enumerate(cnt):
        ans.extend([i] * (v // 2))

    ans += mid + ans[::-1]
    print(''.join(chr(i + ord('a')) for i in ans))


#   93  ms
def solve():
    s, = RS()
    cnt = [0] * 26
    for c in s:
        cnt[ord(c) - ord('a')] += 1
    l, r = 0, 25
    while l < r:  # 找到两个奇数的位置，把大的变成小的
        while l < r and cnt[l] % 2 == 0:
            l += 1
        while l < r and cnt[r] % 2 == 0:
            r -= 1
        if l < r:
            cnt[l] += 1
            cnt[r] -= 1
            l += 1
            r -= 1
    mid = ''
    if cnt[l] & 1:  # 还残留的最后一个中心奇数位置
        mid = chr(ord('a') + l)
    ans = []
    for i, v in enumerate(cnt):
        ans.extend([chr(ord('a') + i)] * (v // 2))
    ans = ''.join(ans)
    ans += mid + ans[::-1]
    print(ans)


if __name__ == '__main__':
    solve()
