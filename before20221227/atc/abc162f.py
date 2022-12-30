import sys
from collections import *
from itertools import *
from math import sqrt, inf
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

FFF = 'abcinput.txt'
if os.path.exists(FFF):
    sys.stdin = open(FFF)

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://atcoder.jp/contests/abc162/tasks/abc162_f

本题是力扣 198. 打家劫舍 的变形题。

输入 n (2≤n≤2e5) 和长为 n 的数组 a (-1e9≤a[i]≤1e9)。
数组 a 就是 198 题的房屋存放金额。
在本题中，你必须恰好偷 floor(n/2) 个房子。
输出你能偷窃到的最高金额。 

你能做到 O(1) 空间吗？
输入
6
1 2 3 4 5 6
输出 12

输入
5
-1000 -100 -10 0 10
输出 0

输入
10
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
输出 5000000000

输入
27
18 -28 18 28 -45 90 -45 23 -53 60 28 -74 -71 35 -26 -62 49 -77 57 24 -70 -93 69 -99 59 57 -49
输出 295
"""


#     624 	 ms
def solve(n, a):
    k = n // 2
    sys.setrecursionlimit(n * 2 + 10)

    @lru_cache()
    def f(n, k, last):  # 前n个屋取k个，且最后一个取或不取
        if n == 1:
            if last == k == 1:  # 剩第一个房子，要么取
                return a[0]
            if last == k == 0:  # 要么不取，其它情况都是非法，返回无穷小
                return 0
            return -inf

        if last == 0:
            if n < 2 * k:  # 尾不取，n最少是2k，剪枝
                return -inf
            return max(f(n - 1, k, 1), f(n - 1, k, 0))
        else:
            if n - 1 < 2 * (k - 1):  # 尾取，剩余n最小是2*剩余k，剪枝
                return -inf
            return f(n - 1, k - 1, 0) + a[n - 1]

    print(max(f(n, k, 1), f(n, k, 0)))


if __name__ == '__main__':
    n, = RI()
    a = RILST()

    solve(n, a)
