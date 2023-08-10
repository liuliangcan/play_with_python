# Problem: F - Xor Minimization
# Contest: AtCoder - AtCoder Beginner Contest 281
# URL: https://atcoder.jp/contests/abc281/tasks/abc281_f
# Memory Limit: 1024 MB
# Time Limit: 2500 ms

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
PROBLEM = """https://atcoder.jp/contests/abc281/tasks/abc281_f

输入 n(1≤n≤1.5e5) 和长为 n 的数组 a(0≤a[i]<2^30)。
选一个非负整数 x，然后把每个 a[i] 更新成 a[i] XOR x。
输出 max(a) 的最小值。
输入
3
12 18 11
输出 16
解释：取 x=2

输入
10
0 0 0 0 0 0 0 0 0 0
输出 0

输入
5
324097321 555675086 304655177 991244276 9980291
输出 805306368
"""
"""处理二进制问题的基本技巧之一是【拆位】。

从高到低枚举比特位。如果在第 k 位上，有些 a[i] 是 0，有些 a[i] 是 1，那么无论 x 的第 k 位是 0 还是 1，max(a) 的第 k 位必定是 1。
分类讨论：
如果 x 第 k 位取 0，那么 a[i] 第 k 位也是 0 的就不用考虑了，只需要考虑 a[i] 第 k 位是 1 的。
如果 x 第 k 位取 1，那么 a[i] 第 k 位也是 1 的就不用考虑了，只需要考虑 a[i] 第 k 位是 0 的。

这启发我们得到如下分治算法：
定义 f(a, k) 表示只考虑 <= k 位的前提下，max(a) 的最小值。
如果 a[i] 的第 k 位都一样，那么 f(a, k) = f(a, k-1)。
如果 a[i] 的第 k 位不都一样，那么 f(a, k) = min(f(b, k-1), f(c, k-1)) | (1 << k)，其中 b 表示第 k 位是 0 的元素组成的数组，c 表示第 k 位是 1 的元素组成的数组。
递归边界：k<0 时，返回 0。
递归入口：f(a, 29)。

代码实现时：
1. 为了快速判断【a[i] 的第 k 位是否都一样】，可以先把 a 排序，再去分治。
2. 为了快速分出数组 b 和数组 c，可以用二分查找 0 和 1 的分界线，为此需要多一个参数 pre 表示 a[i] 二进制的公共前缀，具体见代码。
注：可以不用二分查找，因为写个 for 循环来找分界线也 ok。

https://atcoder.jp/contests/abc281/submissions/44402795"""


#   782     ms
def solve():
    n, = RI()
    a = RILST()

    def dfs(a, bit):
        if bit < 0:
            return 0

        x, y = [v for v in a if v >> bit & 1], [v for v in a if not v >> bit & 1]
        if not x: return dfs(y, bit - 1)
        if not y: return dfs(x, bit - 1)
        return min(dfs(x, bit - 1), dfs(y, bit - 1)) | (1 << bit)

    print(dfs(a, 29))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
