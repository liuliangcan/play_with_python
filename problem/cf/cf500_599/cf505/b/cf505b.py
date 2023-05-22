# Problem: B. Mr. Kitayuta's Colorful Graph
# Contest: Codeforces - Codeforces Round 286 (Div. 2)
# URL: https://codeforces.com/problemset/problem/505/B
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
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，实测这个快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10**9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/505/B

输入 n(2≤n≤100) m(1≤m≤100) 表示一个 n 点 m 边的无向图，节点编号从 1 到 n。
然后输入 m 条边，每条边输入 v w c(1≤c≤m)，表示有条颜色为 c 的边连接 v 和 w。
然后输入 q(1≤q≤100) 和 q 个询问，每个询问输入 v w，你需要输出有多少种颜色 c 满足：从 v 到 w 存在一条路径，这条路径上的边均为颜色 c。

进阶：你能想出一个低于 O(平方) 的算法吗？
见 https://codeforces.com/contest/506/problem/D
输入
4 5
1 2 1
1 2 2
2 3 1
2 3 3
2 4 3
3
1 2
3 4
1 4
输出
2
1
0
"""
"""https://codeforces.com/problemset/submission/505/206755341

由于数据范围比较小，用 m 个并查集统计，对每个询问遍历这 m 种颜色去统计 v 和 w 是否相连。
由于 m 比较小，并查集可以用哈希表实现。"""

class DSU:
    """基于数组的并查集"""
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.set_count = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            self.edge_size[y] += 1
            return False
        # if self.size[x] > self.size[y]:  # 注意如果要定向合并x->y，需要干掉这个；实际上上边改成find_fa后，按轶合并没必要了，所以可以常关
        #     x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.set_count -= 1
        return True

#     92  ms
def solve():
    n,m = RI()
    dsu = [DSU(n) for _ in range(m)]
    for _ in range(m):
        u,v,c = RI()
        dsu[c-1].union(u-1,v-1)
    q, = RI()
    for _ in range(q):
        u,v = RI()
        ans = 0
        for d in dsu:
            if d.find_fa(u-1) == d.find_fa(v-1):
                ans += 1
        print(ans)

if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
