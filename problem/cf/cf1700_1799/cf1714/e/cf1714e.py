# Problem: E. Add Modulo 10
# Contest: Codeforces - Codeforces Round 811 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1714/E
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
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1714/E

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(1≤n≤2e5) 和长为 n 的数组 a(0≤a[i]≤1e9)。

每次操作你可以把 a[i] += a[i] % 10。
你可以操作任意次，相同 a[i] 也可以操作多次。

能否使所有 a[i] 都相等？输出 Yes/No。
输入
10
2
6 11
3
2 18 22
5
5 10 5 10 5
4
1 2 4 8
2
4 5
3
93 96 102
2
40 6
2
50 30
2
22 44
2
1 5
输出
Yes
No
Yes
Yes
No
Yes
No
No
Yes
No
"""
"""https://codeforces.com/contest/1714/submission/205531470

个位数为 0，操作后不变。
个位数为 5 的，操作后个位数变成 0，无法继续增大。
所以如果个位数为 0 或 5 的，操作一次后不能都相等，直接输出 No。

其余的可以无限增大。
手玩一下发现这些数按照模 20 的余数分成两组，每组内的数可以互相转换。
（注意从 1 出发，是无法到达 12 的，但是可以到达 22）

算上模 10 的余数为 0 或 5 的（或者模 5 余数为 0），一共可以分成三组。
所以统计这些数能不能只分成一组。

代码实现时，可以用位运算做到完美的 O(n) 一次遍历 + O(1) 空间。"""
"""不用位运算也可以O(1)空间
一共三种数字:
末尾0和5的；
模20分两组，组内可以转化到组内某个数字，分别是:
    {1, 2, 4, 8, 16, 13, 17, 19} -- 最终可以变成2 4 8 16
    {3, 6, 12, 14, 18, 7, 9, 11} -- 最终可以变成12 14 18
后两种情况直接用两个标记位记录是否存在即可，
0的那组由于0不能变，因此只能存在一个完全相同的数字；5只能加一次5变成0；
那么记录这个数字即可，为了方便我用set，这个set到2就可以记非法了。
最后，三类数字只能存在一种，可以用len(zero) + x + y == 1判断。
"""


#   187    ms
def solve():
    n, = RI()
    a = RILST()
    zero = set()
    p = {1, 2, 4, 8, 16, 13, 17, 19}
    q = {3, 6, 12, 14, 18, 7, 9, 11}
    x = y = 0
    for v in a:
        if v % 10 == 0:
            zero.add(v)
        elif v % 5 == 0:
            zero.add(v + 5)
        elif v % 20 in p:
            x = 1
        else:
            y = 1
        if len(zero) > 1:
            return print('No')
    if len(zero) + x + y != 1:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
