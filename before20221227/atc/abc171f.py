import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

FFF = 'abcinput.txt'
if os.path.exists(FFF):
    sys.stdin = open(FFF)

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://atcoder.jp/contests/abc171/tasks/abc171_f

输入 k(≤1e6) 和一个长度不超过 1e6 的字符串 s，由小写字母组成。
你需要在 s 中插入恰好 k 个小写字母。
输出你能得到的字符串的个数，模 1e9+7。
输入
5
oof
输出 575111451

输入
37564
whydidyoudesertme
输出 318008117

https://atcoder.jp/contests/abc171/submissions/36296507

设 s 的长度为 n。

提示 1：如何避免重复统计？做一个规定，插入在 s[i] 左侧的字符，不能和 s[i] 相同，这不会影响答案的正确性。

提示 2：枚举最后一个字符的右侧插入了多少个字符，设为 i，这些字符没有限制，有 26^i 种方案。

提示 3：剩下 (n-1) + (k-i) 个字符，我们需要考虑其中 n-1 个字符的位置，这就是 C(n-1+k-i, n-1)。

提示 4：其余插入字符的方案数就是 25^(k-i)。

因此答案为 ∑26^i * C(n-1+k-i, n-1) * 25^(k-i), i=[0,k]

不知道组合数怎么算的，需要学一下逆元。
"""


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


#    用类会TLE,不用类1968 	 ms
def solve1(k, s):
    n = len(s)
    p25, p26 = [1] * (k + 1), [1] * (k + 1)
    for i in range(1, k + 1):
        p25[i] = p25[i - 1] * 25 % MOD
        p26[i] = p26[i - 1] * 26 % MOD
    mc = ModComb(n + k, MOD)

    ans = 0
    for i in range(k + 1):
        ans = (ans + p26[i] % MOD * mc.comb(n - 1 + k - i, n - 1) % MOD * p25[k - i] % MOD) % MOD
    print(ans % MOD)


#    1752  	 ms
def solve2(k, s):
    n = len(s)
    mc = ModComb(n + k, MOD)
    p26 = 1
    p25 = pow(25, k, MOD)
    inv25 = pow(25, MOD - 2, MOD)
    ans = 0
    for i in range(k + 1):
        ans = (ans + p26 % MOD * mc.comb(n - 1 + k - i, n - 1) % MOD * p25 % MOD) % MOD
        p26 = p26 * 26 % MOD
        p25 = p25 * inv25 % MOD
    print(ans % MOD)


#     	 ms
def solve(k, s):
    n = len(s)
    MAX_N = n+k
    inv_f, fact = [1] * (MAX_N + 1), [1] * (MAX_N + 1)
    for i in range(2, MAX_N + 1):
        fact[i] = i * fact[i - 1] % MOD
    inv_f[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(MAX_N, 0, -1):
        inv_f[i - 1] = i * inv_f[i] % MOD
    p26 = 1
    p25 = pow(25, k, MOD)
    inv25 = pow(25, MOD - 2, MOD)
    ans = 0
    for i in range(k + 1):
        ans = (ans + p26 % MOD * fact[n-1+k-i]*inv_f[n-1]*inv_f[k-i] % MOD * p25 % MOD) % MOD
        p26 = p26 * 26 % MOD
        p25 = p25 * inv25 % MOD
    print(ans % MOD)


if __name__ == '__main__':
    k, = RI()
    s, = RS()

    solve(k, s)
