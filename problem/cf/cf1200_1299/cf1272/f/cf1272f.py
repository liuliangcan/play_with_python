# Problem: F. Two Bracket Sequences
# Contest: Codeforces - Codeforces Round 605 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1272/F
# Memory Limit: 512 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/1272/F

输入两个长度不超过 200 的字符串 s 和 t，只包含左右括号。
输出 s 和 t 的最短公共超序列，要求这个超序列是一个合法括号字符串。
关于最短公共超序列，见 1092. 最短公共超序列
输入
(())(()
()))()
输出 (())()()

输入
)
((
输出 (())

输入
)
)))
输出 ((()))

输入
())
(()(()(()(
输出 (()()()(()()))
"""
"""https://codeforces.com/problemset/submission/1272/208121980

请先看下面这篇题解

https://leetcode.cn/problems/shortest-common-supersequence/solutions/2194615/cong-di-gui-dao-di-tui-jiao-ni-yi-bu-bu-auy8z/

在计算最长公共超序列的基础上，增加一个参数 k 表示左括号比右括号多多少。"""



#   TLE    ms
def solve():
    s, = RS()
    t, = RS()
    m, n = len(s), len(t)
    f = [[[0] * (m + n + 1) for _ in range(n + 1)] for _ in range(m + 1)]
    # f[0][0][0] = (0,0,0)
    s += '1'
    t += '1'
    q = deque([(0, 0, 0)])
    while q:
        i, j, k = q.popleft()
        # if i>=m or j >= n :continue
        x, y, z = i + int(s[i] == '('), j + int(t[j] == '('), k + 1
        if x <= m and y <= n and z <= m + n and not f[x][y][z]:
            f[x][y][z] = (i, j, k)
            q.append((x, y, z))
        x, y, z = i + int(s[i] == ')'), j + int(t[j] == ')'), k - 1
        if x <= m and y <= n and z >= 0 and not f[x][y][z]:
            f[x][y][z] = (i, j, k)
            q.append((x, y, z))
    # print(f)
    ans = []
    i, j, k = m, n, 0
    while i or j or k:
        # print(i,j,k)
        # print(f[i][j][k])
        i, j, z = f[i][j][k]
        if z < k:
            ans.append('(')
        else:
            ans.append(')')
        k = z

    print(''.join(ans[::-1]))

    # print(ss)

# 1653ms
if __name__ == '__main__':
    s, = RS()
    t, = RS()
    m, n = len(s), len(t)
    f = [[[0] * (m + n + 1) for _ in range(n + 1)] for _ in range(m + 1)]
    # f[0][0][0] = (0,0,0)
    s += '1'
    t += '1'
    q = deque([0])
    mask = (1 << 10) - 1
    while q:
        u = q.popleft()
        i, j, k = u >> 20, (u >> 10) & mask, u & mask
        # if i>=m or j >= n :continue
        x, y, z = i + int(s[i] == '('), j + int(t[j] == '('), k + 1
        if z <= m + n and not f[x][y][z]:
            f[x][y][z] = u
            q.append((x << 20) | (y << 10) | z)
        x, y, z = i + int(s[i] == ')'), j + int(t[j] == ')'), k - 1
        if z >= 0 and not f[x][y][z]:
            f[x][y][z] = u
            q.append((x << 20) | (y << 10) | z)
    # print(f)
    ans = []
    i, j, k = m, n, 0
    while i or j or k:
        # print(i,j,k)
        # print(f[i][j][k])
        u = f[i][j][k]
        i, j, z = u >> 20, (u >> 10) & mask, u & mask
        if z < k:
            ans.append('(')
        else:
            ans.append(')')
        k = z

    print(''.join(ans[::-1]))
