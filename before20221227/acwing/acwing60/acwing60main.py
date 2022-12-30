import io
import os
import sys
from collections import deque

if os.getenv('LOCALTESTACWING'):
    sys.stdin = open('input.txt')
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
MOD = 998244353
if __name__ == '__main__':
    n, m, k = map(int, input().split())
    def factorial(k):
        ans = 1
        for i in range(2,k+1):
            ans*=i
        return ans
    def comb(m,r):
        return factorial(m)//(factorial(r)*factorial(m-r))
    ans = m*comb(n-1,k)
    for _ in range(k):
        ans *= m-1
        ans %= MOD
    print(ans % MOD)
