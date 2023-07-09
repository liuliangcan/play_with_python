# Problem: C - Medicine
# Contest: AtCoder - Denso Create Programming Contest 2023 (AtCoder Beginner Contest 309)
# URL: https://atcoder.jp/contests/abc309/tasks/abc309_c
# Memory Limit: 1024 MB
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
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """Snuke医生开了N种药给高桥。在接下来的a i 天里（包括开药那天），他必须每天服用b i 颗第i种药物。他不需要再服用其他药物。

假设开药的那天是第11天。从第11天开始，他第一次需要服用K颗或更少颗数的药物是哪一天？

限制条件：
1 ≤ N ≤ 3 × 10^5
0 ≤ K ≤ 10^9
1 ≤ a i ，b i ≤ 10^9
所有输入值都是整数。
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


def bootstrap(f, stack=[]):

    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


#       ms
def solve():
    n,k = RI()
    # print(n,k)
    ab = []
    s = 0
    h = [0]
    for _ in range(n):
        a,b = RI()
        a-=1
        h.append(a)
        h.append(a+1)
        ab.append((a,b))
        s += b
    if s <= k:
        return print(1)
    h = sorted(set(h))
    size = len(h)
    d = [0]*(size+1)
    d[0] = s
    for a,b in ab:
        d[bisect_left(h,a+1)] -= b
    # print(d)
    s = 0
    for i,v in enumerate(d):
        s += v
        if s<=k:
            return print(h[i]+1)
    return print(max(a for a,_ in ab) + 1)






if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
