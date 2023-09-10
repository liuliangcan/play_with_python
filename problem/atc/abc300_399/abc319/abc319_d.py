# Problem: D - Minimum Width
# Contest: AtCoder - AtCoder Beginner Contest 319
# URL: https://atcoder.jp/contests/abc319/tasks/abc319_d
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
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """问题陈述
Takahashi在一个窗口中显示了一个有N个单词的句子。所有单词的高度相同，第i个单词（1≤i≤N）的宽度为Li。

这些单词在窗口中以一个宽度为1的空格分隔开。更具体地说，当句子在宽度为W的窗口中显示时，满足以下条件。

句子被分成几行。
第一个单词显示在顶行的开头。
第i个单词（2≤i≤N）要么在第（i-1）个单词之后有一个宽度为1的间隙，要么显示在包含第（i-1）个单词的行的下一行的开头。它不会在其他地方显示。
每行的宽度不超过W。这里，一行的宽度是指从最左边的单词的左端到最右边的单词的右端的距离。
当Takahashi将句子显示在窗口中时，句子适合M行或更少。找出窗口的最小可能宽度。
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


#       ms
def solve():
    n, m = RI()
    a = RILST()

    def ok(x):
        p = 0
        c = 1
        for v in a:
            if p == 0:
                p += v
            else:
                p += v + 1
                if p > x:
                    c += 1
                    p = v
                    if c > m:
                        return False
        return True

    print(lower_bound(max(a), sum(a) + n - 1, ok))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
