import io
import os
import sys
from collections import deque

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7

if __name__ == '__main__':

    def x_add(b):
        x.append(b)


    x = []
    s = 0.0
    k = 0


    def x_query():
        n = len(x)
        if n == 1:
            return print(0.0)
        mx = x[-1]

        global s
        global k
        while k < n - 1 and (s + mx + x[k]) / (k + 2) <= (s + mx) / (k + 1):
            s += x[k]
            k += 1

        print(mx - (s + mx) / (k + 1))


    Q = int(input())
    for _ in range(Q):
        op = list(map(int, input().split()))
        if op[0] == 1:
            x_add(op[1])
        elif op[0] == 2:
            x_query()
