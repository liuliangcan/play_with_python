# Problem: B. Mashmokh and ACM
# Contest: Codeforces - Codeforces Round 240 (Div. 1)
# URL: https://codeforces.com/contest/414/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
from math import factorial

RI = lambda: map(int, sys.stdin.buffer.readline().split())
print = lambda d: sys.stdout.write(
    str(d) + "\n"
)  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/414/problem/B

输入 u n(1≤u,n≤2000)。
输出有多少个长为 n 的数组 a，满足：
1. 1≤a[1]≤a[2]≤...≤a[n]≤u。
2. a[i] 整除 a[i+1]（或者说 a[i] 是 a[i+1] 的因子）。
答案模 1e9+7。
输入 3 2
输出 5

输入 6 4
输出 39

输入 2 1
输出 2
"""
""" 线性dp+刷表法调和级数复杂度"""


class ModComb:
    """通过O(n)预处理逆元，达到O(1)询问组合数"""

    def __init__(self, n, p):
        """
        初始化，为了防止模不一样，因此不写默认值，强制要求调用者明示
        :param n:最大值
        :param p: 模
        """
        self.p = p
        self.inv_f, self.fact = [1] * (n + 1), [1] * (n + 1)
        inv_f, fact = self.inv_f, self.fact
        for i in range(2, n + 1):
            fact[i] = i * fact[i - 1] % p
        inv_f[-1] = pow(fact[-1], p - 2, p)
        for i in range(n, 0, -1):
            inv_f[i - 1] = i * inv_f[i] % p

    def comb(self, m, r):
        if m < r or r < 0:
            return 0
        return self.fact[m] * self.inv_f[r] % self.p * self.inv_f[m - r] % self.p


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


mc = ModComb(2009, MOD)  # n+v-1：v是相同质因子个数，最大就是lg2000=10，
pt = PrimeTable(2000)


# 93    ms
def solve():
    """枚举数组最后一个数字是i的情况：
    枚举i的所有质因数，假设i有v个质因数k，那么在数组的n个位置找到v个位置放这些k；质因数之间用乘法原理。
    n个盒子放v个小球方案数：C(n+v-1,v)
    复杂度O(ulogu) 实际上2000以内的数字质因数分解，平均每个数只有2.5个不同质因数，O(2.5u)
    """
    u, n = RI()
    ans = 1
    for i in range(2, u + 1):
        p = 1
        for _, v in pt.prime_factorization(i):
            p = p * mc.comb(n + v - 1, v) % MOD
        ans = (ans + p) % MOD

    print(ans)


# 186    ms
def solve3():
    u, n = RI()
    f = [0] + [1] * u
    for _ in range(1, n):
        for j in range(u, 0, -1):
            for k in range(j * 2, u + 1, j):
                f[k] = (f[k] + f[j]) % MOD

    print(sum(f) % MOD)


#   234  ms
def solve2():
    u, n = RI()
    f = [1] * u
    for _ in range(1, n):
        g = [0] * u
        for j, v in enumerate(f, start=1):
            for k in range(j, u + 1, j):
                g[k - 1] = (g[k - 1] + v) % MOD
        f = g
    print(sum(f) % MOD)


#   171  ms
def solve1():
    u, n = RI()
    f = [1] * u
    for _ in range(1, n):
        g = [0] * u
        for j, v in enumerate(f, start=1):
            p = j
            while p <= u:
                g[p - 1] = (g[p - 1] + v) % MOD
                p += j
        f = g
    print(sum(f) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
