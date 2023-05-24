# Problem: D. Flipper
# Contest: Codeforces - Codeforces Round 874 (Div. 3)
# URL: https://codeforces.com/contest/1833/problem/D
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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，实测这个快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """给一个长为n的排列p。你必须做如下操作恰好一次：
1. 选一个子段[l,r]，(1<=l<=r<=n)翻转这个段。
2. 把这个段两边的数据交换。即交换[1~l-1],[r+1,n]，注意这两段可以为空

输出操作后字典序最大的p
"""
"""贪心，枚举l即可。注意讨论
- 先找最大的数即n的位置pos,让pos作为r，枚举l。若n在最后，则可以作为r，直接翻转到0.
- 若n在0上，由于必须翻转一次，n一定会向后， 那么考虑让n-1到0，方法和前边一样。
---
- 这题也有O(n)的做法。可以看看灵神的视频。
找到pos后，前边段其实是不变的，r翻转后也是不变的。讨论r-1即可。
"""



#       ms
def solve():
    n, = RI()
    p = RILST()
    if n == 1:
        return print(1)
    ans = p[::-1]
    pos = p.index(n)
    if pos:
        ans = max(ans, p[pos+1:]+p[pos:] + p[:pos])
        mx = []
        r = pos
        for l in range(pos):
            mx = max(mx, p[l:r][::-1] + p[:l])
        ans = max(ans, p[pos:] + mx)
    else:
        pos = p.index(n - 1)
        ans = max(ans, p[pos+1:]+p[pos:] + p[:pos])
        mx = []
        r = pos
        for l in range(pos):
            mx = max(mx, p[l:r][::-1] + p[:l])
        ans = max(ans, p[pos:] + mx)

    print(*ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
