# Problem: G. Skibidus and Capping
# Contest: Codeforces - Codeforces Round 1003 (Div. 4)
# URL: https://codeforces.com/problemset/problem/2065/G
# Memory Limit: 256 MB
# Time Limit: 2000 ms

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

# Decimal(s) 实例化Decimal对象,一般使用字符串
# getcontext().prec=100 修改精度
# sys.setrecursionlimit(10**6) #调整栈空间
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/2065/G

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(2≤n≤2e5) 和长为 n 的数组 a(2≤a[i]≤n)。

如果 x 能表示为两个质数的乘积（两个质数可以相等），那么称 x 为半质数。
输出有多少对 (i,j) 满足 i <= j 且 LCM(a[i], a[j]) 是半质数。
输入
3
4
2 2 3 4
6
2 2 3 4 5 6
9
2 2 4 5 7 8 9 3 5
输出
5
12
18
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


pt = PrimeTable(2 * 10 ** 5 + 1)


#   234    ms
def solve():
    n, = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    cnt2 = [0] * (n + 1)
    s = ans = 0  # 质数总数
    for v in a:
        cnt[v] += 1
        if pt.is_prime(v):
            s += 1
            ans += s - cnt[v] + cnt2[v]
        else:
            x = pt.min_div[v]
            y = v // x
            if not pt.is_prime(y): continue
            if x == y:
                ans += cnt[v] + cnt[x]
                cnt2[x] += 1
            else:
                ans += cnt[x] + cnt[y] + cnt[v]
                cnt2[x] += 1
                cnt2[y] += 1
    print(ans)


#   296    ms
def solve1():
    n, = RI()
    a = RILST()
    p1 = [0] * (n + 1)  # 质数的数量
    s1 = ans = 0  # 质数总数
    p2 = [defaultdict(int) for _ in range(n + 1)]  # 含v的半质数，另一个因子的数量
    p2v = [0] * (n + 1)  # 含v的半质数数量
    for v in a:
        if pt.is_prime(v):
            s1 += 1
            p1[v] += 1
            ans += s1 - p1[v] + p2v[v]
        else:
            x = pt.min_div[v]
            y = v // x
            if not pt.is_prime(y): continue
            if x == y:
                p2v[x] += 1
                p2[x][x] += 1
                ans += p2[x][x] + p1[x]
            else:
                p2v[x] += 1
                p2v[y] += 1
                if x > y:
                    x, y = y, x
                p2[x][y] += 1
                ans += p1[x] + p1[y] + p2[x][y]
    print(ans)


#  359
#  ms
def solve1():
    n, = RI()
    a = RILST()
    p1 = defaultdict(int)  # 质数的数量
    s1 = ans = 0  # 质数总数
    p2 = defaultdict(lambda: defaultdict(int))  # 含v的半质数，另一个因子的数量
    p2v = defaultdict(int)  # 含v的半质数数量
    for v in a:
        if pt.is_prime(v):
            s1 += 1
            p1[v] += 1
            ans += s1 - p1[v] + p2v[v]
        else:
            x = pt.min_div[v]
            y = v // x
            if not pt.is_prime(y): continue
            if x == y:
                p2v[x] += 1
                p2[x][x] += 1
                ans += p2[x][x] + p1[x]
            else:
                p2v[x] += 1
                p2v[y] += 1
                if x > y:
                    x, y = y, x
                p2[x][y] += 1
                ans += p1[x] + p1[y] + p2[x][y]
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
