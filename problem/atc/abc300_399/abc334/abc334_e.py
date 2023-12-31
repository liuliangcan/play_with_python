# Problem: E - Christmas Color Grid 1
# Contest: AtCoder - UNIQUE VISION Programming Contest 2023 Christmas (AtCoder Beginner Contest 334)
# URL: https://atcoder.jp/contests/abc334/tasks/abc334_e
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
# MOD = 10**9 + 7
MOD = 998244353
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


class DSU:
    """基于数组的并查集"""

    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.set_count = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            self.edge_size[y] += 1
            return False
        # if self.size[x] > self.size[y]:  # 注意如果要定向合并x->y，需要干掉这个；实际上上边改成find_fa后，按轶合并没必要了，所以可以常关
        #     x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.set_count -= 1
        return True


#       ms
def solve():
    h, w = RI()
    g = []
    for _ in range(h):
        s, = RS()
        g.append(s)
    dsu = DSU(h * w)
    for i, row in enumerate(g):
        for j, c in enumerate(row):
            if c == '#':
                if i and g[i - 1][j] == '#':
                    dsu.union(i * w + j, (i - 1) * w + j)
                if j and row[j - 1] == '#':
                    dsu.union(i * w + j, i * w + j - 1)
    fs = set()

    for i, row in enumerate(g):
        for j, c in enumerate(row):
            if c == '#':
                fs.add(dsu.find_fa(i*w+j))
    cnt = len(fs)
    fenzi = fenmu = 0
    for i, row in enumerate(g):
        for j, c in enumerate(row):
            if c == '.':
                fenmu += 1
                nb = set()
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < h and 0 <= y < w and g[x][y] == '#':
                        nb.add(dsu.find_fa(x * w + y))

                fenzi += cnt - len(nb) + 1
    # print(cnt,fenzi,fenmu)
    print(fenzi * pow(fenmu, MOD - 2, MOD) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
