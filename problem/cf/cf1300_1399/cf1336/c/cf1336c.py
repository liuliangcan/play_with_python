# Problem: C. Kaavi and Magic Spell
# Contest: Codeforces - Codeforces Round 635 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1336/C
# Memory Limit: 512 MB
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
# MOD = 10 ** 9 + 7
MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1336/C

输入长度不超过 3000 的字符串 S，只包含小写字母。设 S 的长度为 n。
输入长度不超过 n 的字符串 T，只包含小写字母。

从一个空字符串 A 开始，执行如下操作不超过 n 次：
删除 S 的第一个字母，然后加到 A 的开头或者末尾。

问：要使 T 是 A 的前缀，有多少种不同的操作方式？模 998244353。
注：即使两个不同的操作方式得到了相同的字符串 A，也算不同的操作方式。
输入
abab
ba
输出 12
解释：见右图，注意第一个 a 有两种操作方式

输入
defineintlonglong
signedmain
输出 0

输入
rotator
rotator
输出 4

输入
cacdcdbbbb
bdcaccdbbb
输出 24
"""
"""先假设 s 和 t 一样长。
我们不知道 s 的第一个字母和谁匹配，但我们知道 s 的最后一个字母只能与 t[0] 或者 t[m-1] 匹配（加到开头或者末尾）。
假如与 t[0] 匹配，那么问题变成 s[:n-1] 与 t[1:] 匹配的方案数。这是一个规模更小的子问题。
这启发我们得到下面的区间 DP。

把 t 扩充成和 s 一样长，扩充的字母视作任意字符（一定可以和 s[i] 匹配）。
定义 f[i][j] 表示操作前缀 s[0]~s[j-i] 得到子串 t[i]~t[j] 的方案数。
那么答案就是 f[0][m-1]+f[0][m]+...+f[0][n-1]。
考虑 s[j-i] 与 t[i] 还是 t[j] 匹配，可以得到
f[i][j] = (i>=m || s[j-i]==t[i] ? f[i+1][j] : 0) + (j>=m || s[j-i]==t[j] ? f[i][j-1] : 0)
初始值 f[i][i] = (i>=m || s[0]==t[i] ? 2 : 0)
（也可以初始化 f[i+1][i] = 1）

https://codeforces.com/problemset/submission/1336/216028319"""


#       ms
def solve():
    s, = RS()
    t, = RS()
    n, m = len(s), len(t)
    f = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        if i >= m or s[0] == t[i]:
            f[i][i] = 2
        for j in range(i + 1, n):
            if i >= m or s[j - i] == t[i]:
                f[i][j] += f[i + 1][j]
            if j >= m or s[j - i] == t[j]:
                f[i][j] += f[i][j - 1]
            f[i][j] %= MOD
    print(sum(f[0][m - 1:]) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
