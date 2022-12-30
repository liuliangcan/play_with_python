import io
import os
import sys
from collections import deque

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


def sovle(n, x):
    if n == 1:
        print(1)
        print(x[0])
        return
    x.sort()
    s = set(x)
    mx = max(x)
    mn = min(x)
    ans = list()

    def jugde(b):
        if b == 0:
            return False
        return b & (b - 1) == 0

    for i in x:
        j = i
        t = [j]
        k = 0
        while j + 2 ** k <= mx:
            b = j + 2 ** k
            if b in s and all(jugde(abs(b-a)) for a in t):
                t.append(b)
            k += 1
        if len(t) > len(ans):
            ans = t[:]

    print(len(ans))
    print(' '.join(map(str, ans)))


if __name__ == '__main__':

    if False:
        n = int(input())
        m, n = map(int, input().split())
        s = list(map(int, input().split()))

    n = int(input())
    x = list(map(int, input().split()))
    sovle(n, x)
