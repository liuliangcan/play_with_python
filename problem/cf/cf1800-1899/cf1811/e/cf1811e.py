# Problem: E. Living Sequence
# Contest: Codeforces - Codeforces Round 863 (Div. 3)
# URL: https://codeforces.com/contest/1811/problem/E
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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
PROBLEM = """https://codeforces.com/contest/1811/problem/E
输入t(t<=1e4)代表t组数据，每组数据：
输入k。
从1开始向后的自然数中，去除所有带4的数字，问第k个数字是几（注意k从1开始计数）
"""
"""本来我写了个数位DP+二分。但是过不了，我以为和D是一样的卡记忆化，其实不是。
由于t=1e4,数位dp状态数是位数14*2*2，转移要10，再加一个log可能是50，组内复杂度就是2e5，肯定是过不了的。
---
考虑9进制：把所有数字都去掉4的话，那么其实每位只有9个选项，而且大小顺序是不变的。从1开始数的话，找出这个9进制的k即可，然后把每一位换成对应的数字。
直接用连除拆解每一位。
"""
"""想用二分+数位DP？先别急，有更简单的做法。
既然不能包含 4，那我们相当于在用 9 进制计数，所以把 k 转换成 9 进制就行了（>=4 的数位 +1）。

https://codeforces.com/contest/1811/submission/216062310"""

def my_bisect_left(a, x, lo=None, hi=None, key=None):
    """
    由于3.10才能用key参数，因此自己实现一个。
    :param a: 需要二分的数据
    :param x: 查找的值
    :param lo: 左边界
    :param hi: 右边界(闭区间)
    :param key: 数组a中的值会依次执行key方法，
    :return: 第一个大于等于x的下标位置
    """
    if not lo:
        lo = 0
    if not hi:
        hi = len(a) - 1
    else:
        hi = min(hi, len(a) - 1)
    size = hi - lo + 1

    if not key:
        key = lambda _x: _x
    while size:
        half = size >> 1
        mid = lo + half
        if key(a[mid]) < x:
            lo = mid + 1
            size = size - half - 1
        else:
            size = half
    return lo


#  tle     ms
def solve1():
    # n, = RI()
    k, = RI()

    def ok(x):
        s = str(x)
        n = len(s)

        # mp = {}
        @lru_cache
        def f(i, is_limit, is_num):
            if i == n:
                return int(is_num)
            # if (i, is_limit, is_num) in mp:
            #     return mp[i, is_limit, is_num]
            ans = 0
            if not is_num:
                ans += f(i + 1, False, False)
            up = int(s[i]) if is_limit else 9
            down = 0 if is_num else 1
            for j in range(down, up + 1):
                if j != 4:
                    ans += f(i + 1, is_limit and j == up, True)
            # mp[i, is_limit, is_num] = ans
            return ans

        ans = f(0, True, False)
        # f.cache_clear()
        return ans

    print(my_bisect_left(range(10 ** 15), k, key=ok))


#  9进制  140   ms
def solve():
    # n, = RI()
    k, = RI()
    s = '012356789'
    ans = []
    while k:
        ans.append(s[k % 9])
        k //= 9

    print(*ans[::-1], sep='')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
