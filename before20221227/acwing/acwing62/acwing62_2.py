import collections
import io
import os
import sys
from collections import deque

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve(n, m, a):
    c = collections.Counter()
    d = collections.Counter(range(1, n + 1))
    ans = [0] * m
    for i, v in enumerate(a):
        c[v] += 1
        if len(c) == n:
            c -= d
            ans[i] = 1

    print(''.join(map(str, ans)))


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    solve(n, m, a)
