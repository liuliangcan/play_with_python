PROBLEM = """扩展卢卡斯
求C(n,m)%p,其中mod可以不为质数。 单次计算复杂度O(plogp)
自顶向下分解这个问题：
1. 把mod分解质因子变成p0^k0 * p1^k1 *..pi^ki,显然这i部分是互质的，那么分别求出ri=C(n,m)%(pi^ki)后，可以利用中国剩余定理合并求出模mod的余数
    问题转化为求ri=C(n,m)%(pi^ki)
2. n!/(m!(n-m)!) % (p^k),分两步：
    1. 计算这个分式中含有多少个p，如果p的个数是k的倍数，显然这个模数可以直接返回0
        定义f(n)为n!内有多少个p，发现f(n)=f(n//p)+n//p
    2. 和p无关的部分.发现这部分的模是有循环节的，长度为p^k，一共n//(p^k)节；再算上剩下一段尾巴即可
模板题：https://www.luogu.com.cn/problem/P4720
多次模10，把所有方法cache了才过：https://leetcode.cn/problems/check-if-digits-are-equal-in-string-after-operations-ii/

这个算法感觉八百年用不到，只有出题人为了考而考，否则一般都是质数模
"""


def powmod(a, b, mod):
    ans = 1
    while b:
        if b & 1: ans = ans * a % mod
        a = a * a % mod
        b >>= 1
    return ans


def exgcd(a, b):
    if not b: return 1, 0
    x, y = exgcd(b, a % b)
    return y, x - a // b * y


def inv(x, p):  # 用扩展欧几里得求x在p上的逆元
    return exgcd(x, p)[0] % p


def factor_cnt(n, p):  # n!里有多少个p因子
    return 0 if n == 0 else factor_cnt(n // p, p) + n // p


def fac(n, p, pk):  # 计算n!里除了p之外的累乘%pk
    if not n: return 1
    ans = 1
    for i in range(2, pk):
        if i % p:
            ans = ans * i % pk
    ans = powmod(ans, n // pk, pk)
    for i in range(2, n % pk + 1):
        if i % p:
            ans = ans * i % pk
    return ans * fac(n // p, p, pk)


def cmb(m, r, p, pk):  # 求C(m,r)%pk
    cnt = factor_cnt(m, p) - factor_cnt(r, p) - factor_cnt(m - r, p)
    m1 = powmod(p, cnt, pk)
    if not m1: return 0  # p的因子个数是k的倍数
    return m1 * fac(m, p, pk) * inv(fac(m - r, p, pk), pk) * inv(fac(r, p, pk), pk) % pk


def crt(x, r, m):  # 当前模数、模、所有模数积
    return m // x * r % m * inv(m // x, x) % m


def exlucas(m, r, mod):  # 用扩展卢卡斯计算C(m,r)%mod,复杂度modlogmod，注意这里还有一个sqrt的质因数分解
    ans = 0
    x = mod
    i = 2
    while i * i <= x:
        if x % i == 0:
            pk = 1
            while x % i == 0:
                pk *= i
                x //= i
            ans = (ans + crt(pk, cmb(m, r, i, pk), mod)) % mod
        i += 1
    if x > 1:
        ans = (ans + crt(x, cmb(m, r, x, x), mod)) % mod
    return ans % mod


class ExLucas:  # 用这个的话，就不用每次分解质因数，多次时少了个sqrt(mod),但由于内部还是有遍历2-pk的动作，最差依然是p
    def __init__(self, mod):
        self.factorization = []
        i = 2
        x = self.mod = mod
        while i * i <= x:
            if x % i == 0:
                pk = 1
                while x % i == 0:
                    pk *= i
                    x //= i
                self.factorization.append((i, pk))
            i += 1
        if x > 1:
            self.factorization.append((x, x))

    def comb(self, m, r):
        ans = 0
        for p, pk in self.factorization:
            ans += crt(pk, cmb(m, r, p, pk), self.mod)
        return ans % self.mod


#       ms
def solve():
    n, m, p = RI()
    print(exlucas(n, m, p))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()

"""在洛谷发现一个这个板子，好像单次计算是O(lg)的，不确定，再看看
"""


class BinomialCoefficient:
    def __init__(self, mod: int):
        self.MOD = mod
        self.factorization = self._factorize(mod)
        self.facs = []
        self.invs = []
        self.coeffs = []
        self.pows = []
        for p, pe in self.factorization:
            fac = [1] * pe
            for i in range(1, pe):
                fac[i] = fac[i - 1] * (i if i % p else 1) % pe
            inv = [1] * pe
            inv[-1] = fac[-1]
            for i in range(1, pe)[::-1]:
                inv[i - 1] = inv[i] * (i if i % p else 1) % pe
            self.facs.append(fac)
            self.invs.append(inv)
            # coeffs
            c = self._modinv(mod // pe, pe)
            self.coeffs.append(mod // pe * c % mod)
            # pows
            powp = [1]
            while powp[-1] * p != pe:
                powp.append(powp[-1] * p)
            self.pows.append(powp)

    def __call__(self, n: int, k: int):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1 % self.MOD
        res = 0
        for i, (p, pe) in enumerate(self.factorization):
            res += (
                    self._choose_pe(n, k, p, pe, self.facs[i], self.invs[i], self.pows[i])
                    * self.coeffs[i]
            )
            res %= self.MOD
        return res

    def _E(self, n, k, r, p):
        res = 0
        while n:
            n //= p
            k //= p
            r //= p
            res += n - k - r
        return res

    def _choose_pe(self, n, k, p, pe, fac, inv, powp):
        r = n - k
        e0 = self._E(n, k, r, p)
        if e0 >= len(powp):
            return 0
        res = powp[e0]
        if (p != 2 or pe == 4) and self._E(n // (pe // p), k // (pe // p), r // (pe // p), p) % 2:
            res = pe - res
        while n:
            res = res * fac[n % pe] % pe * inv[k % pe] % pe * inv[r % pe] % pe
            n //= p
            k //= p
            r //= p
        return res

    def _factorize(self, N):
        factorization = []
        for i in range(2, N + 1):
            if i * i > N:
                break
            if N % i:
                continue
            c = 0
            while N % i == 0:
                N //= i
                c += 1
            factorization.append((i, i ** c))
        if N != 1:
            factorization.append((N, N))
        return factorization

    def _modinv(self, a, MOD):
        r0, r1, s0, s1 = a, MOD, 1, 0
        while r1:
            r0, r1, s0, s1 = r1, r0 % r1, s1, s0 - r0 // r1 * s1
        return s0 % MOD


if __name__ == "__main__":
    # https://www.luogu.com.cn/problem/P4720
    import sys

    input = lambda: sys.stdin.readline().rstrip("\r\n")
    n, k, mod = map(int, input().split())
    C = BinomialCoefficient(mod)
    print(C(n, k))
