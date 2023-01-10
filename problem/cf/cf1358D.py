# Problem: D. The Best Vacation
# Contest: Codeforces - Codeforces Round #645 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1358/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1358/D

输入 n(n≤2e5) x 和长为 n 的数组 d(1≤d[i]≤1e6 且 1≤x≤sum(d))。
在某地，一年有 n 月，其中第 i 月有 d[i] 天，天数从 1 到 d[i]，在第 j 天你可以得到 j 元。
问在该地连续呆 x 天你最多能得到多少元。
注意：从当年最后一月呆到下一年的第一月是可以的。
输入
3 2
1 3 1
输出 5
解释 在二月呆最后两天，得到 2+3=5

输入
3 6
3 3 3
输出 12
解释 任意完整两月均可，得到 (1+2+3)+(1+2+3)=12

输入
5 6
4 2 3 1 3
输出 15
解释 最后一月呆 2 天，第一月呆 4 天，得到 (2+3)+(1+2+3+4)=15
"""
"""https://codeforces.com/problemset/submission/1358/188648522

提示 1：看成是环形数组，那么数组复制一份接在后面，就变成非环形的了（注意 x 不超过 sum(d)）。

提示 2：这是个窗口大小为 x 的滑窗问题，但是 x 太大了，如何优化？

提示 3：窗口的开头或者末尾只需要在某些关键的 day 就行了，是什么样的 day 呢？

提示 4：月末收益最大。

提示 5：窗口末尾只需要在月末就行。可以用反证法证明：
假设窗口末尾不在月末是最优的，设末尾在第 k 天，那么右边一定是第 k+1 天。
如果窗口向右滑，由于我们假设不在月末更优，因此窗口的元素和减少，所以从左边出去的元素必然大于 k+1，出去的元素的左边那个元素必然大于 k。那么把窗口改为向左滑，窗口左边进来一个大于 k 的数，右边出去一个等于 k 的数，窗口元素和变大，矛盾，因此窗口末尾一定在月末是最优的。

那么在(倍增后的 d 数组)上双指针模拟就好了。
"""

"""由于证明了窗口末位必须在某个月末，因此直接滑窗
"""


#    pypy405   ms;pypy64:155ms
def solve():
    n, x = RI()
    d = RILST()
    d += d  # 环形数组首尾相接转化成一次滑窗
    l = 0
    p = 0  # 窗口内呆了多少天
    s = 0  # 钱
    ans = 0
    for v in d:
        p += v  # 窗口天数增加
        s += (1 + v) * v // 2  # 窗口内能得的钱增加
        while p > x:  # 如果天数超了，就从窗口左侧开始减
            p -= d[l]
            s -= (1 + d[l]) * d[l] // 2
            l += 1
        if l:
            c = x - p
            z = s + (d[l - 1] * 2 - c + 1) * c // 2
            if ans < z:
                ans = z
        elif ans < s:
            ans = s

    print(ans)


#   670    ms
def solve1():
    n, x = RI()
    d = RILST()
    d += d  # 环形数组首尾相接转化成一次滑窗
    q = deque()  # 用队列模拟滑窗
    p = 0  # 窗口内呆了多少天
    s = 0  # 钱
    ans = 0
    for v in d:
        q.append([1, v])  # 窗口右侧纳入一个月的起始和末位
        p += v  # 窗口天数增加
        s += (1 + v) * v // 2  # 窗口内能得的钱增加
        while p > x:  # 如果天数超了，就从窗口左侧开始减
            diff = p - x  # 需要减多少天
            l, r = q[0]  # 窗口最左侧那个月还剩几天
            if r - l + 1 > diff:  # 如果天数超过需要减去的天，显然这个元素不用弹出，从左边减对应天数即可
                s -= (l + l + diff - 1) * diff // 2  # 去掉对应的钱
                q[0][0] += diff  # 弹出部分天
                p -= diff  # 更新窗口总天数
            else:  # 如果不够用，显然需要整个弹出
                l, r = q.popleft()
                s -= (l + r) * (r - l + 1) // 2  # 更新钱数
                p -= r - l + 1  # 更新天数
        if p == x and ans < s:
            ans = s
    print(ans)


if __name__ == '__main__':
    solve()
