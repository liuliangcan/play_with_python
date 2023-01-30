# Problem: A - AB Palindrome
# Contest: AtCoder - AtCoder Regular Contest 145
# URL: https://atcoder.jp/contests/arc145/tasks/arc145_a
# Memory Limit: 1024 MB
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

MOD = 10**9 + 7
PROBLEM = """https://atcoder.jp/contests/arc145/tasks/arc145_a

输入 n(2≤n≤2e5) 和长为 n 的字符串 s，仅包含 'A' 和 'B'。

你可以执行如下操作任意多次：
选择两个相邻字符 s[i] 和 s[i+1]，把 s[i] 替换成 'A'，s[i+1] 替换成 'B'。
能否使 s 变成回文串？输出 Yes 或 No。
输入
3
BBA
输出 Yes
解释 替换后两个字符，得到 BAB

输入
4
ABAB
输出 No
https://atcoder.jp/contests/arc145/submissions/38323634

手玩。

操作方法如下：
如果 s[0]='B'，从 s[1] 开始，左到右替换，得到 BAA...AAB。
如果 s[n-1]='A'，从 s[n-2] 开始，右到左替换，得到 ABB...BBA。

那么，只有两种情况无法操作：
s="BA"。
s[0]='A' 且 s[n-1]='B'。
"""



#       ms
def solve():
    n, = RI()
    s, = RS()
    if s == 'BA' or s[0] == 'A' and s[-1] == 'B':
        return print('No')
    print('Yes')



if __name__ == '__main__':
    solve()
