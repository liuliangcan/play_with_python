# Problem: C. Primes on Interval
# Contest: Codeforces - Codeforces Round 147 (Div. 2)
# URL: https://codeforces.com/contest/237/problem/C
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/237/problem/C

输入 a b k，范围 [1,1e6]，a≤b。
请找到最短的 L，使得对于任意 a≤x≤b-L+1 都满足：在 x,x+1,...,x+L-1 中至少有 k 个质数。
输出 L。如果 L 不存在，输出 -1。
输入 2 4 2
输出 3

输入 6 13 1
输出 4

输入 1 4 3
输出 -1
"""
"""https://codeforces.com/contest/237/submission/207778331

预处理质数（埃氏筛/欧拉筛）。如果不足 k 个，输出 -1。

方法一：二分答案+滑窗验证（可以只在质数列表中滑窗）  O(b/logb * logb) = O(b)

方法二：既然可以只在质数列表中滑窗，那么干脆直接计算。
考虑 k+1 个连续质数对应的区间（减一），例如 5,7,11,13 & k=2，那么 [7,13-1] 就是一个包含 k 个质数的区间。向右滑动一格，变成 [7+1,13]，也仍然包含了 k 个质数。再短一点就不行了。最后再算上 a 和 b 的边界，你可以把 a-1 和 b+1 也视作质数。
答案就是 primes[i] - primes[i-k] 的最大值。"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


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

        # # 埃氏筛O(nlgn),由于切片的原因，仅标记质数的场景下比线性筛表现更好。
        # is_primes = [1] * (n + 1)
        # is_primes[0] = is_primes[1] = 0  # 0和1不是质数
        # for i in range(2, int((n + 1) ** 0.5) + 1):
        #     if is_primes[i]:
        #         is_primes[i * i::i] = [0] * ((n - 1 - i * i) // i + 1)
        # self.primes = [i for i, v in enumerate(is_primes) if v]

    def is_prime(self, x: int):
        """检测是否是质数，最坏是O(sqrt(x)"""
        if x < 3: return x == 2
        if x <= self.n: return self.min_div[x] == x
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0: return False
        return True

    def prime_factorization(self, x: int):
        """分解质因数，复杂度
        1. 若x>n则需要从2模拟到sqrt(x)，如果中间x降到n以下则走2；最坏情况，不含低于n的因数，则需要开方复杂度
        2. 否则x质因数的个数，那么最多就是O(lgx)"""
        n, min_div = self.n, self.min_div
        for p in range(2, int(x ** 0.5) + 1):
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

primes = PrimeTable(10 ** 6).primes

# def tag_primes_eratosthenes(n):  # 返回一个长度n的数组p，如果i是质数则p[i]=1否则p[i]=0
#     primes = [1]*n
#     primes[0] = primes[1] = 0  # 0和1不是质数
#     for i in range(2,int(n**0.5)+1):
#         if primes[i]:
#             primes[i * i::i] = [0] * ((n - 1 - i * i) // i + 1)
#     return primes
# primes = tag_primes_eratosthenes(5*10**5+5)
# # 埃氏筛O(nlgn),由于切片的原因，仅标记质数的场景下比线性筛表现更好。
# n = 10 ** 6
# is_primes = [1] * (n + 1)
# is_primes[0] = is_primes[1] = 0  # 0和1不是质数
# for i in range(2, int((n + 1) ** 0.5) + 1):
#     if is_primes[i]:
#         is_primes[i * i::i] = [0] * ((n  - i * i) // i + 1)
# primes = [i for i, v in enumerate(is_primes) if v]
n = len(primes)
"""
2 4 2 
2 3 4

"""


#    124   ms
def solve():
    a, b, k = RI()
    s = bisect_left(primes, a)
    e = bisect_right(primes, b)
    ans = -1
    p = e - k  # 从末尾开始数k个质数
    if p >= 0 and primes[p] >= a:
        ans = b - primes[p] + 1
    j = s
    for i in range(s, e):
        if i - j + 1 > k:
            a = primes[j] + 1
            j += 1
        if i - j + 1 == k:
            ans = max(ans, primes[i] - a + 1)

    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
