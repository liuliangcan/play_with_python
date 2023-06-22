# Problem: D. Washer, Dryer, Folder
# Contest: Codeforces - MemSQL Start[c]UP 2.0 - Round 1
# URL: https://codeforces.com/problemset/problem/452/D
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/452/D

输入 k (1≤k≤1e4) n1 n2 n3 t1 t2 t3 (1≤n1,n2,n3,t1,t2,t3≤1000)。
有 k 件衣服，每件都需要按照洗净 -> 烘干 -> 熨烫的顺序处理。
现在有 n1 个洗衣机，n2 个烘干机和 n3 个熨斗。
每个机器同时只能处理一件衣服，分别花费 t1, t2, t3 时间。
你必须将一件洗好的衣服立即烘干，烘干完毕后立即熨烫。
输出处理完所有衣服的最短时间。
输入 1 1 1 1 5 5 5
输出 15

输入 8 4 3 2 10 5 2
输出 32
"""
"""https://codeforces.com/problemset/submission/452/210604954

题解（欢迎点赞）"""


#       ms
def solve():
    k, n1, n2, n3, t1, t2, t3 = RI()
    f1 = [0] * n1
    f2 = [0] * n2
    f3 = [0] * n3
    for i in range(k):
        f = max(f1[i % n1] + t1 + t2 + t3, f2[i % n2] + t2 + t3, f3[i % n3] + t3)
        f1[i % n1] = f - t2 - t3
        f2[i % n2] = f - t3
        f3[i % n3] = f
    print(f)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
