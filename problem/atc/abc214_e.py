# Problem: E - Packing Under Range Regulations
# Contest: AtCoder - AtCoder Beginner Contest 214
# URL: https://atcoder.jp/contests/abc214/tasks/abc214_e
# Memory Limit: 1024 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://atcoder.jp/contests/abc214/tasks/abc214_e

输入 t(≤2e5) 表示 t 组数据，每组数据输入 n(≤2e5) 和 n 个区间 [L,R]，范围在 [1,1e9]。
所有数据的 n 之和不超过 2e5。

你有 n 个球，第 i 个球需要放在区间 [L,R] 内的整数位置上。
但每个整数位置上至多能放一个球。
如果可以做到，输出 Yes，否则输出 No
输入
2
3
1 2
2 3
3 3
5
1 2
2 3
3 3
1 3
999999999 1000000000
输出
Yes
No

2022年12月16日
"""
"""按左端点L排序
每个点p放在尽可能靠左的地方，但要<=R。
放完p+=1。
每次把左端点<=p的区间都拿出来，这些都可以放，但优先放R小的，因为它很快就不能放了。
"""

#       ms
def solve():
    t, = RI()
    for _ in range(t):
        n, = RI()
        a = []
        for _ in range(n):
            l, r = RI()
            a.append((l, r))
        a.sort()
        j = p = 0
        h = []
        while j < n or h:
            while j < n and a[j][0] <= p:
                heappush(h, a[j][1])
                j += 1
            if not h:
                p = a[j][0]
            else:
                if heappop(h) < p:
                    print('No')
                    break
                p += 1
        else:
            print('Yes')


if __name__ == '__main__':
    solve()
