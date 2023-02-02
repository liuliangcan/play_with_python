# Problem: C - Lights Out on Tree
# Contest: AtCoder - AtCoder Regular Contest 148
# URL: https://atcoder.jp/contests/arc148/tasks/arc148_c
# Memory Limit: 1024 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://atcoder.jp/contests/arc148/tasks/arc148_c

输入 n(2≤n≤2e5) q(≤2e5)，然后输入 p2,p3,...,pn 表示一棵根为 1 的树，pi 表示点 i 的父节点。
然后输入 q 个询问，每个询问先输入 m，然后输入 m 个互不相同的特殊节点 v1,v2,...,vm。所有询问的 m 之和不超过 2e5。

每个节点都有一盏灯，其中特殊节点的灯打开，其余节点的灯关闭。
每次操作，你可以选择一棵子树，切换子树内所有灯的开/闭状态。
对每个询问，回答：要使所有灯关闭，至少需要多少次操作。
输入
6 6
1 1 2 2 5
6 1 2 3 4 5 6
3 2 5 6
1 3
3 1 2 3
3 4 5 6
4 2 3 4 5
输出
1
2
1
3
2
3
"""
"""https://atcoder.jp/contests/arc148/submissions/38529258

提示 1：如果只有一盏灯 v 亮着，要使所有灯关闭，需要操作 v 和 v 的所有儿子，也就是 1 + child[v] 次，其中 child[v] 表示 v 的儿子个数。

提示 2：如果 v 的儿子已经亮着，就不用操作儿子了；同样地，如果 p[v] 已经亮着，就不用操作 v 自己了。"""


#       ms
def solve():
    n, q = RI()
    p = [0, 0] + RILST()  # p[i]是i的父节点
    child = [0] * (n + 1)  # child[i]代表i有几个儿子
    for i in range(2, n + 1):
        child[p[i]] += 1

    for _ in range(q):
        x = RILST()
        m, s = x[0], set(x[1:])
        ans = 0
        for u in s:
            ans += child[u]
            if p[u] in s:  # 如果它父节点是亮的，自己不用操作变暗，且父节点的一个儿子也不用操作变亮。
                ans -= 1  # 父节点的这个儿子不用操作变亮
            else:
                ans += 1  # 否则自己要变暗
        print(ans)


if __name__ == '__main__':
    solve()
