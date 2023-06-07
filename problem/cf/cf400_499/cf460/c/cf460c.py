# Problem: C. Present
# Contest: Codeforces - Codeforces Round 262 (Div. 2)
# URL: https://codeforces.com/problemset/problem/460/C
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
PROBLEM = """https://codeforces.com/problemset/problem/460/C

输入 n m w (1≤w≤n≤1e5) (1≤m≤1e5) 和长为 n 的数组 a(1≤a[i]≤1e9)。
你需要操作 m 次，每次操作可以选一个长为 w 的连续子数组，把数组内的元素都加一。
输出 min(a) 的最大值。
输入
6 2 3
2 2 2 2 1 1
输出 2

输入
2 5 1
5 8
输出 9
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


#    109   ms
def solve():
    n, m, w = RI()
    a = RILST()

    def ok(x):
        cnt = 0
        s = 0
        d = [0] * (n + w + 1)
        for i, v in enumerate(a):
            s += d[i]
            delta = x - (s + v)
            if delta > 0:
                cnt += delta
                if cnt > m:
                    return True
                d[i + w] -= delta
                s += delta
        return False

    print(lower_bound(min(a), a[0] + m, ok) - 1)


if __name__ == '__main__':
    n, m, w = RI()
    a = RILST()
    l = min(a) - 1
    r = l + m + 2
    while l + 1 < r:
        mid = (l + r) >> 1
        cnt = 0
        s = 0
        d = [0] * (n + w + 1)
        for i, v in enumerate(a):
            s += d[i]
            delta = mid - (s + v)
            if delta > 0:
                cnt += delta
                if cnt > m:
                    break
                d[i + w] -= delta
                s += delta
        if cnt > m:
            r = mid
        else:
            l = mid
    print(r - 1)
