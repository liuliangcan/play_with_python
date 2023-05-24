# Problem: C. Marina and Vasya
# Contest: Codeforces - Codeforces Round #324 (Div. 2)
# URL: https://codeforces.com/problemset/problem/584/C
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/584/C

输入 n t(0≤t≤n≤1e5) 和两个长度均为 n 的字符串 s1 和 s2，均由小写字母组成。

定义 f(a,b) 表示 a[i]!=b[i] 的下标数量。
构造一个长为 n 的，由小写字母组成的字符串 s3，使得 f(s1,s3)=f(s2,s3)=t。
如果无法构造，输出 -1。
输入
3 2
abc
xyc
输出
ayd

输入
1 0
c
b
输出
-1
"""


#    109   ms
def solve():
    n, t = RI()
    s1, = RS()
    s2, = RS()
    p = n - t  # 题目转化为构造ans串使ans和s1\s2相同的字符有p个
    same = []  # same[i] 表示 s1[i] == s2[i] 的下标
    diff = []  # diff[i] 表示 s1[i]!= s2[i] 的下标
    for i, (x, y) in enumerate(zip(s1, s2)):
        if x == y:
            same.append(i)
        else:
            diff.append(i)
    s = len(same)
    # 显然如果p<=s可以直接选same中的p个下标相同即可。
    # 如果d = p-s >0 则需要从diff中选2d个下标分别对应s1和s2的位置
    # 其它位置填一个不同于s1和s2的即可
    if p > s and (p - s) * 2 > len(diff):
        return print(-1)
    ans = [''] * n
    if p <= s:
        for i in same[:p]:
            ans[i] = s1[i]
    else:
        for i in same:
            ans[i] = s1[i]
        for i in range(0, p - s):
            ans[diff[i * 2]] = s1[diff[i * 2]]
            ans[diff[i * 2 + 1]] = s2[diff[i * 2 + 1]]

    for i, c in enumerate(ans):  # 把其余位置填一个不同于s1和s2的字符
        if not c:
            for c in 'abc':  # 从三个中选一定能找到一个同时异与s1和s2的字符
                if c != s1[i] and c != s2[i]:
                    ans[i] = c
                    break
    print(''.join(ans))


if __name__ == '__main__':
    solve()
