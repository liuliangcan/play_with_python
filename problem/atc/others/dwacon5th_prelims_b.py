# Problem: B - Sum AND Subarrays
# Contest: AtCoder - Dwango Programming Contest V
# URL: https://atcoder.jp/contests/dwacon5th-prelims/tasks/dwacon5th_prelims_b
# Memory Limit: 1024 MB
# Time Limit: 2525 ms

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

if not sys.version.startswith('3.5.3'):  # ACW没有comb
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
PROBLEM = """https://atcoder.jp/contests/dwacon5th-prelims/tasks/dwacon5th_prelims_b

输入 n(2≤n≤1000) k(1≤k≤n*(n+1)/2) 和长为 n 的数组 a(1≤a[i]≤1e9)。
a 一共有 n*(n+1)/2 个非空连续子数组，也有对应的 n*(n+1)/2 个子数组元素和。
从这 n*(n+1)/2 个元素和中，选择 k 个，计算这 k 个数的按位与（AND）。
按位与的最大值是多少？

不考虑输入的空间，你能做到 O(1) 额外空间吗？
输入
4 2
2 5 2 5
输出 12

输入
8 4
9 1 8 2 7 5 6 4
输出 32
"""
"""拆位贪心
从高位向低位考虑能否填1：如果和里有k个以上的1能同时满足之前的答案且当前位有1，那么这位就可以填1
"""


#   221  ms
def solve():
    n, k = RI()
    a = RILST()
    ans = 0
    for p in range(40, -1, -1):  # wa两次:注意不是从29开始，因为考虑的是数组和，因此是sum(a).bit_length
        c = 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += a[j]
                if s >> p & 1 and (s & ans) == ans:  # 这个和的当前为是1，且这个和满足当前最大值
                    c += 1
                    if c >= k:  # 这位上的1超过k个，则这位可以是1
                        ans |= 1 << p
                        break
            if c >= k:
                break
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
