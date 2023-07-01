# Problem: 三角形数
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/5048/
# Memory Limit: 256 MB
# Time Limit: 5000 ms

import sys
import random

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""


#       ms
def solve1():
    n, = RI()
    for x in range(1, int(n ** 0.5) + 1):
        y = n - x
        a = int(((8 * x + 1) ** 0.5 - 1) / 2)
        b = int(((8 * y + 1) ** 0.5 - 1) / 2)
        if a * (a + 1) // 2 == x and b * (b + 1) // 2 == y:
            return print('YES')
    print('NO')


def solve():
    n, = RI()
    l, r = 1, int((2 * n) ** 0.5)
    while l <= r:
        x = l * (l + 1) // 2 + r * (r + 1) // 2
        if x == n:
            return print('YES')
        elif x < n:
            l += 1
        else:
            r -= 1
    print('NO')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
