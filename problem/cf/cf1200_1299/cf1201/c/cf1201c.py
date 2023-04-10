# Problem: C. Maximum Median
# Contest: Codeforces - Codeforces Round 577 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1201/C
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/1201/C

【灵茶の试炼】一周年纪念。

输入 n(1≤n≤2e5 且是奇数) k(1≤k≤1e9) 和长为 n 的数组 a(1≤a[i]≤1e9)。

每次操作你可以把 a 中的一个数加一。
至多操作 k 次。

输出 a 的中位数的最大值。
输入
3 2
1 3 5
输出 5

输入
5 5
1 2 1 1 1
输出 3

输入
7 7
4 1 2 4 3 4 4
输出 5
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(开区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi。
    虽然实现是开区间写法，但为了和切片/数组下标统一，接口依然以[左闭,右开)方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


#   156 ms
def solve1():
    n, k = RI()
    a = RILST()
    a.sort()
    a = a[n // 2:]

    def is_right(x):
        s = k
        for i, v in enumerate(a):
            if v < x:
                s -= x - v
            else:
                break
        return s < 0

    print(lower_bound(0, k + a[0] + 1, key=is_right) - 1)
#    171   ms
def solve():
    n, k = RI()
    a = RILST()
    a.sort()
    t = n // 2
    ans = a[t]
    cnt = 1
    for i in range(t + 1, n):
        if cnt * (a[i] - ans) <= k:
            k -= cnt * (a[i] - ans)
            ans = a[i]
        elif k < cnt:
            break
        else:
            p = k // cnt
            ans += p
            k -= cnt * p
        cnt += 1

    if cnt <= k:
        ans += k // cnt
    print(ans)


if __name__ == '__main__':
    solve()
