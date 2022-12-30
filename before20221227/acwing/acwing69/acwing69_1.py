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


def solve(x,y,a,b):
    # print(x,y,a,b)
    ans = (y-x)//(a+b)
    if ans * (a+b) == y-x:
        print( ans)
        return
    print(-1)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        x,y,a,b = RI()

        solve(x,y,a,b)
