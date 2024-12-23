# Problem: C. Bitwise Balancing
# Contest: Codeforces - Codeforces Round 976 (Div. 2) and Divide By Zero 9.0
# URL: https://codeforces.com/problemset/problem/2020/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

from types import GeneratorType
import bisect
import io, os
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from contextlib import redirect_stdout
from itertools import accumulate, combinations, permutations
# combinations(a,k)a序列选k个 组合迭代器
# permutations(a,k)a序列选k个 排列迭代器
from array import *
from functools import lru_cache, reduce
from heapq import heapify, heappop, heappush
from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
from random import randint, choice, shuffle, randrange
# randint(a,b)从[a,b]范围随机选择一个数
# choice(seq)seq可以是一个列表,元组或字符串,从seq中随机选取一个元素
# shuffle(x)将一个可变的序列x中的元素打乱
from string import ascii_lowercase, ascii_uppercase, digits
# 小写字母，大写字母，十进制数字
from decimal import Decimal, getcontext

# Decimal(s) 实例化Decimal对象,一般使用字符串
# getcontext().prec=100 修改精度
# sys.setrecursionlimit(10**6) #调整栈空间
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/2020/C

输入 T(≤1e5) 表示 T 组数据。
每组数据输入三个整数 b c d，范围 [0,1e18]。

输出任意一个在 [0,2^61] 中的整数 a，满足 (a|b)−(a&c)=d。
若不存在这样的 a，输出 -1。
输入
3
2 2 2
4 2 6
10 2 14
输出
0
-1
12
"""
"""方法一

从集合的角度看，a|b 是 a 的超集，a&c 是 a 的子集。
所以 a|b 一定是 a&c 的超集。
所以不可能出现同一个比特位上，a|b 是 0 而 a&c 是 1 的情况。
这意味着减法是没有【借位】的，所以每一位互相独立，我们可以逐位分析。

逐位分析（从高到低或者从低到高都可以）：
如果 d 这一位是 1，那么必须是 1 - 0 = 1。
1. 如果 b 这一位是 0 且 c 这一位是 1，那么没有这样的 a，输出 -1。
2. 否则，如果 b 这一位是 0，那么 a 这一位必须是 1。（注意此时 c 这一位是 0）
如果 d 这一位是 0，那么可以是 1 - 1 = 0 或者 0 - 0 = 0。
1. 如果 b 这一位是 1 且 c 这一位是 0，那么没有这样的 a，输出 -1。
2. 否则，如果 b 这一位是 1（说明 c 这一位是 1），那么 a 这一位必须是 1。

代码一
代码一备份（洛谷）

方法二

根据上面的结论，当 b 和 d 比特位不同的时候，a 这一位是 1，否则是 0。
所以答案就是 b^d。

代码二
代码二备份（洛谷）
"""
"""
题目相当于从a中补一些位做被减数x，抠一些为做减数y，差是d
那么x一定包含y,拆位讨论即可
"""


# print((10|4)-(2&4))
#       ms
def solve():
    b, c, d = RI()
    ans = 0
    for i in range(61):
        x, y, z = b >> i & 1, c >> i & 1, d >> i & 1
        if z:  # z是1，一定要组合成10
            if x == 0 and y == 1:  # 填啥都组不出10
                return print(-1)
            if x == 0:
                ans |= 1 << i
        else:  # z是0，那么一定是11或者00
            if x == 1 and y == 0:  # 这个组合一定是10
                return print(-1)
            if x == 1:  # 这时y==1,选1，一定可以组合成11；否则选0，可以组合成00
                ans |= 1 << i
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
