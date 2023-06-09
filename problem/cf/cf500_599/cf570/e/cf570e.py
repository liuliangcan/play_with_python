# Problem: E. Pig and Palindromes
# Contest: Codeforces - Codeforces Round 316 (Div. 2)
# URL: https://codeforces.com/problemset/problem/570/E
# Memory Limit: 256 MB
# Time Limit: 4000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/570/E

输入 n m (1≤n,m≤500) 和 n 行 m 列的字符矩阵，只包含小写字母。
你需要从左上角的 (1,1) 出发，到达右下角的 (n,m)。
每次只能向下或向右走。
问：有多少条路径对应的字符串是回文串？（见右图）
模 1e9+7。
输入
3 4
aaab
baaa
abba
输出 3
解释 见右图
"""
"""https://codeforces.com/problemset/submission/570/209046565
https://codeforces.com/problemset/submission/570/209046793  循环优化

做法类似 741. 摘樱桃

转换成两个人同时从左上和右下出发，定义 f[i][r1][r2] 表示走了 i 步，两人分别在第 r1 行和第 r2 行的方案数。这样只需要三个数就能表示坐标 (r1,c1) 和 (r2,c2)。
f[0][1][n] = 1（如果 a[1][1] != a[n][m] 直接输出 0）
如果 a[r1][c1] = a[r2][c2]，那么 f[i][r1][r2] = f[i-1][r1][r2] + f[i-1][r1][r2+1] + f[i-1][r1-1][r2] + f[i-1][r1-1][r2+1]，否则就是 0
代码实现时，第一个维度可以去掉。

最后答案按照字符串长度的奇偶性讨论。
如果是奇回文串，那么答案为 sum(f[i][i])，否则答案为 sum(f[i][i]+f[i][i+1])。"""


#    TLE14   ms
def solve():
    n, m = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append(s)
    if n == m == 1:
        return print(1)
    if g[0][0] != g[n - 1][m - 1]:
        return print(0)
    mask = (1 << 10) - 1
    start = ((n - 1) << 10) | (m - 1)

    f = {start: 1}

    def manh(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    ans = 0
    while f:
        p = {}
        for u, cnt in f.items():
            x1, y1, x2, y2 = u >> 30 & mask, u >> 20 & mask, u >> 10 & mask, u & mask
            if manh(x1, y1, x2, y2) <= 1:
                ans = (ans + cnt) % MOD
                continue

            for a1, b1 in (x1 + 1, y1), (x1, y1 + 1):
                if a1 >= n or b1 >= m:
                    continue
                for a2, b2 in (x2 - 1, y2), (x2, y2 - 1):
                    if a2 < a1 or b2 < b1 or g[a1][b1] != g[a2][b2]:
                        continue
                    p[a1 << 30 | b1 << 20 | a2 << 10 | b2] = (p.get(a1 << 30 | b1 << 20 | a2 << 10 | b2, 0) + cnt) % MOD
        f = p
    print(ans)


if __name__ == '__main__':
    n, m = RI()
    g = []
    for _ in range(n):
        s, = RS()
        g.append(s)
    if n == m == 1:
        print(1)
        exit()
    if g[0][0] != g[n - 1][m - 1]:
        print(0)
        exit()
    mask = (1 << 10) - 1
    # start = ((n - 1) << 10) | (m - 1)
    #
    #
    # def manh(x1, y1, x2, y2):
    #     return abs(x1 - x2) + abs(y1 - y2)

    # f = {start: 1}
    # ans = 0
    # while f:
    #     p = {}
    #     for u, cnt in f.items():
    #         x1, y1, x2, y2 = u >> 30 & mask, u >> 20 & mask, u >> 10 & mask, u & mask
    #         if manh(x1, y1, x2, y2) <= 1:
    #             ans = (ans + cnt) % MOD
    #             continue
    #
    #         for a1, b1 in (x1 + 1, y1), (x1, y1 + 1):
    #             if a1 >= n or b1 >= m:
    #                 continue
    #             for a2, b2 in (x2 - 1, y2), (x2, y2 - 1):
    #                 if a2 < a1 or b2 < b1 or g[a1][b1] != g[a2][b2]:
    #                     continue
    #                 p[a1 << 30 | b1 << 20 | a2 << 10 | b2] = (p.get(a1 << 30 | b1 << 20 | a2 << 10 | b2, 0) + cnt) % MOD
    #     f = p
    # print(ans)

    # for _ in range((n+m-1-1)//2):
    #     p = {}
    #     for u, cnt in f.items():
    #         x1, y1, x2, y2 = u >> 30 & mask, u >> 20 & mask, u >> 10 & mask, u & mask
    #         for a1, b1 in (x1 + 1, y1), (x1, y1 + 1):
    #             if a1 >= n or b1 >= m:
    #                 continue
    #             for a2, b2 in (x2 - 1, y2), (x2, y2 - 1):
    #                 if a2 < a1 or b2 < b1 or g[a1][b1] != g[a2][b2]:
    #                     continue
    #                 p[a1 << 30 | b1 << 20 | a2 << 10 | b2] = (p.get(a1 << 30 | b1 << 20 | a2 << 10 | b2, 0) + cnt) % MOD
    #     f = p
    #
    # print(sum(f.values())%MOD)
    # f = [[0] * n for _ in range(n)]
    # p = [[0] * n for _ in range(n)]
    # f[0][n - 1] = 1
    # vis = {(0, n - 1)}
    # for i in range((n + m - 1 - 1) // 2):
    #     v2 = set()
    #     for x1, x2 in vis:
    #         y1 = i - x1
    #         y2 = m - 1 - (i - (n - 1 - x2))
    #
    #         for a1, b1 in (x1 + 1, y1), (x1, y1 + 1):
    #             if a1 >= n or b1 >= m:
    #                 continue
    #             for a2, b2 in (x2 - 1, y2), (x2, y2 - 1):
    #                 if a2 < a1 or b2 < b1 or g[a1][b1] != g[a2][b2]:
    #                     continue
    #                 if (a1, a2) not in v2:
    #                     p[a1][a2] = 0
    #                     v2.add((a1, a2))
    #                 p[a1][a2] = (p[a1][a2] + f[x1][x2]) % MOD
    #     f, p = p, f
    #     vis = v2
    #
    # print(sum(f[x1][x2] for x1, x2 in vis) % MOD)
    # f = [[0] * n for _ in range(n)]
    # p = [[0] * n for _ in range(n)]
    # f[0][n - 1] = 1
    # for i in range((n + m - 1 - 1) // 2):
    #     v2 = set()
    #     for x1 in range(min(i+1,n)):
    #         y1 = i - x1
    #         for x2 in range(n-1,max(n-1-i-1,-1),-1):
    #             y2 = m - 1 - (i - (n - 1 - x2))
    #             # if not f[x1][x2] :continue
    #
    #             for a1, b1 in (x1 + 1, y1), (x1, y1 + 1):
    #                 if a1 >= n or b1 >= m:
    #                     continue
    #                 for a2, b2 in (x2 - 1, y2), (x2, y2 - 1):
    #                     if a2 < a1 or b2 < b1 or g[a1][b1] != g[a2][b2]:
    #                         continue
    #                     if (a1, a2) not in v2:
    #                         p[a1][a2] = 0
    #                         v2.add((a1, a2))
    #                     p[a1][a2] = (p[a1][a2] + f[x1][x2]) % MOD
    #         f, p = p, f
    #         vis = v2
    # print(f)
    # print(sum(sum(row) for row in f) % MOD)
    # 2682 ms
    f = [[0] * n for _ in range(n)]
    p = [[0] * n for _ in range(n)]
    f[0][n - 1] = 1
    for i in range((n + m - 1 - 1) // 2):
        for x1 in range(max(0, i - m), min(n, i + 1)):
            # for x2 in range(min(n - 1, n - 1 - (i - m)), max(n - 1 - i - 1, -1), -1):
            for x2 in range(max(n - 1 - i, 0), min(n, n - (i - m))):
                y1 = i - x1
                y2 = m - 1 - (i - (n - 1 - x2))
                if not f[x1][x2]: continue
                for a1, b1 in (x1 + 1, y1), (x1, y1 + 1):
                    if a1 >= n or b1 >= m: continue  # 出界，寄
                    for a2, b2 in (x2 - 1, y2), (x2, y2 - 1):
                        if a2 < a1 or b2 < b1 or g[a1][b1] != g[a2][b2]: continue  # 这个点必须在上个点右下方
                        p[a1][a2] = (p[a1][a2] + f[x1][x2]) % MOD
                f[x1][x2] = 0  # 清空，就不用担心了
        f, p = p, f

    print(sum(sum(row) for row in f) % MOD)

