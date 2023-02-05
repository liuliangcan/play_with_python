# Problem: D. New Year Letter
# Contest: Codeforces - Good Bye 2013
# URL: https://codeforces.com/problemset/problem/379/D
# Memory Limit: 256 MB
# Time Limit: 1000 ms
#
# Powered by CP Editor (https://cpeditor.org)

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/379/D

输入 k(3≤k≤50) x(0≤x≤1e9) n(1≤n≤100) m(1≤m≤100)。
你需要构造长分别为 n 和 m 的字符串 s[1] 和 s[2]，它们只能包含大写字母。
然后按照 s[i]=s[i-2]+s[i-1] 的方式，生成字符串 s[k]，要求子串 "AC" 在 s[k] 中恰好出现 x 次。
如果可以构造，输出任意符合要求的 s[1] 和 s[2]，否则输出 "Happy new year!"。
输入 
3 2 2 2
输出
AC
AC

输入 
3 3 2 2
输出
Happy new year!

输入 
3 0 2 2
输出
AA
AA

https://codeforces.com/contest/379/submission/187569304

AC 只能发生在这些地方：
s[1] 内部
s[2] 内部
s[1]+s[1] 交界处（这是不可能的）
s[1]+s[2] 交界处
s[2]+s[1] 交界处
s[2]+s[2] 交界处

那么暴力枚举 s[1] 中有多少 AC，开头是否为 C，结尾是否为 A。
s[2] 同理。
然后迭代计算 s[k] 的 AC 个数，看是否为 x。
具体见代码。
"""

if __name__ == '__main__':
    k, x, n, m = RI()

    for c1 in range(2):  # 枚举s1开头是否是c
        for a1 in range(2):  # 枚举s1结尾是否是a
            if a1 + c1 > n:  # 长度超了不合法
                continue
            for ac1 in range((n - c1 - a1) // 2 + 1):  # 枚举s1内部存在几个ac
                for c2 in range(2):
                    for a2 in range(2):
                        if c2 + a2 > m:
                            continue
                        for ac2 in range((m - a2 - c2) // 2 + 1):
                            # A1, C1, C2, AC1, AC2 = a1, c1, c2, ac1, ac2
                            # dp = [(c1, a1, ac1), (c2, a2, ac2)]
                            # for _ in range(k - 2):
                            #     (C1, A1, AC1), (C2, A2, AC2) = dp[-2:]
                            #     dp.append((C1, A2, AC1 + AC2 + (A1 & C2)))A

                            # 93 ms
                            C1, C2, A1, AC1, AC2 = c1, c2, a1, ac1, ac2
                            for _ in range(2, k):
                                C1, C2, A1, AC1, AC2 = C2, C1, a2, AC2, AC1 + (A1 & C2) + AC2

                            if AC2 == x:
                                print('C' * c1 + 'AC' * ac1 + 'Z' * (n - c1 - ac1 * 2 - a1) + 'A' * a1)  # 构造s1
                                print('C' * c2 + 'AC' * ac2 + 'Z' * (m - c2 - ac2 * 2 - a2) + 'A' * a2)
                                exit()
    print('Happy new year!')
