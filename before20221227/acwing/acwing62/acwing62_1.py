import io
import os
import sys
from collections import deque

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve(n, a):
    m = {v:i for i,v in enumerate(a)}
    a = sorted(list(set(a)))
    if len(a) < 3:
        return print(-1, -1, -1)
    print(m[a[0]]+1, m[a[1]]+1, m[a[2]]+1)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)
