# Problem: C. Vasya and Multisets
# Contest: Codeforces - Educational Codeforces Round 51 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1051/C
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
PROBLEM = """https://codeforces.com/problemset/problem/1051/C

输入 n(2≤n≤100) 和长为 n 的数组 s(1≤s[i]≤100)。
把 s 分成两个子序列 A 和 B（子序列可以为空），使得 A 里面只出现一次的数的个数，等于 B 里面只出现一次的数的个数。
如果无法做到，输出 NO。
否则输出 YES 以及方案（见样例）。
注意 s 中可能有重复元素。

思考题：如果分成 k 个子序列要怎么做？
输入
4
3 5 7 1
输出
YES
BABA

输入
3
3 5 1
输出
NO
"""
"""计数1的个数有c个，如果c是偶数就平分，其它的数都放B里，完事；
如果c是奇数，选c//2个放A，其余c//2+1放B。然后选一个出现次数>=3的数放A即可。
"""


#       ms
def sikaoti():
    n, k = RI()
    a = RILST()

    cnt = Counter(a)
    f = [0] * k  # f[i][j]为用前i个数，是否能分出j组比其他组多1
    f[0] = 1
    for x, v in cnt.items():
        g = [0] * k
        for i, p in enumerate(f):
            if p:
                g[(i + v) % k] = 1
                if v > 1:
                    g[i] = 1
                if v > 2:
                    for j in range(k - 1):
                        g[(i + j) % k] = 1
        f = g

    print(['NO', 'YES'][f[0]])


#    93   ms00015
def solve():
    n, = RI()
    a = RILST()

    cnt = [0] * 101
    for v in a:
        cnt[v] += 1
    one = cnt.count(1)
    ans = ['B'] * n
    if one:
        p = one // 2
        for i, v in enumerate(a):
            if cnt[v] == 1 and p:  # 把one//2个数分到A
                ans[i] = 'A'
                p -= 1
    if one % 2 == 0:  # 平分了，直接返回
        print('YES')
        return print(*ans, sep='')
    for i, v in enumerate(a):  # 否则补一个数进A
        if cnt[v] >= 3:
            ans[i] = 'A'
            print('YES')
            return print(*ans, sep='')

    print('NO')


#    124   ms
def solve1():
    n, = RI()
    a = RILST()
    one = three = 0
    cnt = [0] * 101
    for v in a:
        cnt[v] += 1
    for k, v in enumerate(cnt):
        if v == 1:
            one += 1
        elif v >= 3:
            three = 1
    if one % 2 == 0 or three:
        print('YES')
        ans = ['B'] * n
        p = 1
        for i, v in enumerate(a):
            if cnt[v] == 1 and p * 2 <= one:  # 把one//2个数分到A
                ans[i] = 'A'
                p += 1
        if one % 2 == 0:  # 平分了，直接返回
            return print(*ans, sep='')
        for i, v in enumerate(a):  # 否则补一个数进A
            if cnt[v] >= 3:
                ans[i] = 'A'
                return print(*ans, sep='')
    else:
        print('NO')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
