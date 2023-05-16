# Problem: C. Even Number Addicts
# Contest: Codeforces - Codeforces Global Round 22
# URL: https://codeforces.com/problemset/problem/1738/C
# Memory Limit: 512 MB
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
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1738/C

输入 T(≤100) 表示 T 组数据。
每组数据输入 n(1≤n≤100) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)。

Alice 和 Bob 轮流从 a 中取数，Alice 先。
游戏直到 a 为空时停止。
如果 Alice 所取数字之和为偶数，输出 Alice，否则输出 Bob。
输入
4
3
1 3 5
4
1 3 5 7
4
1 2 3 4
4
10 20 30 40
输出
Alice
Alice
Bob
Alice
"""
"""https://codeforces.com/contest/1738/submission/205538013

提示：用记忆化搜索模拟。

f(leftEven, leftOdd, sum, who) 表示剩余偶数个数，剩余奇数个数，Alice 所选数字之和，当前玩家是 Alice 还是 Bob。"""


@lru_cache(None)
def dfs(odd, even, u, alice):  # 剩多少奇数、剩多少偶数、alice现在手里的奇偶性、现在是不是alice的回合
    if not odd:  # 没有奇数了，现在多少就是多少
        return u % 2 == 0
    if alice:
        if not even:  # 没有偶数了，看还能拿多少个奇数
            p = (odd + 1) // 2
            return (u + p) % 2 == 0
        return dfs(odd - 1, even, u ^ 1, False) or dfs(odd, even - 1, u, False)  # alice选，只要有一个方案必胜，alice就选这个
    else:
        if not even:
            p = odd // 2
            return (u + p) % 2 == 0
        return dfs(odd - 1, even, u, True) and dfs(odd, even - 1, u, True)  # bob选，必须两个方案都让alice赢，否则bob选让alice输的那个方案


# for i in range(20):
#     for j in range(20):
#         print(int(dfs(i, j, 0, True)), end=' ')
#     print()
"""
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
"""

#     171  ms
def solve1():
    n, = RI()
    a = RILST()
    odd = even = 0
    for v in a:
        if v & 1:
            odd += 1
        else:
            even += 1
    print('Alice' if dfs(odd, even, 0, True) else 'Bob')


def dabiao(odd, even):
    p = odd % 4
    if p == 0 or p == 3:
        return 1
    if p == 2:
        return 0
    return even & 1


#    93   ms
def solve():
    n, = RI()
    a = RILST()
    odd = even = 0
    for v in a:
        if v & 1:
            odd += 1
        else:
            even += 1

    print('Alice' if dabiao(odd, even) else 'Bob')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
