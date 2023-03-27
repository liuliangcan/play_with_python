# Problem: C. Unstable String
# Contest: Codeforces - Educational Codeforces Round 110 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1535/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1535/C

输入 t(≤1e4) 表示 t 组数据。所有数据的字符串长度之和 ≤2e5。
每组数据输入一个长度不超过 2e5 的字符串 s，仅包含 '0' '1' '?' 三种字符。

定义灵茶字符串为：把字符串中的每个 ? 都改成 0 或者 1（每个 ? 怎么改是独立的），可以使字符串变成 0101... 或者 1010... 这样的 01 交替字符串。
例如 0，0??10，??? 都是灵茶字符串，而 00，?1??1 不是。
输出 s 中有多少个子串是灵茶字符串。

注：子串是连续的。
输入
3
0?10
???
?10??1100
输出 
8
6
25
"""
"""dp
所有合法串都是从头开始0101..或者1010..的完整s中的一个子串。
那么可以分类讨论两种情况，按下标：int(c) == i & 1
1. 下标奇数，值也是奇数 / 下标偶数，值也是偶数
2. 下标奇数，值是偶数数 / 下标偶数，值是奇数
当c是确定的01时，显然情况是互斥的，但若是不确定的?，那么它可以代表两种情况，要算两次，那么需要减去完全一致的情况，即连续串为?的情况
f0[i]代表情况1以i为结尾的字符串，连续合法串的长度
f1[i]代表情况2以i为结尾的字符串，连续合法串的长度
f3[i]代表以i为结尾的连续?的长度。
当c==?时，f0f1f3都可以从前边转移，并且f0f1都累计答案，但是要去掉一次连续的?。
"""
"""https://codeforces.com/problemset/submission/1535/199246246

提示 1：
从左到右遍历 s。
由于 ? 怎么变都可以，重点应该放在值为 0 或 1 的 s[i] 上。
你也可以思考在没有 ? 的情况下，这题要怎么做。

提示 2：
假设 s[i] 是灵茶子串的末尾字符，那么灵茶子串的起始位置最远能到哪？
例如 s = "01101"，如果 s[4] 是灵茶子串的末尾字符，起始位置最远可以到 s[2]。
那么 s[2]~s[4], s[3]~s[4], s[4]~s[4] 这三个都是灵茶子串。
如何记录这样的起始位置呢？

提示 3：
如果没有 ?，上一个 s[i] == s[i-1] 的 i 就是起始位置。
但是由于 ? 的存在，无法判断相邻字符。如何解决？
尝试从 i 和 s[i] 的自身关系去思考，不再依赖其余位置。

提示 4：
定义 pos[0] 为上一个 i 和 s[i] 奇偶性相同的 i，
定义 pos[1] 为上一个 i 和 s[i] 奇偶性不同的 i。
（这里 s[i] != '?'）
例如 s = "01101"，遍历到 s[4] 时，pos[0] = 1，pos[1] = 4

按照 pos 的定义，min(pos[0], pos[1]) + 1 就是起始位置了。
i-min(pos[0], pos[1]) 就是末尾字符为 s[i] 的灵茶子串个数了。
累加 i-min(pos[0], pos[1]) 就是答案。

为方便计算，初始化 pos[0] = pos[1] = -1"""

#   139    ms
def solve1():
    s, = RS()
    n = len(s)
    f0, f1, f3 = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    ans = 0
    for i, c in enumerate(s):
        if c == '?':
            f3[i + 1] = f3[i] + 1
            f0[i + 1] = f0[i] + 1
            f1[i + 1] = f1[i] + 1
            ans += f0[i + 1] + f1[i + 1] - f3[i + 1]
        elif int(c) == i & 1:
            f1[i + 1] = f1[i] + 1
            ans += f1[i + 1]
        else:
            f0[i + 1] = f0[i] + 1
            ans += f0[i + 1]

    print(ans)


#       ms
def solve():
    s, = RS()
    n = len(s)
    pos = [-1, -1]
    ans = 0
    for i, c in enumerate(s):
        if c != '?':
            pos[int(c) ^ i & 1] = i
        ans += i - min(pos)

    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
