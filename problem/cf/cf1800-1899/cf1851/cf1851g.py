# Problem: G. Vlad and the Mountains
# Contest: Codeforces - Codeforces Round 888 (Div. 3)
# URL: https://codeforces.com/contest/1851/problem/G
# Memory Limit: 256 MB
# Time Limit: 5000 ms

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
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/contest/1851/problem/G

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5，m 之和 ≤2e5，q 之和 ≤2e5。
每组数据输入 n(2≤n≤2e5) m(1≤m≤2e5)，表示一个 n 点 m 边的无向图。节点编号从 1 开始。保证图中无自环和重边。
然后输入长为 n 的数组 h(1≤h[i]≤1e9)。每个节点有一座山，第 i 座山的高度为 h[i]。
然后输入 m 条边。
然后输入 q(1≤q≤2e5) 和 q 个询问，每个询问输入 a b e(0≤e≤1e9)。

从第 i 座山移动到和 i 相邻的第 j 座山，你的能量会减少 h[j]-h[i]。如果这个值是负数则你会增加能量。
只有在移动后能量 >= 0 的情况下才能从 i 移动到 j。
对于每个询问，回答：在你初始能量为 e 的情况下，能否从第 a 座山移动到第 b 座山？输出 YES 或 NO。注意节点编号从 1 开始。
"""


#  1095     ms
def solve():
    n, m = RI()
    h = [0] + RILST()
    es = []
    for _ in range(m):
        u, v = RI()
        es.append((max(h[u], h[v]), u, v))
    fa = list(range(n + 1))

    def find(x):
        t = x
        while x != fa[x]:
            x = fa[x]
        while t != x:
            fa[t], t = x, fa[t]
        return x

    q, = RI()
    qs = []
    for i in range(q):
        a, b, e = RI()
        qs.append((h[a] + e, a, b, i))
    qs.sort()
    es.sort()
    j = 0
    ans = ['NO'] * q
    for t, a, b, i in qs:
        while j < m and es[j][0] <= t:
            _, u, v = es[j]
            fa[find(u)] = find(v)
            j += 1
        if find(a) == find(b): ans[i] = 'YES'
    # print(*ans, sep='\n')
    # print()
    print('\n'.join(ans)+'\n')

#    2234   ms
def solve1():
    n, m = RI()
    h = [0] + RILST()
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = RI()
        g[u].append(v)
        g[v].append(u)
    fa = list(range(n + 1))

    def find(x):
        t = x
        while x != fa[x]:
            x = fa[x]
        while t != x:
            fa[t], t = x, fa[t]
        return x

    q, = RI()
    qs = []
    for i in range(q):
        a, b, e = RI()
        qs.append((a, b, e, i))
    qs.sort(key=lambda x: h[x[0]] + x[2])
    hh = sorted((v, u) for u, v in enumerate(h))
    j = 1
    ans = [0] * q
    for a, b, e, i in qs:
        t = h[a] + e
        while j <= n and hh[j][0] <= t:
            u = hh[j][1]
            x = find(u)
            for v in g[u]:
                if h[v] <= t:
                    fa[find(v)] = x
            j += 1
        ans[i] = 'YES' if find(a) == find(b) else 'NO'
    print(*ans, sep='\n')
    print()

"""
1.深呼吸，不要紧张，慢慢读题，读明白题，题目往往比你想的简单。
2.暴力枚举:枚举什么，是否可以使用一些技巧加快枚举速度（预处理、前缀和、数据结构、数论分块）。
3.贪心:需要排序或使用数据结构（pq）吗，这么贪心一定最优吗。
4.二分：满足单调性吗，怎么二分，如何确定二分函数返回值是什么。
5.位运算：按位贪心，还是与位运算本身的性质有关。
6.数学题：和最大公因数、质因子、取模是否有关。
7.dp：怎么设计状态，状态转移方程是什么，初态是什么，使用循环还是记搜转移。
8.搜索：dfs 还是 bfs ，搜索的时候状态是什么，需要记忆化吗。
9.树上问题：是树形dp、树上贪心、或者是在树上搜索。
10.图论：依靠什么样的关系建图，是求环统计结果还是最短路。
11.组合数学：有几种值，每种值如何被组成，容斥关系是什么。
12.交互题：log(n)次如何二分，2*n 次如何通过 n 次求出一些值，再根据剩余次数求答案。
13.如果以上几种都不是，多半是有一个 point 你没有注意到，记住正难则反。
"""
if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
