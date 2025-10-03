# Problem: AT_abc009_4 [ABC009D] 漸化式
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/AT_abc009_4
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
from operator import xor, ixor

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
PROBLEM = """
Ai = C1 & A(i-1) ^ .. ^ C(k-1) & A(i-n+1) ^ Ck & A(i-k)  
Ai-1 = (1<<32) -1 ^ ..0..0
..
Ai-k+1 = 0..^ (1<<32) -1 ^ 0
所以矩阵是:(U=(1<<32)-1)
[
[c1,c2...ck],
[U,0,0...0],
[0,U,0...0],
[0,0,U,0..0],
...
[0,0,...U,0]
]
"""

# 800ms
# def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
#     return [[reduce(ixor, (x & y for x, y in zip(row, col))) for col in zip(*b)]
#             for row in a]

# 369ms
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    ret = [[0]*len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                ret[i][j] ^= a[i][k] & b[k][j]
    return ret


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
    k, m = RI()
    a = RILST()
    c = RILST()
    if m <= k:
        return print(a[m - 1])
    U = (1 << 32) - 1
    mat = [c] + [[0] * k for _ in range(k - 1)]
    for i in range(1, k):
        mat[i][i-1] = U
    # for v in mat:
    #     print(v)
    f0 = [[v] for v in a[::-1]]

    fn = pow_mul(mat, m - k, f0)
    print(fn[0][0])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
