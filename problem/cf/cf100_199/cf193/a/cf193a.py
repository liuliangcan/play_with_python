# Problem: A. Cutting Figure
# Contest: Codeforces - Codeforces Round 122 (Div. 1)
# URL: https://codeforces.com/problemset/problem/193/A
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

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
PROBLEM = """https://codeforces.com/problemset/problem/193/A

输入 n m(1≤n,m≤50) 和一个 n 行 m 列的网格图，仅包含 '#' 和 '.'。
输入保证图中任意两个 '#' 都可以通过四方向移动互相到达（连通图）。
输入保证至少有一个 '#'。
你需要把尽量少的 '#' 修改成 '.'，使得网格图不连通。
如果无法做到，输出 -1，否则输出最少修改次数。
注：规定空集（没有 '#'）视作连通图，只有一个 '#' 也视作连通图。

相似题目：2556. 二进制矩阵中翻转最多一次使路径不连通
输入
5 4
####
#..#
#..#
#..#
####
输出 2

输入
5 5
#####
#...#
#####
#...#
#####
输出 2
"""
"""脑筋急转弯，答案要么是1要么是2.要么是-1.
如果只有1个或者2个#，他们是相连的，那么一定不能修改。
3个及以上可以修改。
图里至少有一个'角'，这个角位置的方块，最多只和两个相邻，那么移除这两个即可。
所以只需暴力尝试枚举移除每个位置试试即可。
"""
"""脑筋急转弯。
如果 # 个数小于 3，那么无法分成多个连通块，输出 -1。
否则有解（注意原图是连通的）。
对于角落的 #，可以把相邻的两个 # 改成 . 使得图不连通，所以至多操作 2 次。
如果角落没有 #，一定存在一个边上的 # 至多有两个 . 邻居，所以也至多操作 2 次。
那么只需要判断能否操作 1 次使图不连通。
代码写的是 O(n^2m^2) 的暴力，可以用 Tarjan 割点做到 O(nm)。

https://codeforces.com/contest/193/submission/215507875

相似题目：2556. 二进制矩阵中翻转最多一次使路径不连通"""

#    1464   ms
def solve():
    n, m = RI()
    g = []
    cnt = 0
    for _ in range(n):
        s, = RS()
        cnt += s.count('#')
        g.append(s)
    if cnt <= 2:
        return print(-1)

    def inside(x, y):
        return 0 <= x < n and 0 <= y < m

    tag = [[c == '#' for c in row] for row in g]

    def check(x, y):
        cnt = 0
        f = [row[:] for row in tag]
        f[x][y] = False

        def bfs(i, j):
            q = deque([(i, j)])
            f[i][j] = False
            while q:
                c, d = q.popleft()
                for a, b in (c, d + 1), (c, d - 1), (c - 1, d), (c + 1, d):
                    if inside(a, b) and f[a][b]:
                        f[a][b] = False
                        q.append((a, b))

        for i, row in enumerate(f):
            for j, c in enumerate(row):
                if c:
                    if cnt == 1:
                        return True
                    bfs(i, j)
                    cnt += 1
        return False

    for i, row in enumerate(g):
        for j, c in enumerate(row):
            if c == '#':
                if check(i, j):
                    # print(i,j)
                    return print(1)

    print(2)


#       ms
def solvewa():
    n, m = RI()
    g = []
    cnt = 0
    for _ in range(n):
        s, = RS()
        cnt += s.count('#')
        g.append(s)
    if cnt <= 2:
        return print(-1)

    def inside(x, y):
        return 0 <= x < n and 0 <= y < m

    """wa
    10 10
..........
..........
..........
..........
...###....
...#.#....
...#####..
.....#.#..
.....###..
.........."""
    for i, row in enumerate(g):
        for j, c in enumerate(row):
            if c == '#':
                nei = 0
                for a, b in (i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j):
                    if inside(a, b) and g[a][b] == '#':
                        nei += 1
                        if nei >= 2:
                            break
                if nei == 1:
                    # print(i,j)
                    return print(1)

    print(2)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
