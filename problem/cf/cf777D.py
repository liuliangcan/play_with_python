# Problem: D. Cloud of Hashtags
# Contest: Codeforces - Codeforces Round #401 (Div. 2)
# URL: https://codeforces.com/problemset/problem/777/D
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
PROBLEM = """https://codeforces.com/problemset/problem/777/D

输入 n(≤5e5) 和长为 n 的字符串数组 a，每个字符串都以 # 开头，所有字符串的长度之和不超过 5e5。
你可以把字符串的任意后缀去掉。
输出使得 a 变为字典序升序，至少需要去掉多少字符。
输入
3
#book
#bigtown
#big
输出
#b
#big
#big

输入
3
#book
#cool
#cold
输出
#book
#co
#cold
"""

"""贪心，直接逆序暴力。
由于删除后缀不会使字典序变大，因此越靠后的串越少删。具体为：
最后一个串不动，从倒数第二个开始删除后缀。
"""


#   561  ms
def solve():
    n, = RI()
    a = []
    for _ in range(n):
        s, = RS()
        a.append(s)
    for i in range(n - 2, -1, -1):
        p = min(len(a[i]), len(a[i + 1]))
        for x, y, j in zip(a[i], a[i + 1], range(p)):
            if x < y:
                break
            elif x > y:
                a[i] = a[i][:j]
                break
        else:
            if len(a[i]) > p:
                a[i] = a[i][:p]
    print(*a, sep='\n')


if __name__ == '__main__':
    solve()
