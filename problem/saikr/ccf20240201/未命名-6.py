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


class PreSum2d:
    # 二维前缀和(支持加法和异或)，只能离线使用，用n*m时间预处理，用O1查询子矩阵的和；op=0是加法，op=1是异或
    def __init__(self, g, op=0):
        m, n = len(g), len(g[0])
        self.op = op
        self.p = p = [[0] * (n + 1) for _ in range(m + 1)]
        if op == 0:
            for i in range(m):
                for j in range(n):
                    p[i + 1][j + 1] = p[i][j + 1] + p[i + 1][j] - p[i][j] + g[i][j]
        elif op == 1:
            for i in range(m):
                for j in range(n):
                    p[i + 1][j + 1] = p[i][j + 1] ^ p[i + 1][j] ^ p[i][j] ^ g[i][j]

    # O(1)时间查询闭区间左上(a,b),右下(c,d)矩形部分的数字和。
    def sum_square(self, a, b, c, d):
        if self.op == 0:
            return self.p[c + 1][d + 1] + self.p[a][b] - self.p[a][d + 1] - self.p[c + 1][b]
        elif self.op == 1:
            return self.p[c + 1][d + 1] ^ self.p[a][b] ^ self.p[a][d + 1] ^ self.p[c + 1][b]


#       ms
def solve():
    m, n = RI()
    sx, sy, fx, fy = RI()
    sx -= 1
    sy -= 1
    fx -= 1
    fy -= 1
    g = []
    for _ in range(m):
        a, = RS()
        g.append([int(c == '#') for c in a])
    ps = PreSum2d(g)

    def manh(x, y, a, b):
        return abs(x - a) + abs(b - y)

    q = [(manh(sx, sy, fx, fy), sx, sy, 1)]
    vis = {(sx, sy - 1, 1): 0}
    while q:
        _, x, y, size = heappop(q)
        step = vis[(x, y, size)]
        if size == 1 and x == fx and y == fy:
            return print(step)
        for a, b in (x + size, y), (x - size, y), (x, y + size), (x, y - size):
            nxt = (a, b, size)
            if 0 <= a < m - size + 1 and 0 <= b < n - size + 1 \
                    and ps.sum_square(a, b, a + size - 1, b + size - 1) == 0 and nxt not in vis:
                vis[nxt] = step + 1
                heappush(q, (step + 1 + manh(a, b, fx, fy) + abs(size - 1), a, b, size))
        if size < 20:
            p = size + 1
            nxt = (x, y, p)
            if x + p - 1 < m and y + p - 1 < n and ps.sum_square(x, y, x + p - 1,
                                                                 y + p - 1) == 0 and nxt not in vis:
                vis[nxt] = step + 1
                heappush(q, (step + 1 + manh(x, y, fx, fy) + abs(size - 1), x, y, p))
        if size > 1:
            p = size - 1
            nxt = (x, y, p)
            if x + p - 1 < m and y + p - 1 < n and nxt not in vis:
                vis[nxt] = step + 1
                heappush(q, (step + 1 + manh(x, y, fx, fy) + abs(size - 1), x, y, p))
    # step = 0
    # while q:
    #     nq = []
    #     for x, y, size in q:
    #         if size == 1 and x == fx and y == fy:
    #             return print(step)
    #         for a, b in (x + size, y), (x - size, y), (x, y + size), (x, y - size):
    #             nxt = (a, b, size)
    #             if 0 <= a < m - size + 1 and 0 <= b < n - size + 1 \
    #                     and ps.sum_square(a, b, a + size - 1, b + size - 1) == 0 and nxt not in vis:
    #                 vis.add(nxt)
    #                 nq.append(nxt)
    #         if size < 20:
    #             p = size + 1
    #             nxt = (x, y, p)
    #             if x + p - 1 < m and y + p - 1 < n and ps.sum_square(x, y, x + p - 1,
    #                                                                  y + p - 1) == 0 and nxt not in vis:
    #                 vis.add(nxt)
    #                 nq.append(nxt)
    #         if size > 1:
    #             p = size - 1
    #             nxt = (x, y, p)
    #             if x + p - 1 < m and y + p - 1 < n and nxt not in vis:
    #                 vis.add(nxt)
    #                 nq.append(nxt)
    #
    #     step += 1
    #     q = nq
    return print(-1)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
