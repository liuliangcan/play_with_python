# Problem: D - Count Subtractions
# Contest: AtCoder - AtCoder Beginner Contest 297
# URL: https://atcoder.jp/contests/abc297/tasks/abc297_d
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc297/tasks/abc297_d
输入a,b(1<=a,b<=1e18)
你可以执行以下操作直到a==b
    - 如果a>b,令a=a-b
    - 如果a<b,令b=b-a
问能执行多少次操作
"""
"""发现就是gcd操作，直接用取模模拟即可。
"""


#       ms
def solve():
    a, b = RI()
    if a < b:
        a, b = b, a
    ans = 0
    while b:
        c = a // b
        ans += c
        a %= b

        a, b = b, a
    print(ans - 1)


if __name__ == '__main__':
    solve()
