# Problem: C. Water the Trees
# Contest: Codeforces - Educational Codeforces Round 126 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1661/problem/C
# Memory Limit: 256 MB
# Time Limit: 3000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/1661/problem/C

输入 t(≤2e4) 表示 t 组数据，每组数据输入 n(≤3e5) 和长为 n 的数组 h(1≤h[i]≤1e9)，表示 n 棵树的高度。所有数据的 n 之和不超过 3e5。

在第 1,3,5,... 天，你可以把一棵树的高度+1，或者不做任何事。
在第 2,4,6,... 天，你可以把一棵树的高度+2，或者不做任何事。
要使所有树的高度一样，至少要多少天？

输入
3
3
1 2 4
5
4 4 3 5 5
7
2 5 4 8 3 7 4
输出
4
3
16
解释 第一组数据的操作：第一棵树+1，第二棵树+2，跳过，第一棵树+2
"""
"""贪心
最终高度只能是mx或mx+1（我做的时候无法证明不可能是mx+2，因此多算了一次mx+2）
那么把要增加的高度分别求出来，可以拆分成a个1和b个2.
分类讨论即可：
若a>b，则a可以顺序往下填，b靠前即可，填成12121010101，最终是a*2-1
若a==b，则恰好可以1212一直填完，直接return a*2
若a<b，先把a填完，即a个1212..，然后剩下的b可以拆成1212填，每次花2天填3个，下取整，然后讨论剩下的是1还是2决定第一天还是第二天填。

好像二分答案也可以。
"""


#    186   ms
def solve():
    n, = RI()
    h = RILST()
    mx = max(h)

    def f(d):
        a = b = 0  # 1和2的个数
        for x in h:
            p, m = divmod(mx + d - x, 2)
            a += m
            b += p
        if a > b:
            ans = a * 2 - 1
        elif a == b:
            ans = a * 2
        else:
            ans = a * 2
            b -= a
            ans += b * 2 // 3 * 2
            ans += b * 2 % 3
        return ans

    # print(min(f(0), f(1), f(2)))
    return min(f(0), f(1))


if __name__ == '__main__':
    t, = RI()
    ans = []
    for _ in range(t):
        ans.append(solve())
    print(*ans, sep='\n')  # 170ms
