import io
import os
import sys
from collections import deque
from math import factorial, lcm

if os.getenv('LOCALTESTACWING'):
    sys.stdin = open('input.txt')
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
MOD = 998244353
MAX_N = 2005
inv = [0] * MAX_N
inv[1] = 1
p = MOD
for i in range(2, MAX_N):
    inv[i] = (p - p // i) * inv[p % i] % p


def exgcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = exgcd(b, a % b)
    return y, x - a // b * y, d


# 求a关于b的逆元
def inv_exgcd(a, b):
    x, y, d = exgcd(a, b)
    return (x + b) % b if d == 1 else -1


def get_c(m, r):
    if m < r:
        return 0
    c = 1
    for i in range(1, r + 1):
        c = c * (m - i + 1) % MOD * inv[i] % MOD
    return c


def lucas(m, r):
    if r == 0:
        return 1
    return get_c(m % MOD, r % MOD) * lucas(m // MOD, r // MOD) % MOD


if __name__ == '__main__':
    n, m, k = map(int, input().split())

    ans = m * lucas(n - 1, k) * ((m - 1) ** k)
    print(lcm(n,m))
    print(ans % MOD)
