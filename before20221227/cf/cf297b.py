import collections
import os
import sys
from collections import Counter

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


# def solve(n, m, k, a, b):
#     cnt = collections.defaultdict(int)
#     for i in a:
#         cnt[i] += 1
#     for i in b:
#         cnt[i] -= 1
#     s = 0
#     for i in sorted(cnt.keys(), reverse=True):
#         s += cnt[i]
#         if s > 0:
#             return print('YES')
#
#     print('NO')

def solve(n, m, k, a, b):
    if n > m or any(x > y for x, y in zip(sorted(a, reverse=True), sorted(b, reverse=True))):
        return print('YES')
    print('NO')


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    solve(n, m, k, a, b)
