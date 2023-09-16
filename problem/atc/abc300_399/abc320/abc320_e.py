# Problem: E - Somen Nagashi
# Contest: AtCoder - Toyota Programming Contest 2023#5（AtCoder Beginner Contest 320）
# URL: https://atcoder.jp/contests/abc320/tasks/abc320_e
# Memory Limit: 1024 MB
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
PROBLEM = """有 N 个人聚集在一起参加一个叫做“流动面条”的活动。这些人排成一排，从前到后依次编号为 1 到 N。

在活动期间，以下事件发生了 M 次：

在时间 Ti，有数量为 Wi 的面条被送下来。排在队伍前面的人得到了全部的面条（如果队伍里没有人，那么没有人得到面条）。然后这个人离开队伍，在时间 Ti+Si 返回到原来的位置。
在时间 X 返回到队伍的人被认为是在时间 X 在队伍中。

在所有 M 次事件之后，报告每个人得到的总面条数量。

约束条件
1≤N≤2×105
1≤M≤2×105
0<T1<…<TM≤109
1≤Si≤109
1≤Wi≤109

所有输入值都是整数。
"""


#       ms
def solve():
    n, m = RI()
    ans = [0] * n
    wait = []
    a = list(range(n))
    for _ in range(m):
        t, w, s = RI()
        while wait and wait[0][0] <= t:
            heappush(a, heappop(wait)[1])
        if not a: continue

        ans[a[0]] += w
        heappush(wait, (t + s, heappop(a)))
    print(*ans, sep='\n')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
