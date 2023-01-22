import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
# ACW没有comb
# from math import sqrt, gcd, inf, comb
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc214/tasks/abc214_e

输入 t(≤2e5) 表示 t 组数据，每组数据输入 n(≤2e5) 和 n 个区间 [L,R]，范围在 [1,1e9]。
所有数据的 n 之和不超过 2e5。

你有 n 个球，第 i 个球需要放在区间 [L,R] 内的整数位置上。
但每个整数位置上至多能放一个球。
如果可以做到，输出 Yes，否则输出 No
输入
2
3
1 2
2 3
3 3
5
1 2
2 3
3 3
1 3
999999999 1000000000
输出
Yes
No
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


#       ms
def solve():
    n, = RI()
    a = RILST()


if __name__ == '__main__':
    # t, = RI()
    # for _ in range(t):
    #     solve()
    solve()
