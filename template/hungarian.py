"""匈牙利算法，二分图的最大匹配
https://blog.csdn.net/liuliangcan/article/details/127119432"""
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
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""
"""


#  	 ms
def solve(n, m, e, es):
    g = [[] for _ in range(n)]
    for u, v in es:
        g[u - 1].append(v - 1)

    ans = [-1] * m  # 每个女孩分配的男孩id
    vis = [-1] * m  # 这个女孩是否访问过，用时间戳避免重复创建

    def find(i, c):  # 尝试给第i个男孩分配，c是color
        for j in g[i]:  # 遍历i的邻居女孩j
            if vis[j] != c:  # 如果j没有分给i，则尝试分给他
                vis[j] = c  # 在c这个男孩层，j用过了
                if ans[j] == -1 or find(ans[j], c):  # j没有被分配，或者j之前分配的人可以另外分配一个女孩
                    ans[j] = i  # 给j安排i
                    return True
        return False

    cnt = 0
    for i in range(n):  # 遍历每个男孩，尝试分给他一个女孩
        # vis = [-1]*m
        if find(i, i):  # 分配成功
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    n, m, e = RI()
    es = []
    for _ in range(e):
        es.append(RILST())
    solve(n, m, e, es)

