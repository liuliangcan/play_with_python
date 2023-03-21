# Problem: D. Ehab the Xorcist
# Contest: Codeforces - Codeforces Round 628 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1325/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1325/D

输入 u 和 v，范围均在 [0,1e18]。

构造一个长度最短的数组，满足异或和等于 u，和等于 v。
如果无法构造，输出 -1，否则输出数组长度和任意满足要求的数组。
输入
2 4
输出
2
3 1
解释：3^1=2, 3+1=4

输入
1 3
输出
3
1 1 1

输入
8 5
输出
-1

输入
0 0
输出
0
"""
"""https://codeforces.com/contest/1325/submission/97080317

提示 1：u <= v

提示 2：如果 u 是奇数，那么必然有奇数个奇数，所以 v 也是奇数；同理，偶数……
所以 v-u 必须是偶数

提示 3：设 x = (v-u)/2，那么构造数组 [u,x,x]，其异或和为 u，元素和为 2x+u = v
这说明数组长度至多为 3。
什么时候数组长度为 2？也就是说，找到两个数 a b 满足 a^b=u，a+b=v。

提示 4-1：你能得到 | ^ & + 这些运算的关系吗？

提示 4-2：
a|b = (a^b) + (a&b)    类比集合论
a+b = (a|b) + (a&b)    类比加法器
联立得
a+b = (a&b)*2 + (a^b)

提示 5-1：x = a&b

提示 5-2：
如果 u&x = 0，那么直接把 x 放到 u 里面，数组为 [u|x, x] 
如果 u&x ≠ 0，说明有个比特位都是 1，但是 p^q=1 和 p&q=1 不能同时成立，所以此时无法构造长为 2 的数组。"""


#   77    ms
def solve():
    u, v = RI()
    if u > v or (v - u) & 1:
        return print(-1)
    if u == v:
        if u == 0:
            return print(0)
        print(1)
        return print(u)
    x = (v - u) // 2
    if u & x:
        print(3)
        return print(u, x, x)
    else:
        print(2)
        print(u | x, x)


if __name__ == '__main__':
    solve()
