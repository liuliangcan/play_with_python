
import io
import os
import sys
from collections import *

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = sys.stdin.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7


def solve(t):
    d = defaultdict(Counter)
    def padd(x):
        n = len(x)
        y = ''.join(('1' if int(a)&1 else '0') for a in x)
        d[n][y] += 1
    def premove(x):
        n = len(x)
        y = ''.join(('1' if int(a)&1 else '0') for a in x)
        d[n][y] -= 1
    def pquery(x):
        n = len(x)
        b = 0
        while b < n and x[b] == '0':
            b += 1
        y = x[b:]
        ans = d[len(y)][y]
        while len(y)<= 18:
            y = '0'+y
            ans += d[len(y)][y]
        print(ans)

    for _ in range(t):
        a,b = RS()
        if a == '+':
            padd(b)
        elif a =='-':
            premove(b)
        else:
            pquery(b)




if __name__ == '__main__':
    t, = RI()
    solve(t)
