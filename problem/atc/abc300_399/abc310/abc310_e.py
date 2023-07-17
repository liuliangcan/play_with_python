# Problem: E - NAND repeatedly
# Contest: AtCoder - freee Programming Contest 2023（AtCoder Beginner Contest 310）
# URL: https://atcoder.jp/contests/abc310/tasks/abc310_e
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
PROBLEM = """问题陈述
给定一个长度为N的由0和1组成的字符串S。它描述了一个长度为N的序列A=(A1,A2,…,AN)。如果S的第i个字符（1≤i≤N）为0，则Ai=0；如果为1，则Ai=1。

找出以下内容：

∑1≤i≤j≤N(⋯((Ai⊼Ai+1)⊼Ai+2)⊼⋯⊼Aj)
更正式地说，找出∑i=1→N∑j=i→N f(i,j) for (i,j) (1≤i≤j≤N)的值。

其中f(i,j) (1≤i≤j≤N)的定义如下：

f(i,j)={ Ai f(i,j−1)⊼Aj (i=j) (i<j)

这里，⊼，NAND，是一个满足以下条件的二元运算符：

0⊼0=1,0⊼1=1,1⊼0=1,1⊼1=0.

约束条件
1≤N≤10^6
S是一个长度为N的由0和1组成的字符串。
"""
""" 题目实际上是问有多少个子段结果是1。首先手玩一下：
00->1
01->1
10->1
11->0
发现只要有0结果必1；只有同时1结果才是0.那么枚举右端点，分类讨论：
1. 如果当前右端点s[i]=0，显然左端点可以从0取到i-1任意位置，不管前边结果是几，这个子段都会被a[i]变成1.
2. 如果当前右端点s[i]=1，需要手玩一下，发现找到前边第一个0继续讨论：
    1. 对于连续的1，枚举任意一个为左端点，发现只有奇数个1才会使这段是1，那么记录连续1的个数f,ans+=(f+1)//2
    2. 对于前边的第一个0，
        如果0前边还有长度（这个0不是s[0]）
            那么它会使前边所有串的结果拦下变成1，等于前边所有位置作为左端点结果是一样的。这时如果从0到当前1的长度是奇数，就可以贡献答案。
        如果前边没有长度，那么这个0只能作为0向后贡献，
            那么若后边1长度是奇数，0可以作为1次左端点        
"""


#       ms
def solve1():
    n, = RI()
    s, = RS()
    ans = 0
    f = 0
    for i, c in enumerate(s):  #
        if c == '0':
            ans += i
            f = 0
        else:
            f += 1
            ans += (f + 1) // 2
            if f % 2 == 0 and i - f > 0:
                ans += (i - f)
            if f & 1 and i - f >= 0:
                ans += 1
        # print(i,ans)
    print(ans)


def solve():
    n, = RI()
    s, = RS()
    ans = x = y = 0  # x,y分别代表当前位置作为右端点时，结果0的个数和结果1的个数
    for c in s:  #
        if c == '0':
            x, y = 1, x + y
        else:
            x, y = y, x + 1
        ans += y
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
