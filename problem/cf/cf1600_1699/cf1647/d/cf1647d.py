# Problem: D. Madoka and the Best School in Russia
# Contest: Codeforces - Codeforces Round 777 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1647/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1647/D

输入 T(≤100) 表示 T 组数据。
每组数据输入 x d (2≤x,d≤1e9)，保证 x 是 d 的倍数。

定义好数为 d 的倍数。
定义美丽数为好数且不能表示为两个好数的乘积。

x 能否表示为一个或多个美丽数的乘积，且表示方式不唯一？
输出 YES/NO。

注：2*4 和 4*2 是同一种表示方式。
输入
8
6 2
12 2
36 2
8 2
1000 10
2376 6
128 4
16384 4
输出
NO
NO
YES
NO
YES
YES
NO
YES
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


pt = PrimeTable(10 ** 4)

"""分类讨论：首先明确好数是含有d因子；美丽数只含1个d因子
先把x中d的因子全部除光，假设有cnt个d，剩余因子为k。
那么x一定可以表达成cnt个x，然后给其中一个乘上k的形式。我们只需要讨论能否找到第二种组合形式。
1. 若cnt==1: 则x本身就是一个美丽数，也不能拆成两个美丽数，因为x只含1个d。那么表示方式是唯一的，就是x本身。
2. 若cnt==2: 如果变成1个数的话，这个数就不是美丽数了，不可以；因此只能考虑两个数的方案，考虑k如果是合数，就可以拆成2个因子分别放到两个数上。否则就不可以。
3. 若cnt==3: 如果k是合数，同样可以；否则考虑拆掉一个d，分别放到另外两个d上：注意其中一个d上有个k，假设往这上边放的因子是p，那么p*k不能是d的倍数，否则这个数会变得不美丽。因此只需要一个质因子p*k%d!=0即可
4. 若cnt==4: 如果k是合数，同上；否则考虑拆掉一个d，放到不放k的两个位置上即可。
"""


#   93    ms
def solve():
    x, d = RI()
    cnt = 0
    while x % d == 0:
        cnt += 1
        x //= d
    if cnt == 1:
        return print('NO')
    elif cnt == 2:
        if x > 1 and not pt.is_prime(x):
            return print('YES')
        return print('NO')
    elif cnt == 3:
        if x > 1 and not pt.is_prime(x):
            return print('YES')
        if not pt.is_prime(d):
            for p, _ in pt.prime_factorization(d):
                if p * x % d != 0:
                    return print('YES')
        print('NO')
    else:
        if x > 1 and not pt.is_prime(x):
            return print('YES')
        if not pt.is_prime(d):
            return print('YES')
        print('NO')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
