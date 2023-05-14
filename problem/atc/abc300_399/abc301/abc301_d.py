# Problem: D - Bitmask
# Contest: AtCoder - パナソニックグループプログラミングコンテスト2023（AtCoder Beginner Contest 301）
# URL: https://atcoder.jp/contests/abc301/tasks/abc301_d
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
PROBLEM = """给一个只含'01?'的01字符串，你可以把'?'替换成0/1.
给一个数字n。问s能生成的最大数字x(x<=n)是多少。
"""
"""
- s长度超过n，且前边的位数有1是无法生成的，返回-1；否则可以都填0
- 后边对齐的位，前缀相同的情况下，出现n里0，s是1是非法的。否则一定可以生成。
类似数位dp的dfs即可，贪心的让每位优先取1再取0。
---
另外，可以直接贪：
先把所有1放到数字里，计算这些1是否已经>n，返回-1;
否则：
从高到低，对s里每个?，尝试放1，不行就放0.
"""



#       ms
def solve():
    s, = RS()
    n, = RI()
    p = bin(n)[2:]
    if len(s) < len(p):
        s = s.replace('?', '1')
        return print(int(s, 2))
    if len(s) >= len(p):
        d = len(s) - len(p)
        for i in range(d):
            if s[i] == '1':
                return print(-1)
        s = s[d:]

        for x, y in zip(s, p):
            if y == '1' and x in '?0':
                break
            if y == '0' and x == '1':
                return print(-1)

        ans = []

        def dfs(i, is_limit):
            if i == len(s):
                return True

            if s[i] != '?':
                if is_limit and s[i] > p[i]:
                    return False
                ans.append(s[i])
                if dfs(i + 1, is_limit and s[i] == p[i]):
                    return True
                ans.pop()
            else:
                if not is_limit or p[i] == '1':
                    ans.append('1')
                    if dfs(i + 1, is_limit and '1' == p[i]):
                        return True
                    ans.pop()
                ans.append('0')
                if dfs(i + 1, is_limit and '0' == p[i]):
                    return True
                ans.pop()
            return False

        if dfs(0, True):
            print(int(''.join(ans), 2))
        else:
            print(-1)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
