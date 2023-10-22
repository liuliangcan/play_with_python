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
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://www.lanqiao.cn/problems/5132/learning/?contest_id=144
由于只能转动s，去匹配t，可以把s翻倍，然后查找t有没有，没有就No
否则kmp查找位置，看看最左和最右的位置哪个更近
"""


def f(s):
    ans = []
    for c in s:
        if c.isupper():
            ans.append(c.lower())
        else:
            ans.append(c.upper())
    return ''.join(ans)


class Kmp:
    """kmp算法，计算前缀函数pi,根据pi转移，复杂度O(m+n)"""

    def __init__(self, t):
        """传入模式串，计算前缀函数"""
        self.t = t
        n = len(t)
        self.pi = pi = [0] * n
        j = 0
        for i in range(1, n):
            while j and t[i] != t[j]:
                j = pi[j - 1]  # 失配后缩短期望匹配长度
            j += t[i] == t[j]  # 多配一个
            pi[i] = j

    def find_all_yield(self, s):
        """查找t在s中的所有位置，注意可能为空"""
        n, t, pi, j = len(self.t), self.t, self.pi, 0
        for i, v in enumerate(s):
            while j and v != t[j]:
                j = pi[j - 1]
            j += v == t[j]
            if j == n:
                yield i - j + 1
                j = pi[j - 1]

    def find_one(self, s):
        """查找t在s中的第一个位置，如果不存在就返回-1"""
        for ans in self.find_all_yield(s):
            return ans
        return -1


#       ms
def solve():
    n, = RI()
    s, = RS()
    t, = RS()

    kmp = Kmp(t)
    if -1 == kmp.find_one(f(s+s)):
        return print('No')
    print('Yes')
    pos = list(kmp.find_all_yield(f(s + s)))
    print(min(pos[0], n - pos[-1]))

#       ms
# def solve():
#     n, = RI()
#     s, = RS()
#     t, = RS()
#     if f(s) not in t + t:
#         return print('No')
#     print('Yes')
#     print(t[::-1])
#     print((s+s)[::-1])
#     print(Kmp(t[::-1]).find_one((s+s)[::-1]))
#     print(min(Kmp(t).find_one(f(s+s)), Kmp(t[::-1]).find_one((s+s)[::-1])))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
