# Problem: C. Baby Ehab Partitions Again
# Contest: Codeforces - Codeforces Round 717 (Div. 2)
# URL: https://codeforces.com/contest/1516/problem/C
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
# MOD = 998244353
PROBLEM = """https://codeforces.com/contest/1516/problem/C

输入 n(2≤n≤100) 和长为 n 的数组 a(1≤a[i]≤2000)。
你需要删除 a 中的一些数，使 a 无法分成两个元素和相等的子序列。
输出最少要删除多少个数，以及这些数的下标（从 1 开始）。
注：子序列不要求连续。
输入
4
6 3 9 12
输出
1
2
解释 6+9=3+12，删除 3。

输入
2
1 2
输出
0
"""
"""分类讨论：

1. 如果 sum(a) 是奇数，显然没法分，无需删除任何数字，输出 0。
2. 如果无法从 a 中选出元素和等于 sum(a)/2 的子序列，那么也没法分，输出 0。这可以用 0-1 背包判断。
3. 否则就可以分，那么要如何删除呢？此时 sum(a) 是偶数，由于偶数 - 奇数 = 奇数，所以减去一个奇数即可。
4. 要是没有奇数呢？此时每个 a[i] 都是偶数，那么把每个 a[i] 都除以 2，是不会影响答案的。反复除以 2 直到 a 中有奇数为止。

代码实现时，无需反复除以 2，而是除以最小的 lowbit(a[i])。如果要删除数字，也是删除 lowbit 最小的数。

https://codeforces.com/contest/1516/submission/213269180"""
"""灵神这个做法本质和除gcd一样，但是只除了gcd里的所有2.
因为最终是要找奇数，除完2即可。
"""
#   78    ms
def solve():
    n, = RI()
    a = RILST()
    s = sum(a)
    if s & 1:  # 和是奇数不能划分
        return print(0)
    t = s // 2
    f = [1] + [0] * t  # 背包试一下能不能划分
    for v in a:
        for j in range(t, v - 1, -1):
            f[j] |= f[j - v]
    if not f[-1]:
        return print(0)
    g = reduce(gcd, a)  # 把所有数字中相同的部分除光，这部分会随着数字移动，没有影响；然后找到一个奇数，拿掉它，剩下的和就是奇数。
    for i, v in enumerate(a, start=1):
        if (v // g) & 1:
            return print(f'1\n{i}')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
