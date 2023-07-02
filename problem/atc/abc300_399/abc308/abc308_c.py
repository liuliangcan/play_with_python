# Problem: C - Standings
# Contest: AtCoder - AtCoder Beginner Contest 308
# URL: https://atcoder.jp/contests/abc308/tasks/abc308_c
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
from functools import lru_cache, reduce, cmp_to_key
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
PROBLEM = """给出每个人投硬币正面和反面的次数，定义命中率为a/(a+b)，
要求按命中率降序，若相同，则按序号升序。
"""
"""其实就是自定义排序，但py的自定义key写法涉及到浮点数，这题会卡。
因此要自定义比较器：`key=cmp_to_key(comp)`.
实现时return 小值-大值。
具体参考代码
"""


#       ms
def solve():
    n, = RI()
    a = []
    for i in range(1, n + 1):
        x, y = RI()
        a.append((x, y, i))

    def comp(t1, t2):
        if t1[0] * (t2[0] + t2[1]) == t2[0] * (t1[0] + t1[1]):
            return t1[2] - t2[2]
        return -t1[0] * (t2[0] + t2[1]) + t2[0] * (t1[0] + t1[1])

    a.sort(key=cmp_to_key(comp))
    print(*[y for _, _, y in a])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
