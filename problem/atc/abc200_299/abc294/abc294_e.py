# Problem: E - 2xN Grid
# Contest: AtCoder - AtCoder Beginner Contest 294
# URL: https://atcoder.jp/contests/abc294/tasks/abc294_e
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
PROBLEM = """https://atcoder.jp/contests/abc294/tasks/abc294_e

给你两个长度均 L 的数组 a 和 b，输出有多少个下标 i 满足 a[i]=b[i]。

由于 L 很大，输入用一种压缩格式表示，即 (元素值，连续出现次数)。
例如 [(10,2),(20,1),(10,3)] 表示数组 [10,10,20,10,10,10]。

具体输入格式和数据范围见题目链接。

进阶：
https://ac.nowcoder.com/acm/contest/62033/D
输入
8 4 3
1 2
3 2
2 3
3 1
1 4
2 1
3 3
输出
4
"""


#   267     ms
def solve():
    l, n1, n2 = RI()
    a, b = [], []
    for _ in range(n1):
        a.append(RILST())
    for _ in range(n2):
        b.append(RILST())

    ans = i = j = 0
    while i < n1 and j < n2:
        if a[i][0] == b[j][0]:
            ans += min(a[i][1], b[j][1])
        if a[i][1] > b[j][1]:
            a[i][1] -= b[j][1]
            j += 1
        else:
            b[j][1] -= a[i][1]
            i += 1
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
