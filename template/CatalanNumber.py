"""卡特兰数
数列的前几项为：1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862 ：https://zhuanlan.zhihu.com/p/97619085
只需要19项就超过int32了
https://blog.csdn.net/sherry_yue/article/details/88364746
https://blog.csdn.net/weixin_44520881/article/details/105437210

递推公式： f[0] = f[1] = 1
公式1： f[n]=f[0]f[n-1]+f[1]f[n-2]+...+f[n-1]f[0]
公式2： f[n]=f[n−1]∗(4∗n−2)/(n+1)
通项公式
公式3： f[n]=C(2n,n)/(n+1)(n=0,1,2,...)
公式4： f[n]=C(2n,n)−C(2n,n−1)
"""


# # 打印前 n 个卡特兰数
# ans, n = 1, 20
# print("1:" + str(ans))
# for i in range(2, n + 1):
#     ans = ans * (4 * i - 2) // (i + 1)  # 注意不能写成ans*=的形式，因为右边可能不是偶数，除法丢失精度
#     print(str(i) + ":" + str(ans))

def get_catalan2(n=20):  # 递推法计算卡特兰数,注意取模
    ans = [1] * (n + 1)
    for i in range(2, n + 1):
        ans[i] = (ans[i - 1] * (4 * i - 2) // (i + 1))  # 注意不能写成ans*=的形式，因为右边可能不是偶数，除法丢失精度
    return ans


MOD = 10 ** 9 + 7


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


def get_catalan3(n=20):  # 通项公式计算卡特兰数，通常比较大要结合组合数取模
    mc = ModComb(n * 2, MOD)
    # return [mc.comb(2*i,i)//(i+1) for i in range(n+1)]
    return [mc.comb(2 * i, i) * pow(i + 1, MOD - 2, MOD) % MOD for i in range(n + 1)]


def get_catalan4(n=20):  # 通项公式计算卡特兰数，通常比较大要结合组合数取模
    mc = ModComb(n * 2, MOD)
    return [(mc.comb(2 * i, i) - mc.comb(2 * i, i - 1)) % MOD for i in range(n + 1)]


print(get_catalan2(20))
print(get_catalan3(20))
print(get_catalan4(20))
