# Problem: C. Arithmetic Progression
# Contest: Codeforces - Codeforces Round 224 (Div. 2)
# URL: https://codeforces.com/problemset/problem/382/C
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
PROBLEM = """https://codeforces.com/problemset/problem/382/C

输入 n(1≤n≤1e5) 和长为 n 的整数数组 a(1≤a[i]≤1e8)。

请你往 a 中添加恰好一个整数 x，使得 a 排序后是一个等差数列。
输出 x 的个数，以及所有的 x（按升序输出）。
如果 x 有无穷多个，输出 -1。

【易错题】
输入
3
4 1 7
输出 
2
-2 10

输入
1
10
输出 
-1

输入
4
1 3 5 9
输出 
1
7

输入
4
4 3 4 5
输出 
0

输入
2
2 4
输出 
3
0 3 6
"""


#     124  ms
def solve():
    n, = RI()
    a = RILST()
    if n == 1:
        return print(-1)
    a.sort()
    if a[0] == a[-1]:
        print(1)
        return print(a[0])
    ans = []
    if len(a) == 2:
        d = a[1] - a[0]
        ans.append(a[0] - d)
        if d & 1 == 0:
            ans.append(a[0] + d // 2)
        ans.append(a[1] + d)
        print(len(ans))
        return print(*ans)

    cnt = Counter()  # 储存可能的公差
    for i in range(n - 1):
        cnt[a[i + 1] - a[i]] += 1
        if len(cnt) >= 3:
            return print(0)
    if len(cnt) == 1:
        d = list(cnt.keys())[0]
        print(2)
        return print(*[a[0] - d, a[-1] + d])
    if len(cnt) == 2:
        c = [(k, v) for k, v in cnt.items()]
        c.sort()
        if c[1][1] != 1 or c[1][0] != c[0][0] * 2:
            return print(0)
        print(1)
        for i in range(n - 1):
            if a[i + 1] - a[i] == c[1][0]:
                return print(a[i] + c[1][0] // 2)
    print(0)


if __name__ == '__main__':
    solve()
