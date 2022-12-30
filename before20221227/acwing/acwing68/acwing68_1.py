import collections
import io
import os
import sys
from collections import deque

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


def solve(s):
    if s.count('0') == 0 or s.count('1') == 0:
        return print(0)
    while s and s[0] == '0':
        s = s[1:]
    while s and s[-1] == '0':
        s = s[:-1]
    # print(s)
    print(s.count('0'))


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        s, = RS()

        solve(s)
