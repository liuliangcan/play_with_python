# Problem: B -  Fill the Gaps
# Contest: AtCoder - パナソニックグループプログラミングコンテスト2023（AtCoder Beginner Contest 301）
# URL: https://atcoder.jp/contests/abc301/tasks/abc301_b
# Memory Limit: 1024 MB
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
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """给长为n的数组a，保证相邻的数不同。
在a中添加数，规则如下：
若a[i]<a[i+1]，添加a[i]+1,a[i]+2..a[i+1]-1.
若a[i]>a[i+1]，添加a[i]-1,a[i]-2..a[i+1]+1.
"""
"""直接模拟"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    ans = [a[0]]
    for i in range(1, n):
        v = a[i]
        if ans[-1] < v:
            ans.extend(list(range(ans[-1] + 1, v)))
        else:
            ans.extend(list(range(v + 1, ans[-1]))[::-1])
        ans.append(v)
    print(*ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
