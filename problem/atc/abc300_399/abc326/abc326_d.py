# Problem: D - ABC Puzzle
# Contest: AtCoder - Panasonic Programming Contest 2023（AtCoder Beginner Contest 326）
# URL: https://atcoder.jp/contests/abc326/tasks/abc326_d
# Memory Limit: 1024 MB
# Time Limit: 4000 ms

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
PROBLEM = """
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


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
    r, = RS()
    c, = RS()
    c = [ord(v) - ord('A') + 1 for v in c]  # 都变成数字
    r = [ord(v) - ord('A') + 1 for v in r]
    g = [[0] * n for _ in range(n)]  # 存答案
    row = [0] * n  # 状压，看看这行是不是123各一个
    col = [0] * n
    rf = [0] * n  # 首
    cf = [0] * n

    def dfs(pos):  # pos = i*n+j
        if pos == n * n:
            return sum(row) == 14 * n == sum(col)  # 每行每列都是abc各一个

        i, j = divmod(pos, n)

        for v in (1, 2, 3):  # 尝试在这个格子放123
            if row[i] >> v & 1: continue  # 这行有了
            if col[j] >> v & 1: continue
            if not rf[i] and v != r[i]: continue  # 这行开头没有，那么v必须是r[i]
            if not cf[j] and v != c[j]: continue

            g[i][j] = v  # 放
            row[i] |= 1 << v
            col[j] |= 1 << v
            if not rf[i]: rf[i] = v
            if not cf[j]: cf[j] = v
            if dfs(pos + 1):
                return True
            g[i][j] = 0  # 回溯
            row[i] ^= 1 << v
            col[j] ^= 1 << v
            if rf[i] == v: rf[i] = 0
            if cf[j] == v: cf[j] = 0

        return dfs(pos + 1)  # 尝试放0

    if not dfs(0):
        return print('No')
    print('Yes')
    d = '.ABC'
    for r in g:
        print(''.join([d[v] for v in r]))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()