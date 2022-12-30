import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/contest/988/problem/F

输入正整数 dst(≤2000), n(≤(dst+1)/2) 和 m(≤2000)。
然后输入 n 个互不相交的下雨区间，左右端点满足 0≤L<R≤dst。
然后输入 m 行，每行两个数表示雨伞的位置 x[i](≤dst) 和重量 w[i](≤1e5)。

你需要从 0 出发走到 dst。在下雨区间内移动必须打伞（区间端点处不算下雨）。
你可以中途换伞。
带着伞移动时，每走一单位长度，消耗的耐力等于伞的重量。
你可以丢掉伞，空手移动时消耗的耐力为零。
输出到达 dst 至少需要消耗多少耐力。如果无法到达 dst，输出 -1。

进阶：请写一个和坐标范围无关的代码，即使坐标范围达到 1e9 也可以通过。
输入
10 2 4
3 7
8 10
0 10
3 4
8 1
1 2
输出 14

输入
10 1 1
0 9
0 5
输出 45

输入
10 1 1
0 9
1 5
输出 -1
"""


#  RE	 ms
def solve1(dst, n, m, lr, xw):
    lr.sort()
    xw.sort()
    if xw[0][0] > lr[0][0]:
        return print(-1)
    rs = set()  # 所有雨区右端点
    rain = set()  # 所有下雨的伞点， 以上两种位置必须打伞到达
    umbrella = {}  # 每个位置上最轻的那把伞是谁
    for i, (x, w) in enumerate(xw):
        if x in umbrella and xw[umbrella[x]] <= w:
            continue
        umbrella[x] = i
    h = {0, dst}  # 所有点的位置 离散化
    j = 0
    for l, r in lr:
        while j < m and xw[j][0] <= r:
            if xw[j][0] > l:
                rain.add(xw[j][0])  # 伞在雨区（必须打伞到这
            h.add(xw[j][0])
            j += 1
        rs.add(r)
        h.add(r)
        h.add(l)
    h = sorted(h)
    # f[i][j] 代表走到h[i]时，手里拿着第j把伞(j从1开始)，消耗的最低体力；
    # j==0代表手里没伞。
    f = [[inf] * (m + 1) for _ in range(len(h))]
    # 初始：位置0可以不拿伞，如果有伞，就拿，注意伞编号+1
    f[0][0] = 0
    if 0 in umbrella:
        f[0][umbrella[0] + 1] = 0
    # print(f)
    for i in range(1, len(h)):
        for j in range(1, m + 1):  # 考虑打伞走过来
            f[i][j] = f[i - 1][j] + (h[i] - h[i - 1]) * xw[j - 1][1]

        if h[i] not in rs and h[i] not in rain:  # 不在雨区，允许从上一步扔掉伞走过来
            f[i][0] = min(f[i - 1])

        if h[i] in rs:  # 在这里可以扔伞，不管怎么走过来,都扔
            f[i][0] = min(f[i])

        if h[i] in umbrella:  # 在这里可以拿伞，不管怎么走过来，都拿起来,拿的伞编号是umbrella[h[i]]，注意j要+1
            f[i][umbrella[h[i]] + 1] = min(f[i])

    print(min(f[-1]))


#  RE	 ms
def solve2(dst, n, m, lr, xw):
    lr.sort()
    xw.sort()
    if xw[0][0] > lr[0][0]:
        return print(-1)
    rs = set()  # 所有雨区右端点
    rain = set()  # 所有下雨的伞点， 以上两种位置必须打伞到达
    umbrella = {}  # 每个位置上最轻的那把伞是谁
    for i, (x, w) in enumerate(xw):
        if x in umbrella and xw[umbrella[x]] <= w:
            continue
        umbrella[x] = i
    h = {0, dst}  # 所有点的位置 离散化
    j = 0
    for l, r in lr:
        while j < m and xw[j][0] <= r:
            if xw[j][0] > l:
                rain.add(xw[j][0])  # 伞在雨区（必须打伞到这
            h.add(xw[j][0])
            j += 1
        rs.add(r)
        h.add(r)
        h.add(l)
    h = sorted(h)
    # f[i][j] 代表走到h[i]时，手里拿着第j把伞(j从1开始)，消耗的最低体力；
    # j==0代表手里没伞。
    f = [inf] * (m + 1)  # 滚动优化
    # 初始：位置0可以不拿伞，如果有伞，就拿，注意伞编号+1
    f[0] = 0
    if 0 in umbrella:
        f[umbrella[0] + 1] = 0
    g = f[:]
    # print(f)
    for i in range(1, len(h)):
        f, g = g, f
        f[0] = inf
        for j in range(1, m + 1):  # 考虑打伞走过来
            f[j] = g[j] + (h[i] - h[i - 1]) * xw[j - 1][1]

        if h[i] not in rs and h[i] not in rain:  # 不在雨区，允许从上一步扔掉伞走过来
            f[0] = min(g)

        if h[i] in rs:  # 在这里可以扔伞，不管怎么走过来,都扔
            f[0] = min(f)

        if h[i] in umbrella:  # 在这里可以拿伞，不管怎么走过来，都拿起来,拿的伞编号是umbrella[h[i]]，注意j要+1
            f[umbrella[h[i]] + 1] = min(f)

    print(min(f))


def solve(dst, n, m, lr, xw):
    lr.sort()
    xw.append([dst, 0])
    xw.sort()
    if dst <= lr[0][0]:
        return print(0)
    if xw[0][0] > lr[0][0]:
        return print(-1)
    g = [0] * (len(xw))  # 每个伞之前，可以扔伞的位置(最近的雨区右端点;如果这个伞在雨里，那只能到了自己这才扔
    j = 0
    for i, (x, w) in enumerate(xw):
        while j < n and lr[j][1] < x:  # 雨区严格在左边，向右寻找
            j += 1
        if j:  # 上一个严格在左边的右端点可能是扔伞点
            g[i] = lr[j - 1][1]
        if j < n and lr[j][0] < x:  # 当前雨区覆盖伞，只能过来扔
            g[i] = x
    # print(lr,xw)
    # print(g)
    f = [inf] * (len(xw))
    f[0] = 0
    for i in range(1, len(xw)):
        if xw[i - 1][0] >= g[i]:
            f[i] = f[i - 1]
            continue
        for j in range(i):
            if xw[j][0] > g[i]:
                break
            f[i] = min(f[i], f[j] + xw[j][1] * (g[i] - xw[j][0]))
        if xw[i][0] == dst:
            return print(f[i])


if __name__ == '__main__':
    dst, n, m = RI()
    lr = []
    for _ in range(n):
        lr.append(RILST())
    xw = []
    for _ in range(m):
        xw.append((RILST()))

    solve(dst, n, m, lr, xw)
