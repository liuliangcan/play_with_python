import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: sys.stdin.readline().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/827/B

输入 n 和 k (2≤k<n≤2e5)。
构造一棵有 n 个节点的树，其中度数为 1 的点恰好有 k 个，且这些点之间的最大距离最小。
输出这个最小值，和这棵树的 n-1 条边。节点编号从 1 开始。
如果有多种构造方案，输出任意一种。

注：一个点的度数等于与该点相连的边的数目。
输入
3 2
输出
2
1 2
2 3
解释 见右图

输入
5 3
输出
3
1 2
2 3
3 4
3 5
解释 见右图
"""


# 	 ms
def solve(n, k):
    d = (n - 1) // k
    if d * k == n - 1:
        print(2 * d)
        v = 1
        for _ in range(k):
            print(1, v + 1)
            v += 1
            for _ in range(d - 1):
                print(v, v + 1)
                v += 1
        return

    m = (n - 1) % k
    if m == 1:
        print(2 * d + 1)
    else:
        print(2 * d + 2)
    v = 1
    for _ in range(k):
        print(1, v + 1)
        v += 1
        for _ in range(d - 1):
            print(v, v + 1)
            v += 1
        if m:
            m -= 1
            print(v, v + 1)
            v += 1


if __name__ == '__main__':
    n, k = RI()

    solve(n, k)
