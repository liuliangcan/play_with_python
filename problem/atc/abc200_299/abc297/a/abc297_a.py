# Problem: A - Double Click
# Contest: AtCoder - AtCoder Beginner Contest 297
# URL: https://atcoder.jp/contests/abc297/tasks/abc297_a
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc297/tasks/abc297_a
"""


#       ms
def solve():
    n, d = RI()
    a = RILST()
    for i in range(n - 1):
        if a[i + 1] - a[i] <= d:
            return print(a[i + 1])
    print(-1)


if __name__ == '__main__':
    solve()
