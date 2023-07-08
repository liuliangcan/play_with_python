# Problem: E2. Rudolf and Snowflakes (hard version)
# Contest: Codeforces - Codeforces Round 883 (Div. 3)
# URL: https://codeforces.com/contest/1846/problem/E2
# Memory Limit: 256 MB
# Time Limit: 2000 ms

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
PROBLEM = """
n = 1 +x +x**2 + x**3 +..
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi





#       ms
def solve():
    n, = RI()
    if n <= 3:
        return print('NO')

    def calc(x, i):
        s = (1-x**(i+1))/(1-x)  # 等比数列求和公式

        return s
    for i in range(2, 64):  # 枚举指数
        def ok(x):
            return (x**(i+1)-1) >= n*(x-1)  # 注意分母右移时，由于是负数，因此要改变大于小于号；这里把分子分母同时变符号，就不用改了

        x = lower_bound(2, n + 1, ok)
        # print(i,ok(2),(1-3**(i+1)),n*(1-3))
        # print(i,ok(3),(1-3**(i+1)),n*(1-3))
        # print(x, i, (1-x**(i+1)),n*(1-x))
        if x > 1 and (1-x**(i+1)) == n*(1-x):
            # print(x,i,calc(x,i))
            return print('YES')
    print('NO')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
