# Problem: E. Round Dance
# Contest: Codeforces - Codeforces Round 874 (Div. 3)
# URL: https://codeforces.com/contest/1833/problem/E
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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，实测这个快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """给出n和长为n的数组a[i].其中a[i]是i的一个邻居。
已知每个i其实有2邻居，整体组成多个环。
问最少、最多有几个环。
"""
"""并查集。
直接按已知邻居合并。最后有几个家族，最多就有几个环。
最少怎么讨论呢。
    - 已知的边合并时，若x,y已经在一个环里了，要么是x连过y，要么是z连过y，且z和x已经连接。显然第二种情况会导致这个环闭合。
    - 那么这就可以计算一个封闭的环。先计算出有多少个封闭的环。cc
    - 再计算有多少个点在非封闭的家族里。（这里计算有1个即可，因为是讨论最少），把所有非封闭的点连成1个环。op
    - mn=cc+op
"""



class DSU:
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.setCount = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            # self.edge_size[y] += 1
            return False
        # if self.size[x] > self.size[y]:  # 注意如果要定向合并x->y，需要干掉这个；实际上上边改成find_fa后，按轶合并没必要了，所以可以常关
        #     x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.setCount -= 1
        return True


#       ms
def solve():
    n, = RI()
    a = RILST()
    dsu = DSU(n)

    c = set()  # 环内的点
    vis = set()
    for i, v in enumerate(a):
        if not dsu.union(i, v - 1) and (v - 1, i) not in vis:
            c.add(dsu.find_fa(i))
        vis.add((i, v - 1))

    cc = set()  # 每个环的代表元
    for p in c:
        cc.add(dsu.find_fa(p))
    op = set()  # 不在环的点
    for i in range(n):
        if dsu.find_fa(i) not in cc:
            op.add(i)
            break  # 只要一个就行
    if not op:
        mn = len(cc)
    elif not cc:
        mn = 1
    else:
        mn = len(cc) + 1
    # print(cc,op)
    print(mn, dsu.setCount)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
