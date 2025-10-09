# Problem: B. Stay or Mirror
# Contest: Codeforces - Codeforces Round 1040 (Div. 1)
# URL: https://codeforces.com/problemset/problem/2129/B
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
# DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')  # cf突然编不过这行了
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/2129/B

输入 T(≤1e3) 表示 T 组数据。所有数据的 n 之和 ≤5e3。
每组数据输入 n(2≤n≤5e3) 和 1~n 的排列 p。

对于每个 p[i]，可以保持不变，也可以改成 2n-p[i]。
目标是让 p 的逆序对个数最小。

输出最小逆序对个数。
输入
5
2
2 1
3
2 1 3
4
4 3 2 1
5
2 3 1 5 4
6
2 3 4 1 5 6
输出
0
1
0
2
2
"""
"""从特殊情况入手。想一想，等于 1 的那个数，是保持不变，还是变成 2n-1？对于逆序对的贡献分别是多少？
继续，等于 2 的那个数，是保持不变，还是变成 2n-2？对于逆序对的贡献分别是多少？

方法一

我们可以维护一个数组 a，一开始均为 0，表示未填入数字。
按照元素值从小到大考虑。v=1,2,3,...,n。
对于元素 v，遍历 a，可以算出不变时的与 a 相关的逆序对个数：对于没填入的位置的元素，无论变还是不变，一定比 v 大！
对于 2n-v 来说，没填入的位置的元素，无论变还是不变，一定比 2n-v 小！
这样便能算出 v 是变还是不变。

最后遍历 a 算出逆序对个数。

方法二

对于 1 来说，逆序对的贡献为 min(1 不变，1 变成 2n-1) = min(1 左边的数的个数，1 右边的数的个数)。注意左右两边的数都是大于 1 的。
去掉 1，问题变成规模为 n-1 的子问题。对于 2 来说，逆序对的贡献为 min(2 左边的大于 2 的数的个数，2 右边的大于 2 的数的个数)。
依此类推。对于每个 p[i]，计算 min(p[i] 左边的大于 p[i] 的数的个数，p[i] 右边的大于 p[i] 的数的个数)。

每个 p[i] 的计算公式是互相独立的，我们可以按照任意顺序计算（而不是从小到大），所以可以直接从左到右遍历 p 计算。

注：用主席树可以快速求出区间中的某个值域的元素个数（也支持修改），从而做到 O(nlogn)。

方法一
方法二
方法一备份
方法二备份"""


#   187    ms
def solve():
    n, = RI()
    a = RILST()
    c = [1] * (n + 1)
    for i in range(1, n + 1):
        fa = i + (i & -i)
        if fa <= n:
            c[fa] += c[i]

    def add(i, v):
        while i <= n:
            c[i] += v
            i += i & -i

    def get(i):
        s = 0
        while i:
            s += c[i]
            i -= i & -i
        return s

    pos = [0] * (n + 1)
    for i, v in enumerate(a, 1):
        pos[v] = i
    ans = 0
    for i in range(1, n + 1):
        p = pos[i]
        add(p, -1)
        left = get(p - 1)
        ans += min(left, get(n) - left)
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
