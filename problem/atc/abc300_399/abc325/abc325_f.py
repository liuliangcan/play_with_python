# Problem: F - Sensor Optimization Dilemma
# Contest: AtCoder - KEYENCE Programming Contest 2023 Autumn（AtCoder Beginner Contest 325）
# URL: https://atcoder.jp/contests/abc325/tasks/abc325_f
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
    a = RILST()
    l1, c1, k1 = RI()
    l2, c2, k2 = RI()# Problem: F - Sensor Optimization Dilemma
# Contest: AtCoder - KEYENCE Programming Contest 2023 Autumn（AtCoder Beginner Contest 325）
# URL: https://atcoder.jp/contests/abc325/tasks/abc325_f
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
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    l1, c1, k1 = RI()
    l2, c2, k2 = RI()
    '''#f[i][j]:前i段需求，选了j个l1时，最少要用几个l2
    由于费用都是正的，所以其实就是最小化i和j。
    '''

    f = [0] * (k1 + 1)
    for v in a:
        g = [inf] * (k1 + 1)
        for i, f1 in enumerate(f):
            if f1 == inf:
                continue
            left1 = k1 - i
            left2 = k2 - f1
            # print(left1,left2,i,f1)
            if left1 < 0 or left2 < 0:
                continue
            for x in range(left1 + 1):
                y = (v - x * l1 + l2 - 1) // l2
                if y < 0:
                    break
                if 0 <= y <= left2:
                    g[i + x] = min(g[i + x], f1 + y)
            for y in range(left2 + 1):
                x = (v - y * l2 + l1 - 1) // l1
                if x < 0:
                    break
                if 0 <= x <= left1:
                    g[i + x] = min(g[i + x], f1 + y)
        f = g
    ans = min(i * c1 + v * c2 for i, v in enumerate(f))
    if ans < inf:
        print(ans)
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

    '''#f[i][j]:前i段需求，选了j个l1时，最少要用几个l2
    f[j]
    '''

    f = [0] * (k1 + 1)
    for v in a:
        g = [inf] * (k1 + 1)
        for i, f1 in enumerate(f):
            left1 = k1 - i
            left2 = k2 - f1
            # print(left1,left2,i,f1)
            if left1 < 0 or left2 < 0:
                continue
            for x in range(left1 + 1):
                y = (v - x * l1 + l2 - 1) // l2
                # print(x,y)
                if 0 <= y <= left2:
                    g[i + x] = min(g[i + x], f1 + y)
                    # print(i+x,g[i+x])
            for y in range(left2 + 1):
                x = (v - y * l2 + l1 - 1) // l1
                if 0 <= x <= left1:
                    g[i + x] = min(g[i + x], f1 + y)
        f = g
        # print(f)
    ans = min(i * c1 + v * c2 for i, v in enumerate(f))
    if ans < inf:
        print(ans)
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
