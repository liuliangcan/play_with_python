# Problem: 最短Hamilton路径
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/996/D
# Memory Limit: 524288 MB
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

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """链接：https://ac.nowcoder.com/acm/contest/996/D
来源：牛客网
给定一张n个节点的无向图，给出所有距离 a[i][j]。保证a[x,y]+a[y,z]≥a[x,z]。问从起点0到终点n-1不重不漏的路过所有节点的最短距离。
n<=20
"""
"""看似是图论，其实是状压DP。算是模板题。
注意到所有节点都是可达的，那么一笔画下来，尝试每个节点两两相连就是答案。
题目保证的那个>号，其实是已经帮你做了一遍floyd了。
用mask<=1<<n压缩这20个点，第j位1代表这个状态下j点已访问过。那么这个状态就可以尝试从一个1的点转移到0的点，来生成新的状态。
令dp[mask][j]表示生成了mask状态，且最后到达点是j的最短路径。
用刷表法方便，枚举mask的每一1作为j，转移到一个0作为k，加上dist[j][k]就是下一个状态的花费。
注意生成的mask一定是变大的，因此mask从小到大转移。
---
- 然后py就卡常了，需要进行一点优化：
1. 注意到转移时尝试找到这个mask里所有0和1的位置并且互相转移看似是n方20*20，但可以先枚举拆开转移，那就最多是10*10(1*19,2*18,3*17...)
2. 注意到最后一步一定是要到达n-1，这个位置是1但其它位置有0的mask都没用，可以先移除终点，计算其它点的满mask，然后尝试从每个节点转移到n-1即可。
可以使复杂度减半。
"""


#       ms
def solve1():
    n, = RI()
    dis = []
    for _ in range(n):
        dis.append(RILST())

    f = [[10 ** 13] * (1 << n) for _ in range(n)]  # f[i][j] 代表在状态i最后位置是j需的步数
    f[0][1] = 0  # 一开始站在位置0上，这个状态是1。
    for i in range(1 << n):
        for j in range(n):  # i状态里有j这个点，尝试从j出发
            if i >> j & 1:
                for k in range(n):
                    if i >> k & 1: continue  # k不在i里，那么从j到k
                    # f[k][i | (1 << k)] = min(f[k][i | (1 << k)], f[j][i] + dis[j][k])
                    if f[k][i | (1 << k)] > f[j][i] + dis[j][k]:
                        f[k][i | (1 << k)] = f[j][i] + dis[j][k]
    print(f[n - 1][-1])


#       ms
def solve2():
    n, = RI()
    dis = []
    for _ in range(n):
        dis.append(RILST())

    f = [[10 ** 13] * (1 << n) for _ in range(n)]  # f[i][j] 代表在状态i最后位置是j需的步数
    f[0][1] = 0  # 一开始站在位置0上，这个状态是1。
    one, zero = [], []
    for i in range(1 << n):
        one.clear()
        zero.clear()
        for j in range(n):
            if i >> j & 1:
                one.append(j)
            else:
                zero.append(j)
        for j in one:  # i状态里有j这个点，尝试从j出发
            for k in zero:  # k不在i里，那么从j到k
                # f[k][i | (1 << k)] = min(f[k][i | (1 << k)], f[j][i] + dis[j][k])
                if f[k][i | (1 << k)] > f[j][i] + dis[j][k]:
                    f[k][i | (1 << k)] = f[j][i] + dis[j][k]
    print(f[n - 1][-1])


#  1564     ms
def solve3():
    n, = RI()
    dis = []
    for _ in range(n):
        dis.append(RILST())
    n -= 1  # 先不计算到终点,最后用满mask尝试到终点，这个优化可以让py过
    """复杂度说明:
    solve1 tle 复杂度是2^20 * 20 * 20 ≈ 4e8
    solve2 tle 复杂度是2^20 *(19 + 90) ≈ 1e8
    本solve ac 复杂度是2^19 * (20 + 100) ≈ 5e7; 先不计算中间过程到终点的距离，最终用其他位置的满mask到终点，
    """
    f = [[10 ** 13] * (1 << n) for _ in range(n)]  # f[i][j] 代表在状态i最后位置是j需的步数
    f[0][1] = 0  # 一开始站在位置0上，这个状态是1。

    for i in range(1 << n):
        one, zero = [], []
        for j in range(n):
            if i >> j & 1:
                one.append(j)
            else:
                zero.append(j)
        for j in one:  # i状态里有j这个点，尝试从j出发
            for k in zero:  # k不在i里，那么从j到k
                # f[k][i | (1 << k)] = min(f[k][i | (1 << k)], f[j][i] + dis[j][k])
                if f[k][i | (1 << k)] > f[j][i] + dis[j][k]:
                    f[k][i | (1 << k)] = f[j][i] + dis[j][k]

    print(min(f[j][-1] + dis[j][n] for j in range(1, n)))
#       ms
def solve():
    n, = RI()
    dis = []
    for _ in range(n):
        dis.append(RILST())
    n -= 1  # 先不计算到终点,最后用满mask尝试到终点，这个优化可以让py过
    """复杂度说明:
    solve1 tle 复杂度是2^20 * 20 * 20/2 ≈ 2e8
    solve2 tle 复杂度是2^20 *(20 + 100) ≈ 1e8
    solve3 ac 复杂度是2^19 * (19 + 90) ≈ 5e7; 先不计算中间过程到终点的距离，最终用其他位置的满mask到终点，
    本solve ac 复杂度是2^19 * 19 * 19 /2 ≈ 1e8; 先不计算中间过程到终点的距离，最终用其他位置的满mask到终点，
    """
    f = [[10 ** 13] * (1 << n) for _ in range(n)]  # f[i][j] 代表在状态i最后位置是j需的步数
    f[0][1] = 0  # 一开始站在位置0上，这个状态是1。

    for i in range(1 << n):
        for j in range(n):  # i状态里有j这个点，尝试从j出发
            if i >> j & 1:
                for k in range(n):
                    if i >> k & 1: continue  # k不在i里，那么从j到k
                    # f[k][i | (1 << k)] = min(f[k][i | (1 << k)], f[j][i] + dis[j][k])
                    if f[k][i | (1 << k)] > f[j][i] + dis[j][k]:
                        f[k][i | (1 << k)] = f[j][i] + dis[j][k]

    print(min(f[j][-1] + dis[j][n] for j in range(1, n)))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
