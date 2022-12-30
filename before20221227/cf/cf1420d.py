import sys
from collections import *
from itertools import *
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

# MOD = 10 ** 9 + 7
MOD = 998244353
"""https://codeforces.com/problemset/problem/1420/D

输入 n, k (1≤k≤n≤3e5) 和 n 个闭区间，区间的范围在 [1,1e9]。
你需要从 n 个区间中选择 k 个区间，且这 k 个区间的交集不为空。
输出方案数模 998244353 的结果。
输入
7 3
1 7
3 8
4 5
6 7
1 3
5 10
8 9
输出 9

输入
3 1
1 1
2 2
3 3
输出 3

输入
3 2
1 1
2 2
3 3
输出 0

输入
3 3
1 3
2 3
3 3
输出 1

输入
5 2
1 3
2 4
3 5
4 6
5 7
输出 7
"""


#  1778 	 ms
def solve1(n, k, lr):
    def quick_pow_mod(a, b, p):
        ans = 1
        while b:
            if b & 1:
                ans = (ans * a) % p
            a = (a * a) % p
            b >>= 1
        return ans

    MAX_N = n + 1
    inv_f, fact = [1] * MAX_N, [1] * MAX_N
    p = MOD
    for i in range(2, MAX_N):
        fact[i] = i * fact[i - 1] % p
    inv_f[MAX_N - 1] = pow(fact[MAX_N - 1], p - 2, p)
    for i in range(MAX_N - 1, 0, -1):
        inv_f[i - 1] = inv_f[i] * i % p

    def get_c(m, r):
        if m < r or r < 0:
            return 0
        # 公式C(m,r) = m!//(r!*(m-r)!)
        return fact[m] * inv_f[r] % p * inv_f[m - r] % p

    lr.sort()
    h = []
    ans = 0
    for l, r in lr:
        while h and h[0] < l:
            heapq.heappop(h)
        if len(h) >= k - 1:
            ans = (ans + get_c(len(h), k - 1)) % MOD
        heapq.heappush(h, r)
    print(ans)


#  358  	 ms
def solve2(n, k, lr):
    def quick_pow_mod(a, b, p):
        ans = 1
        while b:
            if b & 1:
                ans = (ans * a) % p
            a = (a * a) % p
            b >>= 1
        return ans

    MAX_N = n + 1
    inv_f, fact = [1] * MAX_N, [1] * MAX_N
    p = MOD
    for i in range(2, MAX_N):
        fact[i] = i * fact[i - 1] % p
    inv_f[MAX_N - 1] = pow(fact[MAX_N - 1], p - 2, p)
    for i in range(MAX_N - 1, 0, -1):
        inv_f[i - 1] = inv_f[i] * i % p

    def get_c(m, r):
        if m < r or r < 0:
            return 0
        # 公式C(m,r) = m!//(r!*(m-r)!)
        return fact[m] * inv_f[r] % p * inv_f[m - r] % p

    l, r = [], []
    for a, b in lr:
        l.append(a)
        r.append(b)
    l.sort()
    r.sort()
    i = j = s = 0
    ans = 0
    while i < n and j < n:
        if l[i] <= r[j]:
            ans = (ans + get_c(s, k - 1)) % MOD
            i += 1
            s += 1
        else:
            j += 1
            s -= 1

    print(ans)

# 514 ms
def solve(n, k, lr):
    def quick_pow_mod(a, b, p):
        ans = 1
        while b:
            if b & 1:
                ans = (ans * a) % p
            a = (a * a) % p
            b >>= 1
        return ans

    MAX_N = n + 1
    inv_f, fact = [1] * MAX_N, [1] * MAX_N
    p = MOD
    for i in range(2, MAX_N):
        fact[i] = i * fact[i - 1] % p
    inv_f[MAX_N - 1] = pow(fact[MAX_N - 1], p - 2, p)
    for i in range(MAX_N - 1, 0, -1):
        inv_f[i - 1] = inv_f[i] * i % p

    def get_c(m, r):
        if m < r or r < 0:
            return 0
        # 公式C(m,r) = m!//(r!*(m-r)!)
        return fact[m] * inv_f[r] % p * inv_f[m - r] % p

    x = []
    for a, b in lr:
        x.append(a << 1)
        x.append(b << 1 | 1)
    x.sort()
    s = ans = 0
    for i in x:
        if i & 1:
            s -= 1
        else:
            ans = (ans + get_c(s, k - 1)) % MOD
            s += 1

    print(ans)


if __name__ == '__main__':
    n, k = RI()
    lr = []
    for _ in range(n):
        lr.append(RILST())

    solve(n, k, lr)
