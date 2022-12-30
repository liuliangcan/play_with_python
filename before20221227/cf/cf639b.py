import os
import sys

import sortedcontainers as sortedcontainers

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 10 ** 9 + 7


def solve(n, d, h):
    if 2 * h < d or (d == 1 and n > 2):
        print(-1)
        return
    if n == 2:
        print(1, 2)
        return
    if h == 1:
        for i in range(2, n + 1):
            print(1, i)
        return

    for i in range(1, h + 1):  # 从1，一条高h的链
        print(i, i + 1)

    if d > h:  # 从1，一条d-h的链
        print(1, h + 2)
        for i in range(h + 2, d + 1):
            print(i, i + 1)
    # 剩下的全挂2上
    for i in range(d + 2, n + 1):
        print(2, i)


if __name__ == '__main__':
    n, d, h = map(int, input().split())
    # print(n,d,h)
    solve(n, d, h)
    a = sortedcontainers.SortedList()
