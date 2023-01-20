# Problem: D. Training Session
# Contest: Codeforces - Educational Codeforces Round 115 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1598/D
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
from math import sqrt, gcd, inf, comb
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1598/D

输入 t(≤5e4) 表示 t 组数据，每组数据输入 n(3≤n≤2e5) 和 n 个点 (xi,yi)，横纵坐标都在 [1,n] 内。没有重复的点。所有数据的 n 之和不超过 2e5。

从 n 个点中选出 3 个点，满足「横坐标互不相同」或者「纵坐标互不相同」。
输出有多少种选择方案。注意选的是组合，(1,2,3) 和 (3,2,1) 算相同的方案。
输入
2
4
2 4
3 4
2 1
1 3
5
1 5
2 4
3 3
4 2
5 1
输出
3
10
解释 第一组数据，你可以选 (1,2,4),(1,3,4),(2,3,4)，数字表示点的编号
"""
"""https://codeforces.com/problemset/submission/1598/189793851

提示 1：正难则反，考虑哪些不满足要求的选法。

提示 2：如果选了三个横坐标相同的点，由于题目保证没有重复的点，所以三个纵坐标互不相同，这样是满足题目要求的。纵坐标同理，因此我们只能选恰好有两个横坐标相同的点，恰好有两个纵坐标相同的点。

提示 3：这三个点组成了一个 L 型。

提示 4：枚举每个点 (x,y) 作为 L 型的拐点，那么另外有 cntX[x]-1 个横坐标相同的点，cntY[y]-1 个横坐标相同的点。对答案的贡献是 (cntX[x]-1)*(cntY[y]-1)。
答案为 C(n,3) - 这些贡献之和。"""

#       ms
def solve():
    n, = RI()
    ps = []
    cnt_x = [0] * (n + 1)
    cnt_y = [0] * (n + 1)
    for _ in range(n):
        x, y = RI()
        ps.append((x, y))
        cnt_x[x] += 1
        cnt_y[y] += 1
    ans = comb(n, 3)
    for x, y in ps:
        ans -= (cnt_x[x] - 1) * (cnt_y[y] - 1)
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
