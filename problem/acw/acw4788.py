# Problem: 奇偶
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4788/
# Memory Limit: 256 MB
# Time Limit: 1000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import sys
import heapq
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
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """4785. 奇偶
 

给定一个由小写字母组成的字符串，请你统计其中包含的不同小写字母数量。

如果给定字符串中包含奇数个不同小写字母，则输出 odd。

如果给定字符串中包含偶数个不同小写字母，则输出 even。

输入格式
共一行，一个由小写字母组成的字符串。

输出格式
共一行，按题目要求输出答案。

如果给定字符串中包含奇数个不同小写字母，则输出 odd。

如果给定字符串中包含偶数个不同小写字母，则输出 even。

数据范围
所有测试点满足，给定字符串的长度范围 [1,100]。

输入样例1：
wjmzbmr
输出样例1：
even
"""



if __name__ == '__main__':
    s, = RS()
    cnt = 0
    for c in set(s):
        if c.isalpha() and c == c.lower():
            cnt += 1
    if cnt&1:
        print('odd')
    else:
        print('even')
