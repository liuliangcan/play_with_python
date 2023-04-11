# Problem: 小d和超级泡泡堂
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/53366/C
# Memory Limit: 524288 MB
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
PROBLEM = """
"""


#       ms
def solve():
    n, m = RI()
    g = []
    start = (0, 0)
    for i in range(n):
        s, = RS()
        g.append(list(s))
        if '@' in s:
            j = s.index('@')
            start = (i, j)
            g[i][j] = '#'
    ans = 0
    q = deque([start])
    while q:
        x, y = q.popleft()
        for a, b in (x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1):
            if 0 <= a < n and 0 <= b < m and g[a][b] != '#':
                if g[a][b] == '!':
                    ans += 1
                g[a][b] = '#'
                q.append((a, b))
    print(ans)


if __name__ == '__main__':
    # t, = RI()
    # for _ in range(t):
    #     solve()
    solve()
