# Problem: E - Transition Game
# Contest: AtCoder - AtCoder Beginner Contest 296
# URL: https://atcoder.jp/contests/abc296/tasks/abc296_e
# Memory Limit: 1024 MB
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
PROBLEM = """https://atcoder.jp/contests/abc296/tasks/abc296_e
给你N和长度为N的数组a，其中1<=a[i]<=N,下标从1开始。
A和B做N轮游戏，轮数下标从1开始。在第i轮，玩法如下：
1. A指定一个正整数ki,告诉B。
2. B指定一个1~N之间的数，写在黑板上。
3. 做如下操作ki次:把黑板上的数字x替换成a[x]。
操作结束后，如果黑板上的数字是i，B赢；否则A赢。
请问在A和B都做最优操作的情况下，B能赢多少次。
"""
"""手玩一下发现：替换操作就是把数字沿着值作为下标->值这个路径往后走，路径可以用图考虑。
把整个数组按这个操作建图，图中会存在环，n个节点n条边；而且这个图是内向的，因为出度最多是1.即进了环就出不来。
由于第i轮操作的目标数字是知道的，即i，B的目标是让路径的终点是i，那么若i在环上，B可以调整起始点的位置，使ki步后正好到达i。(因为在环上代表前边步数可以无限)
A的目标是让i不在终点，那么对于所有没进环上的i，可以设置ki>=n足够大，使终点进环。
因此对于所有在环上的i，B必赢；不在环上的点，A必赢。
找所有环上的点数量不好弄；反过来求不在环上的点，用拓扑排序即可。
————————————————
版权声明：本文为CSDN博主「七水shuliang」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liuliangcan/article/details/129972406"""

#       ms
def solve():
    n, = RI()
    a = RILST()
    g = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for i, v in enumerate(a, start=1):
        g[i].append(v)
        degree[v] += 1
    q = deque([i for i, v in enumerate(degree) if i and v == 0])
    ans = n
    while q:
        ans -= 1
        u = q.popleft()
        for v in g[u]:
            degree[v] -= 1
            if degree[v] == 0:
                q.append(v)
    print(ans)


if __name__ == '__main__':
    solve()
