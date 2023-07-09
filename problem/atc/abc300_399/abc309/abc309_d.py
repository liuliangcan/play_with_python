# Problem: D - Add One Edge
# Contest: AtCoder - Denso Create Programming Contest 2023 (AtCoder Beginner Contest 309)
# URL: https://atcoder.jp/contests/abc309/tasks/abc309_d
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

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
if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """我们有一个无向图，有 (N1+N2) 个顶点和 M 条边。对于 i=1,2,...,M，第 i 条边连接顶点 a_i 和顶点 b_i。以下属性是保证的：

对于所有整数 u 和 v，满足 1≤u,v≤N1，顶点 u 和顶点 v 是连通的。
对于所有整数 u 和 v，满足 N1+1≤u,v≤N1+N2，顶点 u 和顶点 v 是连通的。
顶点 11 和顶点 (N1+N2) (N1+N2) 是不连通的。
考虑执行以下操作一次：

选择一个整数 u，满足 1≤u≤N1，选择一个整数 v，满足 N1+1≤v≤N1+N2，添加一条连接顶点 u 和顶点 v 的边。
我们可以证明，在结果图中，顶点 1 和顶点 (N1+N2)  总是连通的；因此，设 d 为顶点 1 和顶点 (N1+N2) 之间路径的最小长度（边数）。

找到通过添加适当边来得到的最大可能的 d。

“连通”的定义
约束条件
1≤N1,N2≤1.5×10^5
0≤M≤3×10^5
1≤ai,bi≤N1+N2
(ai,bi)≠(aj,bj)，当i≠j时
对于所有整数 u 和 v，满足 1≤u,v≤N1，顶点 u 和顶点 v 是连通的。
对于所有整数 u 和 v，满足 N1+1≤u,v≤N1+N2，顶点 u 和顶点 v 是连通的。
顶点 11 和顶点 (N1+N2) (N1+N2) 是不连通的。
输入值都是整数。
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


def bootstrap(f, stack=[]):

    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


#       ms
def solve():
    n1,n2,m = RI()
    g = [[] for _ in range(n1+n2)]
    for _ in range(m):
        u,v = RI()
        u-=1
        v-=1
        g[u].append(v)
        # print(v,len(g))
        g[v].append(u)

    def bfs(u):
        step = 0
        vis = {u}
        q = [u]
        while q:
            nq = []
            step += 1
            for u in q:
                for v in g[u]:
                    if v not in vis:
                        vis.add(v)
                        nq.append(v)
            q = nq
        return step-1
    print(bfs(0)+bfs(n1+n2-1)+1)



if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
