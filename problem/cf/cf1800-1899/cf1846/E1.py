# Problem: E1. Rudolf and Snowflakes (simple version)
# Contest: Codeforces - Codeforces Round 883 (Div. 3)
# URL: https://codeforces.com/contest/1846/problem/E1
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
# MOD = 998244353
PROBLEM = """这是问题的一个简单版本。唯一的区别是，在这个版本中n≤106。

一个冬天的早晨，鲁道夫若有所思地望着窗外的飘落的雪花。他很快注意到雪花的排列中存在一种特殊的对称性。作为一个真正的数学家，鲁道夫提出了一个雪花的数学模型。

他将雪花定义为一个无向图，按照以下规则构建：

开始时，图只有一个顶点。
随后，将更多的顶点添加到图中。初始顶点与k个新顶点（k>1）相连。
将只与另一个顶点相连的每个顶点，再与k个新顶点相连。这个步骤至少要执行一次。
当k=4时，最小可能的雪花如图所示。

经过一些数学研究，鲁道夫意识到这样的雪花可能不存在具有任意数量的顶点。帮助鲁道夫检查一个具有n个顶点的雪花是否存在。

输入
输入的第一行包含一个整数t（1≤t≤104）——测试用例的数量。

然后是每个测试用例的描述。

每个测试用例的第一行包含一个整数n（1≤n≤106）——需要检查雪花是否存在的顶点数。

输出
输出t行，每行都是对应测试用例的答案——如果存在至少一个k>1，使得可以构造具有给定顶点数量的雪花，则输出"YES"；否则输出"NO"。
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


pt = PrimeTable(10 ** 6 + 1)


def check(n):
    if n <= 3:
        return False
    n -= 1

    def ok(i):
        s = 0
        p = i
        while s < n:
            s += p
            p *= i
        return s == n

    for i in pt.get_factors(n):
        if 1 != i != n and ok(i):
            # print(i)
            return True

    return False


# for i in range(1,50):
#     print(i-1,check(i))

#       ms
def solve():
    n, = RI()
    print(['NO', 'YES'][check(n)])


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
