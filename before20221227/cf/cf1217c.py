import os
import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

MOD = 10 ** 9 + 7

input = sys.stdin.buffer.readline
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().split())
RILST = lambda: list(RI())



def solve1(s):
    s = list(map(int, s))
    n = len(s)
    f = [0] * (n + 1)
    for i in range(1, n):
        if s[i - 1] == 0:
            f[i] = f[i - 1] + 1
        else:
            f[i] = 0
    ans = 0
    for i, v in enumerate(s):
        if not v:
            continue
        ans += 1
        for j in range(i + 1, min(n, i + 18)):
            v = v * 2 + s[j]
            if v > j - i + 1 + f[i]:
                break
            ans += 1
    print(ans)


def solve(s):
    s = list(map(int, s))
    n = len(s)
    f = 0
    ans = 0
    for i, v in enumerate(s):
        if not v:
            f += 1
            continue
        ans += 1
        for j in range(i + 1, n):
            v = v * 2 + s[j]
            if v > j - i + 1 + f:
                break
            ans += 1
        f = 0
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        s, = RS()
        solve(s)
