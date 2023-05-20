
class ModComb:
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

    def perm_count_with_duplicate(self, a):
        """含重复元素的列表a，全排列的种类。
        假设长度n,含x种元素，分别计数为[c1,c2,c3..cx]
        则答案是C(n,c1)*C(n-c1,c2)*C(n-c1-c2,c3)*...*C(cx,cx)
        或：n!/c1!/c2!/c3!/../cn!
        """
        ans = self.fact[len(a)]
        for c in Counter(a).values():
            ans = ans * self.inv_f[c] % self.p
        return ans
        # 下边这种也可以
        # s = len(a)
        # ans = 1
        # for c in Counter(a).values():
        #     ans = ans * self.comb(s,c) % MOD
        #     s -= c
        # return ans


# mc = ModComb(2 * 10 ** 5 + 5, MOD)

