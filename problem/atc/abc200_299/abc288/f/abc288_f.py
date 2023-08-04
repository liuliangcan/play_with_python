# Problem: F - Integer Division
# Contest: AtCoder - Toyota Programming Contest 2023 Spring Qual A（AtCoder Beginner Contest 288）
# URL: https://atcoder.jp/contests/abc288/tasks/abc288_f
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
# MOD = 10**9 + 7
MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc288/tasks/abc288_f

输入 n(2≤n≤2e5) 和长为 n 的数字 s，保证 s 不含 0。
把 s 分割成若干段，得分为每一段的乘积。特别地，如果不分割，则得分为 s。
输出所有分割方案的得分之和，模 998244353。
注：一共有 2^(n-1) 种分割方案。
输入
3
234
输出 418
解释 234 + 2*34 + 23*4 + 2*3*4 = 418

输入
4
5915
输出 17800

输入
9
998244353
输出 258280134
"""

"""提示 1：从划分型 DP 入手，你能否找到一个规模更小的子问题？

例如 s=1234，如果最后一段为 34，那么得分为 12*34+1*2*34 = (12+1*2)*34。
注意 12+1*2 是 12 的所有划分的得分之和。
由此可见，枚举出最后一段后，我们可以把问题变成一个规模更小的子问题。

提示 2：定义 f[i] 表示分割前 i 个数字的得分之和（i 从 1 开始）
f[0] = 0
f[i] = val(1,i) + f[1]*val(2,i) + f[2]*val(3,i) + ... + f[i-1]*val(i,i)
其中 val(j,i) 表示 s[j] 到 s[i] 这一段对应的数字。
但这样写是 O(n^2) 的。

提示 3：观察 f[i-1] 的转移方程与 f[i] 的转移方程的差异。

提示 4：val(j,i) = val(j,i-1) * 10 + (s[i] - '0') 
根据这一式子可以得到
f[i] = f[i-1] * 10 + (1+f[1]+f[2]+...+f[i-1]) * (s[i] - '0')
所以再用一个变量 sumF 表示 1+f[1]+f[2]+...+f[i-1]，就可以 O(1) 地从 f[i-1] 算出 f[i] 了。

https://atcoder.jp/contests/abc288/submissions/44204756"""


#       ms
def solve1():
    n, = RI()
    s, = RS()
    f = [0] * (n + 1)
    sf = 0
    for i, c in enumerate(s, start=1):
        f[i] = (f[i - 1] * 10 + (1 + sf) * int(c)) % MOD
        sf += f[i]
    print(f[-1])


#       ms
def solve2():
    n, = RI()
    s, = RS()
    f = 0
    sf = 0
    for i, c in enumerate(s, start=1):
        f = (f * 10 + (1 + sf) * int(c)) % MOD
        sf += f
    print(f)


#       ms
def solve():
    n, = RI()
    s, = RS()
    f = 0
    sf = 1
    for i, c in enumerate(s, start=1):
        f = (f * 10 + sf * int(c)) % MOD
        sf += f
    print(f)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
