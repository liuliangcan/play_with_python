import collections
import io
import os
import sys
from collections import deque
from functools import lru_cache

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = sys.stdin.buffer.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7


def solve(n, a, b, s):
    ks = [-1]
    for i, v in enumerate(s):
        if v == '1':
            ks.append(i)
    ks.append(n)
    kong = []
    c = 0
    for i in range(1, k + 2):
        d = ks[i] - ks[i - 1] - 1
        c += d // b
        kong.append((d, ks[i - 1], ks[i]))
    hit = c - a + 1
    print(hit)
    ans = []
    for d,i,j in kong:
        while i+b< j:
            i += b
            ans.append(i)
            if len(ans) == hit:
                print(' '.join(map(lambda x: str(x + 1), ans)))
                return




if __name__ == '__main__':
    n, a, b, k = RI()
    s, = RS()

    solve(n, a, b, s)
