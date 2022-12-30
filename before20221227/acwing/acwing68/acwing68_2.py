import collections
import io
import os
import sys
from collections import deque
from functools import lru_cache

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


def solve(n, s):
    # sys.setrecursionlimit(10**5+5)
    # @lru_cache
    # def f(p):
    #     if p == 0 and s[p] == '<':
    #         return True
    #     if p == n-1 and s[p] == '>':
    #         return True
    #     if p == '<':
    #         return f(p-1)
    #     if p == '>':
    #         return f(p+1)
    #     return False
    # ans = 0
    # for i in range(n):
    #     if f(i):
    #         ans += 1
    ans = 0
    for i in range(n):
        if s[i] == '>':
            break
        ans += 1
    for i in range(n-1,-1,-1):
        if s[i] == '<':
            break
        ans += 1
    print(ans)



if __name__ == '__main__':
    n,  = RI()
    s, = RS()

    solve(n, s)
