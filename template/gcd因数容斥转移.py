"""对于一个数字如果可以从因数来容斥转移，可以用这个优化。比如要从前边状态里所有不互质/互质的状态里来。优化成nlgn  (<1e5里因数最多的数是128个，这里还能把系数为0的都干掉，可以更少)
状态机DP，求方案数。状态转移时，需要从上一层的不互质的状态里转移过来。暴力的话是n方了。传智杯国赛。
定义f[v]表示到本层时，末尾数字是v的方案数。 定义s[v]表示当前，状态是v的倍数的方案数。
那么对每个状态p，考虑v的因数f1,f2,f3...，那么f[p]可以从s[f1]，s[f2]，s[f3]。。里容斥而来。这个枚举就比较小了(<128,如果是1~n排列认为均摊是lg， ①)
如何容斥呢，观察：
    状态6， 一定是s[2]+s[3]-s[6]，明确一下系数：s[2]*1 +s[3]*1 + s[6]*(-1)
    状态8， s[2]*1 + s[4]*0 + s[8]*0
    状态12，s[2]*1 + s[3]*1 + s[4]*0 + s[6]*(-1) + s[12]*0
    状态30，s[2]*1 + s[3]*1 + s[5]*1 + s[6]*(-1) + s[10]*(-1) + s[15]*(-1) + s[30]*1
可以看出，系数都是1,0,-1，有重复质因数的都是0，不同质因数个数为奇数的是1，偶数是-1。
这个系数可以和预处理因数的时候同时处理，调和级数方式

另外，对于coef为0的项，是不是考虑从因数列表里去掉，这样复杂度可以进一步降低
其实就是莫反、莫比乌斯反演、莫比乌斯函数

https://ac.nowcoder.com/acm/contest/108576/G
线性筛莫反,mo2：
    mu[i]={0， 如果i含平方因子；(-1)^c, c是不同质因子个数}
用法：
    对gcd的题来说，很多可以用莫反，一般来说答案形如：
    for i in range(1,mx+1):
        ans += mu[i]*f(i)
    其中f(i)是i的倍数合集的一个贡献。
例题：
    求gcd为i非空子序列数量： https://codeforces.com/problemset/problem/803/F， f(i)=pow(2,cnt[i]+cnt[2i]+..cnt[k*i])-1
"""


def mo1(n):  # 返回[1, 0, 1, 1, 0, 1, -1, 1, 0, 0]
    coef = [1] * (n + 1)
    coef[1] = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            if j > i:
                coef[j] -= coef[i]
    return coef


def mo2(n):  # 返回[1, 1, -1, -1, 0, -1, 1, -1, 0, 0]
    mu = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n: break
            is_prime[i * p] = False
            if i % p == 0:
                mu[i * p] = 0
                break
            else:
                mu[i * p] = -mu[i]
    return mu

# n = 20
# coef = [1] * n
# coef[1] = 0
# fac = [[] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(i, n + 1, i):
#         fac[j].append(i)
#         if j > i:
#             coef[j] -= coef[i]

# Problem: 小苯的地下城寻宝
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/108576/G
# Memory Limit: 2048 MB
# Time Limit: 6000 ms

import sys

from collections import Counter, defaultdict, deque
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。



MOD = 998244353
PROBLEM = """
"""
N = 10 ** 5
coef = [1] * (N + 1)
coef[1] = 0
facs = [[] for i in range(N + 1)]
for i in range(1, N + 1):
    facs[i].append(i)
    for j in range(i*2, N + 1, i):
        facs[j].append(i)
        coef[j] -= coef[i]  # i的贡献前边算过了，在j里就要去掉
for i, v in enumerate(facs):
    facs[i] = [x for x in v if coef[x] != 0]


#       ms
def solve():
    n, = RI()
    # raise Exception(f"{n}")
    a = RILST()
    fa = RILST()
    g = [[] for _ in range(n)]
    for i, v in enumerate(fa):
        if i:
            g[v - 1].append(i)
    order = []
    q = [0]
    while q:
        order.append(q)
        nq = []
        for u in q:
            for v in g[u]:
                nq.append(v)
        q = nq
    # print(order)
    # print(coef)
    # print(facs)
    f = [0] * (n + 1)  # 以i为当前最后一层拾取 的方案数
    s = [0] * (n + 1)  # 最后一层数字为i的倍数的方案数
    f[a[0]] = 1
    for fac in facs[a[0]]:
        s[fac] += 1

    # for o in order[1:]:
    #     nf = []
    #     for v in o:
    #         v = a[v]
    #         for fac in facs[v]:
    #             nf.append((v,s[fac] * coef[fac]))  # 1.9s 还是得去重
    #
    #
    #     for k, v in nf:
    #         f[k] += v
    #         f[k] %= MOD
    #         for fac in facs[k]:
    #             s[fac] += v
    #             s[fac] %= MOD
    nf = defaultdict(int)
    for o in order[1:]:
        nf.clear()
        for v in o:
            v = a[v]
            for fac in facs[v]:
                nf[v] += s[fac] * coef[fac]

        for k, v in nf.items():
            f[k] += v
            f[k] %= MOD
            for fac in facs[k]:
                s[fac] += v
                s[fac] %= MOD

    print(sum(f) % MOD)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
