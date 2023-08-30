# Problem: D -  Three Days Ago
# Contest: AtCoder - AtCoder Beginner Contest 295
# URL: https://atcoder.jp/contests/abc295/tasks/abc295_d
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
PROBLEM = """https://atcoder.jp/contests/abc295/tasks/abc295_d

输入长度 ≤5e5 的字符串 s，只包含数字字符。
定义 f(t)：如果字符串 t 中的每个字符都出现偶数次，则 f(t)=1，否则 f(t)=0。
枚举 s 的所有非空连续子串 t，输出 f(t) 之和。
输入 20230322
输出 4

输入 0112223333444445555556666666777777778888888889999999999
输出 185

输入 3141592653589793238462643383279502884197169399375105820974944
输出 9
"""


#     178  ms
def solve():
    s, = RS()
    ans = p = 0
    cnt = [0] * (1 << 10)
    cnt[0] = 1
    for c in s:
        p ^= 1 << int(c)
        ans += cnt[p]
        cnt[p] += 1
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
