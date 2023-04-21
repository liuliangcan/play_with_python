# Problem: Minimum Operation
# Contest: CodeChef - START86D
# URL: https://www.codechef.com/START86D/problems/MINIMUMOP
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
from bisect import *
from collections import Counter
from functools import lru_cache, reduce
from math import sqrt, gcd, inf

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')


def tag_primes_eratosthenes(n):  # 返回一个长度n的数组p，如果i是质数则p[i]=1否则p[i]=0
    primes = [1] * n
    primes[0] = primes[1] = 0  # 0和1不是质数
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i::i] = [0] * ((n - 1 - i * i) // i + 1)
    return primes


primes = tag_primes_eratosthenes(2 * 10 ** 6 + 5)
ps = [i for i, v in enumerate(primes) if v]
# print(ps)
"""预处理质数表ps
- 若a数字全一样，0步。
- 若g=gcd(a)>=2,1步，选g。
- 否则g必为1。
    - 枚举所有小于m的质数，若有一个质数v不不在a的因子里。

"""

#       ms
def solve():
    n, m = RI()
    a = set(RILST())
    if len(a) == 1:
        return print(0)
    g = reduce(gcd, a)
    if g >= 2:
        print(1)
        return print(g)

    s = set()
    for x in a:
        i = 2
        while i * i <= x:
            while x % i == 0:
                s.add(i)
                x //= i
            i += 1
        if x > 1: s.add(x)

    for v in ps:
        if v > m: break
        if v not in s:
            print(1)
            return print(v)

    print(2)
    print(2)
    print(3)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
    # solve()
