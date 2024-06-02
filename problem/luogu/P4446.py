# Problem: P4446 [AHOI2018初中组] 根式化简
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P4446
# Memory Limit: 125 MB
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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """ 根式化简，从立方中化简。可以扩展成其他次方。比如ccf20230602 D题就是开方根化简
结论：从n中先把<=n^(1/4)的质数去掉，剩下的数里，一定没有立方数因子了。（除非n本身是立方数，可以特判）
反证法：如果剩下的数里存在立方数，那么可以写成b*x^3,根据前边的筛法，b和x都是>n^(1/4)的，那么n本身就超过原数了。
    - 除非b==1，因为前边只筛了质数，没筛1。所以最后特判一下n是不是立方数。
    - 这里用二分特判，试了用set预处理会mle。直接开立方判断精度会wa。
    - 用数组预处理1e6，然后二分可以过。也可以不预处理，直接二分，更好一些。
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


pt = PrimeTable(4 * 10 ** 4 + 5).primes


# ping = []
# for i in range(10 ** 6 + 1):
#     ping.append(i * i * i)
# ping = set()  # 用set会MLE
# for i in range(10 ** 6 + 1):
#     ping.add(i * i * i)


#       ms
def solve():
    t, = RI()
    for n in RI():
        ans = 1
        for v in pt:
            if v * v * v > n: break
            cnt = 0
            while n % v == 0:
                n //= v
                cnt += 1
                if cnt == 3:
                    cnt = 0
                    ans *= v
        # if n in ping:  # MLE
        #     ans *= int(n**(1/3))
        # if int(n**(1/3))**3 == n:  # wa
        #     ans *= int(n ** (1 / 3))
        # p = bisect_left(ping, n)
        # if p ** 3 == n:
        #     ans *= p
        l, r = 1, int(n ** (1 / 3) + 1)
        while l + 1 < r:
            mid = (l + r) >> 1
            if mid ** 3 >= n:
                r = mid
            else:
                l = mid
        if r ** 3 == n:
            ans *= r
        print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
