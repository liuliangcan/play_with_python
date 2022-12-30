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
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    # input_int = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    input_int = sys.stdin.buffer.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

# MOD = 10 ** 9 + 7
MOD = 998244353
"""https://codeforces.com/problemset/problem/1066/E

输入 n (≤2e5) 和 m (≤2e5)，以及两个长度分别为 n 和 m 的二进制数 a 和 b。

然后执行如下计算：
ans = 0
while b > 0:
    ans += a & b
    b >>= 1

输出 ans % 998244353 的结果。

输入
4 4
1010
1101
输出 12

输入
4 5
1001
10101
输出 11
"""


# TLE
def solve1(n, m, a, b):
    ans = 0
    a = int(a, 2)
    b = int(b, 2)

    while b > 0:
        ans = (ans + (a & b)) % MOD
        b >>= 1
    print(ans)


# 93 ms  前缀和构造答案数组
def solve2(n, m, a, b):
    a = list(map(int, a))
    b = list(accumulate(map(int, b)))
    ans = [0] * n
    if m >= n:
        for i in range(n):
            ans[i] = a[i] * b[i + m - n]
    else:
        for i in range(n - m, n):
            ans[i] = a[i] * b[i - n + m]
    ret = 0
    for v in ans:
        ret = (ret * 2 + v) % MOD

    print(ret % MOD)


# 93 ms  前缀和+直接算答案
def solve3(n, m, a, b):
    b = list(accumulate(map(int, b)))
    ret = 0
    if m >= n:
        for i in range(n):
            ret = (ret * 2 + int(a[i]) * b[i + m - n]) % MOD
    else:
        for i in range(n - m, n):
            ret = (ret * 2 + int(a[i]) * b[i - n + m]) % MOD

    print(ret % MOD)


# 109 ms  两种情况合并
def solve4(n, m, a, b):
    b = list(accumulate(map(int, b)))
    ret = 0
    for i in range(max(n - m, 0), n):
        ret = (ret * 2 + int(a[i]) * b[i - n + m]) % MOD
    print(ret % MOD)


# 93 ms  一次遍历同时计算前缀和+答案，空间O(1)
def solve5(n, m, a, b):
    ret = 0
    c = m - n
    s = 0 if c <= 0 else sum(map(int, b[:c]))
    for i in range(max(n - m, 0), n):
        s += int(b[i + c])
        ret = (ret * 2 + int(a[i]) * s) % MOD

    print(ret % MOD)


# 93 ms  减少强制类型转换 p用没有
def solve(n, m, a, b):
    ret = 0
    c = m - n
    # s = 0 if c <= 0 else sum(map(int, b[:c]))
    s = 0
    if c > 0:
        for i in range(c):
            if b[i] == '1':
                s += 1
    for i in range(max(n - m, 0), n):
        if b[i + c] == '1':
            s += 1

        ret = ((ret * 2 + s) % MOD) if a[i] == '1' else (ret * 2 % MOD)

    print(ret % MOD)


# 92 ms  不trip
def solve7(n, m):
    a = input()
    b = input()
    ret = 0
    c = m - n
    s = 0 if c <= 0 else sum(map(int, b[:c]))
    for i in range(max(n - m, 0), n):
        s += int(b[i + c])
        ret = (ret * 2 + int(a[i]) * s) % MOD

    print(ret % MOD)


if __name__ == '__main__':
    n, m = RI()

    a, = RS()
    b, = RS()

    solve(n, m, a, b)
    # solve(n, m)
