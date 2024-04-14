# Problem: D. Blue-Red Permutation
# Contest: Codeforces - Codeforces Round 753 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1607/D
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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1607/D

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(1≤n≤2e5) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)，长为 n 的字符串 s，仅包含 'B' 和 'R'。

每次操作，你可以选择一个下标 i。
如果 s[i]=B，把 a[i] 减少 1。
如果 s[i]=R，把 a[i] 增加 1。

能否在执行若干次（或者零次）操作后，把 a 变成一个 1 到 n 的排列？
输出 YES 或 NO。
输入
8
4
1 2 5 2
BRBR
2
1 1
BB
5
3 1 4 2 5
RBRRB
5
3 1 3 1 3
RBRRB
5
5 1 5 1 5
RBRRB
4
2 2 2 2
BRBR
2
1 -2
BR
4
-2 -1 4 0
RRRR
输出
YES
NO
YES
YES
NO
YES
YES
YES
"""
"""分类讨论+贡献累计
对于对应R的数v来说，它只能增加，那么：
    若n<v，则一定不合法
    若v<=0,则可以把他操作到任意数字。
    否则，它只能变成[v,n]之间的数字
    因此我们令f[i]表示有多少个数字必须分配到i右侧，那么贡献就是f[v]+=1。
    从n遍历到1累计数量不超过槽位即可。
对于B同理。
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    s, = RS()
    left, right = [0] * (n + 1), [0] * (n + 1)
    for v, c in zip(a, s):
        if c == 'R':
            if v > n:
                return print('NO')
            elif v >= 1:
                right[v] += 1
        else:
            if v <= 0:
                return print('NO')
            elif v <= n:
                left[v] += 1

    def ok(a):
        cnt = 0
        for i in range(1, n + 1):
            cnt += a[i]
            if cnt > i:
                return False
        return True

    if ok(left) and ok([0] + right[::-1]):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
