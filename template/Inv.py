"""逆元,在模数下约等于除法
求一个数的逆元： pow(x,MOD-2,MOD)  或者 pow(x,-1,MOD)
求累乘的逆元，主要出现在modcomb和presum:
        self.p = p
        self.fact = pre = [1] * (n + 1)
        self.inv = inv = [1] * (n + 1)
        for i, v in enumerate(a, start=1):
            pre[i] = pre[i - 1] * v % p

        inv[-1] = pow(pre[-1], p - 2, p)
        for i in range(n - 1, -1, -1):
            inv[i] = a[i] * inv[i + 1] % p


1~n的逆元线性递推：
百度之星20240602 B:n个人，每个人跑1圈的要花i分钟，一直到大家同时到终点才停。问所有人两两相遇几次。答案取模
显然最后时间是lcm分钟。设一圈长度是1，那么他们的速度分别是1/1,1/2,1/3。。。1/n
对于x<y的两个人来说，他们的速度差是1/x-1/y,在lcm分钟，一共追及(1/x-1/y)圈，即相遇次数。
那么 对于一个i来说，比它大的数有n-i个，即贡献n-i次=(n-i)/i,
        比它小的有i-1个，即贡献(i-1)/i
        即ans+=((n-i)/i-(i-1)/i)*lcm
只需要解决两个问题：
1. 求1~n每个数的逆元：inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD，  O(n)
2. 求1~n的lcm:求出<=n的所有质数，然后把每个质数的k次方加到lcm里即可。  O(n)求质数，遍历prime添加，应该也<O(n)


"""

def get_inv1_n(n,MOD):  # 线性时间推出1~n的逆元 https://blog.csdn.net/liyizhixl/article/details/78426576
    inv = [1] * (n + 1)
    for i in range(2, n + 1):
        inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD
    return inv




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


#       ms
def solve():
    n, = RI()
    pt = PrimeTable(n).primes
    lcm = 1
    for v in pt:
        p = v
        while p * v <= n:
            p *= v
        lcm = lcm * p % MOD

    inv = [1] * (n + 1)
    for i in range(2, n + 1):
        inv[i] = (MOD - MOD // i) * inv[MOD % i] % MOD

    # ans = 0
    # for i in range(1, n + 1):
    #     ans = (ans + lcm * inv[i] % MOD * (n - i) % MOD - lcm * inv[i] % MOD * (i - 1) % MOD) % MOD
    # print(ans)
    ans = 0
    for i in range(1, n + 1):
        ans = (ans + inv[i] * (n + 1 - i * 2) % MOD) % MOD

    print(ans * lcm % MOD)
