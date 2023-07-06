# Problem: F. Group Projects
# Contest: Codeforces - 8VC Venture Cup 2016 - Elimination Round
# URL: https://codeforces.com/contest/626/problem/F
# Memory Limit: 256 MB
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
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/contest/626/problem/F

输入 n(1≤n≤200) k(0≤k≤1000) 和长为 n 的数组 a(1≤a[i]≤500)。

有 n 个人，第 i 个人的能力值为 a[i]。
把这 n 个人分成若干组，一个组的不平衡度定义为组内最大值减最小值。
特别地，如果组内只有一个人，那么不平衡度为 0。
要求所有组的不平衡度之和不超过 k。
有多少种分组方案？模 1e9+7。

注：一个组是 a 的子序列，不要求连续。
输入
3 2
2 4 5
输出 3

输入
4 3
7 8 9 10
输出 13

输入
4 0
5 10 20 21
输出 1
"""
"""先排序。

提示 1：把作为最小值的数看成左括号，作为最大值的数看成右括号。由于作为最小值的个数不能低于作为最大值的个数，所以这和括号问题是相似的，可以用解决括号问题的技巧来思考。

提示 2：如何优雅地计算不平衡度呢？假设从小到大有 a b c d 四个数，选了 a c d，那么 d-a = (d-c) + (c-b) + (b-a)。注意这里算上了没有选的 b。
这意味着我们只需要考虑相邻两个数对不平衡度的影响。

提示 3：记忆化搜索，我的实现是从 n-1 开始，递归到 -1。先选最大值，再选最小值。
定义 dfs(i, groups, leftK) 表示前 i 个数中，有最大值但是尚未确定最小值的组有 groups 个，剩余不平衡度为 leftK。
需要考虑四种情况：
1. a[i] 作为一个新的组的最大值（创建一个新的组）。
2. a[i] 作为某个组的最小值（有 groups 种选择方案）。
3. a[i] 单独形成一个组（这个组只有一个数）。
4. a[i] 添加到某个组中（有 groups 种选择方案）。
具体见代码 https://codeforces.com/contest/626/submission/211471819

注：这题用到的思路和我在【1681. 最小不兼容性】这题评论区发的代码是类似的
https://leetcode.cn/problems/minimum-incompatibility/discussion/comments/2051770"""


#   904    ms
def solve():
    n, m = RI()
    a = RILST()
    a.sort()
    a = [0] + a
    f = [[0] * (m + 1) for _ in range(n + 1)]  # f[i][j][k]表示前i个数，有j个段尚未闭合，不平衡度为k时的方案数
    f[0][0] = 1
    for i in range(1, n + 1):
        g = [[0] * (m + 1) for _ in range(n + 1)]
        d = a[i] - a[i - 1]
        for j in range(n + 1):
            for k in range(m + 1):
                if j != 0 and k - (j - 1) * d >= 0:
                    g[j][k] += f[j - 1][k - (j - 1) * d]
                if j != n and k - (j + 1) * d >= 0:
                    g[j][k] += f[j + 1][k - (j + 1) * d] * (j + 1)
                if k - j * d >= 0:
                    g[j][k] += f[j][k - j * d] * (j + 1)
                g[j][k] %= MOD
        f = g
    print(sum(f[0][:m + 1]) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
