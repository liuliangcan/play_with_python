import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *
from types import GeneratorType

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://atcoder.jp/contests/abc201/tasks/abc201_e

输入 n(≤2e5) 和一棵有边权的树的 n-1 条边，节点编号从 1 开始，边权范围 [0,2^60)。
定义 xor(i,j) 表示从 i 到 j 的简单路径上的边权的异或和。
累加所有满足 1≤i<j≤n 的 xor(i,j)，对结果模 1e9+7 后输出。
输入
3
1 2 1
1 3 3
输出 6

输入
5
3 5 2
2 3 2
1 5 1
4 5 13
输出 62

输入
10
5 7 459221860242673109
6 8 248001948488076933
3 5 371922579800289138
2 5 773108338386747788
6 10 181747352791505823
1 3 803225386673329326
7 8 139939802736535485
9 10 657980865814127926
2 4 146378247587539124
输出 241240228
https://atcoder.jp/contests/abc201/submissions/36166044

提示 1：逐位考虑。也就是假设边权只有 0 和 1。

提示 2：xor(i,j) = xor(1,i) ^ xor(1,j)。

提示 3：DFS，统计 xor(1,i) 中 1 的个数，记作 c。由于只有 1 和 0 异或才能是 1，这个比特位上的答案为 c * (n-c)。

笔记:
    先把题目简化成只有 0 1 的边权。
    f(1,i)代表从根(1)到i点这个路径的异或和。 易得f(1,i)不是0就是1。
    那么每个f(1,i)对答案的贡献是多少呢？
    题目要求每条路径的求和，那么要考虑从i到其它任意点的路径上的异或和，再求和。
    这里用到一个性质f(i,j)=f(1,i)^f(1,j)，这个很容易证明(考虑ij有祖孙关系或没有)。    
    只有0和1异或才是1，也就是说只要f(1,i)和f(1,j)不同，对答案的贡献就+1。找到和i不同的j即可。假设有x个不同的j,则对答案贡献+x。
    换句话说:ans=找有多少对不同f的ij对=1的数量*0的数量。
    由于f(0,1)∈{0,1},我们遍历一遍,计数1的个数c,那么0的个数就是n-c。不同的ij对数=c*(n-c)。
    
    看回题目，只需逐位分开考虑计数，最后乘上2的幂系数即可。
"""


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


#   1009   	 ms
def solve1(n, es):
    g = [{} for _ in range(n)]
    for u, v, w in es:
        g[u - 1][v - 1] = w
        g[v - 1][u - 1] = w
    cnt = [0] * 60

    @bootstrap
    def dfs(u, fa, xor_s):
        for i in range(60):
            cnt[i] += (xor_s >> i) & 1
        for v, w in g[u].items():
            if v != fa:
                yield dfs(v, u, w ^ xor_s)
        yield

    dfs(0, -1, 0)
    ans = 0
    p = 1
    for x in cnt:
        ans = (ans + x * (n - x) * p % MOD) % MOD
        p = p * 2 % MOD

    print(ans % MOD)


#     815 	 ms
def solve(n, es):
    g = [[] for _ in range(n)]
    for u, v, w in es:
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
    cnt = [0] * 60

    @bootstrap
    def dfs(u, fa, xor_s):
        for i in range(60):
            cnt[i] += (xor_s >> i) & 1
        for v, w in g[u]:
            if v != fa:
                yield dfs(v, u, w ^ xor_s)
        yield

    dfs(0, -1, 0)
    ans = 0
    p = 1
    for x in cnt:
        ans = (ans + x * (n - x) * p % MOD) % MOD
        p = p * 2 % MOD

    print(ans % MOD)


if __name__ == '__main__':
    n, = RI()
    es = []
    for _ in range(n - 1):
        es.append(RILST())

    solve(n, es)
