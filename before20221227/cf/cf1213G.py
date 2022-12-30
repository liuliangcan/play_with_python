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

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())
input = sys.stdin.buffer.readline
RI = lambda: map(int, input().split())
# RS = lambda: sys.stdin.readline().strip().split()
RS = lambda: map(bytes.decode, input().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1213/G

输入 n(≤2e5) 和 m(≤2e5)，表示一棵有 n 个节点的树，和 m 个询问。
然后输入 n-1 行，每行 3 个数，表示树的每条边连接的点的编号（从 1 开始），以及边权(1≤边权≤2e5)。
最后输入 m 个询问 q[i](1≤q[i]≤2e5)，你需要对每个询问，输出树上有多少条简单路径，路径上的最大权值不超过 q[i]。
输入
7 5
1 2 1
3 2 3
2 4 1
4 5 2
5 7 4
3 6 2
5 2 3 4 1
输出
21 7 15 21 3 

输入
1 2
1 2
输出
0 0 

输入
3 3
1 2 1
2 3 2
1 3 2
输出
1 3 3 
"""


# def find(a):
#     c = []
#     while par[a] != a:
#         c.append(a)
#         a = par[a]
#     for i in c:
#         par[i] = a
#     return a
# def find_father(x):
#     if fathers[x] != x:
#         fathers[x] = find_father(fathers[x])
#     return fathers[x]
# def find_father(x):
#     c = []
#     while fathers[x] != x:
#         c.append(x)
#         x = fathers[x]
#     for i in c:
#         fathers[i] = x
#
#     return x

# def find(self, a):
#     acopy = a
#     while a != self.parent[a]:
#         a = self.parent[a]
#     while acopy != a:
#         self.parent[acopy], acopy = a, self.parent[acopy]
#     return a

# 1341 ms
def solve(n, m, e, q):
    cnt = [1] * (n + 1)
    fathers = list(range(n + 1))

    def find_father(x):
        t = x
        while fathers[x] != x:
            x = fathers[x]
        while t != x:
            fathers[t], t = x, fathers[t]
        return x

    def union(x, y):
        x = find_father(x)
        y = find_father(y)
        if x == y:
            return 0
        fathers[x] = y
        t = cnt[x] * cnt[y]
        cnt[y] += cnt[x]
        return t

    e.sort(key=lambda x: x[2])
    ans = [0] * m
    j = 0
    s = 0
    # for limit, i in sorted([(v, i) for i, v in enumerate(q)]):  # 不够短，用下边的
    for limit, i in sorted(zip(q, range(len(q)))):
        while j < n - 1 and e[j][2] <= limit:
            s += union(e[j][0], e[j][1])
            j += 1
        ans[i] = s
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    n, m = RI()
    e = []
    for _ in range(n - 1):
        u, v, w = RI()
        e.append((u, v, w))
    q = RILST()
    # print(n, m)
    # print(e)
    # print(q)
    solve(n, m, e, q)
