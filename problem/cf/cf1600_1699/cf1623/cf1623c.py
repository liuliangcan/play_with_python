# Problem: C. Balanced Stone Heaps
# Contest: Codeforces - Codeforces Round 763 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1623/C
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
PROBLEM = """https://codeforces.com/problemset/problem/1623/C

输入 T(≤2e5) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(3≤n≤2e5) 和长为 n 的数组 a(1≤a[i]≤1e9)。

有 n 堆石子，第 i 堆石子有 a[i] 颗。
从左到右依次操作第 i=3,4,5,...,n 堆石子。
每次操作，你从第 i 堆中拿出 3k 颗石子，其中 k 颗放入第 i-1 堆，另外 2k 颗放入第 i-2 堆。
输出 min(a) 最大可以是多少。

如果您没有思路，可以先做做这题
2439. 最小化数组中的最大值
输入
4
4
1 2 10 100
4
100 100 100 1
5
5 1 1 1 8
6
1 2 3 4 5 6
输出
7
1
1
3
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
    a = RILST()

    def ok(x):
        p = [0] * n
        for i in range(n - 1, 1, -1):
            v = p[i] + a[i]
            if v < x:
                return True
            elif v > x:
                k = min(v - x, a[i]) // 3
                p[i - 1] += k
                p[i - 2] += k * 2

        if min(p[0] + a[0], p[1] + a[1]) < x:
            return True
        return False

    print(lower_bound(min(a), a[-1], ok) - 1)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
