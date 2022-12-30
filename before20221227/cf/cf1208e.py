import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *
from operator import or_

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1208/E

输入 n(≤1e6) 和 w(≤1e6)，表示一个 n 行 w 列的表格。
然后输入 n 个数组，第 i 个数组放在第 i 行中。
输入的格式为：第一个数字表示数组的长度 m(≤w)，然后输入一个长为 m 的数组，元素范围 [-1e9,1e9]。
保证所有数组的长度之和不超过 1e6。

你可以滑动任意一行的整个数组。
对表格的每一列，输出这一列的元素和的最大值。
注意：每一列是单独计算的，不同列可以有不同的滑动方案。
输入
3 3
3 2 4 8
2 2 5
2 6 3
输出
10 15 16 
解释 如图

输入
2 2
2 7 8
1 -8
输出
7 8 
"""
#
#
# class SparseTable:
#     def __init__(self, data: list, func=or_):
#         # 稀疏表，O(nlgn)预处理，O(1)查询区间最值/或和/gcd
#         # 下标从0开始
#         self.func = func
#         self.st = st = [list(data)]
#         i, N = 1, len(st[0])
#         while 2 * i <= N + 1:
#             pre = st[-1]
#             st.append([func(pre[j], pre[j + i]) for j in range(N - 2 * i + 1)])
#             i <<= 1
#
#     def query(self, begin: int, end: int):  # 查询闭区间[begin, end]的最大值
#         lg = (end - begin + 1).bit_length() - 1
#         return self.func(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])
#
#
# # MLE	 ms
# def solve1(n, w, a):
#     # st = [SparseTable(row, max) for row in a]
#     ans = [0] * w
#     for i in range(n):
#         L = len(a[i])
#         s = SparseTable(a[i], max)
#         for j in range(w):
#             l = max(0, j - (w - L))
#             r = min(j, L - 1)
#             # p = st[i].query(l, r)
#             p = s.query(l, r)
#             if (j >= L or j < w - L) and p < 0:
#                 p = 0
#
#             ans[j] += p
#     print(*ans)
#
#
# # TLE	 ms
# def solve2(n, w, a):
#     ans = [0] * w
#     for i in range(n):
#         L = len(a[i])
#         q = deque()
#         for j in range(w):
#             l = max(0, j - (w - L))
#             r = min(j, L - 1)
#             if j < L:
#                 while q and a[i][q[-1]] <= a[i][j]:
#                     q.pop()
#                 q.append(j)
#             while q and q[0] < l:
#                 q.popleft()
#             p = a[i][q[0]]
#             if (j >= L or j < w - L) and p < 0:
#                 p = 0
#             ans[j] += p
#     print(*ans)
#
#
# # 1231 ms
# def solve3(n, w, a):
#     ans = [0] * (w + 1)  # 差分
#     for i in range(n):
#         L = len(a[i])
#         q = deque()
#
#         if w > 2 * L:
#             for j in range(L):
#                 l = max(0, j - (w - L))
#                 r = min(j, L - 1)
#                 if j < L:
#                     while q and a[i][q[-1]] <= a[i][j]:
#                         q.pop()
#                     q.append(j)
#                 while q and q[0] < l:
#                     q.popleft()
#                 p = a[i][q[0]]
#                 if (j >= L or j < w - L) and p < 0:
#                     p = 0
#                 ans[j] += p
#                 ans[j + 1] -= p
#
#             p = max(0, a[i][q[0]])
#             ans[L] += p
#             ans[w - L] -= p
#
#             for j in range(w - L, w):
#                 l = max(0, j - (w - L))
#                 r = min(j, L - 1)
#                 while q and q[0] < l:
#                     q.popleft()
#                 p = a[i][q[0]]
#                 if (j >= L or j < w - L) and p < 0:
#                     p = 0
#                 ans[j] += p
#                 ans[j + 1] -= p
#         else:
#             for j in range(w):
#                 l = max(0, j - (w - L))
#                 r = min(j, L - 1)
#                 if j < L:
#                     while q and a[i][q[-1]] <= a[i][j]:
#                         q.pop()
#                     q.append(j)
#                 while q and q[0] < l:
#                     q.popleft()
#                 p = a[i][q[0]]
#                 if (j >= L or j < w - L) and p < 0:
#                     p = 0
#                 ans[j] += p
#                 ans[j + 1] -= p
#
#     p = [ans[0]]
#     for i in range(1, w):
#         p.append(p[-1] + ans[i])
#     print(*p)
#
#
# # 1138  ms
# def solve4(n, w, a):
#     ans = [0] * (w + 1)  # 差分
#     for i in range(n):
#         L = len(a[i])
#         q = deque()
#         for j in range(L):
#             l = max(0, j - (w - L))
#             r = min(j, L - 1)
#             if j < L:
#                 while q and a[i][q[-1]] <= a[i][j]:
#                     q.pop()
#                 q.append(j)
#             while q and q[0] < l:
#                 q.popleft()
#             p = a[i][q[0]]
#             if (j >= L or j < w - L) and p < 0:
#                 p = 0
#             ans[j] += p
#             ans[j + 1] -= p
#
#         if w > 2 * L:
#             p = max(0, a[i][q[0]])
#             ans[L] += p
#             ans[w - L] -= p
#
#         for j in range(max(L, w - L), w):
#             l = max(0, j - (w - L))
#             r = min(j, L - 1)
#             while q and q[0] < l:
#                 q.popleft()
#             p = a[i][q[0]]
#             if (j >= L or j < w - L) and p < 0:
#                 p = 0
#             ans[j] += p
#             ans[j + 1] -= p
#
#     p = [ans[0]]
#     for i in range(1, w):
#         p.append(p[-1] + ans[i])
#     print(*p)
#
#
# #  1247  ms
# def solve(n, w, a):
#     ans = [0] * (w + 1)  # 差分
#     for i in range(n):
#         L = len(a[i])
#         q = deque()
#
#         def hua(j):  # 窗口右边界滑到j位置
#             l = max(0, j - (w - L))
#             if j < L:
#                 while q and a[i][q[-1]] <= a[i][j]:
#                     q.pop()
#                 q.append(j)
#             while q and q[0] < l:
#                 q.popleft()
#             p = a[i][q[0]]
#             if (j >= L or j < w - L) and p < 0:
#                 p = 0
#             ans[j] += p
#             ans[j + 1] -= p
#
#         for j in range(L):
#             hua(j)
#
#         if w > 2 * L:
#             p = max(0, a[i][q[0]])
#             ans[L] += p
#             ans[w - L] -= p
#
#         for j in range(max(L, w - L), w):
#             hua(j)
#
#     p = [ans[0]]
#     for i in range(1, w):
#         p.append(p[-1] + ans[i])
#     print(*p)


if __name__ == '__main__':
    # n, w = RI()
    # a = []
    # for _ in range(n):
    #     a.append(RILST())
    #     a[-1].pop(0)
    #
    # solve(n, w, a)

    # ### st 779 ms
    # n, w = RI()
    # dff = [0] * (w + 1)
    # for _ in range(n):
    #     L, *a = RILST()
    #     st = SparseTable(a,max)
    #     # print(L,a)
    #     for j in range(L):
    #         l = max(0, j - (w - L))
    #         r = min(j, L - 1)
    #         p = st.query(l, r)
    #         # print(j,l,r,p)
    #         if (j >= L or j < w - L) and p < 0:
    #             p = 0
    #         dff[j] += p
    #         dff[j + 1] -= p
    #     if w > 2 * L:
    #         p = max(0, st.query(0, L - 1))
    #         dff[L] += p
    #         dff[w - L] -= p
    #     for j in range(max(L, w - L), w):
    #         l = max(0, j - (w - L))
    #         r = min(j, L - 1)
    #         p = st.query(l, r)
    #         if (j >= L or j < w - L) and p < 0:
    #             p = 0
    #         dff[j] += p
    #         dff[j + 1] -= p
    #
    # ans = [dff[0]]
    # for i in range(1, w):
    #     ans.append(ans[-1] + dff[i])
    # print(*ans)
    ### 滑窗 514  ms
    n, w = RI()
    d = [0] * (w + 1)
    q = deque()
    for _ in range(n):
        L, *a = RILST()

        # def hua(j):  # 窗口右边界滑到j位置;下边两个for里的代码都可以直接替换为hua(j)
        #     l = max(0, j - (w - L))
        #     if j < L:
        #         while q and a[q[-1]] <= a[j]:
        #             q.pop()
        #         q.append(j)
        #     while q and q[0] < l:
        #         q.popleft()
        #     p = a[q[0]]
        #     if (j >= L or j < w - L) and p < 0:
        #         p = 0
        #     dff[j] += p
        #     dff[j + 1] -= p
        p = w-L
        for j in range(L):
            n = j - p if j - p > 0 else 0
            while q and a[q[-1]] <= a[j]:
                q.pop()
            q.append(j)
            if q[0] < n:
                q.popleft()
            n = a[q[0]]
            if j < w - L and n < 0:
                continue
            d[j] += n
            d[j + 1] -= n

        if w > L << 1 and a[q[0]] > 0:
            d[L] += a[q[0]]
            d[p] -= a[q[0]]

        for j in range(max(L, p), w):
            n = j - p
            if q[0] < n:
                q.popleft()
            n = a[q[0]]
            if n > 0:
                d[j] += n
                d[j + 1] -= n
        q.clear()
    # ans = [dff[0]]
    # for i in range(1, w):
    #     ans.append(ans[-1] + dff[i])
    # print(*ans)
    d.pop()
    print(' '.join(map(str, accumulate(d))))
