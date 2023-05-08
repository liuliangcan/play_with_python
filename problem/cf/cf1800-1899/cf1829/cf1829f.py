# Problem: F. Forever Winter
# Contest: Codeforces - Codeforces Round 871 (Div. 4)
# URL: https://codeforces.com/contest/1829/problem/F
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """输入t代表t组数据，每组数据：
输入n,m代表图的点数和边数。
接下来输入m行代表边。
已知输入的图是雪花图，其中雪花图的定义是：
中间一个点有x条边，连接x个跳板点；对于每个跳板点，连接y条新边，y个新点。（x,y>1)
求输入图形的x和y
（建议去网站里看图)
"""
"""记录每个点的度，只有最外层的点可以是1，中间点和跳板点的度可以相同，也可以不同。那么度只有2种或者3种。
若是3种，则中间点的度只出现1次。
若是2种，则中间点的度应该大。因为跳板点除了y还多连了一个中间点"""


#       ms
def solve():
    n, m = RI()
    degree = [0] * n
    for _ in range(m):
        u, v = RI()
        u -= 1
        v -= 1
        degree[u] += 1
        degree[v] += 1
    cnt = Counter(degree)
    # print(cnt)
    s = sorted([(k, v) for k, v in cnt.items()])
    if len(s) == 3:
        x, y = s[1][0], s[2][0]
        if s[1][1] == 1:
            x, y = y, x
        x -= 1
        print(y, x)
    else:
        x = y = s[1][0]
        x -= 1
        print(y, x)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
