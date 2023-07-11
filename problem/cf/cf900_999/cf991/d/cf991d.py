# Problem: D. Bishwock
# Contest: Codeforces - Codeforces Round 491 (Div. 2)
# URL: https://codeforces.com/contest/991/problem/D
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
from math import sqrt, gcd, inf


RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/contest/991/problem/D

输入一个 2 行 n(≤100) 列的棋盘。
用数字 0 表示空格子，大写字母 X 表示一开始就被占据的格子。

你有无数个 L 形状的积木，可以旋转，也就是如下 4 种形状：
XX   XX   0X   X0
X0   0X   XX   XX

积木只能放在空格子上（占据 3 个空格子），不能放在被占据的格子上。积木之间不能重叠。
问：最多可以往棋盘上放多少个积木？
输入
00
00
输出 1

输入
00X00X0XXX0
0XXX0X00X00
输出 4

输入
0X0X0
0X0X0
输出 0

输入 
0XXX0
00000
输出 2
"""


#    92   ms
def solve1():
    a, = RS()
    b, = RS()
    a = 'X' + a
    b = 'X' + b
    n = len(a)
    f = [[-inf] * 4 for _ in range(n)]  # f[i][0/1/2/3] 表示扫完前i列，第i列全空/只占据上排/只占据下排/占满 时，能放的最多数量
    f[0][3] = 0
    for i in range(1, n):
        mask = (a[i] == 'X') | ((b[i] == 'X') << 1)
        f[i][mask] = max(f[i - 1])  # 什么都不放，那么目前状态总数就是前边的总数
        if not mask & 1:
            f[i][mask | 1] = f[i - 1][0] + 1  # 如果第一排没占据，可以放第1种形状，需要从前排全空转移即f[i-1][0]+1
        if not mask & 2:
            f[i][mask | 2] = f[i - 1][0] + 1  # 如果第二排没占据，可以放第4种形状，需要从前排全空转移即f[i-1][0]+1

        if mask == 0:
            f[i][3] = max(f[i - 1][:-1]) + 1  # 如果这排是空的，还可以放第2/3种形状，可以从前排0/1/2三种状态转移过来。
    print(max(f[-1]))


#   62    ms
def solve():
    a, = RS()
    b, = RS()
    f = [-inf] * 4  # f[i][0/1/2/3] 表示扫完前i列，第i列全空/只占据上排/只占据下排/占满 时，能放的最多数量
    f[3] = 0
    for x, y in zip(a, b):
        mask = (x == 'X') | ((y == 'X') << 1)
        g = [-inf] * 4
        g[mask] = max(f)
        if not mask & 1:
            g[mask | 1] = f[0] + 1
        if not mask & 2:
            g[mask | 2] = f[0] + 1
        if mask == 0:
            g[3] = max(f[:-1]) + 1
        f = g
    print(max(f))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
