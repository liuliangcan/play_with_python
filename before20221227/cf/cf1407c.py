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
"""https://codeforces.com/problemset/problem/1407/D

输入 n(≤3e5) 和一个长为 n 的数组 h (1≤h[i]≤1e9)。
满足如下三个条件之一，就可以从 i 跳到 j (i<j)：
1. i+1=j
2. max(h[i+1],...,h[j-1]) < min(h[i],h[j])
3. min(h[i+1],...,h[j-1]) > max(h[i],h[j])
输出从 1 跳到 n 最少需要多少步。
输入
5
1 3 1 4 5
输出 3

输入
4
4 2 2 4
输出 1

输入
2
1 1
输出 1

输入
5
100 1 100 1 100
输出 2
"""


#  296 	 ms
def solve1(n, h):
    lless = [-1] * n  # 每个数左边最近比它小或等于的数
    lbig = [-1] * n  # 每个数左边最近比它大或等于的数
    rless = [n] * n  # 每个数右边最近比它小或等于的数
    rbig = [n] * n  # 每个数右边最近比它大或等于的数
    stless = []  # 单调不降栈
    stbig = []  # 单调不升栈
    for i, v in enumerate(h):
        while stless and h[stless[-1]] > v:
            stless.pop()
        if stless:
            lless[i] = stless[-1]
        stless.append(i)
        while stbig and h[stbig[-1]] < v:
            stbig.pop()
        if stbig:
            lbig[i] = stbig[-1]
        stbig.append(i)
    # print(lless,lbig)
    stless, stbig = [], []
    for i in range(n - 1, -1, -1):
        v = h[i]
        while stless and h[stless[-1]] > v:
            stless.pop()
        if stless:
            rless[i] = stless[-1]
        stless.append(i)
        while stbig and h[stbig[-1]] < v:
            stbig.pop()
        if stbig:
            rbig[i] = stbig[-1]
        stbig.append(i)
    # print(rless,rbig)
    f = [n] + list(range(n)) + [n]  # f[i] 从1转移到i(i从1计数)需要的最小步数 f:len=n+2,下标[0,n+1] 答案f[n]
    for i in range(1, n + 1):
        f[i] = min(f[i], f[i - 1] + 1)  # rule1 从上一步来
        f[i] = min(f[i], f[lless[i - 1] + 1] + 1)  # rule2 从左边第一个比它小的数来,中间的数均小于它俩
        f[i] = min(f[i], f[lbig[i - 1] + 1] + 1)  # rule3 从左边第一个比它大的数来,中间的数均大于它俩
        f[rless[i - 1] + 1] = min(f[rless[i - 1] + 1], f[i] + 1)  # rule2 可转移到右边第一个比它小的数
        f[rbig[i - 1] + 1] = min(f[rbig[i - 1] + 1], f[i] + 1)  # rule2 可转移到右边第一个比它大的数
        # print(f)

    print(f[n])


# 202 ms
def solve(n, h):
    h = [0] + h
    stless, stbig = [], []
    f = [-1] * (n + 1)  # f[i] 从1转移到i(i从1计数)需要的最小步数 f:len=n+1,下标[0,n] 答案f[n]
    for i in range(1, n + 1):
        f[i] = f[i - 1] + 1  # rule1 从上一步来
        while stless and h[stless[-1]] > h[i]:  # 单调递增栈
            f[i] = min(f[i], f[stless.pop()] + 1)  # 本点作为谷从前边的一个更大谷值更新（但越来越小直至相同
        if stless:
            f[i] = min(f[i], f[stless[-1]] + 1)  # 作为谷从较小或相同的谷值更新,即从栈顶更新;但不会再更进一步,因为对于栈顶k之前的坐标j，（j,i）中的k<=i,
            while stless and h[stless[-1]] == h[i]:  # 相同的高度只有最后一个高度可以被后边的点使用，因此要全干掉
                stless.pop()

        while stbig and h[stbig[-1]] < h[i]:
            f[i] = min(f[i], f[stbig.pop()] + 1)  # 作为峰
        if stbig:
            f[i] = min(f[i], f[stbig[-1]] + 1)
            while stbig and h[stbig[-1]] == h[i]:
                stbig.pop()

        stless.append(i)
        stbig.append(i)
        # print(f)

    print(f[n])


if __name__ == '__main__':
    n, = RI()
    a = RILST()

    solve(n, a)
