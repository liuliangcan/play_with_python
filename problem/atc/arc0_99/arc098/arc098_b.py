# Problem: D - Xor Sum 2
# Contest: AtCoder - AtCoder Beginner Contest 098
# URL: https://atcoder.jp/contests/abc098/tasks/arc098_b
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
if not sys.version.startswith('3.5.3'):  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
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
PROBLEM = """https://atcoder.jp/contests/abc098/tasks/arc098_b

输入 n(1≤n≤2e5) 和长为 n 的数组 a(0≤a[i]<2^20)。
a 有多少个非空连续子数组，满足元素和等于元素异或和？

思考：改成子序列要怎么做？
输入
4
2 5 4 6
输出 5

输入
9
0 0 0 0 0 0 0 0 0
输出 45

输入
19
885 8 1 128 83 32 256 206 639 16 4 128 689 32 8 64 885 969 1
输出 37
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    cnt = 0
    q = deque()
    ans = 0
    for v in a:
        q.append(v)
        while v & cnt:
            cnt ^= q.popleft()
        cnt |= v
        ans += len(q)
    print(ans)



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
