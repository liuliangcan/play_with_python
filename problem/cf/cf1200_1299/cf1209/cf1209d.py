# Problem: D. Cow and Snacks
# Contest: Codeforces - Codeforces Round 584 - Dasha Code Championship - Elimination Round (rated, open for everyone, Div. 1 + Div. 2)
# URL: https://codeforces.com/problemset/problem/1209/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1209/D

输入 n(2≤n≤1e5) 和 k(1≤k≤1e5)。
有 k 个人，每个人都有两种喜欢的零食。零食编号从 1 到 n。
然后输入 k 行，每行两个不同的数，表示第 i 个人喜欢的两种零食的编号。

商店有 n 种零食，每种零食各一个，卖完就没了。
这 k 个人排队购买自己喜欢的所有零食。如果没有买到任何自己喜欢的零食，就会伤心。
请你排列这 k 个人的顺序，最小化伤心的人数。

输入
5 4
1 2
4 3
1 4
3 4
输出 1

输入
6 5
2 3
2 1
3 4
6 5
4 5
输出 0
"""

"""
在喜欢的两种零食之间连边，得到一个图。
对于图中的每个连通块，其任意一棵生成树上的边，对应的人都是可以满足的，我们先满足这些人。其余边，由于零食都被买了，无法满足。

用 DFS 或者并查集可以算出有多少条边无法满足。

代码
代码备份（洛谷）
"""


#       ms
def solve():
    n, k = RI()
    fa = list(range(n + 1))

    def find(x):
        t = x
        while x != fa[x]:
            x = fa[x]
        while t != x:
            fa[t], t = x, fa[t]
        return t

    ans = 0
    for _ in range(k):
        x, y = RI()
        x, y = find(x), find(y)
        if x != y:
            fa[x] = y
            ans += 1
    print(k - ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
