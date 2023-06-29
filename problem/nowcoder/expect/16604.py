# Problem: 麻婆豆腐
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/problem/16604
# Memory Limit: 2 MB
# Time Limit: 16604000 ms

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
RF = lambda: map(float, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """
"""


"""结论题：设有m个0.5，那么ans=2**n-2**(n-m)
设：集合S中，除第一个数外其它值异或和为1的概率是x，第一个数是1的概率是p。
则最后整个集合异或和为1的概率就是x(1-p)+p(1-x),当这个式子=0.5时满足条件。
解得x = (0.5-p)/(1-2p)=0.5
因此只要集合里有0.5这个集合就满足条件
"""

#       ms
def solve():
    RS()
    n, = RI()
    a = list(RF())
    c = 0
    for v in a:
        if v != 0.5:
            c += 1
    print(2**n-2**c)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
