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

if sys.hexversion == 50923504:
    sys.stdin = open('cfinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1400/D

输入 t (≤100) 表示 t 组数据，每组数据输入 n (4≤n≤3000) 和一个长为 n 的数组 a (1≤a[i]≤n)，下标从 1 开始。所有数据的 n 之和 ≤3000。
对每组数据，输出满足 1≤i<j<k<l≤n 且 a[i]=a[k] 且 a[j]=a[l] 的四元组 (i,j,k,l) 的数量。

相似题目 https://codeforces.com/contest/1677/problem/A
"""

D = list(range(1, 6))


# 124 ms
def solve1(n, a):
    if n == 1:
        return print(1)
    b = [1] * n
    if a[0] > a[1]:
        b[0] = 5

    for i in range(1, n):
        x, y = a[i - 1], a[i]
        if y < x:  # 降
            b[i] = b[i - 1] - 1
            if b[i] < 1:
                return print(-1)
            if i < n - 1:
                if y < a[i + 1]:  # i是谷，则直接置1最优
                    b[i] = 1
                elif y == a[i + 1]:
                    # i和右边相同:
                    # 若i+1后要降，则i+1置5最优，i置1;
                    # 若后边升，不操作:i+1尽量小(1)优，i不变(不要趋向1,但可能已经是1，则i+1只能是2)
                    if i < n - 2 and a[i + 1] > a[i + 2]:
                        b[i] = 1
        elif y > x:  # 升
            b[i] = b[i - 1] + 1
            if b[i] > 5:
                return print(-1)
            if i < n - 1:
                if y > a[i + 1]:
                    b[i] = 5
                elif y == a[i + 1]:
                    if i < n - 2 and a[i + 1] < a[i + 2]:
                        b[i] = 5
        else:  # 相同
            b[i] = 3 if b[i - 1] == 2 else 2  # 先随便置一个数
            if i < n - 1:
                if y < a[i + 1]:  # 若后边升，则置尽量小1/2
                    b[i] = 2 if b[i - 1] == 1 else 1
                elif y > a[i + 1]:  # 若后边降，则置尽量大5/4
                    b[i] = 4 if b[i - 1] == 5 else 5
                # else:  # 若相同，置一个不耽误右边值变成1/5的数(2/3/4任选)
                #     b[i] = 3 if b[i - 1] == 2 else 2

    print(' '.join(map(str, b)))


# 	389 ms
def solve2(n, a):
    if n == 1:
        return print(1)
    f = [[0] * 5 for _ in range(n)]
    f[0] = [1] * 5
    for i in range(1, n):
        x, y = a[i - 1], a[i]
        flag = 0
        if y < x:  # 降
            for j in range(5):
                if any(k for k in f[i - 1][j + 1:]):
                    f[i][j] = 1
                    flag = 1
        elif y > x:
            for j in range(5):
                if any(k for k in f[i - 1][:j]):
                    f[i][j] = 1
                    flag = 1
        else:
            for j in range(5):
                if any(f[i - 1][k] for k in range(5) if k != j):
                    f[i][j] = 1
                    flag = 1
        if not flag:
            return print(-1)
    # print(f)
    b = [f[-1].index(1)]
    for i in range(n - 2, -1, -1):
        x, y = a[i], a[i + 1]
        for j in range(5):
            if f[i][j] and ((x < y and j < b[-1]) or (x > y and j > b[-1]) or (x == y and j != b[-1])):
                b.append(j)
                break
    # print(b)
    print(' '.join(map(lambda x: str(x + 1), b[::-1])))

# dfs爆栈
def solve(n, a):
    bo = [1] * n
    up = [5] * n
    for i in range(1, n):
        x, y = a[i - 1], a[i]
        if y > x:
            bo[i] = bo[i - 1] + 1
        elif y < x:
            up[i] = up[i - 1] - 1
        if up[i] < bo[i]:
            return print(-1)

    for i in range(n - 2, -1, -1):
        x, y = a[i], a[i + 1]
        if x > y:
            bo[i] = bo[i + 1] + 1
        elif x < y:
            up[i] = up[i + 1] - 1

        if up[i] < bo[i]:
            return print(-1)
    b = [0] * n
    sys.setrecursionlimit(n + 10)

    def dfs(i):
        # print(b)
        if i == n:
            return True
        for j in range(bo[i], up[i] + 1):
            if i > 0:
                if a[i] == a[i - 1] and j == b[i - 1]:
                    continue
                if a[i] > a[i - 1] and j <= b[i - 1]:
                    continue
                # if i==3 :
                #     print(a[i] ,a[i - 1] , j , b[i])
                if a[i] < a[i - 1] and j >= b[i - 1]:
                    break
            b[i] = j
            if dfs(i + 1):
                return True
        return False

    if dfs(0):
        print(' '.join(map(str, b)))
    else:
        print(-1)
# 249	 ms
def solve(n, a):
    if n == 1:
        return print(1)
    f = [[0] * 5 for _ in range(n)]
    f[0] = [1] * 5
    for i in range(1, n):
        x, y = a[i - 1], a[i]
        flag = 0
        g = f[i-1]
        if y < x:  # 降
            for j in range(5):
                for k in range(j + 1, 5):
                    if g[k]:
                        flag = f[i][j] = 1
                        break

        elif y > x:
            for j in range(5):
                for k in range(j - 1, -1, -1):
                    if g[k]:
                        flag = f[i][j] = 1
                        break

        else:
            for j in range(5):
                for k in range(5):
                    if k != j and g[k]:
                        flag = f[i][j] = 1
                        break
        if not flag:
            return print(-1)
    # print(f)
    b = [f[-1].index(1)]
    for i in range(n - 2, -1, -1):
        x, y = a[i], a[i + 1]
        for j in range(5):
            if f[i][j] and ((x < y and j < b[-1]) or (x > y and j > b[-1]) or (x == y and j != b[-1])):
                b.append(j)
                break
    # print(b)
    print(' '.join(map(lambda x: str(x + 1), b[::-1])))


if __name__ == '__main__':
    n, = RI()
    a = RILST()

    solve(n, a)
