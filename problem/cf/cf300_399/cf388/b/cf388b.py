# Problem: B. Fox and Minimal path
# Contest: Codeforces - Codeforces Round #228 (Div. 1)
# URL: https://codeforces.com/problemset/problem/388/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """
https://codeforces.com/problemset/problem/388/B

输入 k(1≤k≤1e9)。
构造一个节点个数不超过 1000 的简单无向图（节点编号从 1 开始），使得从节点 1 到节点 2 的最短路径的数量恰好为 k。
输出 n 以及一个 n*n 的邻接矩阵 g，如果 i 和 j 之间有边，则 g[i][j]='Y'，否则为 'N'。
注意不能有自环，即 g[i][i] 必须为 'N'。

进阶：请最小化 n。

注：这个构造方案可以用来 hack 一些用方案数取模来做连通性判定的代码。
输入
2
输出
4
NNYY
NNYY
YYNN
YYNN

输入
9
输出
8
NNYYYNNN
NNNNNYYY
YNNNNYYY
YNNNNYYY
YNNNNYYY
NYYYYNNN
NYYYYNNN
NYYYYNNN
"""
"""首先变成0-indexed来考虑，思路：构造5层中间层。0作为源点，1作为汇点。
由于是最短路，考虑BFS分层，每增加一步实际上是经过一层。那么考虑分5层，考虑中间相邻层全部卷积连接拉满，每层只需要64个，则路径有64**5=2**30正好>1e9。
这里说明一下为什么要5层：从底层考虑上来，如果是4层，每层需要178个，5层几乎就把1000个元素用完了，失去机动性。
实现时，尝试把k开5次方，向下取整得x，给每层添加x个元素，互相拉满，贡献p=x**5条路径。k-=p，考虑剩下的k条路径。
继续尝试把剩下的k开5次方，又得x，给每层再添加x个元素，互相拉满。k-x**5。
当k<32时就不要尝试了，x只能得1，把这部分k当做机动处理：第一层创建k个数，2345层1个数，拉满就是k条路径。 
"""


#   109    ms
def solve5():
    k, = RI()
    s = 0
    a = []
    while k >= 32:
        x = int(k ** 0.2)
        k -= x ** 5
        a.append(x)
        s += x
    left = k
    # 共5层，每层s个数，剩下的left，第一层left个数，其余4层1个数
    n = 2 + s * 5 + 4 + left  # 01、每层s个数、剩下left
    start = 2  # 这5层节点从2开始
    ans = [['N'] * n for _ in range(n)]
    # 把5层连接
    for x in a:
        for i in range(4):
            for y in range(x):
                l = start + i * x + y
                for z in range(x):
                    r = start + (i + 1) * x + z
                    ans[l][r] = ans[r][l] = 'Y'
        for y in range(x):
            l = start + y  # 第一排的数
            r = start + 4 * x + y  # 最后一排的数
            ans[0][l] = ans[l][0] = 'Y'
            ans[1][r] = ans[r][1] = 'Y'
        start += 5 * x
    # print(start) = 12
    # 连接剩余left的数
    for i in range(start, start + left):
        ans[0][i] = ans[i][0] = 'Y'  # 第一排连接到0
        ans[start + left][i] = ans[i][start + left] = 'Y'  # 第一排连接到第二排的数
    start += left
    for _ in range(3):
        ans[start][start + 1] = ans[start + 1][start] = 'Y'  # 连接后一排
        start += 1
    ans[start][1] = ans[1][start] = 'Y'  # 最后一排连接1
    print(n)
    print('\n'.join(map(lambda r: ''.join(r), ans)))


#     109  ms
def solve():
    # c = 6  # 124ms
    c = 5  # 109
    k, = RI()
    s = 0
    groups = []
    start = 2
    while k >= 2 ** c:
        x = int(k ** (1 / c))
        k -= x ** c
        cur = []
        for i in range(c):
            cur.append((start, start + x))
            start += x
        groups.append(cur)
        s += x

    # 共8层，每层s个数，剩下的k，第一层k个数，其余7层1个数
    n = 2 + s * c + c - 1 + k  # 01、每层s个数、剩下k
    ans = [['N'] * n for _ in range(n)]

    def add(x, y):
        ans[x][y] = ans[y][x] = 'Y'

    # print(groups)
    for parts in groups:  # 组合同层的
        # print(parts)
        for i in range(c - 1):  # range(len(parts)-1): 一共8层
            for x in range(*(parts[i])):  # 相邻层卷积连接
                for y in range(*(parts[i + 1])):
                    # print(x,y)
                    add(x, y)
    if groups:
        for xs in groups:
            for x in range(*(xs[0])):
                add(x, 0)
            for x in range(*(xs[-1])):
                add(x, 1)
    # print(start) = 12
    # 连接剩余k的路径
    for i in range(start, start + k):
        add(0, i)  # 第一排连接到0
        add(start + k, i)  # 第一排连接到第二排的数
    start += k
    for _ in range(c - 2):
        add(start, start + 1)  # 连接后一排
        start += 1
    add(1, start)  # 最后一排连接1
    print(n)
    print('\n'.join(map(lambda r: ''.join(r), ans)))


if __name__ == '__main__':
    solve()
