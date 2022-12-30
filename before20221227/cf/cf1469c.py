import collections
import os
import sys
from collections import Counter
from itertools import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve1(n, k, hs):
    mn, mx = hs[0], hs[0]  # 当前木板底部位置的上虾界
    for h in hs[1:]:
        mn = max(h, mn - k + 1)
        mx = min(h + k - 1, mx + k - 1)
        if mn > mx:
            return print('NO')

    print('YES' if mn <= hs[-1] <= mx else 'NO')

def solve(n, k, hs):
    mn, mx = hs[0], hs[0]  # 当前木板底部位置的上虾界
    for h in hs[1:]:
        mn = max(h, mn - k + 1)
        mx = min(h + k - 1, mx + k - 1)
        if mn > mx:
            return print('NO')

    print('YES' if mn <= hs[-1] <= mx else 'NO')


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        hs = list(map(int, input().split()))
        solve(n, k, hs)
