# Problem: F - Erase Subarrays
# Contest: AtCoder - AtCoder Beginner Contest 275
# URL: https://atcoder.jp/contests/abc275/tasks/abc275_f
# Memory Limit: 1024 MB
# Time Limit: 2000 ms
#
# Powered by CP Editor (https://cpeditor.org)

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc275/tasks/abc275_f

输入 n(≤3000) m(≤3000) 和长为 n 的数组 a (1≤a[i]≤3000)。
每次操作你可以删除 a 的一个非空连续子数组。
定义 f(x) 表示使 sum(a) = x 的最小操作次数。
输出 f(1), f(2), ..., f(m)。
输入
4 5
1 2 3 4
输出
1
2
1
1
1

输入
1 5
3
输出
-1
-1
0
-1
-1
"""


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


if __name__ == '__main__':
    n, m = RI()
    a = RILST()
    """
    定义:f[i][j][0/1]为前i个数，和为j，第i个数[删除/保留]的状态下，最小操作次数
    答案:ans[j] = 所有j对应的值
    转移:
        f[i][j][0] = min(f[i-1][j][0],f[i-1][j-a[i]][1]+1)
        f[i][j][1] = min(f[i-1][j-a[i]] ) if j>=a[i] else inf
    初始：
        f[0][0] = [0,inf]   # 没有数不删自然是0
        f[i>0][0] = [1,inf]  # 要获得0只需要全删1次，只要保留1个就不可能0        
        其他inf
    实现时，仿照01背包空间压缩，倒序处理    
    """
    inf = 30001
    # 370 ms
    f1 = [0] + [inf] * m
    f0 = [inf] * (m + 1)
    for x in a:
        for j in range(m, -1, -1):
            f0[j], f1[j] = min(f0[j], f1[j] + 1), min(f0[j - x], f1[j - x]) if j >= x else inf
        # f0[0] = 1

    # print(f)
    ans = [min(x) for x in zip(f0, f1)][1:]
    print('\n'.join(map(lambda x: str(x) if x < inf else '-1', ans)))

    # 691 ms
    # f = [[inf, inf] for _ in range(m + 1)]
    # f[0][0] = 0
    # for x in a:
    #     for j in range(m, 0, -1):
    #         f[j] = [min(f[j][0], f[j][1] + 1), min(f[j - x]) if j >= x else inf]
    #     f[0][0] = 1
    #
    # # print(f)
    # ans = [min(x) for x in f[1:]]
    # print('\n'.join(map(lambda x: str(x) if x < inf else '-1', ans)))
