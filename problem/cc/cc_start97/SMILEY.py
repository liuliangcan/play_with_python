# Problem: Schrodinger Smiley
# Contest: CodeChef - START97B
# URL: https://www.codechef.com/START97B/problems/SMILEY
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
PROBLEM = """在表情符号领域，薛定谔笑脸在其状态被观察之前既微笑又皱眉。

给定一个字符串 
�
S，只包含 :, ( 和 )（冒号、右括号和左括号）。
我们将薛定谔笑脸定义为两个冒号之间的任意数量的右括号。例如，:):, :))): 和 :))))): 是薛定谔笑脸，而:))(:, :(:, ::): 和 :: 不是。

找出字符串 
�
S 中所有是薛定谔笑脸的子字符串的总数。

一个子字符串是通过从字符串的开头删除任意（可能为零）数量的字符和从字符串的末尾删除任意（可能为零）数量的字符得到的。

输入格式
输入的第一行包含一个整数 
�
T，表示测试用例的数量。
每个测试用例由两行输入组成。
每个测试用例的第一行包含一个整数 
�
N，表示字符串 
�
S 的长度。
下一行包含字符串 
�
S。
输出格式
对于每个测试用例，输出一个新行，表示字符串 
�
S 中所有是薛定谔笑脸的子字符串的总数。
"""
"""贪心模拟。
用pq分别代表前边是否有冒号和右括号。
遇到冒号尝试更新答案，并且重置p=1 q=0
遇到右括号只需更新q=1
遇到左括号，重置p=q=0
"""

#       ms
def solve():
    n, = RI()
    s, = RS()
    ans = 0
    p = q = 0
    for c in s:
        if c == ':':
            if p and q:
                ans += 1
            p = 1
            q = 0
        elif c == ')':
            q = 1
        else:
            p = q = 0
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
