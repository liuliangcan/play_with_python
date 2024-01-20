# Problem: D - Concatenate Subsequences
# Contest: AtCoder - AtCoder Regular Contest 134
# URL: https://atcoder.jp/contests/arc134/tasks/arc134_d
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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/arc134/tasks/arc134_d

输入 n(1≤n≤1e5) 和长为 2n 的数组 A(1≤a[i]≤1e9)。
你需要从 A 的前 n 个数中删除一些数，删除 A[i] 会把 A[i+n] 也一并删除。
你不能把整个数组都删掉。
设删除后的数组为 A'。
输出字典序最小的 A'。
输入
3
2 1 3 1 2 2
输出 1 2

输入
10
38 38 80 62 62 67 38 78 74 52 53 77 59 83 74 63 80 61 68 55
输出 38 38 38 52 53 77 80 55

输入
12
52 73 49 63 55 74 35 68 22 22 74 50 71 60 52 62 65 54 70 59 65 54 60 52
输出 22 22 50 65 54 52
"""

"""
左半部分一定要保留最小的那个数，假设是mnl.
右边对应mnl的数设为mnr. 
若mnr <= mnl，则 return [mnl,mnr]即可，一定不会有更小的字典序了。
若mnr > mnl, 左边一定要取完所有mnl，且mnl之后，可能还有较小的数，只要它< right0，则应当保留
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    mn = min(a[:n])

    pos = defaultdict(list)

    for i in range(n):
        pos[a[i]].append(i)
    right_min = min(a[i + n] for i in pos[mn])
    if right_min <= mn:
        return print(mn, right_min)
    right0 = a[pos[mn][0] + n]
    rmn = [0] * n
    rmn[-1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        rmn[i] = min(rmn[i + 1], a[i])
    ans = [] + pos[mn]

    while pos[mn][-1]+1 < n:
        i0 = pos[mn][-1] + 1
        mn = rmn[i0]
        if mn < right0:
            for v in pos[mn]:
                if v >= i0:
                    ans.append(v)
        elif mn > right0:
            break
        else:
            right1 = right0
            for i in ans:
                v = a[i + n]
                if v != right0:
                    right1 = v
                    break
            if right1 > right0:
                for v in pos[mn]:
                    if v >= i0:
                        ans.append(v)
            break
    ans = ans + [i + n for i in ans]
    print(*[a[i] for i in ans])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
