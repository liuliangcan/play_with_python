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

cnt_n = {
    2:1,
    3:7,
    4:4,
    5:5,
    7:8,
    6:9
}
def solve(n):
    # print(n, s)
    if n & 1:
        one = n // 2 - 1
        print('7' + '1'*one)
    else:
        print('1'*(n//2))


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        n, = RI()
        solve(n)
