# Problem: D - M<=ab
# Contest: AtCoder - AtCoder Beginner Contest 296
# URL: https://atcoder.jp/contests/abc296/tasks/abc296_d
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc296/tasks/abc296_d
给你两个正整数n,m(1<=N,M<=1e12)。
找到一个最小的x，使x满足:
1.x>=m
2.x可以被分解为两个数ab的乘积，其中1<=a,b<=n
"""
"""由于数据范围大，直接枚举肯定不行。可以先考虑无解的情况：
如果n*n<m肯定无解，因为即使a、b都取到n，乘积也够不到m。
如果n*n=m，那ab只能都取到n，任意数再小都不够m，则乘积只能是m。
若m<=n，显然ab可以是1 m,最小就是m，返回m即可。
其它情况(n*n>m&&n<m)则需要遍历尝试：
首先初始化ans上界，起码ab可以取到n*n，这个数是满足条件的答案。我们枚举找比它更小的答案。
枚举乘积答案肯定是不行的，考虑枚举因子a/b里小的那个（因为乘法满足交换律，枚举哪个都可以）,设为a。
a显然不会超过sqrt(m),这时可以计算b=ceil(m/a)。上取整后就可以保证a*b>=m。
因此这么枚举，只需要保证ab<=n即可更新答案。
————————————————
版权声明：本文为CSDN博主「七水shuliang」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liuliangcan/article/details/129972406"""

#       ms
def solve():
    n, m = RI()
    if n * n < m:
        return print(-1)
    if n * n == m:
        return print(m)
    if m <= n:
        return print(m)
    s = int(m ** 0.5)
    ans = n * n
    for a in range(2, min(s, n) + 1):
        b = (m + a - 1) // a
        if b <= n:
            ans = min(ans, b * a)
    print(ans)


if __name__ == '__main__':
    solve()
