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

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 998244353
"""https://atcoder.jp/contests/abc169/tasks/abc169_e

输入 n (2≤n≤2e5) 和 n 个区间的左右端点，区间范围在 [1,1e9]。
每个区间内选一个整数，然后计算这 n 个整数的中位数。你能得到多少个不同的中位数？
注：偶数长度的中位数是中间两个数的平均值（没有下取整）。
输入
2
1 2
2 3
输出 3

输入
3
100 100
10 10000
1 1000000000
输出 9991

https://atcoder.jp/contests/abc169/submissions/35971735

上下界思想，计算中位数的最小值和最大值，然后范围内的都可以取到。

由于偶数长度的中位数会存在小数点后为 0.5 的情况，所以答案是可以 *2 的。具体见代码。
"""



#    	 ms
def solve(n, a,b):
    a.sort()
    b.sort()
    mn = a[n//2]
    mx = b[n//2]
    if n & 1:  # 奇数长度中位数就是这些数
        return print(mx-mn+1)
    # 偶数长度 可以取到x.5把这些数都乘2计算mn = (a[n//2]+a[n//2+1])//2,mx = (b[n//2]+b[n//2+1])//2;答案还得计算差乘2因此直接把mn mx乘2
    mn += a[n//2-1]
    mx += b[n//2-1]
    print(mx-mn+1)


if __name__ == '__main__':
    n, = RI()
    a,b = [], []
    for _ in range(n):
        l,r = RI()
        a.append(l)
        b.append(r)


    solve(n, a,b)
