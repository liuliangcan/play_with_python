# Problem: D. Odd-Even Subsequence
# Contest: Codeforces - Codeforces Round #651 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1370/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1370/D

输入 n k (2≤k≤n≤2e5) 和长为 n 的数组 a (1≤a[i]≤1e9)。
从 a 中选出一个长为 k 的子序列 s，下标从 1 开始。
定义 x=max(s[1],s[3],s[5],...)，y=max(s[2],s[4],s[6],...)
输出 min(x,y) 的最小值。
注：子序列不一定是连续的。
输入
4 2
1 2 3 4
输出 1
解释 s=[1,3]

输入
4 3
1 2 3 4
输出 2
解释 s=[1,2,4]

输入
5 3
5 3 4 2 6
输出 2

输入
6 4
5 3 50 2 4 5
输出 3
解释 s=[3,50,2,4]

https://codeforces.com/contest/1370/submission/95403435

提示 1：讨论 min(x, y) 是 x 还是 y，那么问题就变成「最小化最大值」了，二分答案。

提示 2：假设是 x，遍历 a，遇到一个 <= mid 的数，把它当作是属于 x 的，计数器+1；同时后面一个数必须要属于 y，那么随便选（因为只看 x），计数器也+1。如果最后计数器 >= k 那么 check 返回 true，否则返回 false。
假设是 y，那么同理，只不过要从 a 的第二个数开始算（第一个数已经属于 x 了）。

"""


def my_bisect_left(a, x, lo=None, hi=None, key=None):
    """
    由于3.10才能用key参数，因此自己实现一个。
    :param a: 需要二分的数据
    :param x: 查找的值
    :param lo: 左边界
    :param hi: 右边界(闭区间)
    :param key: 数组a中的值会依次执行key方法，
    :return: 第一个大于等于x的下标位置
    """
    if not lo:
        lo = 0
    if not hi:
        hi = len(a) - 1
    else:
        hi = min(hi, len(a) - 1)
    size = hi - lo + 1

    if not key:
        key = lambda _x: _x
    while size:
        half = size >> 1
        mid = lo + half
        if key(a[mid]) < x:
            lo = mid + 1
            size = size - half - 1
        else:
            size = half
    return lo


#    311   ms
def solve():
    n, k = RI()
    a = RILST()

    # 最小化最大值:左false右True模型；分别讨论x满足和y满足的情况（只要一边满足就行）
    def check(x):
        def f(i):  # i是遍历的起始位置：若认为答案在x中，则从0开始遍历，子序列一开始长度0；若认为答案在y中，则y从1开始遍历，a[0]给x，子序列长度直接是1。
            cnt = i
            while i < n:
                if a[i] <= x:  # 这个数符合，则给x或y
                    cnt += 1
                    i += 1
                    if i < n:  # 下个数直接给对面
                        cnt += 1
                        i += 1
                    continue
                i += 1
                if cnt >= k:
                    return True
            return cnt >= k

        return f(0) or f(1)  # 任意x或y里的最大值满足<=x即可

    print(my_bisect_left(range(max(a) + 1), True, key=check))


if __name__ == '__main__':
    solve()
