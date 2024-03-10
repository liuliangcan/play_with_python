# Problem: 数学家的四不要
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/76681/F
# Memory Limit: 131072 MB
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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
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

    def mr_is_prime(self, x):
        """
        Miller-Rabin 检测. 检测x是否是质数，置信度: 1 - (1/4)^k. 复杂度k*log^3
        但是longlong以内可以用k==3或7的代价，换取100%置信度
        https://zhuanlan.zhihu.com/p/349360074
        """
        if x < 3 or x % 2 == 0:
            return x == 2
        if x % 3 == 0:
            return x == 3

        u, t = x - 1, 0
        while not u & 1:
            u >>= 1
            t += 1
        ud = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)  # long long 返回用这个7个数检测100%正确
        # ud = (2, 7, 61)  # int 返回用这3个数检测100%正确
        # for _ in range(k):
        #     a = random.randint(2, x - 2)
        for a in ud:
            v = pow(a, u, x)
            if v == 1 or v == x - 1 or v == 0:
                continue
            for j in range(1, t + 1):
                v = v * v % x
                if v == x - 1 and j != t:
                    v = 1
                    break
                if v == 1:
                    return False
            if v != 1:
                return False
        return True
# ans, n = 1, 20
# print("1:" + str(ans))
# for i in range(2, n + 1):
#     ans = ans * (4 * i - 2) // (i + 1)
#     print(str(i) + ":" + str(ans),4 * i - 2,i+1)
#       ms
def solve():
    n, = RI()
    pt = PrimeTable(n)
    ans = [1]*(n+1)
    s = 0

    c = 1
    for i in range(n+1):
        if not i&1 or pt.is_prime(i):
            ans[i] = 0
        s += i
        if s <= n:
            ans[s] = 0
        if i >= 2 and c <= n:
            # print(i-1,c,4*i-2,i+1)
            c = c*(4*i-2)//(i+1)
            # print(i,c)
            if c <= n:
                ans[c] = 0
    if n >= 1:
        ans[1] = 0
    # print(ans)
    print(sum(ans))




if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
