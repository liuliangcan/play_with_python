# Problem: G. Rudolf and CodeVid-23
# Contest: Codeforces - Codeforces Round 883 (Div. 3)
# URL: https://codeforces.com/contest/1846/problem/G
# Memory Limit: 256 MB
# Time Limit: 1000 ms

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

if sys.version >= '3.8':  # ACW没有comb
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
PROBLEM = """一种名为“CodeVid-23”的新病毒已在程序员中传播开来。 鲁道夫作为一个程序员，无法避免感染。

感染时可能出现从1到n的n个症状。最初，鲁道夫有其中的一些症状。他去了药店买了m种药物。

对于每种药物，都知道需要服用的天数和它所能缓解的症状。不幸的是，药物通常会有副作用。因此，对于每种药物，也知道服用时出现的症状。

阅读说明后，鲁道夫意识到同时服用多种药物对健康非常不利。

鲁道夫希望尽快康复。因此，他请你计算去除所有症状所需的最少天数，或者判断是否不可能。

输入
第一行包含一个整数t（1≤t≤100）— 测试用例的数量。

然后是测试用例的描述。

每个测试用例的第一行包含两个整数n和m（1≤n≤10,1≤m≤103）— 分别是症状和药物的数量。

每个测试用例的第二行包含一个长度为n的字符串，由字符0和1组成— 鲁道夫的症状描述。如果字符串的第i个字符为1，表示鲁道夫有第i个症状，否则没有。

然后是3m行 — 药物的描述。

每个药物描述的第一行包含一个整数d（1≤d≤103）— 药物需要服用的天数。

药物描述的后两行包含两个长度为n的字符串，由字符0和1组成—分别是药物所能缓解的症状和药物的副作用的描述。

在两行中的第一行，字符1在第i个位置表示药物能够缓解第i个症状，否则为0。

在两行中的第二行，字符1在第i个位置表示服用药物后第i个症状出现，否则为0。

不同的药物可以有相同的症状和副作用。如果一种药物缓解某种症状，那么该症状将不会出现在副作用中。

所有测试用例中m的总和不超过103。

输出
对于每个测试用例，在单独的一行上输出一个整数 — 鲁道夫去除所有症状所需的最少天数。如果这永远不会发生，则输出-1。
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
    n, m = RI()
    s, = RS()
    s = int(s, 2)
    fuck = [[] for _ in range(n)]
    for _ in range(m):
        d, = RI()
        f, = RS()
        ff, = RS()
        f = int(f, 2)
        ff = int(ff, 2)
        med = (d, f, ff)
        for i in range(n):
            if f >> i & 1:
                fuck[i].append(med)

    dis = [inf] * (1 << n)
    mask = (1 << n) - 1
    dis[s] = 0
    q = [(0, s)]
    while q:
        d, u = heappop(q)
        if u == 0:
            return print(d)
        if d > dis[u]: continue
        for i in range(n):  # 找每一位对应的药
            if u >> i & 1:
                for day, f, ff in fuck[i]:
                    c = d + day
                    v = u & (mask ^ f) | ff  # 吃完药去掉f增加ff
                    if c < dis[v]:
                        dis[v] = c
                        heappush(q, (c, v))
    print(-1)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
