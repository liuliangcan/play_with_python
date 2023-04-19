# Problem: A. Hilbert's Hotel
# Contest: Codeforces - Codeforces Round 639 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1344/A
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
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法;数据量小的时候不一定更快

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1344/A

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(≤2e5) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)。

如果对于任意两个不同的整数 k1 和 k2，都满足 a[k1 mod n] + k1 ≠ a[k2 mod n] + k2，则输出 YES，否则输出 NO。
注意对于负数 k，k mod n 的结果也在 [0,n-1] 内。
输入
6
1
14
2
1 -1
4
5 5 5 1
3
3 2 1
2
0 1
5
-239 -2 -100 -3 -11
输出
YES
YES
YES
NO
NO
YES
"""
"""取模+哈希表
- 取模相同的k1,k2，他们会落在同一个a[i]由于k1k2不同，因此不需要考虑。
- 考虑每个位置上会落下哪些数：
    - 位置0,若k=0,得a[0];k=n,得a[0]+n;k=2n,得a[0]+2n ...; 发现k只能间隔n取，注意可以取负数，-n,-2n；这是个公差n的等差序列。
    - 位置1,若k=1,得a[1]+1;k=n+1,得a[1]+n+1...;同样是个公差n的等差数列，底是a[1]+1。
    - 位置i,若k=i,得a[i]+i;k=n+i,得a[i]+n+i。。。;公差n，底是a[i]+1。
- 要使这n个等差数列互不重叠，当且仅当他们在[0,n-1]内取的那个数不同。
- 因此直接用哈希表记录每个(a[i]+i)%n即可
"""
"""https://codeforces.com/contest/1344/submission/202560069

考虑什么时候输出 NO。
设 k1 = p1*n + i, k2 = p2*n + j
则有 a[i] + (p1*n + i) = a[j] + (p2*n + j)
变形得 (a[i] + i) - (a[j] + j) = (p2-p1) * n
由于 p2-p1 可以随意取，所以变成 a[i] + i 和 a[j] + j 模 n 同余。
所以问题变成 a 中是否有相同的 (a[i]+i) % n，用 bool 数组记录即可。
注意取模为负数时要调整到非负数。"""
#       ms
def solve():
    n, = RI()
    a = RILST()
    s = set()
    for i, v in enumerate(a):
        x = (v + i) % n
        if x in s:
            return print('NO')
        s.add(x)
    print('YES')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
