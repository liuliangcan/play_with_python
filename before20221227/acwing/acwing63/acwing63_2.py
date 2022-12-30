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


def solve(s):
    stack = []
    cnt = 0
    for c in s:
        if stack  and stack[-1] == c:
            cnt += 1
            stack.pop()
        else:
            stack.append(c)

    if cnt & 1:
        print('Yes')
    else:
        print('No')




if __name__ == '__main__':
    if False:
        n = int(input())
        m, n = map(int, input().split())
        s = list(map(int, input().split()))
    s = input()
    solve(s)
