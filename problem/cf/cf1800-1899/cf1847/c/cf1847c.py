# Problem: C. Vampiric Powers, anyone?
# Contest: Codeforces - Codeforces Round 882 (Div. 2)
# URL: https://codeforces.com/contest/1847/problem/C
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
PROBLEM = """DIO知道星尘十字军已经确定了他的位置，并将前来与他战斗。为了破坏他们的计划，他决定派出一些Stand使用者来与他们战斗。最初，他召唤了n个Stand使用者，第i个使用者的力量为ai。利用他的吸血鬼能力，他可以随意多次进行以下操作：

假设当前的Stand使用者数量为m。
DIO选择一个索引i（1≤i≤m）。
然后他召唤一个新的Stand使用者，索引为m+1，并且力量为：
am+1=ai⊕ai+1⊕…⊕am，
其中⊕表示按位异或运算。

现在，Stand使用者的数量变为m+1。
不幸的是，通过使用紫色隐士的预知能力，十字军知道他正在策划这个计划，他们也知道原始Stand使用者的力量。帮助十字军找到DIO可以召唤的所有可能方式中，Stand使用者的最大可能力量。

输入
每个测试包含多个测试用例。第一行包含测试用例的数量t（1≤t≤10000）。以下是测试用例的描述。

每个测试用例的第一行包含一个整数n（1≤n≤105）- 最初召唤的Stand使用者数量。

每个测试用例的第二行包含n个整数a1,a2,…,an（0≤ai<28）- 每个Stand使用者的力量。

保证所有测试用例中n的总和不超过1e5。
"""
"""
i..n 
j.n^i..n
k..n
"""
"""手玩一下发现，第一次添加是个尾缀异或和，第二次开始是任意子段异或和，那么题目转化成找最大子段异或和
当然是可以01trie，但这题a[i]<2**8，异或和不超过256个，因此可以n方搞。
"""

#       ms
def solve():
    n, = RI()
    a = RILST()
    x = set()
    p = 0
    for v in a[::-1]:
        p ^= v
        x.add(p)
    ans = max(x)
    for a in x:
        for b in x:
            ans = max(ans, a ^ b)
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
