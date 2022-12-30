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

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/652/C

输入 n 和 m (≤3e5)，一个 1~n 的全排列 p，以及 m 个 pair，元素值均在 [1,n] 中。
称 p 的子数组 b 是合法的，当且仅当对于所有 pair (x,y)，x 和 y 至多有一个在 b 中。
输出有多少个 p 的合法子数组。
"""


# 951 ms
def solve1(n, m, p, xy):
    s = [[] for _ in range(n + 1)]
    for i, (x, y) in enumerate(xy):
        s[x].append(i)
        s[y].append(i)
    ps = [s[a] for a in p]
    q = deque()
    cnt = Counter()
    ans = 0
    for r in range(n):
        q.append(r)
        for i in ps[r]:
            cnt[i] += 1
            while cnt[i] >= 2:
                l = q.popleft()
                for j in ps[l]:
                    cnt[j] -= 1

        ans += len(q)

    print(ans)


# 592 ms 滑窗，计算窗口内每个点对出现的次数，超2则缩窗，窗内以r为结尾的合法子数组数量有len个
def solve2(n, m, p, xy):
    s = [[] for _ in range(n + 1)]  # 记录每个数出现在第几对，每个对下标在一个合法区间内只能出现一次
    for i, (x, y) in enumerate(xy):
        s[x].append(i)
        s[y].append(i)
    ps = [s[a] for a in p]  # 记录原排列每一位的数字出现在哪些对里
    l = 0
    # cnt = Counter()  # 记录当前区间内，每个对下标出现次数，不能超过2
    cnt = [0] * m  # 记录当前区间内，每个对下标出现次数，不能超过2;注意这里是 m ！！！点对下标的数量
    ans = 0
    for r in range(n):
        for i in ps[r]:
            cnt[i] += 1
            while cnt[i] >= 2:
                for j in ps[l]:
                    cnt[j] -= 1
                l += 1

        ans += r - l + 1

    print(ans)


# 623 ms 哈希，直接计算p中每个数字关联的所有邻居数字最后出现的位置作为窗口左边缘外侧
def solve3(n, m, p, xy):
    g = [[] for _ in range(n + 1)]
    for u, v in xy:
        g[u].append(v)
        g[v].append(u)
    ans = 0
    # ls = {}
    ls = [-1] * (n + 1)  # 记录每个数最后出现的位置
    l = -1
    for r, u in enumerate(p):
        # l = max(l, max([ls.get(v, l) for v in g[u]], default=l))
        l = max(l, max([ls[v] for v in g[u]], default=l))
        ls[u] = r

        ans += r - l

    print(ans)


# 608 ms 哈希
def solve4(n, m, p, xy):
    g = [[] for _ in range(n + 1)]
    for u, v in xy:
        g[u].append(v)
        g[v].append(u)
    ans = 0
    # ls = {}
    ls = [-1] * (n + 1)  # 记录每个数最后出现的位置
    l = -1
    for r, u in enumerate(p):
        for v in g[u]:
            # pos = ls.get(v, -1)
            pos = ls[v]
            if pos > l:
                l = pos
        ans += r - l
        ls[u] = r

    print(ans)


# 608 ms
def solve5(n, m, p, xy):
    g = [[] for _ in range(n + 1)]
    for u, v in xy:
        g[u].append(v)
        g[v].append(u)
    ans = 0
    # ls = {}
    ls = [-1] * (n + 1)  # 记录每个数最后出现的位置
    l = -1
    for r, u in enumerate(p):
        # l = max(l, max([ls.get(v, l) for v in g[u]], default=l))
        t = max(l, max([ls[v] for v in g[u]], default=l))
        if t > l:
            l = t
        ls[u] = r

        ans += r - l

    print(ans)


# 217 ms ,计算每个下标对应的数的'左'邻居，左边下标的最大值；然后遍历下标累加窗口大小。
def solve6(n, m, p):
    # ps = {v: i for i, v in enumerate(p)}
    ps = [0] * (n + 1)
    for i, v in enumerate(p):
        ps[v] = i
    ls = [-1] * (n + 1)
    for _ in range(m):
        x, y = RI()
        x, y = ps[x], ps[y]
        if x > y:
            x, y = y, x
        if x > ls[y]:
            ls[y] = x
    ans = 0
    l = -1
    for r in range(n):
        if ls[r] > l:
            l = ls[r]
        ans += r - l
    print(ans)


# 312   ms ,计算每个下标对应的数的'左'邻居，左边下标的最大值；然后遍历下标累加窗口大小。
def solve7(n, m, p, xy):
    ps = [0] * (n + 1)
    for i, v in enumerate(p):
        ps[v] = i
    ls = [-1] * (n + 1)
    for x, y in xy:
        x, y = ps[x], ps[y]
        if x > y:
            x, y = y, x
        if x > ls[y]:
            ls[y] = x
    ans = 0
    l = -1
    for r in range(n):
        if ls[r] > l:
            l = ls[r]
        ans += r - l
    print(ans)

#  187  ms ,计算每个下标对应的数的'左'邻居，左边下标的最大值；然后遍历下标累加窗口大小。这次p和xy都不存了，极快
def solve(n, m):
    ps = [0] * (n + 1)
    i = 0
    for v in RI():
        ps[v] = i
        i += 1
    ls = [-1] * (n + 1)
    for _ in range(m):
        x, y = RI()
        x, y = ps[x], ps[y]
        if x > y:
            x, y = y, x
        if x > ls[y]:
            ls[y] = x
    ans = 0
    l = -1
    for r in range(n):
        if ls[r] > l:
            l = ls[r]
        ans += r - l
    print(ans)


# 592 ms 滑窗，计算窗口内每个点对出现的次数，超2则缩窗，窗内以r为结尾的合法子数组数量有len个
def solve9(n, m, p, xy):
    s = [[] for _ in range(n + 1)]  # 记录每个数出现在第几对，每个对下标在一个合法区间内只能出现一次
    for i, (x, y) in enumerate(xy):
        s[x].append(i)
        s[y].append(i)
    ps = [s[a] for a in p]  # 记录原排列每一位的数字出现在哪些对里
    l = 0
    # cnt = Counter()  # 记录当前区间内，每个对下标出现次数，不能超过2
    cnt = [0] * m  # 记录当前区间内，每个对下标出现次数，不能超过2;注意这里是 m ！！！点对下标的数量
    ans = 0
    for r in range(n):
        for i in ps[r]:
            cnt[i] += 1
            while cnt[i] >= 2:
                for j in ps[l]:
                    cnt[j] -= 1
                l += 1

        ans += r - l + 1

    print(ans)

if __name__ == '__main__':
    n, m = RI()
    p = RILST()
    xy = []
    for _ in range(m):
        xy.append(RILST())
    # solve6(n, m, p)
    solve(n, m)
    # solve(n, m, p, xy)