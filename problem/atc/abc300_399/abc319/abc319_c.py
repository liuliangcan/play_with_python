# Problem: C - False Hope
# Contest: AtCoder - AtCoder Beginner Contest 319
# URL: https://atcoder.jp/contests/abc319/tasks/abc319_c
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
from math import sqrt, gcd, inf, perm

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
PROBLEM = """有一个3×3的方格，每个方格内写着介于1和9之间（包括1和9）的数字。第i行从顶部开始，第j列从左边开始（1≤i≤3,1≤j≤3）的方格包含数字ci,j。

同一个数字可能写在不同的方格中，但不能在垂直、水平或对角线方向上连续出现三个方格。更确切地说，保证ci,j满足以下所有条件。

对于任意1≤i≤3，不满足ci,1=ci,2=ci,3。
对于任意1≤j≤3，不满足c1,j=c2,j=c3,j。
不满足c1,1=c2,2=c3,3。
不满足c3,1=c2,2=c1,3。
高桥将以随机顺序看到每个方格中的数字。当存在一条线（垂直、水平或对角线），满足以下条件时，他会感到失望。

他看到的前两个方格包含相同的数字，但最后一个方格包含不同的数字。
计算高桥在没有失望的情况下看到所有方格中数字的概率。

约束条件
ci,j∈{1,2,3,4,5,6,7,8,9} (1≤i≤3,1≤j≤3)
对于任意1≤i≤3，不满足ci,1=ci,2=ci,3。
对于任意1≤j≤3，不满足c1,j=c2,j=c3,j。
不满足c1,1=c2,2=c3,3。
不满足c3,1=c2,2=c1,3。
"""
"""听木木老师的：枚举9个数的排列 只有362880种,然后这9个数的排列中，不能有前两个数相同的行是按aab顺序排列的
用bad储存所有这种的线：包括三行三列、两条对角线，每条线最多只有两种方法进bad，因此bad最多只有16个元素(case2就是这种数据)

所以，总复杂度是362880*9*16=52254720
"""


#  527     ms
def solve():
    g = []
    for _ in range(3):
        g.append(RILST())
    bad = []  # 失望顺序
    for x, y, z in (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6):
        for x, y, z in permutations((x, y, z)):
            if g[x // 3][x % 3] == g[y // 3][y % 3]:
                bad.append((x, y, z))
    # print(bad)
    # print(len(bad))
    p = 0  # 会失望的排列方法
    for q in permutations(range(9)):
        for x, y, z in bad:
            if q.index(x) < q.index(y) < q.index(z):  # 不能有这个顺序，有就寄
                p += 1
                break

    print(1 - p / perm(9))


#       ms
def solve1():
    from itertools import permutations as p

    C = [list(map(int, input().split())) for _ in range(3)]
    N = [l for r in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)] for l in
         p(r)
         if C[l[0] // 3][l[0] % 3] == C[l[1] // 3][l[1] % 3]]
    print(N)
    a = 0
    for q in p(range(9)):
        for n in N:
            if q.index(n[0]) < q.index(n[1]) < q.index(n[2]): break
        else:
            a += 1
    print(a / 362880)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
