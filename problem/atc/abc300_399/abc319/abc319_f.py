# Problem: F - Fighter Takahashi
# Contest: AtCoder - AtCoder Beginner Contest 319
# URL: https://atcoder.jp/contests/abc319/tasks/abc319_f
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
PROBLEM = """有一棵具有N个顶点的树。第一个顶点是根节点，第i个顶点（2≤i≤N）的父节点是pi（1≤pi<i）。

每个非根节点上都有一个敌人或药物。高桥想要打败所有的敌人。初始时，他的力量为1，他位于第一个顶点。对于i=2，…，N，第i个顶点的信息由三个整数（ti，si，gi）表示，如下所示。

如果ti=1，表示第i个顶点上有一个敌人。当高桥第一次访问这个顶点时，如果他的力量小于si，高桥被敌人打败并输掉比赛，之后他不能移动到其他顶点。否则，他打败敌人，他的力量增加gi。

如果ti=2，表示第i个顶点上有一种药物。当高桥第一次访问这个顶点时，他服用了这种药物，他的力量乘以gi。（对于一个带有药物的顶点，si=0。）

最多有10个带有药物的顶点。

高桥可以重复移动到相邻的顶点。确定他是否能够打败所有的敌人。
"""
"""由于吃药是乘一个>=1的数，因此一定放在加法后边更好，越滞后越好。
因此优先打怪，用小顶堆优先打弱的怪。打不过了再去吃药。
每次吃药枚举最小的但满足打赢怪的组合。可以直接暴力枚举
"""

#       ms
def solve():
    n, = RI()
    pw = 1  # 初始力量
    g = [[] for _ in range(n)]
    ee = [(1, 0, 0)]  # 根视为100
    for i in range(1, n):
        p, t, s, gg = RI()
        g[p - 1].append(i)
        ee.append((t, s, gg))

    yao = []  # 现在可用的药

    def viagra(pw, t):  # 从现在能访问的药里，找到最小的组合，使pw*s>=t，直接状压枚举
        if not yao:
            return 0
        ans = mn = inf  # 组合、最小乘积
        n = len(yao)
        for i in range(1, 1 << n):  # 状压
            s = 1  # 这个组合的乘积
            for j in range(n):
                if i >> j & 1:
                    s *= yao[j]
                    if s > mn:  # 超过当前了不用看了
                        break
            if s * pw >= t and s < mn:  # 能打过怪了
                mn = s
                ans = i
        if ans == inf:  # 没有能打过怪的组合，直接死
            return 0
        for j in range(n - 1, -1, -1):  # 用掉这些药，逆序
            if ans >> j & 1:
                yao.pop(j)
        return mn

    h = [(0, 0)]  # 小顶堆，优先搞最弱的怪，如果搞不动，才去吃药，每次吃(最小但满足的组合)
    while h:
        t, u = heappop(h)
        if ee[u][0] == 2:
            yao.append(ee[u][2])
        if pw < t:  # 需要吃药
            pw *= viagra(pw, t)  # 吃
        if pw < t:  # 吃完药还是打不过
            return print('No')
        if ee[u][0] == 1:
            pw += ee[u][2]
        for v in g[u]:
            heappush(h, (ee[v][1], v))  # 如果是药，优先加入药袋，正好它的s是0

    print('Yes')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
