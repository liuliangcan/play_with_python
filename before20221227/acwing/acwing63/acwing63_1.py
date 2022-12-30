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


def solve(a,b,n):
    ans = 0
    for x in range(0,a+1):
        y = n-x
        if 0<=y<=b:
            ans += 1


    print(ans)


if __name__ == '__main__':
    if False:
        n = int(input())
        m, n = map(int, input().split())
        s = list(map(int, input().split()))
    a = int(input())
    b = int(input())
    n = int(input())
    solve(a,b,n)
