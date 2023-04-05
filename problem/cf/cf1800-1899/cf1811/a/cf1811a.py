# Problem: A. Insert Digit
# Contest: Codeforces - Codeforces Round 863 (Div. 3)
# URL: https://codeforces.com/contest/1811/problem/A
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/1811/problem/A
输入t(<=1e4)表示t组数据，每组数据：
输入数字n<=2e5和d(0<=d<=9)，然后输入一个n位的数字x。
你可以把d插入到x的任意位置，包括首尾。使得到的数尽可能大。
"""
"""贪心，从左找到第一个小于d的数字，插到它前边"""


#       ms
def solve():
    n, d = RI()
    a, = RS()
    a = list(a)
    for i, c in enumerate(a):
        if d > int(c):
            a.insert(i, str(d))
            break
    else:
        a.append(str(d))
    print(*a, sep='')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
