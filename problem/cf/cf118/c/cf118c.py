# Problem: C. Fancy Number
# Contest: Codeforces - Codeforces Beta Round 89 (Div. 2)
# URL: https://codeforces.com/problemset/problem/118/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/118/C

输入 n k(2≤k≤n≤1e4) 和长为 n 的字符串 s，仅包含 '0'~'9'。

每次操作你可以把一个 s[i] 修改成任意 '0'~'9'，假设修改成 b，则花费为 abs(s[i]-b)。
要使 s 中至少有 k 个相同字符，求最小总花费。
同时，你需要在总花费最小的前提下，让修改后的 s 的字典序尽量小。
输出最小总花费以及修改后的 s。

思考：如果把 s 换成一个值域范围更大的整数数组，你能想出一个更优的做法吗？
输入
6 5
898196
输出
4
888188

输入
3 2
533
输出
0
533

输入
10 6
0001112223
输出
3
0000002223
"""
"""https://codeforces.com/contest/118/submission/197621784

枚举+贪心。

枚举修改后有 k 个 0/1/2/.../9。取花费最小且字典序最小的为答案。

比如修改成 4，那么从近到远依次考虑，修改 53627189 成 4。（注意先改 5 再改 3）
为了让字典序尽量小：
比 4 大的数字，从左到右修改。
比 4 小的数字，从右到左修改。"""


def my_bisect_left(a, x, lo=None, hi=None, key=None):
    """
    由于3.10才能用key参数，因此自己实现一个。
    :param a: 需要二分的数据
    :param x: 查找的值
    :param lo: 左边界
    :param hi: 右边界(闭区间)
    :param key: 数组a中的值会依次执行key方法，
    :return: 第一个大于等于x的下标位置
    """
    if not lo:
        lo = 0
    if not hi:
        hi = len(a) - 1
    else:
        hi = min(hi, len(a) - 1)
    size = hi - lo + 1

    if not key:
        key = lambda _x: _x
    while size:
        half = size >> 1
        mid = lo + half
        if key(a[mid]) < x:
            lo = mid + 1
            size = size - half - 1
        else:
            size = half
    return lo


#  二分预处理   218  ms
def solve1():
    n, k = RI()
    s, = RS()
    s = list(map(int, s))
    cnt = Counter(s)
    mx = max(cnt.values())
    if mx >= k:
        return print(f"0\n{''.join(map(str, s))}")
    poses = [[] for _ in range(10)]
    for i, v in enumerate(s):
        poses[v].append(i)

    # 花x是否能搞出k个相同
    def calc(x):
        def f(i):
            cost = 0
            remain = k - cnt[i]
            for j in range(1, 10):
                if remain <= 0: break
                for p in i - j, i + j:
                    if 0 <= p <= 9:
                        c = min(cnt[p], remain)
                        cost += c * j
                        if cost > x: break
                        remain -= c
            return cost

        return any(f(i) <= x for i in range(10))

    mn = my_bisect_left(range(n * 10), True, key=calc)
    # DEBUG(mn)
    print(mn)

    def find(i):
        t = s[:]
        cost = 0
        remain = k - cnt[i]
        for j in range(1, 10):
            if remain <= 0:
                return ''.join(map(str, t))

            p = i + j
            if 0 <= p <= 9:
                ps = poses[p]
                c = min(cnt[p], remain)
                cost += c * j
                for x in range(c):
                    t[ps[x]] = i
                if cost > mn: break
                remain -= c
            p = i - j
            if 0 <= p <= 9:
                ps = poses[p][::-1]
                c = min(cnt[p], remain)
                cost += c * j
                for x in range(c):
                    t[ps[x]] = i
                if cost > mn: break
                remain -= c
        if remain <= 0:
            return ''.join(map(str, t))
        return 's'

    print(min(find(i) for i in range(10)))


#   直接贪心枚举 248    ms
def solve2():
    n, k = RI()
    s, = RS()
    s = list(map(int, s))
    cnt = Counter(s)
    mx = max(cnt.values())
    if mx >= k:
        return print(f"0\n{''.join(map(str, s))}")
    poses = [[] for _ in range(10)]
    for i, v in enumerate(s):
        poses[v].append(i)

    mn = inf
    ans = []
    for i in range(10):  # 尝试把别的数变成i
        t = s[:]  # 复制一份处理
        cost = 0
        remain = k - cnt[i]  # 需要变的数量
        for j in range(1, 10):  # 依次尝试距离i为j的数
            if remain <= 0: break
            p = i + j  # 贪心，如果要把别的数变成i，则优先把大于i的数变过来，才能是字典序小
            if 0 <= p <= 9:
                ps = poses[p]  # p的所有位置，贪心，先变下标小的
                c = min(cnt[p], remain)  # 能变c个数
                cost += c * j
                for x in ps[:c]:  # 比i大的这个p，从左往右变c个
                    t[x] = i
                if cost > mn: break
                remain -= c  # 变c个i

            p = i - j  # 贪心，处理完大的再处理小的
            if 0 <= p <= 9:
                ps = poses[p][::-1]  # p的所有位置，由于p<i，因此优先变下标大的才能使字典序小
                c = min(cnt[p], remain)
                cost += c * j
                for x in ps[:c]:
                    t[x] = i
                if cost > mn: break
                remain -= c
        if remain == 0:
            if cost < mn:
                mn = cost
                ans = t
            elif cost == mn:
                ans = min(ans, t)
    print(mn)
    print(*ans, sep='')


#   直接贪心枚举 248    ms
def solve():
    n, k = RI()
    s, = RS()
    s = list(map(int, s))
    cnt = [0] * 10
    poses = [[] for _ in range(10)]
    for i, v in enumerate(s):
        cnt[v] += 1
        poses[v].append(i)

    if max(cnt) >= k:
        return print(f"0\n{''.join(map(str, s))}")
    mn = inf  # 最小花费
    ans = []
    for i in range(10):  # 尝试把别的数变成i
        t = s[:]  # 复制一份处理
        cost = 0
        remain = k - cnt[i]  # 需要变的数量
        for j in range(1, 10):  # 依次尝试距离i为j的数
            if remain <= 0: break
            for d in 1, -1:  # 贪心，如果要把别的数变成i，则优先把大于i的数变过来，才能是字典序小；从大的变，优先变下标小的、从小的变，优先变下标大的。
                p = i + j * d
                if 0 <= p <= 9:
                    ps = poses[p][::d]  # p的所有位置，贪心，比i大的数优先变下标小的；比i小的数优先变下标大的
                    c = min(cnt[p], remain)  # 能变c个数
                    cost += c * j
                    for x in ps[:c]:  # 比i大的这个p，从左往右变c个
                        t[x] = i
                    if cost > mn: break
                    remain -= c  # 变c个i

        if remain == 0:
            if cost < mn:
                mn = cost
                ans = t
            elif cost == mn:
                ans = min(ans, t)
    print(mn)
    print(*ans, sep='')


if __name__ == '__main__':
    solve()
