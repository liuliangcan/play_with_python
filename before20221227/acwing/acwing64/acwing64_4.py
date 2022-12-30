import io
import os
import sys
from collections import *
from itertools import *
from operator import *

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


def sovle(n, a, b, xs):
    c = Counter()
    d = Counter()
    ans = 0
    for _, vx, vy in xs:
        k = vy - a * vx
        ans += c[k] - d[(vx, vy)]
        c[k] += 1
        d[(vx, vy)] += 1

    print(ans * 2)


if __name__ == '__main__':

    if False:
        n = int(input())
        m, n = map(int, input().split())
        s = list(map(int, input().split()))

    n, a, b = map(int, input().split())
    xs = []
    for _ in range(n):
        xs.append(list(map(int, input().split())))
    sovle(n, a, b, xs)
