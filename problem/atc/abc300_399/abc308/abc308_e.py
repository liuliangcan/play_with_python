# Problem: E - MEX
# Contest: AtCoder - AtCoder Beginner Contest 308
# URL: https://atcoder.jp/contests/abc308/tasks/abc308_e
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
PROBLEM = """给出长为n的数列a，仅包含012
给出长为n的字符串s，仅包含'm''e''x'。
找到所有s中的mex三元组下标，对应的a中的三个数组成的集合，求mex，最后sum。
"""
"""由于三元组只含012因此一定求mex可以暴力最多操作4次。
mex一定从me转移而来才有效，me一定从m转移而来才有效。
而这些字母对应数字是有限的，可以用哈希表计数即可。
"""


def mex(s):
    for i in count(0):
        if i not in s:
            return i


#       ms
def solve():
    n, = RI()
    a = RILST()
    s, = RS()
    ans = 0
    m, me, x = Counter(), Counter(), Counter()
    i = 0
    for x, c in zip(a, s):
        if c == 'M':
            m[x] += 1
        elif c == 'E':
            for k, v in m.items():
                me[(k, x)] += v
        else:
            for k, v in me.items():
                s = set(k)
                s.add(x)

                ans += mex(s) * v
        i += 1
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
