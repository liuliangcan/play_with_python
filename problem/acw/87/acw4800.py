# Problem: 移动棋子
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4800/
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
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10**9 + 7


#       ms
def solve():
    x,y = 0,0
    for i in range(5):
        a = RILST()
        for j in range(5):
            if a[j] == 1:
                x,y = i,j
    print( abs(x-2)+abs(y-2))


if __name__ == '__main__':

    solve()
