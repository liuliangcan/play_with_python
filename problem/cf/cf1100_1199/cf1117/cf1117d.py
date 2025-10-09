# Problem: D. Magic Gems
# Contest: Codeforces - Educational Codeforces Round 60 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1117/D
# Memory Limit: 256 MB
# Time Limit: 3000 ms

import sys

from types import GeneratorType
import bisect
import io, os
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from contextlib import redirect_stdout
from itertools import accumulate, combinations, permutations
# combinations(a,k)a序列选k个 组合迭代器
# permutations(a,k)a序列选k个 排列迭代器
from array import *
from functools import lru_cache, reduce
from heapq import heapify, heappop, heappush
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from random import randint, choice, shuffle, randrange
# randint(a,b)从[a,b]范围随机选择一个数
# choice(seq)seq可以是一个列表,元组或字符串,从seq中随机选取一个元素
# shuffle(x)将一个可变的序列x中的元素打乱
from string import ascii_lowercase, ascii_uppercase, digits
# 小写字母，大写字母，十进制数字
from decimal import Decimal, getcontext
from typing import List

# Decimal(s) 实例化Decimal对象,一般使用字符串
# getcontext().prec=100 修改精度
# sys.setrecursionlimit(10**6) #调整栈空间
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
# DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')  # cf突然编不过这行了
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1117/D

输入 n(1≤n≤1e18) m(2≤m≤100)。

构造一个数组 a，只包含 1 和 m，且 sum(a) = n。
输出方案数，模 1e9+7。

注意元素顺序不同，也算不同的数组，比如 [1,1,m] 和 [m,1,1] 是不同的数组。
输入 4 2
输出 5

输入 3 2
输出 3
"""


# # a @ b，其中 @ 是矩阵乘法,这个不一定快
# def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
#     return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
#             for row in a]

def mul1(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    ret = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                ret[i][j] = (ret[i][j] + a[i][k] * b[k][j]) % MOD

    return ret


def mul2(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    ret = [[0] * len(b[0]) for _ in range(len(a))]
    for i, row in enumerate(ret):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                row[j] = (row[j] + a[i][k] * b[k][j]) % MOD

    return ret


def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    ret = [[0] * len(b[0]) for _ in range(len(a))]
    n, z = len(b[0]), len(a[0])
    for row1, row2 in zip(ret, a):
        for j in range(n):
            for k in range(z):
                row1[j] = (row1[j] + row2[k] * b[k][j]) % MOD
    return ret


# def mul(A,B):
#     res = [[0]*len(B[0]) for _ in range(len(A))]
#     for i, row in enumerate(res):
#         for k,a in enumerate(A[i]):
#             for j,b in enumerate(B[k]):
#                 row[j] += a*b
#                 row[j] %= MOD
#     return res

# a^n @ f1
def pow_mul(a: List[List[int]], n: int, f1: List[List[int]]) -> List[List[int]]:
    res = f1
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res


#       ms
def solve():
    n, m = RI()
    """
    f[0] = 1
    f[1~m-1] = 1
    
    f[i] = f[i-1]+0+0+..+0+ f[i-m]
    f[i-1] = f[i-1] + 0+.. + 0
    f[i-m+1] = 0+0+ ..+ 0+ f[i-m+1] + 0
    """
    if n < m:
        return print(1)
    mat = [[0] * m for _ in range(m)]
    mat[0][0] = mat[0][m - 1] = 1
    for i in range(1, m):
        mat[i][i - 1] = 1
    fm1 = [[1] for _ in range(m)]
    fn = pow_mul(mat, n - m + 1, fm1)
    print(fn[0][0])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
