# Problem: F - Damage over Time
# Contest: AtCoder - NS Solutions Corporation Programming Contest 2023（AtCoder Beginner Contest 303）
# URL: https://atcoder.jp/contests/abc303/tasks/abc303_f
# Memory Limit: 1024 MB
# Time Limit: 3500 ms

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
PROBLEM = """怪物血量h，
你有n个dot技能，第i个技能持续ti秒，秒伤di
每秒可以放一个技能，问怪物最早啥时候死
1<=n<=3e5
1<=h<=1e18
1<=ti,di<=1e9
"""
"""首先发现答案可以二分：总时间越大，可以造成的伤害越高。
主要是check很难写：因为时间高达1e18,要考虑降到n。
假设当前剩余时间是x，那么所以技能可以分为两类：
1. t<=x的技能，我们可以选p=t*d最大的那个技能，能选几次？显然是cnt=x-t+1次，因为在t~x这个区间内，都是它最屌。直接选cnt次，那么下次不用考虑它了，只会考虑t更小的技能。
2. t>=x的技能，他们能造成的伤害是q=d*x，那么要找d最大的那个技能。他能选几次呢？
我们考虑从上边两种情况选更大的那个:
1. 当p>=q: 我们就直接选cnt次p，因为这次一定是选p；下次x会变小，q只会更小，可以继续选p。
2. 当p<q: 考虑选一次d*x，然后再选几次d*x'，直到剩余d*x'<=p。即cnt=x-p//d
这样，不管是选哪种，每个技能最多被考虑两次，check就可以O(n)了。
实现时，用类似单调栈的思想，对t排序后，预处理记录t*d的前缀最大值，同时记录每个d。
check时，可以让剩余时间x一直降，那么用双指针逆序访问单调栈，同时记录后缀最大的d即可。
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


#    wa   ms
def solve():
    n, h = RI()
    a = []
    for _ in range(n):
        t, d = RI()
        a.append((t, d))
    a.sort()
    pre = [(a[0][0], a[0][0] * a[0][1], a[0][1])]
    for t, d in a[1:]:
        if t * d > pre[-1][1]:
            pre.append((t, t * d, d))

    # suf = [tuple(a[-1])]
    # for i in range(n - 2, -1, -1):
    #     if a[i][1] > suf[-1][1]:
    #         suf.append(tuple(a[i]))
    # suf = suf[::-1]

    def ok(x):
        s = 0
        if x >= pre[-1][0]:
            delta = x - pre[-1][0] + 1
            s += delta * pre[-1][1]
            x = pre[-1][0] - 1
        i = len(pre) - 1
        suf = 0
        while x > 0 and s < h:
            while i >= 0 and pre[i][0] > x:
                suf = max(suf, pre[i][2])
                i -= 1
            p = 0
            if i >= 0:
                t, p, d = pre[i]

            if p < suf * x:
                d = max(x - p // suf - 1, 1)
                s += suf * (x + x - d + 1) * d // 2
            else:
                d = x - t + 1
                s += p * d
            x -= d
        return s >= h

    print(lower_bound(1, 10 ** 18, ok))


#   wa    ms
def solve2():
    n, h = RI()
    a = []
    for _ in range(n):
        t, d = RI()
        a.append((t, d))
    a.sort()
    pre = [(a[0][0], a[0][0] * a[0][1])]
    for t, d in a[1:]:
        if t * d > pre[-1][1]:
            pre.append((t, t * d))
        else:
            pre.append(pre[-1])

    def ok(x):
        s = 0
        i = n - 1
        suf = 0
        while x > 0 and s < h:
            while i >= 0 and pre[i][0] > x:
                suf = max(suf, a[i][1])
                i -= 1
            # p = 0
            # if i >= 0:
            #     t, p = pre[i]

            if i < 0 or pre[i][1] < suf * x:
                down = 0
                if i >= 0:
                    down = pre[i][1] // suf
                d = x - down
                x -= d
                s += (x + x - d + 1) * d // 2 * suf
            else:
                d = x - pre[i][0] + 1
                s += pre[i][1] * d
                x -= d
        return s >= h

    print(lower_bound(0, 10 ** 18, ok))


#   1967     ms
def solve3():
    n, h = RI()
    a = []
    for _ in range(n):
        t, d = RI()
        a.append((t * d, -t, d))
    a.sort(key=lambda x: -x[1])
    pre = [a[0]] * n
    for i in range(1, n):
        pre[i] = max(pre[i - 1], a[i])

    def ok(x):
        cur = h
        pos = n - 1
        suf = 0
        while x > 0 and cur > 0:
            while pos >= 0 and -pre[pos][1] > x:
                suf = max(suf, a[pos][2])
                pos -= 1

            if pos < 0 or pre[pos][0] < suf * x:
                down = 0
                if pos >= 0:
                    down = pre[pos][0] // suf
                d = x - down
                cur -= (x + x - d + 1) * d // 2 * suf
            else:
                d = x - -pre[pos][1] + 1
                cur -= pre[pos][0] * d
            x -= d
        return cur <= 0

    # l,r = 0,10**18
    # while l + 1< r:
    #     mid = (l+r)>>1
    #     if ok(mid):
    #         r = mid
    #     else:
    #         l = mid
    # print(r)
    print(lower_bound(1, 10 ** 18, ok))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
