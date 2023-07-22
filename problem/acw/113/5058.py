# Problem: 画矩形
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/5058/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """cf 2000分原题
https://codeforces.com/contest/128/problem/C
"""

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


#       ms
def solve():
    n, m, k = RI()
    mc = ModComb(1005, MOD)

    print(mc.comb(n - 1, k * 2) * mc.comb(m - 1, k * 2) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
