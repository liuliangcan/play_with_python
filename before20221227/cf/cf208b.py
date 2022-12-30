import collections
import os
import sys
from collections import Counter

# print(sys.hexversion)
# if os.getenv('LOCALCFTEST'):
#     sys.stdin = open('abcinput.txt')
# else:
#     input = sys.stdin.readline
from itertools import product

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve(n, s):
    left = [-1] * n
    stack = []
    for i, v in enumerate(s):
        while stack and s[stack[-1]] < v:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)
    right = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
        v = s[i]
        while stack and s[stack[-1]] < v:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    ans = 0
    for v, l, r in zip(s, left, right):
        if l > -1:
            ans = max(ans, v ^ s[l])
        if r < n:
            ans = max(ans, v ^ s[r])

    print(ans)


if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))
    solve(n, s)
