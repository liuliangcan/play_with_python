# Problem: 最大数量
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/description/4869/
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


class DSU:
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.setCount = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            self.edge_size[y] += 1
            return False
        if self.size[x] > self.size[y]:
            x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.setCount -= 1
        return True


#       ms
def solve():
    n, d = RI()
    dsu = DSU(n + 1)
    ans = []
    no_use = 0
    for i in range(1, d + 1):
        x, y = RI()
        if not dsu.union(x, y):
            no_use += 1
        s = [dsu.size[j] for j in range(1, n + 1) if j == dsu.find_fa(j)]
        s.sort(reverse=True)
        z = sum(s[:no_use + 1])

        ans.append(z - 1)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
