# Problem: 整除数
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4870/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())

#       ms
def solve():
    n, k = RI()
    n += 1
    print((n + k - 1) // k * k)


if __name__ == '__main__':
    solve()
