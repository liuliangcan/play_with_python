# Problem: E. Xor-sequences
# Contest: Codeforces - Educational Codeforces Round 14
# URL: https://codeforces.com/problemset/problem/691/E
# Memory Limit: 256 MB
# Time Limit: 3000 ms

import sys
from functools import reduce
from operator import iadd

from typing import List

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RILST = lambda: list(RI())
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/691/E

输入 n(1≤n≤100) k(1≤k≤1e18) 和长为 n 的数组 a(0≤a[i]≤1e18)。

构造一个长为 k 的数组 b，每个 b[i] 都等于 a 中的某个数，且对于 b 中任意相邻元素 (x,y)，都满足 x XOR y 中的 1 的个数是 3 的倍数。

输出有多少个不同的数组 b，模 1e9+7。
注意：即使元素值相同，但选自 a 的位置不同，也算不同的 b。例如 a=[1,1]，k=1，有两个不同的 b=[1]。
输入
5 2
15 1 2 4 8
输出 13

输入
5 1
15 1 2 4 8
输出 5
"""


# 缓存友好写法
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    n, z = len(b[0]), len(a[0])
    ret = [[0] * n for _ in range(len(a))]
    for row1, row2 in zip(ret, a):
        for j in range(n):
            for k in range(z):
                row1[j] = (row1[j] + row2[k] * b[k][j]) % MOD
    return ret


def mul2(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    res = [[0] * len(B[0]) for _ in [None] * len(A)]
    for i, resi in enumerate(res):
        for k, aik in enumerate(A[i]):
            for j, bkj in enumerate(B[k]):
                resi[j] = (resi[j] + aik * bkj) % MOD
    return res


# a^n @ f1
def pow_mul(a: List[List[int]], n: int, f1: List[List[int]]) -> List[List[int]]:
    res = f1
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res


def mul_lat(a: List[int], b: List[int], r: int) -> List[int]:
    n = len(b) // r
    ret = [0] * len(b)
    for i in range(len(a) // r):
        for j in range(n):
            for k in range(r):
                ret[i * n + j] += a[i * r + k] * b[k * n + j]
                ret[i * n + j] %= MOD
    return ret


def pow_mul_flat(a: List[List[int]], n: int, f1: List[List[int]]) -> List[List[int]]:
    r = len(a)
    a = reduce(iadd, a, [])
    f1 = reduce(iadd, f1, [])
    res = f1
    while n:
        if n & 1:
            res = mul_lat(a, res, r)
        a = mul_lat(a, a, r)
        n >>= 1

    return [[v] for v in res]


#       ms
def solve():
    n, k = RI()
    a = RILST()
    m = [[0] * n for _ in range(n)]
    for i, x in enumerate(a):
        for j, y in enumerate(a):
            if (x ^ y).bit_count() % 3 == 0:
                m[i][j] = 1
    f1 = [[1]] * n
    fk = pow_mul_flat(m, k - 1, f1)

    print(sum(f[0] for f in fk) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
