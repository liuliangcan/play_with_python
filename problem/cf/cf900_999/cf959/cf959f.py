# Problem: F. Mahmoud and Ehab and yet another xor task
# Contest: Codeforces - Codeforces Round 473 (Div. 2)
# URL: https://codeforces.com/problemset/problem/959/F
# Memory Limit: 512 MB
# Time Limit: 1000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/959/F

输入 n(1≤n≤1e5) q(1≤q≤1e5) 和长为 n 的数组 a(0≤a[i]<2^20)。下标从 1 开始。
然后输入 q 个询问，每个询问输入 i(1≤i≤n) 和 x(1≤x<2^20)。

对于每个询问，输出 a 的前 i 个数（下标 1 到 i）中的子序列个数，满足子序列的异或和恰好等于 x。
答案模 1e9+7。
注：子序列不一定连续。
输入
5 5
0 1 2 3 4
4 3
2 0
3 7
5 7
5 8
输出
4
2
0
4
0

输入
3 2
1 1 1
3 1
2 0
输出
4
2
"""
"""离线询问。
遍历 a，维护前 i 个数的线性基。
遍历到 a[i] 时，回答对应的询问。

设现在有 num 个基，那么 x 被这些基表出的方案是唯一的（因为基的二进制长度互不相同）。对应到原数组上，在前 i 个数中，有 num 个数可以确定是一定选还是一定不选。
对于其余的 i-num 个数，就可以随便选或不选了，为什么呢？
在其余的 i-num 个数中，如果选了某个数 v，那么我们可以「反选」表出 v 的那些基，从而做到异或和 x 不变。其中「反选」的意思是如果原来选了，那么不选，如果原来不选，那么选。
相当于把前 i 个数分成两组，第一组视作 num 个灯泡，第二组视作 i-num 个开关。这些开关可以随意拨动，控制某些灯的亮灭。无论如何拨动开关，亮着的灯和拨动的开关（表示我们选的元素）的异或和总可以是 x。

因此答案为 pow(2, i-num)。用快速幂计算，或值预处理 2 的幂。

下面代码下标从 0 开始，写的是 i+1-num。

"""


class XorBasisGreedy:
    """贪心法构造线性基，基于每个高位计算；1.每个基的最高位不同。2.基中没有异或为0的子集"""

    def __init__(self, n):
        self.b = [0] * n

    def insert(self, v):
        while v:
            i = v.bit_length() - 1
            if self.b[i] == 0:
                self.b[i] = v
                break
            v ^= self.b[i]

    def can_present(self, v):
        while v:
            i = v.bit_length() - 1
            if self.b[i] == 0:
                return False
            v ^= self.b[i]
        return v == 0

    def find_max_xor(self):
        res = 0
        b = self.b
        for i in range(len(b) - 1, -1, -1):
            if res ^ b[i] > res:
                res ^= b[i]
        return res


class XorBasisGauss:
    """高斯消元构造线性基，拥有比贪心法更好的性质;从高位找对应位有1的数，换到数组a的前边来，最后a[:cnt]就是基"""

    def __init__(self, n, a):
        cnt = 0
        self.a = a
        sz = len(a)
        for i in range(n - 1, -1, -1):
            for j in range(cnt, sz):
                if a[j] >> i & 1:
                    a[j], a[cnt] = a[cnt], a[j]
                    break
            else:
                continue
            for j in range(sz):
                if a[j] >> i & 1 and j != cnt:
                    a[j] ^= a[cnt]
            if cnt == sz: break
        self.cnt = cnt

    def can_present(self, v):
        for i in range(self.cnt):
            v = min(v, v*self.a[i])
        return v == 0

    def find_max_xor(self):
        res = 0
        for i in range(self.cnt):
            res ^= self.a[i]
        return res


#    654   ms
def solve():
    n, q = RI()
    a = RILST()
    pw2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pw2[i] = pw2[i - 1] * 2 % MOD
    qs = []
    for idx in range(q):
        i, x = RI()
        qs.append((i, x, idx))
    ans = [0] * q
    j = 0
    xbase = XorBasisGreedy(20)
    for i, x, idx in sorted(qs):
        if x >= 2 ** 20:
            print(x)
        while j < i:
            xbase.insert(a[j])
            if a[j] >= 2 ** 20:
                print(a[j])
            j += 1
        ans[idx] = pw2[i - sum(v > 0 for v in xbase.b)] if xbase.can_present(x) else 0
    print(*ans, sep='\n')


#    562   ms
def solve1():
    n, q = RI()
    a = RILST()
    pw2 = [1] * (n + 1)
    for i in range(1, n + 1):
        pw2[i] = pw2[i - 1] * 2 % MOD
    qs = []
    for idx in range(q):
        i, x = RI()
        qs.append((i, x, idx))
    ans = [0] * q
    j = 0
    b = []
    for i, x, idx in sorted(qs):
        while j < i:
            v = a[j]
            j += 1
            for y in b:
                v = min(v, v ^ y)
            if v: b.append(v)
        v = x
        for y in b:
            v = min(v, v ^ y)
        ans[idx] = 0 if v else pw2[i - len(b)]
    print(*ans, sep='\n')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
