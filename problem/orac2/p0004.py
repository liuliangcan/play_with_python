"""https://orac2.info/problem/seln03monsters/"""
import os.path
import sys
from functools import cache


from sortedcontainers import SortedList

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
INFILE = 'monsterin.txt'
OUTFILE = 'monsterout.txt'
if INFILE and os.path.exists(INFILE):
    sys.stdin = open(INFILE, 'r')
if INFILE and os.path.exists(INFILE):
    sys.stdout = open(OUTFILE, 'w')
"""区间合并，n(<=30)个数ai(<=30),相邻两个数xy可以变成abs(x-y)。
问是否能变成s。并求路径,输出i代表每步合并i和i+1,注意这个i是当前状态的第几个。因此需要sl或者bit模拟，当然暴力也可以因为n<=30。
一开始TLE，因为卡cache，转memo就过了。
直接区间DP，dfs(s,l,r)表示[l,r]是否能合并成s,然后在[l,r)里分割，枚举左边0~30,和右边。
这样复杂度是30^5，大概2.5e7。
然后再写一个dfs2,沿着合法路径走一遍。

"""

memo = [[[-1] * 30 for _ in range(30)] for _ in range(31)]


def solve():
    n, = RI()
    s, = RI()
    a = []
    for _ in range(n):
        v, = RI()
        a.append(v)

    mx = max(a)

    def dfs(s, l, r):
        if s < 0 or s > mx:
            return False
        if l == r:
            return s == a[l]
        if memo[s][l][r] != -1: return memo[s][l][r]
        for i in range(l, r):
            for x in range(mx + 1):
                if dfs(x, l, i) and (dfs(x - s, i + 1, r) or dfs(x + s, i + 1, r)):
                    memo[s][l][r] = 1
                    return True
        memo[s][l][r] = 0
        return False

    if not dfs(s, 0, n - 1):
        return print(0)
    route = []

    def f(s, l, r):
        if s < 0 or s > mx:
            return
        if l == r:
            return
        for i in range(l, r):
            for x in range(mx + 1):
                if dfs(x, l, i):
                    if dfs(x - s, i + 1, r):
                        f(x, l, i)
                        f(x - s, i + 1, r)
                        route.append(i)
                        return
                    elif dfs(x + s, i + 1, r):
                        f(x, l, i)
                        f(x + s, i + 1, r)
                        route.append(i)
                        return

    f(s, 0, n - 1)
    ans = []
    sl = SortedList(range(n))

    for v in route:
        ans.append(sl.bisect_left(v) + 1)
        sl.remove(v)

    print(*ans, sep='\n')


def solve1():
    n, = RI()
    s, = RI()
    a = []
    for _ in range(n):
        v, = RI()
        a.append(v)

    mx = max(a)

    @cache
    def dfs(s, l, r):
        if s < 0 or s > mx:
            return False
        if l == r:
            return s == a[l]
        for i in range(l, r):
            for x in range(mx + 1):
                if dfs(x, l, i) and (dfs(x - s, i + 1, r) or dfs(x + s, i + 1, r)):
                    return True
        return False

    if not dfs(s, 0, n - 1):
        return print(0)
    route = []

    def f(s, l, r):
        if s < 0 or s > mx:
            return
        if l == r:
            return
        for i in range(l, r):
            for x in range(mx + 1):
                if dfs(x, l, i):
                    if dfs(x - s, i + 1, r):
                        f(x, l, i)
                        f(x - s, i + 1, r)
                        route.append(i)
                        return
                    elif dfs(x + s, i + 1, r):
                        f(x, l, i)
                        f(x + s, i + 1, r)
                        route.append(i)
                        return

    f(s, 0, n - 1)
    ans = []
    # print(route)
    # sl = SortedList(range(n))
    #
    # for v in route:
    #     ans.append(sl.bisect_left(v) + 1)
    #     sl.remove(v)
    c = [0] * (n + 1)

    for i in range(1, n + 1):
        while i <= n:
            c[i] += 1
            i += i & -i

    for v in route:
        s = 0
        i = v + 1
        while i:
            s += c[i]
            i -= i & -i
        i = v + 2
        while i <= n:
            c[i] -= 1
            i += i & -i
        ans.append(s)

    print(*ans, sep='\n')


solve()

sys.stdout.close()