# Problem: F. Editorial for Two
# Contest: Codeforces - Educational Codeforces Round 149 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1837/problem/F
# Memory Limit: 256 MB
# Time Limit: 4000 ms

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
PROBLEM = """https://codeforces.com/contest/1837/problem/F

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤3e5。
每组数据输入 n k (1≤k≤n≤3e5) 和长为 n 的数组 a(1≤a[i]≤1e9)。

1. 从 a 中找到一个长度恰好为 k 的子序列 b。
2. 选定一个长度 L，将 b 划分成长为 L 的前缀 p，长为 k-L 的后缀 q，其中 0 <= L <= k。
3. 最小化 max(sum(p), sum(q))。
输出这个最小值。

注：子序列不一定连续。
输入
6
5 4
1 10 1 1 1
5 3
1 20 5 15 3
5 3
1 20 3 15 5
10 6
10 8 20 14 3 8 6 4 16 11
10 5
9 9 2 13 15 19 4 9 13 12
1 1
1
输出
2
6
5
21
18
1
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


#    tle33   ms
def solve1():
    n, k = RI()
    a = RILST()
    b = a[::-1]
    mx = sum(sorted(a)[:k])  # 最差的情况可以选最小的k个数然后分同一边

    def ok(x):
        def get(a):
            pre = [0] * n
            h = []
            s = 0
            for i, v in enumerate(a):
                if s + v <= x:
                    s += v
                    heappush(h, -v)
                elif h and v < -h[0]:
                    s += heapreplace(h, -v) + v  # s += v + - -h[0]
                pre[i] = len(h)
            return pre

        pre, suf = get(a), get(b)[::-1]
        if pre[-1] >= k:
            return True
        for i in range(n - 1):
            if pre[i] + suf[i + 1] >= k:
                return True
        return False

    print(lower_bound(1, mx, ok))


#       ms
def solve():
    n, k = RI()
    a = RILST()

    def ok(x):
        pre = [0] * n
        h = []
        s = 0
        for i, v in enumerate(a):
            if s + v <= x:
                s += v
                heappush(h, -v)
            elif h and v < -h[0]:
                s += heapreplace(h, -v) + v  # s += v + - -h[0]
            pre[i] = len(h)
        if len(h) >= k:
            return True
        s = 0
        h = []
        for i in range(n - 1, 0, -1):
            v = a[i]
            if s + v <= x:
                s += v
                heappush(h, -v)
            elif h and v < -h[0]:
                s += heapreplace(h, -v) + v
            if len(h) + pre[i - 1] >= k:
                return True
        return False

    mx = sum(sorted(a)[:k])
    print(lower_bound(mx // 2, mx - 1, ok))  # 最差的情况可以选最小的k个数,最好也是这k个数平分两边


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
