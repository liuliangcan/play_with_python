# Problem: 游游的问号替换
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/66943/C
# Memory Limit: 524288 MB
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

# if not sys.version.startswith('3.5.3') or not sys.version.startswith('3.6.1'):  # ACW没有comb\牛客
#     from math import comb

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
PROBLEM = """
"""


# sys.setrecursionlimit(2014)


#       ms
def solve1():
    s, = RS()
    n = len(s)

    def dfs(i, ans=''):
        if i == n:
            print(ans)
            return True
        if s[i] != '?':
            if ans and ans[-1] == s[i]:
                return False
            if len(ans) > 1 and (int(ans[-2]) * 9 + int(ans[-1]) * 3 + int(s[i])) & 1:
                return False
            if dfs(i + 1, ans + s[i]):
                return True
        else:
            for j in range(3):
                c = str(j)
                if ans and ans[-1] == c:
                    continue
                if len(ans) > 1 and (int(ans[-2]) * 9 + int(ans[-1]) * 3 + int(c)) & 1:
                    continue
                if dfs(i + 1, ans + c):
                    return True
        return False

    if not dfs(0):
        print(-1)


def solve():
    s, = RS()
    n = len(s)
    ans = []

    def dfs(i):
        if i == n:
            return True
        if s[i] != '?':
            if ans and ans[-1] == s[i]:
                return False
            if len(ans) > 1 and (int(ans[-2]) * 9 + int(ans[-1]) * 3 + int(s[i])) & 1:
                return False
            ans.append(s[i])
            if dfs(i + 1):
                return True
            else:
                ans.pop()
        else:
            for j in range(3):
                c = str(j)
                if ans and ans[-1] == c:
                    continue
                if len(ans) > 1 and (int(ans[-2]) * 9 + int(ans[-1]) * 3 + int(c)) & 1:
                    continue
                ans.append(c)
                if dfs(i + 1):
                    return True
                else:
                    ans.pop()
        return False

    if dfs(0):
        print(''.join(ans))
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
