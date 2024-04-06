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
PROBLEM = """https://www.lanqiao.cn/problems/17159/learning/?contest_id=179
两个数字操作后，不会减小总和，但是可以把大数变小，小数*2（换言之，小数可以进一位）。
先贪心的用相同数的两个k可以合并为k+1。
这样每个位上只有1个数，如果可以直接合并成1个则答案是1.
否则，答案一定是2：可以用最大那个数，从最小的数开始进，并且剩余的数字足够继续进其余的数，因为2^k前边所有位加起来也不会超过2^k：
    即2^k > 2^k -1 == 2^0+2^1+2^2+2^3+..+2^(k-1) 
那么，最后只会剩两个数。
"""

#
# #       ms
# def solve():
#     dd, = RI()
#     lst = RILST()
#     if dd == 1: return print(1)
#
#     lst.sort()
#     cnt = Counter(lst)
#     h = sorted(set(lst))
#     abcbc = []
#     while h:
#         vvv = heappop(h)
#         xxx = cnt[vvv]
#         if xxx & 1:  abcbc.append(vvv)
#         xxx //= 2
#         if xxx:
#             if vvv + 1 not in cnt:  heappush(h, vvv + 1)
#             cnt[vvv + 1] += xxx
#     print(1 if len(abcbc) == 1 else 2)


#       ms
def solve2():
    n, = RI()
    a = RILST()
    if n == 1:
        return print(1)

    a.sort()
    cnt = Counter(a)
    h = sorted(set(a))
    left = []
    while h:
        x = heappop(h)
        c = cnt[x]
        if c & 1:
            left.append(x)
        c //= 2
        if c:
            if x + 1 not in cnt:
                heappush(h, x + 1)
            cnt[x + 1] += c
    if len(left) == 1:
        return print(1)

    print(2)


#       ms
def solve():
    n, = RI()
    a = RILST()
    if n == 1:
        return print(1)
    a.sort()
    ans = []
    while a:
        x = heappop(a)
        while a and x == a[0]:
            # print(x,a)
            heapreplace(a, x + 1)
            x = heappop(a)
        ans.append(x)
        # print(ans,a)
    print(min(len(ans),2))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
