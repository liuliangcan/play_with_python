# Problem: D. Reverse Sort Sum
# Contest: Codeforces - Codeforces Round #782 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1659/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1659/D

输入 t(≤1000) 表示 t 组数据，每组数据输入 n(≤2e5) 和长为 n 的数组 c(0≤c[i]≤n)。
所有数据的 n 之和不超过 2e5。

对于只有 0 和 1 的数组 a，定义 b[i] 为把 a 的前 i 个元素从小到大排序后的新数组（下标从 1 开始）。
定义 c[j] = b[1][j] + b[2][j] + ... + b[n][j]。
现在数组 c 输入给你了，请你构造任意一个符合要求的数组 a。输入保证数组 a 存在。

*本题做法不止一种，欢迎在群内交流。
"""
"""https://codeforces.com/problemset/submission/1659/195082636

提示 1：从特殊到一般，思考 a 中只有一个 1 时，数组 c 会是什么样的。你可以从这个 1 在末尾开始思考。

看到不变量了吗？

提示 2：a 中 1 的数量等于 sum(c)/n，记作 k。

提示 3：试试倒着构造 a。

提示 4：假设 c[n]=n，此时 a[n]=1。
为了把问题转换成 n-1 个数的问题，需要从 c 中去掉 b[n] 带来的影响。如何去掉？
由于 b[n] 是一个末尾有 k 个 1 的数组，所以把 c 中的 [n-k+1,n] 都减一即可。
用差分数组/树状数组/线段树实现。
继续思考，注意每次都需要把 b[i] 带来的影响去掉。"""


#    156   ms
def solve():
    n, = RI()
    c = RILST()
    k = sum(c) // n
    d = [0] * n
    sd = 0
    a = [0] * n
    for i in range(n - 1, -1, -1):
        sd += d[i]
        if c[i] + sd == i + 1:
            a[i] = 1
        sd -= 1
        if i - k >= 0:
            d[i - k] += 1
        if a[i] == 1:
            k -= 1
    print(*a)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
