# Problem: D. Array Differentiation
# Contest: Codeforces - Codeforces Global Round 15
# URL: https://codeforces.com/problemset/problem/1552/D
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
PROBLEM = """https://codeforces.com/problemset/problem/1552/D

输入 t(≤20) 表示 t 组数据，每组数据输入 n(≤10) 和长为 n 的数组 a(-1e5≤a[i]≤1e5)。

如果存在一个长为 n 的数组 b，对于任意 i，都存在 j 和 k，使得 a[i]=b[j]-b[k]，则输出 YES，否则输出 NO。
注意 j 可以等于 k。
输入
5
5
4 -7 -1 5 10
1
0
3
1 10 100
4
-3 2 10 2
9
25 -171 250 174 152 242 100 -205 -258
输出
YES
YES
NO
YES
YES
"""
"""https://www.luogu.com.cn/blog/endlesscheng/solution-cf1552d
由于 a_ia 
i
​
  可以由 bb 的任意两元素相减表示，不妨将 aa 中的部分元素取反，记新数组为 a'a 
′
 。

设 b_1=0b 
1
​
 =0，将 bb 视作 a'a 
′
  的前 n-1n−1 个元素的前缀和。

若 a'a 
′
  的前 n-1n−1 个元素中存在一个子数组 a'[l\cdots r]a 
′
 [l⋯r]，其区间和等于 a'_na 
n
′
​
 ，由于 bb 是前缀和，所以 a'_na 
n
′
​
  也能用 bb 的两个元素相减表示。

写成等式就是 a'_l+...+a'_r=a'_na 
l
′
​
 +...+a 
r
′
​
 =a 
n
′
​
 
移项得 a'_l+...+a'_r-a'_n=0a 
l
′
​
 +...+a 
r
′
​
 −a 
n
′
​
 =0
实际上，由于 a'a 
′
  的元素既可以随意取反，也可以随意调换顺序，我们相当于是在 a'a 
′
  中寻找一个子集，其元素和为 00。

因此得出结论：需要在 aa 中找到一个子集，该子集的部分元素取反后，能够使该子集元素和为 00。若能找到这样的子集则输出 \texttt{YES}YES，否则输出 \texttt{NO}NO。

进一步地，我们只需要判断 aa 中是否存在两个子集，其子集和相等就行了。

简单地证明一下：

设这两个子集为 AA 和 BB，若有 \sum A=\sum B∑A=∑B，移项得 \sum A-\sum B=0∑A−∑B=0。

注意，若 AA 和 BB 有相同的元素，会在上式中消去。消去后的剩余部分就是 aa 的一个子集，其中部分元素取反，且该子集和为 00，这正是我们需要寻找的。"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    s = set()
    for i in range(1 << n):
        x = 0
        for j in range(n):
            if i & (1 << j):
                x += a[j]
        if x in s:
            return print('YES')
        s.add(x)
    print('NO')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
