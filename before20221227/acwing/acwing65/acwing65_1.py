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
    input_int = sys.stdin.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7


def solve(n, s):
    # print(n, s)
    f = int(s[n - 1] == 'P')
    ans = 0
    for i in range(n - 2, -1, -1):
        if s[i] == 'P':
            f += 1
        else:
            ans = max(ans, f)
            f = 0

    print(ans)


if __name__ == '__main__':
    T, = RI()
    for _ in range(T):
        n, = RI()
        s, = RS()
        solve(n, s)
