# Problem: 01背包问题
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/2/
# Memory Limit: 64 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import sys
import heapq
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7

if __name__ == '__main__':
    N, V = RI()
    f = [0] * (V + 1)
    a = []
    for _ in range(N):
        v, w = RI()
        for j in range(V, v - 1, -1):
            f[j] = max(f[j], f[j - v] + w)
    print(f[-1])
