# Problem: 三元组
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/5298/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
from itertools import *

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
PROBLEM = """
"""


#       ms
def solve():
    """
    best = (0~x)+(y~z) - (s-(0~x)-(y~z)) = 2((0~x)+(y~z)) - s
    因此是 找最大的两段和， pre[x] + pre[z] - pre[y],其中x<=y<=z,
    记录y之前最大的pre[x]，z之前最大的pre[x]-pre[y]即可
    """
    n, = RI()
    a = RILST()
    p = 0
    mx = [0, 0, 0, 0]  # best,x,y,z
    px = [0, 0]  # prex,x
    py = [0, 0, 0]  # pre[x]-pre[y]
    for z, v in enumerate(a, start=1):
        p += v
        px = max(px, [p, z])
        py = max(py, [px[0] - p, px[1], z])
        mx = max(mx, [p + py[0], py[1], py[2], z])
        # print(px,py,mx)
    print(*mx[1:])


#       ms
def solve1():
    n, = RI()
    a = RILST()
    pre = [0] + list(accumulate(a))
    mx = [0, 0, 0, 0]
    pm = [(i, v) for i, v in enumerate(pre)]
    for i in range(1, n + 1):
        if pm[i][1] <= pm[i - 1][1]:
            pm[i] = pm[i - 1][:]
    for y in range(0, n):
        for z in range(y, n):
            mx = max(mx, [pre[z + 1] - pre[y] + pm[y][1], pm[y][0], y, z + 1])
    print(*mx[1:])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
