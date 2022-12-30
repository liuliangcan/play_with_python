import collections
import io
import os
import sys
from bisect import bisect_right
from collections import *
from itertools import accumulate
from math import inf

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


def solve(a):
    # a = 1
    # print(a)
    c = bin(a).count('1')
    # a.bit_count() py3.10以上才有
    print(2**c)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        a, = RI()
        solve(a)

