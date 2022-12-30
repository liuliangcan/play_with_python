import io
import os
import sys
from collections import *

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = sys.stdin.buffer.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RSLST = lambda: list(RS())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7


def solve(n, k, a):
    mxl = max(len(v) for v in a)+1
    power = [1]
    for i in range(mxl):
        power.append(power[-1] * 10)

    def get(a):
        ans = 0
        d = [Counter() for _ in range(mxl)]
        for s in a:
            l = len(s)
            v = int(s)
            for j in range(mxl):
                p = -v * power[j] % k
                ans += d[j][p]
            p = v % k
            d[l][p] += 1
        return ans

    print(get(a) + get(a[::-1]))


if __name__ == '__main__':
    n, k = RI()
    a = RSLST()
    solve(n, k, a)
