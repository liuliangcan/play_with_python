# Problem: E. Split Into Two Sets
# Contest: Codeforces - Codeforces Round 805 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1702/E
# Memory Limit: 256 MB
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
PROBLEM = """https://codeforces.com/problemset/problem/1702/E

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(2≤n≤2e5) 表示 n 块骨牌，每块骨牌上写有两个数。
然后输入 n 行，每行 2 个数，表示骨牌上的数字，范围 [1,n]。

你需要把这 n 块骨牌分成两组，使得每组内都不含重复数字。
能否做到？输出 YES 或 NO。

例如有 4 块骨牌：(1,4), (1,3), (3,2), (4,2)。
可以分成如下两组：
第一组：(1,4), (3,2)。
第二组：(1,3), (4,2)。
输入
6
4
1 2
4 3
2 1
3 4
6
1 2
4 5
1 3
4 6
2 3
5 6
2
1 1
2 2
2
1 2
2 1
8
2 1
1 2
4 3
4 3
5 6
5 7
8 6
7 8
8
1 2
2 1
4 3
5 3
5 4
6 7
8 6
7 8
输出
YES
NO
NO
YES
YES
NO
"""


def iii():  # 牛客输入格式有bug
    num = 0
    neg = False
    while True:
        c = sys.stdin.read(1)
        if c == '-':
            neg = True
            continue
        elif c < '0' or c > '9':
            continue
        while True:
            num = 10 * num + ord(c) - ord('0')
            c = sys.stdin.read(1)
            if c < '0' or c > '9':
                break
        return -num if neg else num


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
    cnt = [0] * n
    g = [[] for _ in range(n)]

    for _ in range(n):
        u, v = RI()
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
        cnt[u] += 1
        cnt[v] += 1
    if max(cnt) >= 3:
        return print('NO')
    color = [-1] * n
    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            q = deque([start])
            while q:
                u = q.popleft()
                c = color[u]
                for v in g[u]:
                    if color[v] == c:
                        return print('NO')
                    elif color[v] == -1:
                        color[v] = c ^ 1
                        q.append(v)
    print('YES')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
