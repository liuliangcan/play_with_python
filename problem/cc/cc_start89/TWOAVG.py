# Problem: Two Averages
# Contest: CodeChef - START89B
# URL: https://www.codechef.com/START89B/problems/TWOAVG
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
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """给出长为n的数组a和长为m的数组b，a[i]b[i]值域都是1~k。
每次操作你可以从选一个1~k的数追加进a或者b。
问最少几次操作可以使a的平均数严格>b。
"""
"""只有k==1是不合法的，这时ab的平均数只能是1.
否则一定可以向a无限追加2，向b无限追加1，使mean(a)≈2，mean(b)≈1。
贪心，
每次变更尝试让平均数的移动更大即可。
"""



#       ms
def solve():
    n, m, k = RI()
    a = RILST()
    b = RILST()
    sa = sum(a)
    sb = sum(b)
    # print(sa,sa/n)
    # print(sb,sb/m)
    if k == 1:
        return print(-1)
    if sa * m > sb * n:
        return print(0)
    if sa * m == sb * n:
        return print(1)
    # sa*m - sb*n 让这个式子尽快>0
    # 每次变更
    #    ->(sa+k)*m - sb*(n+1)
    # 或 ->sa*(m+1) - (sb+1)*n
    """
    """
    ans = 0
    # q = deque([(sa,m,sb,n)])
    while sa * m <= sb * n:
        if (sa + k) / (n + 1) - sa / n > (sb + 1) / (m + 1) - sb / m:
            sa += k
            n += 1
        else:
            m += 1
            sb += 1
        ans += 1
    print(ans)


#       ms
def solve2():
    n, m, k = RI()
    a = RILST()
    b = RILST()
    sa = sum(a)
    sb = sum(b)
    # print(sa,sa/n)
    # print(sb,sb/m)
    if k == 1:
        return print(-1)
    if sa * m > sb * n:
        return print(0)
    if sa * m == sb * n:
        return print(1)
    # sa*m - sb*n 让这个式子尽快>0
    # 每次变更
    #    ->(sa+k)*m - sb*(n+1)
    # 或 ->sa*(m+1) - (sb+1)*n
    """
    """
    ans = 0
    q = [(sb / m - sa / n, sa, m, sb, n, 0)]
    vis = {(sa, m, sb, n)}
    while q:
        _, sa, m, sb, n, ans = heappop(q)

        if sa * m > sb * n:
            return print(ans)
        ans += 1
        sa += k
        n += 1
        if (sa, m, sb, n) not in vis:
            heappush(q, (sb / m - sa / n, sa, m, sb, n, ans))
        sa -= k
        n -= 1
        sb += 1
        m += 1
        if (sa, m, sb, n) not in vis:
            heappush(q, (sb / m - sa / n, sa, m, sb, n, ans))

    print(-1)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
