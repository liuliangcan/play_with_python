# Problem: D - Between Two Arrays
# Contest: AtCoder - Exawizards Programming Contest 2021（AtCoder Beginner Contest 222）
# URL: https://atcoder.jp/contests/abc222/tasks/abc222_d
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
RANDOM = random.randrange(2 ** 62)
# MOD = 10**9 + 7
MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc222/tasks/abc222_d

输入 n(1≤n≤3000) 和两个长为 n 的数组 a b，元素范围在 [0,3000]，且均为递增数组（允许有相同元素）。
构造递增数组 c（允许有相同元素），满足 a[i]<=c[i]<=b[i]。
输出你能构造多少个不同的 c，模 998244353。
输入
2
1 1
2 3
输出 5

输入
3
2 2 2
2 2 2
输出 1

输入
10
1 2 3 4 5 6 7 8 9 10
1 4 9 16 25 36 49 64 81 100
输出 978222082
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    f = [0] * 3001
    for i in range(a[0], b[0] + 1):
        f[i] = 1
    for x, y in zip(a[1:], b[1:]):
        pre = list(accumulate(f))
        f = [0] * 3001
        for i in range(x, y + 1):
            f[i] = pre[i] % MOD
    print(sum(f) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
