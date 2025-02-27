# Problem: F - #(subset sum = K) with Add and Erase
# Contest: AtCoder - SuntoryProgrammingContest2023（AtCoder Beginner Contest 321）
# URL: https://atcoder.jp/contests/abc321/tasks/abc321_f
# Memory Limit: 1024 MB
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
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = randrange(2 ** 62)

MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc321/tasks/abc321_f

输入 q(1≤n≤5000) 和 k(1≤k≤5000)。
一开始有一个空箱子。输入 q 个操作：
"+ v"：把一个写有数字 v 的小球放入箱子。
"- v"：从箱子中移除一个写有数字 v 的小球，保证箱子中有这样的小球。
v 的范围是 [1,5000]。

每次操作后，输出有多少种方案，从箱子中选取一些球，元素和恰好等于 k。答案模 998244353。
注意球是有区分的。
输入
15 10
+ 5
+ 2
+ 3
- 2
+ 5
+ 10
- 3
+ 1
+ 3
+ 3
- 5
+ 1
+ 7
+ 4
- 3

输出
0
0
1
0
1
2
2
2
2
2
1
3
5
8
5
"""
"""小球是有区别的，将这些小球视作一些物品，用 0-1 背包计算恰好装满容量为 k 的背包的方案数。

添加数字的时候，按照 0-1 背包的方法转移，也就是 f[i] += f[i-v]，倒序循环。
删除数字的时候，撤销掉之前的转移，也就是 f[i] -= f[i-v]，正序循环。

注意取模。
注意保证取模之后的结果非负。

可撤销背包

问：为什么撤销是对的？
答：可以这样理解，物品顺序不影响 f 的计算，那么当我取出数字 v 的时候，我可以把 "+ v" 调换到取出之前，也就是刚加进去就拿出来，这样之前写的 f[i] += f[i-v] 就可以立刻用 f[i] -= f[i-v] 撤销掉，f 现在是没有 x 的方案数。"""


#       ms
def solve():
    q, k = RI()
    f = [1] + [0] * k
    for _ in range(q):
        t, v = RS()
        v = int(v)

        if t == '+':
            for j in range(k, v - 1, -1):
                f[j] = (f[j]+f[j - v])%MOD

        else:
            for j in range(v, k + 1):
                f[j] = (f[j] -f[j - v])%MOD

        print(f[k])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
