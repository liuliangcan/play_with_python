# Problem: C. Flag
# Contest: Codeforces - Codeforces Round 567 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1181/C
# Memory Limit: 512 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/1181/C

输入 n(≤1e3) m(≤1e3) 和一个 n 行 m 列的字符矩阵，元素都是小写字母。

定义「国旗」为一个 3h 行的子矩阵，前 h 行的字符都相同，中间 h 行的字符都相同，后 h 行的字符都相同，它们分别记作 A B C，要求 A 和 B 的字符不同，B 和 C 的字符不同（A 和 C 无要求）。
输出是国旗的子矩阵数量。
输入
4 3
aaa
bbb
ccb
ddd
输出 
6
解释 见右图

输入
6 1
a
a
b
b
c
c
输出 
1
"""
"""https://codeforces.com/contest/1181/submission/198473717

提示 1：枚举子矩阵的右边界（第 j 列）。

提示 2：枚举第 j 列的连续三种字符。
比如这一列从上到下是 aabbbbcccddcc，那么压缩成 abcdc，枚举 abc bcd cdc，这一列上的国旗只会有这三种情况。

提示 3：需要知道从 (i,j) 往左连续出现了多少个相同字符，记作 f[i][j]，这可以递推预处理，或者一边遍历一边算。
这个国旗的最远左边界就是 f[i][j] 的最小值。从最远左边界到 j 都可以作为国旗的左边界，贡献答案。"""


#     280  ms
def solve1():
    n, m = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append(s)
    left = [[1] * m for _ in range(n)]  # g[i][j]向左能找到几个相同的字符，从自己开始算
    up = [[1] * m for _ in range(n)]  # g[i][j]向上能找到几个相同的字符，从自己开始算
    f1 = [[1] * m for _ in range(n)]  # 上缀最小值:g[i][j]向上相邻的字符中(包含自己)，向左相同的最小值，只需要保证最下边这个有效即可
    f2 = [[1] * m for _ in range(n)]  # 下缀最小值:g[i][j]向下相邻的字符中(包含自己)，向左相同的最小值，只需要保证最下边这个有效即可
    for i, row in enumerate(g):
        for j in range(1, m):
            if row[j] == row[j - 1]:
                f1[i][j] = f2[i][j] = left[i][j] = left[i][j - 1] + 1
    for j in range(m):
        for i in range(1, n):
            if g[i][j] == g[i - 1][j]:
                up[i][j] = up[i - 1][j] + 1
                f1[i][j] = min(f1[i][j], f1[i - 1][j])
        for i in range(n - 2, -1, -1):
            if g[i][j] == g[i + 1][j]:
                f2[i][j] = min(f2[i][j], f2[i + 1][j])
    ans = 0

    # 枚举旗帜的右下角那个点，它向上如果是u，则旗帜高3u，且等分；然后看向左能滑多远即可.
    # 关键位置：右下角(i,j),上块右下角(i-2u),中间块右下角(i-i,j)，右上角(i-3*u+1,j)
    for i, row in enumerate(g):
        for j, c in enumerate(row):
            u = up[i][j]
            if i + 1 < u * 3: continue  # 当前排必须超过3个u，即上边必须含3个u
            if up[i - u][j] != u or up[i - u * 2][j] < u:  # 上部分长度需要>=u，中间部分必须是u
                continue
            mn = min(f1[i][j], f1[i - u][j], f2[i - 3 * u + 1][j])
            ans += mn
    print(ans)


#   组合前后缀最小值  233  ms
def solve2():
    n, m = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append(s)
    # left = [[1] * m for _ in range(n)]  # g[i][j]向左能找到几个相同的字符，从自己开始算
    up = [[1] * m for _ in range(n)]  # g[i][j]向上能找到几个相同的字符，从自己开始算
    f1 = [[1] * m for _ in range(n)]  # 上缀最小值:g[i][j]向上相邻的字符中(包含自己)，向左相同的最小值，只需要保证最下边这个有效即可
    f2 = [[1] * m for _ in range(n)]  # 下缀最小值:g[i][j]向下相邻的字符中(包含自己)，向左相同的最小值，只需要保证最下边这个有效即可
    for i, row in enumerate(g):
        for j in range(1, m):
            if row[j] == row[j - 1]:
                # f1[i][j] = f2[i][j] = left[i][j] = left[i][j - 1] + 1
                f1[i][j] = f2[i][j] = f1[i][j - 1] + 1
    for j in range(m):
        for i in range(1, n):
            if g[i][j] == g[i - 1][j]:
                up[i][j] = up[i - 1][j] + 1
                f1[i][j] = min(f1[i][j], f1[i - 1][j])
        for i in range(n - 2, -1, -1):
            if g[i][j] == g[i + 1][j]:
                f2[i][j] = min(f2[i][j], f2[i + 1][j])
    ans = 0

    # 枚举旗帜的右下角那个点，它向上如果是u，则旗帜高3u，且等分；然后看向左能滑多远即可.
    # 关键位置：右下角(i,j),上块右下角(i-2u),中间块右下角(i-i,j)，右上角(i-3*u+1,j)
    for i, row in enumerate(g):
        for j, c in enumerate(row):
            u = up[i][j]
            if i + 1 < u * 3: continue  # 当前排必须超过3个u，即上边必须含3个u
            if up[i - u][j] != u or up[i - u * 2][j] < u:  # 上部分长度需要>=u，中间部分必须是u
                continue
            mn = min(f1[i][j], f1[i - u][j], f2[i - 3 * u + 1][j])
            ans += mn
    print(ans)


#   单调递增队列 311   ms
def solve3():
    n, m = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append(s)
    left = [[1] * m for _ in range(n)]  # g[i][j]向左能找到几个相同的字符，从自己开始算
    up = [[1] * m for _ in range(n)]  # g[i][j]向上能找到几个相同的字符，从自己开始算
    for i, row in enumerate(g):
        for j in range(1, m):
            if row[j] == row[j - 1]:
                left[i][j] = left[i][j - 1] + 1

    for j in range(m):
        for i in range(1, n):
            if g[i][j] == g[i - 1][j]:
                up[i][j] = up[i - 1][j] + 1
    ans = 0

    # 枚举旗帜的右下角那个点，它向上如果是u，则旗帜高3u，且等分；然后看向左能滑多远即可.
    for j in range(m):
        q = deque([0])  # 单增队列求窗口内最小值
        up = [1] * n
        for i in range(1, n):
            if g[i][j] == g[i - 1][j]:
                up[i] += up[i - 1]
            u = up[i]
            while q and left[q[-1]][j] >= left[i][j]:  # 单调递增队列求min，窗口内(队尾)比我大的数全没用
                q.pop()
            q.append(i)

            if i + 1 < u * 3: continue  # 当前排必须超过3个u，即上边必须含3个u
            if up[i - u] != u or up[i - u * 2] < u:  # 上部分长度需要>=u，中间部分必须是u
                continue

            while q[0] <= i - 3 * u:  # 命中了才能pop，一个位置不能作为多个旗帜的右上角；没命中不能pop，wa9，会提前干掉有用信息
                q.popleft()

            ans += left[q[0]][j]
    print(ans)


#   组合前后缀最小值优化空间  233  ms
def solve4():
    n, m = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append(s)
    left = [[1] * m for _ in range(n)]  # g[i][j]向左能找到几个相同的字符，从自己开始算
    # up = [[1] * m for _ in range(n)]  # g[i][j]向上能找到几个相同的字符，从自己开始算
    # f1 = [[1] * m for _ in range(n)]  # 上缀最小值:g[i][j]向上相邻的字符中(包含自己)，向左相同的最小值，只需要保证最下边这个有效即可
    # f2 = [[1] * m for _ in range(n)]  # 下缀最小值:g[i][j]向下相邻的字符中(包含自己)，向左相同的最小值，只需要保证最下边这个有效即可
    for i, row in enumerate(g):
        for j in range(1, m):
            if row[j] == row[j - 1]:
                left[i][j] = left[i][j - 1] + 1
    ans = 0

    # 枚举旗帜的右下角那个点，它向上如果是u，则旗帜高3u，且等分；然后看向左能滑多远即可.
    # 关键位置：右下角(i,j),上块右下角(i-2u),中间块右下角(i-i,j)，右上角(i-3*u+1,j)
    for j in range(m):
        up = [1] * n
        f2 = [row[j] for row in left]  # 下缀最小值
        f1 = f2[:]  # 上缀最小值
        for i in range(n - 2, -1, -1):
            if g[i][j] == g[i + 1][j]:
                f2[i] = min(f2[i], f2[i + 1])

        for i in range(1, n):
            if g[i][j] == g[i - 1][j]:
                up[i] += up[i - 1]
                f1[i] = min(f1[i], f1[i - 1])
            u = up[i]
            if i + 1 < u * 3: continue  # 当前排必须超过3个u，即上边必须含3个u
            if up[i - u] != u or up[i - u * 2] < u:  # 上部分长度需要>=u，中间部分必须是u
                continue
            ans += min(f1[i], f1[i - u], f2[i - 3 * u + 1])

    print(ans)


#   组合前后缀最小值优化空间  171  ms
def solve():
    n, m = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append(s)
    ans = 0

    # 枚举旗帜的右下角那个点，它向上如果是u，则旗帜高3u，且等分；然后看向左能滑多远即可.
    # 关键位置：右下角(i,j),上块右下角(i-2u),中间块右下角(i-i,j)，右上角(i-3*u+1,j)
    left = [1] * n  # 当前列的每行，向左能数几个相同值，显然第一列都是1；其余的dp
    for j in range(m):
        if j > 0:
            for i in range(n):
                if g[i][j] == g[i][j - 1]:
                    left[i] += 1
                else:
                    left[i] = 1
        up = [1] * n  # 当前列向上能数几个相同值
        f2 = left[:]  # 块内下缀最小值
        f1 = left[:]  # 块内上缀最小值
        for i in range(n - 2, -1, -1):
            if g[i][j] == g[i + 1][j]:
                f2[i] = min(f2[i], f2[i + 1])

        for i in range(1, n):
            if g[i][j] == g[i - 1][j]:
                up[i] += up[i - 1]
                f1[i] = min(f1[i], f1[i - 1])
            u = up[i]
            if i + 1 < u * 3: continue  # 当前排必须超过3个u，即上边必须含3个u
            if up[i - u] != u or up[i - u * 2] < u:  # 上部分长度需要>=u，中间部分必须是u
                continue
            ans += min(f1[i], f1[i - u], f2[i - 3 * u + 1])

    print(ans)




#   暴力 枚举中段   ms
def solve9():
    n, m = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append(s)
    ans = 0

    # 枚举旗帜的中段右下角那个点，中段长度如果是u，则，向上走u，向下走u，计算min.
    # 这个复杂度算不明白
    left = [1] * n  # 当前列的每行，向左能数几个相同值，显然第一列都是1；其余的dp
    for j in range(m):
        if j > 0:
            for i in range(n):
                if g[i][j] == g[i][j - 1]:
                    left[i] += 1
                else:
                    left[i] = 1
        up = [1] * n  # 当前列向上能数几个相同值

        for i in range(1, n):
            if g[i][j] == g[i - 1][j]:
                up[i] += up[i - 1]
            if i < n - 1 and g[i][j] == g[i + 1][j]: continue  # 由于是枚举中段，只有下边的值不同才需要讨论
            u = up[i]
            if i + 1 < u * 2: continue  # 即上边高度必须含2个u
            if i + u >= n: continue  # 下边高度必须还有u个
            if len(set(g[k][j] for k in range(i + 1, i + u + 1))) == 1 and len(
                    set(g[k][j] for k in range(i - u * 2 + 1, i - u + 1))) == 1:
                ans += min(left[i - u * 2 + 1:i + u + 1])

    print(ans)


if __name__ == '__main__':
    solve()
