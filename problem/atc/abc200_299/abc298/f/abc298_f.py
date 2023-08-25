# Problem: F - Rook Score
# Contest: AtCoder - TOYOTA MOTOR CORPORATION Programming Contest 2023#1 (AtCoder Beginner Contest 298)
# URL: https://atcoder.jp/contests/abc298/tasks/abc298_f
# Memory Limit: 1024 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://atcoder.jp/contests/abc298/tasks/abc298_f

输入 n(1≤n≤2e5) 和 n 行，每行三个数 x y v，表示一个二维坐标点 (x,y) 和这个坐标点上的数字 v (1≤x,y,v≤1e9)。
不在输入中的坐标点上的数字均为 0。

请你选择一个坐标点 (X,Y)，累加所有横坐标为 X 的坐标点上的数字，以及所有纵坐标为 Y 的坐标点上的数字。
(X,Y) 上的数字只累加一次。
(X,Y) 不一定要在输入中。

输出累加值的最大值。
输入 
4
1 1 2
1 2 9
2 1 8
3 2 3
输出 20

输入 
1
1 1000000000 1
输出 1
"""
"""先预处理所有行和列的元素和（用两个哈希表）。

暴力做法：把所有横纵坐标都记录下来，写一个二重循环枚举所有横坐标和纵坐标的组合。
显然这个做法会超时。

但如果把纵坐标按照列的元素和从大到小排序，对于内层循环，只要当前枚举的 (x,y) 不在输入中，就可以退出内层循环了，因为后面算出的元素和只会更小。

这种做法可以保证至多遍历 n 个值为 0 的坐标。

https://atcoder.jp/contests/abc298/submissions/44850426"""


#     734  ms
def solve():
    n, = RI()
    p = {}
    rows, cols = Counter(), Counter()
    for _ in range(n):
        x, y, v = RI()
        rows[x] += v
        cols[y] += v
        p[(x, y)] = v
    # row = [(k, v) for k, v in rows.items()]
    col = sorted([(k, v) for k, v in cols.items()], key=lambda x: x[1], reverse=True)

    ans = 0
    for i, xx in rows.items():
        for k, (j, yy) in enumerate(col):
            v = p.get((i, j), 0)  # 存在的值都不是0,每个点至多访问一次
            ans = max(ans, xx + yy - v)
            if not v:  # 这行保证最多取到n个0值，非0值也就是输入的n个，因此复杂度是n
                break
    print(ans)


#     635  ms
def solve1():
    n, = RI()
    p = {}
    rows, cols = Counter(), Counter()
    for _ in range(n):
        x, y, v = RI()
        rows[x] += v
        cols[y] += v
        p[(x, y)] = v
    row = [(k, v) for k, v in rows.items()]
    col = sorted([(k, v) for k, v in cols.items()], key=lambda x: x[1], reverse=True)
    ans = 0
    for i, xx in row:
        for j, yy in col:
            v = p.get((i, j), 0)  # 存在的值都不是0
            ans = max(ans, xx + yy - v)
            if not v:  # 这行保证最多取到n个0值，非0值也就是输入的n个，因此复杂度是n
                break
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
