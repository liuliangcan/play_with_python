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


def sovle(n, a):
    # pre = list(accumulate(a, func=xor,initial=0))
    pre = [0] + list(accumulate(a, func=xor))
    # print(pre)
    c = Counter()
    ans = 0
    for i, v in enumerate(pre):
        ji = i & 1
        ans += c[(ji, v)]
        c[(ji, v)] += 1

    print(ans)


if __name__ == '__main__':

    if False:
        n = int(input())
        m, n = map(int, input().split())
        s = list(map(int, input().split()))

    n = int(input())
    x = list(map(int, input().split()))
    sovle(n, x)
