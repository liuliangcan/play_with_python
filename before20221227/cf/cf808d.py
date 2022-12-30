import collections
import os
import sys
from collections import Counter

# print(sys.hexversion)
# if os.getenv('LOCALCFTEST'):
#     sys.stdin = open('abcinput.txt')
# else:
#     input = sys.stdin.readline
if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve(n, a):
    s = sum(a)
    if s & 1 or n == 1:
        return print('NO')
    half = s // 2

    def judge(a):
        pre = set()
        p = 0
        for i in a:
            pre.add(i)
            p += i
            if (p - half) in pre:
                return True
        return False

    print('YES' if judge(a) or judge(a[::-1]) else 'NO')


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    solve(n, a)
