# Problem: G - Minimum Permutation
# Contest: AtCoder - Tokio Marine & Nichido Fire Insurance Programming Contest 2023（AtCoder Beginner Contest 299)
# URL: https://atcoder.jp/contests/abc299/tasks/abc299_g
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
PROBLEM = """https://atcoder.jp/contests/abc299/tasks/abc299_g

输入 n m(1≤m≤n≤2e5) 和长为 n 的数组 a(1≤a[i]≤m)，保证 [1,m] 内的所有整数都在 a 中。
输出 a 的一个长为 m 的子序列，要求它是一个 1~m 的排列，且字典序最小。
输入
4 3
2 3 1 3
输出
2 1 3

输入
4 4
2 3 1 4
输出
2 3 1 4

输入
20 10
6 3 8 5 8 10 9 3 6 1 8 3 3 7 4 7 2 7 8 5
输出
3 5 8 10 9 6 1 4 2 7
"""
"""这题和 316. 去除重复字母 是一样的
！"""
"""用栈模拟，如果栈顶大于当前字符，应该移除栈顶；除非这个栈顶后续没有了"""


#       ms
def solve():
    n, m = RI()
    a = RILST()
    ans = []
    vis = set()
    cnt = Counter(a)
    for v in a:
        if v not in vis:
            while ans and ans[-1] > v and cnt[ans[-1]]:
                vis.remove(ans.pop())
            ans.append(v)
            vis.add(v)
        cnt[v] -= 1
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
