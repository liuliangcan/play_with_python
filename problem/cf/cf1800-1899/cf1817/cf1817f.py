# Problem: F. Vasilije Loves Number Theory
# Contest: Codeforces - Codeforces Round 900 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1878/F
# Memory Limit: 256 MB
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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1878/F

定义 d(N) 为 N 的因子个数。
输入 T(≤100) 表示 T 组数据。所有数据的 q 之和 ≤1000。
每组数据输入 n0(1≤n0≤1e6) q(1≤q≤1000) 以及 q 个询问。
初始化 n=n0。
然后输入 q 个询问，格式如下：
"1 x" (1≤x≤1e6)：把 n 更新为 n*x，同时询问：是否存在一个正整数 a，满足 gcd(n,a)=1 且 d(n*a)=n？输出 YES 或 NO。
"2"：把 n 更新为 n0。
保证任何时刻 d(n)≤1e9。

样例太长，请在原题查看。

输入
7
1 5
1 1
1 2
2
1 8
1 9
20 4
1 3
2
1 7
1 12
16 10
1 6
1 6
1 10
1 9
1 1
1 9
1 7
1 3
1 2
1 10
9 1
1 3
8 1
1 2
8 3
1 5
1 8
1 10
11 5
1 8
1 2
1 1
1 3
1 1
输出
YES
YES
YES
YES

YES
NO
YES

YES
NO
YES
YES
YES
NO
YES
NO
YES
YES

NO

NO

YES
NO
NO

YES
NO
NO
NO
NO
"""


class PrimeTable:
    def __init__(self, n: int) -> None:
        self.n = n
        self.primes = primes = []  # 所有n以内的质数
        self.min_div = min_div = [0] * (n + 1)  # md[i]代表i的最小(质)因子
        min_div[1] = 1

        # 欧拉筛O(n)，顺便求出min_div
        for i in range(2, n + 1):
            if not min_div[i]:
                primes.append(i)
                min_div[i] = i
            for p in primes:
                if i * p > n: break
                min_div[i * p] = p
                if i % p == 0:
                    break

    def is_prime(self, x: int):
        """检测是否是质数，最坏是O(sqrt(x)"""
        if x < 3: return x == 2
        if x <= self.n: return self.min_div[x] == x
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0: return False
        return True

    def prime_factorization(self, x: int):
        """分解质因数，复杂度；建议x不要超过n^2,这样可以在prime里枚举
        1. 若x>n则需要从2模拟到sqrt(x)，如果中间x降到n以下则走2；最坏情况，不含低于n的因数，则需要开方复杂度
        2. 否则x质因数的个数，那么最多就是O(lgx)"""
        n, min_div = self.n, self.min_div
        for p in self.primes:  # 在2~sqrt(x)的质数表上遍历，会快一些
            if x <= n or p * p > x:
                break
            if x % p == 0:
                cnt = 0
                while x % p == 0: cnt += 1; x //= p
                yield p, cnt
        if x > n * n:
            for p in range(n, int(x ** 0.5) + 1):  # 分解质因数不要直接遍历2~sqrt(x)的自然数，
                if x <= n: break
                if x % p == 0:
                    cnt = 0
                    while x % p == 0: cnt += 1; x //= p
                    yield p, cnt
        while 1 < x <= n:
            p, cnt = min_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= n and x > 1:
            yield x, 1

    def get_factors(self, x: int):
        """求x的所有因数，包括1和x"""
        factors = [1]
        for p, b in self.prime_factorization(x):
            n = len(factors)
            for j in range(1, b + 1):
                for d in factors[:n]:
                    factors.append(d * (p ** j))
        return factors


pt = PrimeTable(10 ** 5 + 5)


#       ms
def solve():
    n0, q = RI()
    cnt = Counter()
    for x, y in pt.prime_factorization(n0):
        cnt[x] = y
    d0 = 1
    for y in cnt.values():
        d0 *= y + 1
    cur = cnt.copy()
    dn = d0
    for _ in range(q):
        t, *a = RI()
        if t == 2:
            cur = cnt.copy()
            dn = d0
        else:
            x = int(a.pop())
            for k, v in pt.prime_factorization(x):
                dn //= cur[k] + 1
                cur[k] += v
                dn *= cur[k] + 1
            t = dn
            for k, v in cur.items():
                c = 0
                while t % k == 0:
                    t //= k
                    c += 1
                if c > v:
                    print('NO')
                    break
            else:
                print('YES' if t == 1 else 'NO')
    print('')
def solve1():
    n0, q = RI()
    cnt = Counter()
    for x, y in pt.prime_factorization(n0):
        cnt[x] = y
    d0 = 1
    for y in cnt.values():
        d0 *= y + 1
    cur = cnt.copy()
    dn = d0
    for _ in range(q):
        t, *a = RI()
        if t == 2:
            cur = cnt.copy()
            dn = d0
        else:
            x = int(a.pop())
            for k, v in pt.prime_factorization(x):
                dn //= cur[k] + 1
                cur[k] += v
                dn *= cur[k] + 1
            for k, v in pt.prime_factorization(dn):
                if v > cur[k]:
                    print('NO')
                    break
            else:
                print('YES')
    print('')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
