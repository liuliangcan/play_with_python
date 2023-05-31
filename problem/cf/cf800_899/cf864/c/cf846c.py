# Problem: C. Four Segments
# Contest: Codeforces - Educational Codeforces Round 28
# URL: https://codeforces.com/contest/846/problem/C
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """https://codeforces.com/contest/846/problem/C

输入 n(1≤n≤5000) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)。
定义 s(i,i)=0, s(i,j)=a[i]+a[i+1]+...+a[j-1]。
计算 s(0,i)-s(i,j)+s(j,k)-s(k,n) 的最大值，其中 0≤i≤j≤k≤n。
你需要输出最大值对应的 i,j,k。
如果有多个满足要求的答案，输出任意一个。

进阶：你能想出一个 O(n) 的算法吗？
输入
3
-1 2 3
输出 0 1 3

输入
4
0 0 -1 0
输出 0 0 0

输入 
1
10000
输出 1 1 1
"""


#       ms
def solveTLe():
    n, = RI()
    a = RILST()
    if n == 1:
        if a[0] >= 0:
            return print(1, 1, 1)
        else:
            return print(0, 0, 0)
    pre = [0] + list(accumulate(a)) + [0]

    def s(i, j):
        return pre[j] - pre[i]

    ans = ss = sum(a)
    x, y, z = n, n, n
    if ss < 0:
        x, y, z = 0, 0, 0
        ans = -ans
    suf = 0
    for k in range(n, -1, -1):
        if k < n:
            suf += a[k]
        for i in range(k + 1):
            for j in range(i, k + 1):
                if pre[i] - (pre[j] - pre[i]) + pre[k] - pre[j] - suf > ans:
                    ans = pre[i] - (pre[j] - pre[i]) + pre[k] - pre[j] - suf
                    x, y, z = i, j, k

    print(x, y, z)
    print(ans)
    i, j, k = 43, 68, 100
    print(s(0, i) - s(i, j) + s(j, k) - s(k, n))
    i, j, k = 43, 68, 98
    print(s(0, i) - s(i, j) + s(j, k) - s(k, n))


#   109    ms
def solve1():
    n, = RI()
    a = RILST()
    if n == 1:
        if a[0] >= 0:
            return print(1, 1, 1)
        else:
            return print(0, 0, 0)
    # pre = [0] + list(accumulate(a))
    f = [0] * n
    start = list(range(n))
    f[0] = a[0]
    for i in range(1, n):
        if f[i - 1] < 0:
            f[i] = f[i - 1] + a[i]
            start[i] = start[i - 1]
        else:
            f[i] = a[i]
    ans = ss = sum(a)
    x, y, z = n, n, n
    if ss < 0:
        x, y, z = 0, 0, 0
        ans = -ans
    suf = 0
    for k in range(n, -1, -1):
        if k < n:
            suf += a[k]
        for i in range(k):
            if f[i] < 0 and ans < ss - 2 * f[i] - 2 * suf:
                ans = ss - 2 * f[i] - 2 * suf
                x, y, z = start[i], i + 1, k

    print(x, y, z)
    # def s(i, j):
    #     return pre[j] - pre[i]
    # print(ans)
    # i,j,k=43,68,98
    # print(s(0,i)-s(i,j)+s(j,k)-s(k,n))
    # i,j,k=44,68,98
    # print(s(0,i)-s(i,j)+s(j,k)-s(k,n))


#   O(n) 93    ms
def solve2():
    n, = RI()
    a = RILST()
    if n == 1:
        if a[0] >= 0:
            return print(1, 1, 1)
        else:
            return print(0, 0, 0)
    f = [0] * n  # 最小子段和
    start = list(range(n))
    f[0] = a[0]
    pre = list(range(n))  # 前缀最小子段和的f下标
    for i in range(1, n):
        if f[i - 1] < 0:
            f[i] = f[i - 1] + a[i]
            start[i] = start[i - 1]
        else:
            f[i] = a[i]
        if f[i] < f[pre[i - 1]]:
            pre[i] = i
        else:
            pre[i] = pre[i - 1]
    ans = ss = sum(a)
    x, y, z = n, n, n
    if ss < 0:  # 讨论整段正/负的情况
        x, y, z = 0, 0, 0
        ans = -ans
    suf = 0
    for k in range(n, 0, -1):  # 枚举尾段k~n；在前边找最小子段，那么结果就是ss-2*s(i,j)-2*s(k,n)
        if k < n:
            suf += a[k]

        i = pre[k - 1]
        if f[i] < 0 and ans < ss - 2 * f[i] - 2 * suf:  # 只需要讨论负数段
            ans = ss - 2 * f[i] - 2 * suf
            x, y, z = start[i], i + 1, k

    print(x, y, z)


#   O(n) 77    ms
def solve3():
    """计算最小子段和作为s(i,j)，枚举k，那么ans=sum(a)-2s(i,j)-2(j,n);对最小子段和求个前缀最小则可以做到O(n)
    换言之就是找两个最小的负数段，第二段必须连着n
    """
    n, = RI()
    a = RILST()
    if n == 1:
        if a[0] >= 0:
            return print(1, 1, 1)
        else:
            return print(0, 0, 0)
    f = [0] * n  # 以i为结尾的最小子段和
    start = list(range(n))  # 每个最小子段的起始下标（左端点
    f[0] = a[0]
    pre = list(range(n))  # 前缀最小子段和的f下标
    for i in range(1, n):
        if f[i - 1] < 0:  # 计算最小子段和，只有前边是负数才会贡献，继承左端点
            f[i] = f[i - 1] + a[i]
            start[i] = start[i - 1]
        else:
            f[i] = a[i]
        if f[i] < f[pre[i - 1]]:
            pre[i] = i
        else:
            pre[i] = pre[i - 1]
    ans = ss = sum(a)
    x, y, z = n, n, n
    if ss < 0:  # 讨论整段正/负的情况
        x, y, z = 0, 0, 0
        ans = -ans
    suf = 0
    a.append(0)  # 加个哨兵，这样k就可以从n开始不用额外if
    for k in range(n, 0, -1):  # 枚举尾段k~n；在前边找最小子段，那么结果就是ss-2*s(i,j)-2*s(k,n)
        suf += a[k]
        i = pre[k - 1]
        if f[i] < 0 and ans < ss - 2 * f[i] - 2 * suf:  # 只需要讨论负数段
            ans = ss - 2 * f[i] - 2 * suf
            x, y, z = start[i], i + 1, k

    print(x, y, z)


#   93   ms
def solve():
    """https://codeforces.com/contest/846/submission/207819522

用前缀和将 s(0,i)-s(i,j)+s(j,k)-s(k,n) 变成
2*(s[i]-s[j]+s[k])-s[n]。
转换成求 s[i]-s[j]+s[k] 的最大值。
前后缀分解，计算 s 的前缀最大值和后缀最大值，然后枚举 s[j]。"""
    n, = RI()
    a = RILST()
    if n == 1:
        if a[0] >= 0:
            return print(1, 1, 1)
        else:
            return print(0, 0, 0)
    pre = [0] + list(accumulate(a))
    p = pre[:]
    for i in range(1, n + 1):
        if pre[i] > pre[p[i - 1]]:
            p[i] = i
        else:
            p[i] = p[i - 1]
    ans = ss = sum(a)
    x, y, z = n, n, n
    if ss < 0:  # 讨论整段正/负的情况
        x, y, z = 0, 0, 0
        ans = -ans
    sufi = n
    for j in range(n, -1, -1):
        if pre[j] > pre[sufi]:
            sufi = j
        if ans < (pre[p[j]] - pre[j] + pre[sufi]) * 2 - pre[n]:
            ans = (pre[p[j]] - pre[j] + pre[sufi]) * 2 - pre[n]
            x, y, z = p[j], j, sufi

    print(x, y, z)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
