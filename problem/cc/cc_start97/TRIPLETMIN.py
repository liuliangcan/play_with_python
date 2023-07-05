# Problem: Triplets Min
# Contest: CodeChef - START97B
# URL: https://www.codechef.com/START97B/problems/TRIPLETMIN
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

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(
#     str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""
"""先是尝试二分 tle了。发现复杂度是qnlgU
然后发现check里求的是前缀和，那么预处理前缀和，check里可以二分位置，还是tle，q*lgn*lgu。这样的话是3e5*19*30 确实会挂。
还是由于前缀和，不会变小，那么可以考虑离线询问，双指针回答，就变成n+q了，再加上两个sort复杂度即可。
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


#   nlgn+qnlgU  tle4  ms
def solve1():
    n, q = RI()
    a = RILST()
    a.sort()
    for _ in range(q):
        k, = RI()

        def ok(x):
            s = 0
            p = n
            for v in a:
                if v > x: break
                p -= 1
                s += p * (p - 1) // 2
                if s >= k:
                    return True
            return False

        print(lower_bound(a[0], a[-1], ok))


# nlgn+ qlgnlogU  tle2   ms
def solve2():
    n, q = RI()
    a = RILST()
    a.sort()
    ss = [0] * n
    r = 1
    for i in range(n - 2, -1, -1):
        ss[i] = r * (r - 1) // 2
        r += 1
    pre = list(accumulate(ss))
    for _ in range(q):
        k, = RI()

        def ok(x):
            return pre[bisect_right(a, x) - 1] >= k

        print(lower_bound(a[0], a[-1], ok))

# ac nlgn + qlogq + q+n
def solve():
    n, q = RI()
    a = RILST()
    a.sort()
    ss = [0] * n
    r = 1
    for i in range(n - 2, -1, -1):
        ss[i] = r * (r - 1) // 2
        r += 1

    pre = list(accumulate(ss))
    qs = []
    for _ in range(q):
        k, = RI()
        qs.append(k)
    ans = [0] * q
    j = 0
    for k, i in sorted(zip(qs, range(q))):
        while pre[j] < k:
            j += 1
        ans[i] = a[j]
    print(*ans, sep='\n')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
