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


def solve(n, m,a):
    def check(aa,b):
        for a in aa:
            cnt = 0
            for x,y in zip(a,b):
                if x!=y:
                    cnt += 1
                    if cnt > 2:
                        return False
        return True

    o = list(range(1, m + 1))
    if check(a,o):
        return print('YES')
    for i in range(m-1):
        for j in range(i+1,m):
            o[i],o[j] = o[j],o[i]
            if check(a,o):
                return print('YES')
            o[i], o[j] = o[j], o[i]
    print('NO')


if __name__ == '__main__':
    n, m = RI()
    a = []
    for _ in range(n):
        a.append(RILST())
    solve(n, m,a)
